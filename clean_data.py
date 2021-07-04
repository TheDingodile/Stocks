import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
from datetime import date
import numpy as np
import matplotlib.pyplot as plt
import torch
from sklearn import preprocessing
import pickle

def get_data(stocks=['TSLA']):
    # import data
    final = torch.tensor([])
    normalizes = dict()
    l = 0
    for stock in stocks:
        l += 1
        ticker = yf.Ticker(stock)
        try:
            tsla_df = ticker.history(period='10y', interval='1d')
        except:
            continue
        # clean data
        tsla_df = tsla_df.reset_index()
        pre_year, pre_month, pre_day = None, None, None
        difs = [1]
        for index, row in tsla_df.iterrows():
            timestamp = str(row[0])
            year, month, day = int(timestamp[:4]), int(timestamp[5:7]), int(timestamp[8:10])
            if pre_year != None:
                dif = date(year, month, day) - date(pre_year, pre_month, pre_day)
                difs.append(int(str(dif)[0]))
            pre_year, pre_month, pre_day = year, month, day
        n = tsla_df.columns[0]
        tsla_df.drop(n, axis = 1, inplace = True)
        n = tsla_df.columns[-1]
        tsla_df.drop(n, axis = 1, inplace = True)
        n = tsla_df.columns[-1]
        tsla_df.drop(n, axis = 1, inplace = True)
        difs = [x - 1 for x in difs]

        data = tsla_df.to_numpy() 
        # plt.plot(data[:,3])
        # plt.plot(data[:,-1]*10)
        # plt.show()

        if data.shape[0] <= 2500:
            continue
        k = 0
        for i in range(len(difs)):
            for j in range(difs[i]):
                data = np.insert(data, i + k, data[i + k - 1] + (j + 1) * (data[i + k] - data[i + k - 1])/(difs[i] + 1), 0)
                k += 1
        #normalizes[stock] = (np.std(data, axis=0), np.mean(data, axis=0))
        #data = (data - normalizes[stock][1]) / normalizes[stock][0]
        #plt.plot(data[:,0])
        #plt.show()
        torcher = torch.tensor(data[-2500:])
        if torch.sum(torcher.isnan()) == 0:
            final = torch.cat((final, torcher.unsqueeze(0)),0)
        if l % 50 == 0:
            print("preparation of data " + str(round(l/len(stocks)*100)) + " percent")
            print(final.shape)
    return final, normalizes

def read_data(name = 'DayliData5ynosplit.pt'):
    names = pd.read_csv(r'stock_names.csv')
    names = names[names.columns[0]].to_numpy()
    #names = names[:500]
    data, normalizes = get_data(stocks=names)
    #pickle.dump(normalizes, open("normalizes.pkl", "wb"))
    torch.save(data, name)
    print(data.shape)
    return name