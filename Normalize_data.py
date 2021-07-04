import torch
from torch.nn import Module, Conv2d, MaxPool2d, Linear, MSELoss, LSTM, LeakyReLU, Sequential, ReLU, Sigmoid, functional
from torch.optim import Adam
import matplotlib.pyplot as plt
from agent import NetWork
from torch import device as devicer, cuda
import pickle
from saver import loadagent
device = devicer('cuda' if cuda.is_available() else 'cpu')

def normalize(all_data, train_start, train_end, test_start, test_end, normalizer="minmax", splits = 1):
    nans = torch.sum(torch.sum(all_data.isnan(), axis=1), axis=1)
    all_data = all_data[nans == False]
    new_all_data = all_data[:,-train_start:-test_end]
    slice_size = new_all_data.shape[1]//splits

    shape0, shape2 = new_all_data.shape[0], new_all_data.shape[2]
    #means = torch.zeros([shape0, 1, shape2]).to(device=device)
    #stds = torch.zeros([shape0, 1, shape2]).to(device=device)
    mins = torch.zeros([shape0, 1, shape2]).to(device=device)
    maxes = torch.zeros([shape0, 1, shape2]).to(device=device)
    for i in range(shape0):
        for j in range(shape2):
            #means[i,0,j] = torch.mean(new_all_data[i,:,j])
            #stds[i,0,j] = torch.std(new_all_data[i,:,j])
            mins[i,0,j] = torch.min(new_all_data[i,:,j])
            maxes[i,0,j] = torch.max(new_all_data[i,:,j])

    new_all_data2 = torch.tensor([]).to(device)
    new_mins = torch.tensor([]).to(device)
    new_maxes = torch.tensor([]).to(device)
    for i in range(splits):
        new_all_data2 = torch.cat((new_all_data2, new_all_data[:, slice_size * i: slice_size * (i+1)]), 0)
        new_mins = torch.cat((new_mins, mins), 0)
        new_maxes = torch.cat((new_maxes, maxes), 0)

    print(new_all_data2.shape)
    #train_start, train_end, test_start, test_end = 280, 120, 120, 1
    temp_min = new_mins[:,0,3] < 1
    idx_min = temp_min.nonzero()
    temp_max = new_maxes[:,0,3] > 1000
    idx_max = temp_max.nonzero()
    temp_min2 = new_mins[:,0,3] > 1000
    idx_min2 = temp_min2.nonzero()
    temp_max2 = new_maxes[:,0,3] < 1
    idx_max2 = temp_max2.nonzero()
    bad_data = torch.cat((idx_min, idx_max, idx_min2, idx_max2), 0).flatten()
    bad_data = torch.unique(bad_data)
    temper = torch.ones(new_all_data2.shape[0])
    temper[bad_data] = 0
    temper = temper.nonzero().flatten()
    new_mins = new_mins[temper]
    new_maxes = new_maxes[temper]
    new_all_data2 = new_all_data2[temper]
    print(new_all_data2.shape)

    final_data = new_all_data2[:,:-(train_end - train_start)//splits]
    simulate = new_all_data2[:,-(train_end - train_start)//splits:]
    print(final_data.shape, simulate.shape, -train_end//splits)
    # torch.sort((new_mins)[:,0,3])[0]
    # plt.plot(torch.sort((new_mins)[:,0,3])[0][:].cpu().numpy())
    # plt.show()
    # plt.plot(torch.sort((new_maxes)[:,0,3], descending=True)[0][:].cpu().numpy())
    # plt.show()
    if normalizer == "minmax":
        normalized_data = (final_data - new_mins)/(new_maxes - new_mins)
        normalized_simulate = (simulate - new_mins)/(new_maxes - new_mins)
        return normalized_data, normalized_simulate, new_mins, new_maxes

