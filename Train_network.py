import torch
from torch.nn import Module, Conv2d, MaxPool2d, Linear, MSELoss, LSTM, LeakyReLU, Sequential, ReLU, Sigmoid
from torch.optim import Adam
import matplotlib.pyplot as plt
from agent import NetWork
from torch import device as devicer, cuda
import pickle
from saver import saveAgent
from Normalize_data import normalize
device = devicer('cuda' if cuda.is_available() else 'cpu')

all_data = torch.load('DayliData.pt').to(device=device)
predictor = NetWork().double().to(device)

normalized_data, normalized_simulate, mins, maxes = normalize(all_data = all_data, train_start = 2000, train_end = 1000, test_start = 1000, test_end = 1, splits = 10)
print(normalized_data.shape, normalized_simulate.shape)
final_inputs = normalized_data[:,:-1,:]
final_label = normalized_data[:,1:,:]

def train(data, labels, model, epoches, training_splits, lossf, name):
    for epo in range(epoches):
        perm = torch.randperm(data.size()[0])
        training_input = data[perm]
        training_label = labels[perm]
        for j in range(training_splits):
            len_input = training_input.shape[0]//training_splits   
            len_labels = training_label.shape[0]//training_splits   
            train_input = training_input[j * len_input:(j+1) * len_input]
            train_label = training_label[j * len_labels:(j+1) * len_labels]
            #model.train(train_input[:,:,3].unsqueeze(2), train_label[:,:,3].unsqueeze(2), lossf) #change to 3 or :
            model.train_5_features(train_input, train_label, lossf)
        print("training " + str(round((epo+1)/epoches*100)) + " %")
        if epo % 20 == 0:
            plt.plot(predictor.loss_list)
            plt.pause(2)
            plt.close('all')
    saveAgent(model, name)
plt.plot(predictor.loss_list)



train(final_inputs, final_label, predictor, epoches=1000, training_splits=40, lossf="next_no20", name="test7")