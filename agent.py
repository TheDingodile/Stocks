import torch
from torch.nn import Module, Conv2d, MaxPool2d, Linear, MSELoss, LSTM, LeakyReLU, Sequential, ReLU, Sigmoid
from torch.optim import Adam
import matplotlib.pyplot as plt
from torch import device as devicer, cuda
device = devicer('cuda' if cuda.is_available() else 'cpu')

class NetWork(Module):
    def __init__(self):
        super(NetWork, self).__init__()
        self.loss_list = []
        self.hidden_size = 25
        self.LSTM_stacks = 1
        self.input_size = 5
        self.output_size = 5
        self.rnn = LSTM(self.input_size, self.hidden_size, self.LSTM_stacks, batch_first=True).to(device=device)
        self.linear = Sequential(
            LeakyReLU(),
            Linear(25, 25),
            LeakyReLU(),
            Linear(25, self.output_size),
        ).to(device=device)
        self.optimizer = Adam(list(self.rnn.parameters()) + list(self.linear.parameters()), lr=1e-5, weight_decay=1e-5)
        self.criterion = MSELoss()

    def train(self, input, label, lossf="next_no20"):
        bs, seq_sz, _ = input.size()
        h0 = torch.zeros(self.LSTM_stacks, bs, self.hidden_size).double().to(device=device)
        c0 = torch.zeros(self.LSTM_stacks, bs, self.hidden_size).double().to(device=device)
        y, (hn, cn) = self.rnn(input, (h0, c0))
        y = self.linear(y)
        if lossf == "next_no20":
            loss = self.criterion(y[:,20:], label[:,20:])
            loss.backward()
            self.optimizer.step()
        if lossf == "closing":
            loss = self.criterion(y[:,20:,0], label[:,20:,0])
            loss.backward()
            self.optimizer.step()
        self.loss_list.append(loss.item())

    def train_5_features(self, input, label, lossf="next_no20"):
        bs, seq_sz, _ = input.size()
        h0 = torch.zeros(self.LSTM_stacks, bs, self.hidden_size).double().to(device=device)
        c0 = torch.zeros(self.LSTM_stacks, bs, self.hidden_size).double().to(device=device)
        y, (hn, cn) = self.rnn(input, (h0, c0))
        y = self.linear(y)
        if lossf == "next_no20":
            loss = self.criterion(y[:,20:], label[:,20:])
            loss.backward()
            self.optimizer.step()
        if lossf == "closing":
            loss = self.criterion(y[:,20:,3], label[:,20:,3])
            loss.backward()
            self.optimizer.step()
        self.loss_list.append(loss.item())


    def predict(self, input):
        bs, seq_sz, _ = input.size()
        h0 = torch.zeros(self.LSTM_stacks, bs, self.hidden_size).double().to(device=device)
        c0 = torch.zeros(self.LSTM_stacks, bs, self.hidden_size).double().to(device=device)
        y, (hn, cn) = self.rnn(input, (h0, c0))
        y = self.linear(y)
        return y

    def prepare_hidden(self, input):
        self.rnn.flatten_parameters()
        bs, seq_sz, _ = input.size()
        h0 = torch.zeros(self.LSTM_stacks, bs, self.hidden_size).double().to(device=device)
        c0 = torch.zeros(self.LSTM_stacks, bs, self.hidden_size).double().to(device=device)
        _, (self.hn, self.cn) = self.rnn(input, (h0, c0))

    def predict_from_hidden(self, input):
        self.rnn.flatten_parameters()
        y, (self.hn, self.cn) = self.rnn(input, (self.hn, self.cn))
        y = self.linear(y)
        return y

    def output_hidden(self, input):
        self.rnn.flatten_parameters()
        y, (self.hn, self.cn) = self.rnn(input, (self.hn, self.cn))
        return y