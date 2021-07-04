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

class trainer():
    def train(self, name="trader6", data='DayliData.pt', predict="test7", batch_splits=50, epoches=100, time_splits = 3, ts = 1100, te = 1000, tes = 1000, tee = 1):
        all_data = torch.load(data).to(device=device) #yo
        trader = RL_agent()
        predictor = loadagent(predict)
        # OBS SET SPLITS = 10
        normalized_data, normalized_simulate, mins, maxes = normalize(all_data = all_data, train_start = ts, train_end = te, test_start = tes, test_end = tee, splits = time_splits)
        print(normalized_data.shape, normalized_simulate.shape)
        for k in range(epoches):
            perm = torch.randperm(normalized_data.size()[0])
            prepare_dat = normalized_data[perm]
            print(prepare_dat.shape)
            train_dat = normalized_simulate[perm]
            miner = mins[perm]
            maxer = maxes[perm]
            for j in range(batch_splits):
                len_input = prepare_dat.shape[0]//batch_splits
                with torch.no_grad():
                    predictor.prepare_hidden(prepare_dat[j * len_input:(j+1) * len_input,:,3].unsqueeze(2))
                    hidden_state = predictor.output_hidden(train_dat[j * len_input:(j+1) * len_input,:,3].unsqueeze(2))
                    hidden_state = torch.zeros(hidden_state.shape).to(device)
                stocks = torch.zeros(len_input).to(device).double()
                money = torch.rand(len_input).to(device).double() * 35000 / 5000 + 1
                current_min = miner[j * len_input:(j+1) * len_input, 0, 3]
                current_max = maxer[j * len_input:(j+1) * len_input, 0, 3]
                last = False
                for i in range(train_dat.shape[1] - 1):
                    if i == train_dat.shape[1] - 2:
                        last = True
                    true_values = train_dat[j * len_input:(j+1) * len_input, i, :].unsqueeze(1)
                    true_values_next = train_dat[j * len_input:(j+1) * len_input, i+1, :].unsqueeze(1)
                    RL_input = torch.cat((hidden_state[:,i].unsqueeze(0), true_values.transpose(0,1), torch.clone(stocks).unsqueeze(0).unsqueeze(2), torch.clone(money).unsqueeze(0).unsqueeze(2)), 2).squeeze(0).detach()
                    #RL_input = torch.cat((hidden_state[:,i].unsqueeze(0), true_values.transpose(0,1), torch.clone(stocks).unsqueeze(0).unsqueeze(2)), 2).squeeze(0).detach()
                    actions = trader.choose(RL_input)
                    temp = torch.clone(actions)
                    rewards, stocks, money, extra = self.calculate_reward(actions, true_values[:,0,3].double(), stocks, current_min, current_max, last, money)
                    RL_next = torch.cat((hidden_state[:,i+1].unsqueeze(0), true_values_next.transpose(0,1), torch.clone(stocks).unsqueeze(0).unsqueeze(2), torch.clone(money).unsqueeze(0).unsqueeze(2)), 2).squeeze(0).detach()
                    #RL_next = torch.cat((hidden_state[:,i+1].unsqueeze(0), true_values_next.transpose(0,1), torch.clone(stocks).unsqueeze(0).unsqueeze(2)), 2).squeeze(0).detach()
                    trader.train(RL_next, rewards, actions, extra)
                print("trained " + str(round(10000 * ((j + 1)/(batch_splits * epoches) + k/epoches))/100) + " percent")
            saveAgent(trader, name)
            trader.show_return()
            
        trader.show_return_forever()

    def calculate_reward(self, actions, prices, stocks, mins, maxes, last, money, fee=19):
        prices = prices * (maxes - mins) + mins
        actions = torch.clone(actions)
        actions[money < 0] = 0
        #print(stocks, actions, prices)
        rewards = torch.zeros(actions.shape).to(device=device).double()
        rewards[actions == 0] = (100 * prices * stocks)[actions == 0] - fee
        rewards[actions == 2] = -5000 - fee
        rewards[actions == 3] = -10000 - fee
        rewards[actions == 4] = -20000 - fee

        money[actions == 0] += ((100 * prices * stocks)[actions == 0] - fee)/5000
        money[actions == 2] -= (5000 + fee)/5000
        money[actions == 3] -= (10000 + fee)/5000
        money[actions == 4] -= (20000 + fee)/5000

        stocks[actions == 0] = 0
        stocks[actions == 2] += (5000 / prices[actions == 2])/100
        stocks[actions == 3] += (10000 / prices[actions == 3])/100
        stocks[actions == 4] += (20000 / prices[actions == 4])/100
        #stocks *= 0.999
        #print(stocks, rewards)
        if last:
            extra = (100 * prices * stocks) - fee
            return rewards/5000, stocks, money, extra/5000
        return rewards/5000, stocks, money, None





