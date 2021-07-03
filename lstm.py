import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import random

class LSTM(nn.Module):
    def __init__(self, GPU):
        if GPU == True:
            torch.set_default_tensor_type('torch.cuda.FloatTensor')
        super(LSTM, self).__init__()
        self.hidden_size = 64
        self.LSTM_stacks = 2
        self.input_size = 29
        self.output_size = 29

        self.rnn = nn.LSTM(self.input_size, self.hidden_size, batch_first=True)
        self.l1 = nn.Linear(self.hidden_size, self.output_size)
        self.relu = nn.LeakyReLU()
        self.l2 = nn.Linear(self.hidden_size, self.hidden_size)
        self.criterion = nn.MSELoss()
        self.learning_rate = 0.001
        self.optimizer = torch.optim.Adam(self.rnn.parameters(), lr = self.learning_rate)
        self.lostlist = []

    def forward(self, x=None, train=False):
        x = torch.tensor(x, dtype = torch.float32)
        h0 = torch.zeros([self.LSTM_stacks, x.size(0), self.hidden_size]).requires_grad_()
        c0 = torch.zeros([self.LSTM_stacks, x.size(0), self.hidden_size]).requires_grad_()

        out, (hn, cn) = self.rnn(x, (h0, c0))
        #out = self.l2(out)
        out = self.relu(out)
        out = self.l1(out)
        out = out.transpose(1, 2)
        return out

    def train(self, alldata, labels, epochs, batch):
        for _ in range(epochs):
            
            #Shuffle data
            for l in range(len(alldata)):
                holder = list(zip(alldata[l], labels[l]))
                random.shuffle(holder)
                #print(alldata[l], holder)
                alldata[l], labels[l] = zip(*holder)
                alldata[l] = list(alldata[l])
                labels[l] = list(labels[l])
            holder = list(zip(alldata, labels))
            random.shuffle(holder)
            alldata, labels = zip(*holder)      
            alldata = list(alldata)
            labels = list(labels)
            
            for i in range(len(alldata)):
                j = 0
                while True:
                    batch_input = alldata[i][j*batch:(j+1)*batch:]
                    batch_label = labels[i][j*batch:(j+1)*batch:]
                    self.optimizer.zero_grad()
                    tensorlabels = torch.tensor(batch_label, dtype = torch.long)
                    output = self.forward(batch_input, train=True)
                    loss = self.criterion(output, tensorlabels)
                    loss.backward()
                    self.optimizer.step()
                    j += 1
                    if (j+1)*batch > len(alldata[i]):
                        break
        
    
    def test(self, alldata, labels):
        sumloss = 0
        self.totalcounter = [0]*14
        for i in range(len(alldata)):
            self.counter = [0]*14
            predictions = self.forward(alldata[i], train=True)
            pred = np.array(predictions.tolist())
            for t in range(len(pred)):
                for r in range(len(pred[t][0])):
                    pred[t][0][r], pred[t][1][r], pred[t][2][r] = (pred[t][2][r] - pred[t][1][r]), (pred[t][0][r] - pred[t][2][r]), (pred[t][1][r] - pred[t][0][r])
            best_move = pred.argmax(axis=1).tolist()
            self.movelist.append(best_move)
            for k in range(len(best_move)):
                for j in range(len(best_move[0])):
                    win = (best_move[k][j] + 2) % 3
                    lose = (best_move[k][j] + 1) % 3
                    if win == labels[i][k][j]:
                        self.counter[j] += 1
                    elif lose == labels[i][k][j]:
                        self.counter[j] -= 1
            self.counter = [x / len(best_move) for x in self.counter]
            tensorlabels = torch.tensor(labels[i], dtype = torch.long)
            #print(predictions)
            #print(tensorlabels)
            loss = self.criterion(predictions, tensorlabels)
            sumloss += loss.item()
            self.totalcounter = [sum(x) for x in zip(self.totalcounter, self.counter)]

        for k in range(14):
            self.correct_list[k].append(self.totalcounter[k]/(14-k))

    
        self.lostlist.append(sumloss)

    def train_test(self, alldata, labels, epochs=100, batch=1024, split=0.9, test_frequency=0.05, showplots=True, playpercent = 100):
        self.lostlist = []
        train_X = []
        train_Y = []
        test_X = []
        test_Y = []
        for i in range(len(alldata)):
            train_X.append(alldata[i][:int(len(alldata[i])*split)])
            train_Y.append(labels[i][:int(len(labels[i])*split)])
            test_X.append(alldata[i][int(len(alldata[i])*split):])
            test_Y.append(labels[i][int(len(labels[i])*split):])

        for j in range(int(1/test_frequency)):
            epoch = int(epochs*test_frequency)
            self.test(test_X, test_Y)
            self.train(train_X, train_Y, epochs=epoch, batch=batch)

            if j % int(1+((1/test_frequency)/1000)) == 0:
                print(str(100*j/int((1/test_frequency))) + " percent done with training")

        if showplots == True:
            plt.plot(np.arange(len(self.lostlist))*epochs*test_frequency, self.lostlist)
            plt.ylabel("lossfunction")
            plt.xlabel("epochs")
            plt.show()
            colors = ['red', 'black', 'midnightblue', 'orange', 'forestgreen', 'lime', 'royalblue', 'violet', 'deeppink', 'darkviolet', 'lightpink', 'cadetblue', 'gold', 'gray']
            for k in range(len(self.correct_list)):
                if self.correct_list[k] != []:
                    for i in range(len(self.correct_list[k])-2):
                        self.correct_list[k][i+1] = (self.correct_list[k][i]+2*self.correct_list[k][i+1]+self.correct_list[k][i+2])/4
                    label = "Round " + str(k + 1)
                    plt.plot(np.arange(len(self.correct_list[k]))*epochs*test_frequency, self.correct_list[k], label=label, color=colors[k])
            plt.legend(loc="upper left")
            plt.ylabel("Expected score per round")
            plt.xlabel("epochs")
            plt.show()
        
            flat_moves = [item for sublist in self.movelist for item in sublist]
            flat_moves = [item for sublist in flat_moves for item in sublist]
            rocks = []
            papers = []
            scissors = []
            for k in range(playpercent):
                density = flat_moves[(k-1)*len(flat_moves)//playpercent:(k*len(flat_moves))//playpercent:]
                if len(density) > 0:
                    # Sum det, der slår det den tror modstanderen spiller
                    rocks.append(np.sum(np.array(density) == 0)/len(density))
                    papers.append(np.sum(np.array(density) == 1)/len(density))
                    scissors.append(np.sum(np.array(density) == 2)/len(density))

            #high low pass filter
            for i in range(len(rocks)-2):
                rocks[i+1] = (rocks[i]+2*rocks[i+1]+rocks[i+2])/4
                papers[i+1] = (papers[i]+2*papers[i+1]+papers[i+2])/4
                scissors[i+1] = (scissors[i]+2*scissors[i+1]+scissors[i+2])/4

            plt.plot(np.arange(len(rocks))/len(rocks), rocks, label="rock")
            plt.plot(np.arange(len(rocks))/len(rocks), papers, label="paper")
            plt.plot(np.arange(len(rocks))/len(rocks), scissors, label="scissors")
            plt.ylabel("Play_frequency")
            plt.xlabel("Percent of training")
            plt.legend(loc="upper left")
            plt.show()