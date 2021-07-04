import torch
from torch.nn import Module, Conv2d, MaxPool2d, Linear, MSELoss, LSTM, LeakyReLU, Sequential, ReLU, Sigmoid
from torch.optim import Adam
import matplotlib.pyplot as plt
from agent import NetWork
from torch import device as devicer, cuda
import pickle
from saver import loadagent
device = devicer('cuda' if cuda.is_available() else 'cpu')
from Normalize_data import normalize

predictor = loadagent("test4")
all_data = torch.load('DayliData.pt').to(device=device)
normalized_data, normalized_simulate, mins, maxes = normalize(all_data = all_data, train_start = 2100, train_end = 2000, test_start = 2000, test_end = 1001, splits=4)
print(normalized_data.shape)
money = 100
splits = 20
normal_normalize = False
five_features = False
if normal_normalize:
    with torch.no_grad():
        for j in range(splits):
            len_input = normalized_data.shape[0]//splits
            predictor.prepare_hidden(normalized_data[j * len_input:(j+1) * len_input])
            for i in range(normalized_simulate.shape[1] - 1):
                true_values = normalized_simulate[j * len_input:(j+1) * len_input, i, :].unsqueeze(1)
                true_prices = true_values[:,0,3]
                output = predictor.predict_from_hidden(true_values)
                expected_percent_difs = (output[:,0,3] - true_prices)/(true_prices + means[j * len_input:(j+1) * len_input,0,3])
                true_difs = (normalized_simulate[j * len_input:(j+1) * len_input, i + 1, 3] - true_prices) * stds[j * len_input:(j+1) * len_input,0,3]
                #money += money/100 * torch.sum(expected_percent_difs * true_difs)
                money += money/100 * torch.sum(true_difs[torch.where(expected_percent_difs > 0.2, True, False)])
                #money -= money/100 * torch.sum(true_difs[torch.where(expected_percent_difs < -0.2, True, False)])
                #money += 1 * money/100 * torch.sum(true_difs[torch.where(expected_percent_difs > 0.01, True, False)])
                print("Current money " + str(round(money.item()*100)/100) + " after " + str(100 * j/splits) + " %")
elif five_features:
    buys, sells = 0, 0
    with torch.no_grad():
        for j in range(splits):
            len_input = normalized_data.shape[0]//splits
            predictor.prepare_hidden(normalized_data[j * len_input:(j+1) * len_input])
            for i in range(normalized_simulate.shape[1] - 1):
                true_values = normalized_simulate[j * len_input:(j+1) * len_input, i, :].unsqueeze(1)
                true_prices = true_values[:,0,3]
                output = predictor.predict_from_hidden(true_values)
                expected_percent_difs = (output[:,0,3] - true_prices)/(true_prices + mins[j * len_input:(j+1) * len_input,0,3])
                true_difs = (normalized_simulate[j * len_input:(j+1) * len_input, i + 1, 3] - true_prices)
                #money += torch.sum(true_difs)
                money += torch.sum(true_difs[torch.where(expected_percent_difs > 0, True, False)])
                money -= torch.sum(true_difs[torch.where(expected_percent_difs < 0, True, False)])
                print("Current money " + str(round(money.item()*100)/100) + " after " + str(100 * j/splits) + " %")
else:
    with torch.no_grad():
        for j in range(splits - 1):
            len_input = normalized_data.shape[0]//splits
            predictor.prepare_hidden(normalized_data[j * len_input:(j+1) * len_input,:,3].unsqueeze(2))
            for i in range(normalized_simulate.shape[1] - 1):
                true_values = normalized_simulate[j * len_input:(j+1) * len_input, i, :].unsqueeze(1)
                true_prices = true_values[:,0,3]
                output = predictor.predict_from_hidden(true_values[:,:,3].unsqueeze(2))
                expected_percent_difs = (output[:,0,0] - true_prices)/(true_prices + mins[j * len_input:(j+1) * len_input,0,3])
                true_difs = (normalized_simulate[j * len_input:(j+1) * len_input, i + 1, 3] - true_prices)
                #money += torch.sum(true_difs)
                money += torch.sum(true_difs[torch.where(expected_percent_difs > 0.0, True, False)])
                money -= torch.sum(true_difs[torch.where(expected_percent_difs < -0.0, True, False)])
                print("Current money " + str(round(money.item()*100)/100) + " after " + str(100 * j/splits) + " %")


#final_inputs = normalized_data[:,:-1,:]
#final_label = normalized_data[:,1:,:]


