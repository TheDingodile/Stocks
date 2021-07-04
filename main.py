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
from RL_agent import Network1, LSTMNetwork, RL_agent
from torch.autograd.grad_mode import no_grad
from agent import NetWork
from saver import loadagent, saveAgent
from Normalize_data import normalize
from Train_trader import trainer

train = trainer()
train.train()