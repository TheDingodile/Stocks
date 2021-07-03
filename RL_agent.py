import torch
from torch.nn import Module, Conv2d, MaxPool2d, Linear, MSELoss, LSTM, LeakyReLU, Sequential, ReLU, Sigmoid
from torch.optim import Adam
import matplotlib.pyplot as plt
from torch import device as devicer, cuda
device = devicer('cuda' if cuda.is_available() else 'cpu')
import pickle
from torch.nn.functional import softmax
from random import random
from numpy.random import choice

class Network(Module):
    def __init__(self):
        super(Network, self).__init__()
        self.input_size = 32
        self.output_size = 5
        self.linear = Sequential(
            Linear(self.input_size, 100),
            LeakyReLU(),
            Linear(100, 50),
            LeakyReLU(),
            Linear(50, 50),
            LeakyReLU(),
            Linear(50, self.output_size),
        ).to(device=device).double()

class LSTMNetwork(Module):
    def __init__(self):
        super(Network, self).__init__()
        self.input_size = 5
        self.output_size = 5
        self.hidden_size = 50
        self.LSTM_stacks = 1
        self.input_size = 5
        self.output_size = 3
        self.rnn = LSTM(self.input_size, self.hidden_size, self.LSTM_stacks, batch_first=True).to(device=device)
        self.linear = Sequential(
            Linear(self.hidden_size, 50),
            LeakyReLU(),
            Linear(50, 50),
            LeakyReLU(),
            Linear(50, self.output_size),
        ).to(device=device).double()
        self.optimizer = Adam(list(self.rnn.parameters()) + list(self.linear.parameters()), lr=1e-5, weight_decay=1e-5)


class RL_agent():
    def __init__(self, LSTM=True) -> None:
        self.LSTM = LSTM
        if LSTM:
            self.network = LSTMNetwork().to(device)
            self.placeholder = LSTMNetwork().to(device)
            self.target = LSTMNetwork().to(device)
        else:
            self.network = Network().to(device)
            self.placeholder = Network().to(device)
            self.target = Network().to(device)
        self.optimizer = Adam(self.network.linear.parameters(), lr=1e-5, weight_decay=1e-5)
        self.criterion = MSELoss()
        self.gamma = 0.998
        self.counter = 0
        self.values = None
        self.rewards = 0
        self.reward_list = []
        self.hn = None
        self.cn = None

    def update(self):
        self.target = pickle.loads(pickle.dumps(self.placeholder))
        self.placeholder = pickle.loads(pickle.dumps(self.network))

    def reset_hn(self):
        self.hn = None
        self.cn = None   
    
    def choose(self, state):
        if self.LSTM:
            if self.hn is None:
                self.hn = torch.zeros(self.LSTM_stacks, state.shape[0], self.hidden_size).double().to(device=device)
                self.cn = torch.zeros(self.LSTM_stacks, state.shape[0], self.hidden_size).double().to(device=device)
            y, (self.hn, self.cn) = self.network.rnn(state.double(), (self.hn, self.cn))
            self.values = self.network.linear(self.network.rnn(state.double(), (self.hn, self.cn))[0]).double()
            actions = self.eps_greedy(self.values)
            return actions
        else:
            #print(state[3])
            self.values = self.network.linear(state.double()).double()
            actions = self.eps_greedy(self.values)
            return actions
    
    def softmax_explore(self, values):
        epsilon = 5 * 10**5
        k = max(0.01, 10 * (1 - self.counter/epsilon))
        if self.counter % 1000 == 0:
            print(values[0])
            print(softmax(values / k, dim=1)[0])
            print("eps at " + str(max(0.01, 10 * (1 - self.counter/epsilon))))
        return torch.flatten(torch.multinomial(softmax(values / k, dim=1), 1, replacement=True))
    
    def eps_greedy(self, values):
        epsilon = 5 * 10**5 / 0.2
        eps = max(0.01, 0.2 - self.counter/epsilon)
        if self.counter % 1000 == 0:
            print(values[0])
            print("eps at " + str(eps))
        return torch.argmax(values, dim=1).flatten() if random() > eps else torch.tensor(choice(values.shape[1], values.shape[0]), device=device).long()

    
    def greedy(self, values):
        return torch.argmax(values, dim=1).flatten()

    
    def train(self, next_state, reward, action, extra):
        #print(next_state[3], reward[3], action[3])
        self.counter += 1
        self.rewards += torch.sum(reward).item()
        if extra != None:
            self.rewards += torch.sum(extra).item()
        if self.counter % 2000 == 0:
            self.update()
            self.reward_list.append(5000 * self.rewards/2000)
            self.rewards = 0
        with torch.no_grad():
            vals_target_next = self.target.linear(next_state)
        value_next = torch.gather(vals_target_next, 1, torch.argmax(self.network.linear(next_state), 1).unsqueeze(1)).view(-1)
        td_target = (value_next * self.gamma + reward).view(-1).detach()
        action_value_before = torch.gather(self.values.squeeze(0), 1, action.unsqueeze(1)).squeeze(1)
        loss_value_network = self.criterion(action_value_before, td_target)
        loss_value_network.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()
    
    def show_return(self):
        plt.plot(self.reward_list)
        if len(self.reward_list) > 30:
            smooth_loss = []
            for i in range(len(self.reward_list) - 30):
                smooth_loss.append(sum(self.reward_list[i:i + 30])/30)
            plt.plot(smooth_loss)
        plt.pause(10)
        plt.close('all')
    
    def show_return_forever(self):
        plt.plot(self.reward_list)
        if len(self.reward_list) > 30:
            smooth_loss = []
            for i in range(len(self.reward_list) - 30):
                smooth_loss.append(sum(self.reward_list[i:i + 30])/30)
            plt.plot(smooth_loss)
        plt.show()
