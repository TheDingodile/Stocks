from torch.autograd.grad_mode import no_grad
from agent import NetWork
import torch
from torch.nn import Module, Conv2d, MaxPool2d, Linear, MSELoss, LSTM, LeakyReLU, Sequential, ReLU, Sigmoid
from torch.optim import Adam
import matplotlib.pyplot as plt
from torch import device as devicer, cuda
device = devicer('cuda' if cuda.is_available() else 'cpu')
import pickle
from RL_agent import RL_agent
from saver import loadagent, saveAgent
from Normalize_data import normalize

all_data = torch.load('DayliData.pt').to(device=device) #yo
predictor = loadagent("test3")
plt.plot(predictor.loss_list)
plt.show()
agent = loadagent("trader6")
agent.show_return_forever()
input = torch.zeros(1, 31).to(device)
input[0,25] = 1
input[0,26] = 1
input[0,27] = 1
input[0,28] = 1
input[0,29] = 1
input[0,30] = 100
print(input)
agent.choose(input)
print(agent.values)