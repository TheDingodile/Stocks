import torch
from torch.nn import Module, Conv2d, MaxPool2d, Linear, MSELoss, LSTM, LeakyReLU, Sequential, ReLU, Sigmoid
from torch.optim import Adam
import matplotlib.pyplot as plt
from agent import NetWork
from torch import device as devicer, cuda
import pickle

device = devicer('cuda' if cuda.is_available() else 'cpu')


data = torch.load('DayliData.pt').to(device=device)
nans = torch.sum(torch.sum(data.isnan(), axis=1), axis=1)
data = data[nans == False]
print(data.shape)
final_data = torch.tensor([]).to(device=device)
spts = 20
size = data.shape[1]//spts
for i in range(spts):
    final_data = torch.cat((final_data, data[:, i * size:(i + 1) * size, :]), 0)

perm = torch.randperm(final_data.size()[0])
final_data = final_data[perm]

shape0, shape2 = final_data.shape[0], final_data.shape[2]
means = torch.zeros([shape0, 1, shape2]).to(device=device)
stds = torch.zeros([shape0, 1, shape2]).to(device=device)

for i in range(shape0):
    for j in range(shape2):
        means[i,0,j] = torch.mean(final_data[i,:,j])
        stds[i,0,j] = torch.std(final_data[i,:,j])

normalized_data = (final_data - means)/stds

final_label = normalized_data[:,1:,:]
final_inputs = normalized_data[:,:-1,:]

def crossvalidate(inputs, labels, stds, means, splits=10, training_splits=400, epoches=2):
    for i in range(splits):
        predictor = NetWork().double()
        len_input = inputs.shape[0]//splits
        len_labels = labels.shape[0]//splits
        training_input = torch.cat((inputs[:i * len_input], inputs[(i+1) * len_input:]), 0)
        training_label = torch.cat((labels[:i * len_labels], labels[(i+1) * len_labels:]), 0)
        test_input = inputs[i * len_input:(i+1) * len_input]
        test_label = labels[i * len_labels:(i+1) * len_labels]
        std = stds[i * len_input:(i+1) * len_input]
        mean = means[i * len_input:(i+1) * len_input]
        error1 = torch.mean(((predictor.predict(test_input) - test_label)[:,:,0])**2).item()
        for epo in range(epoches):
            perm = torch.randperm(training_input.size()[0])
            training_input = training_input[perm]
            training_label = training_label[perm]
            for j in range(training_splits):
                len_input = training_input.shape[0]//training_splits
                len_labels = training_label.shape[0]//training_splits      
                train_input = training_input[j * len_input:(j+1) * len_input]
                train_label = training_label[j * len_labels:(j+1) * len_labels]
                predictor.train(train_input, train_label)
            print("split number " + str(i + 1) + " out of " + str(splits) + ": " + str(round(epo/epoches*100)) + " %")
        plt.plot(predictor.loss_list)
        plt.show()
        error2 = torch.mean(((predictor.predict(test_input) - test_label)[:,:,0])**2).item()
        print("average wrong prediction before " + str(error1))
        print("average wrong prediction after " + str(error2))
        predictions_percent = (((predictor.predict(test_input)[:,:,0] - test_input[:,:,0]) * std[:,:,0]) / (test_input[:,:,0] * std[:,:,0] + mean[:,:,0]))[:,20:]
        truth_percent = (((test_label[:,:,0] - test_input[:,:,0]) * std[:,:,0]) / (test_input[:,:,0] * std[:,:,0] + mean[:,:,0]))[:,20:]
        for i in range(10):
            buy = torch.where(predictions_percent > (i+1)/100, True, False)
            sell = torch.where(predictions_percent < -(i+1)/100, True, False)
            print(torch.mean(truth_percent[buy]).item()) 
            print(torch.mean(-truth_percent[sell]).item())
            print(truth_percent[buy].shape) 
            print(truth_percent[sell].shape)       
            print(truth_percent.shape)  


predictor = NetWork().double().to(device)
crossvalidate(final_inputs, final_label, stds, means)