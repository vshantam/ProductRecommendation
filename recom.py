# -*- Dataset encoding: Latin-1 -*-
"""
Created on Sat Apr 14 13:24:47 2018

@author: Shantam Vijayputra
"""

import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import pickle


class Predict(object):

    def __init__(self):
        self.path = None

    @staticmethod
    def createset(dataframe, colname):
        return set(dataframe[colname])

    @classmethod
    def loaddata(cls, path):
        return pd.read_csv(path, sep =",", encoding="latin-1", engine="python", dialect=None, na_filter=True)

    @classmethod
    def proddict(cls, prod):
        dict = {}

        for i in range(len(prod)):
            dict[list(prod)[i]]= i+1
        return dict

    @classmethod
    def intprice(cls, prices):
        i: int
        for i in range(prices.shape[0]):
            if "," in str(prices[i]):
                prices[i] = int(prices[i].replace(",", ""))
        return prices

    @classmethod
    def save_clf(self, clf, path_with_name, _type):

        # dumping the data
        return pickle.dump(clf, open(path_with_name, _type))



if __name__=="__main__":

    obj = Predict()

    df = obj.loaddata("Book1.csv")

    brands = obj.createset(df,'Brand')
    products = obj.createset(df,'Product')
    models = obj.createset(df,'model')
    colors = obj.createset(df,'Color')
    prices = df['Price']
    ratings =  df['Rating']


    brand_dict = obj.proddict(brands)
    products_dict = obj.proddict(products)
    models_dict = obj.proddict(models)
    colors_dict = obj.proddict(colors)
    prices = obj.intprice(prices)

    dictlist = [brand_dict, products_dict, models_dict, colors_dict, prices, ratings]

    new_data_frame = np.zeros(df.shape)

    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            if j <=3:
                new_data_frame[i][j] = dictlist[j][df.iloc[i][j]]
            else:
                new_data_frame[i][j] =  df.iloc[i][j]

    algorithms = ["auto", "ball_tree", "kd_tree", "brute"]

    for i in algorithms:

        clf = NearestNeighbors(n_neighbors=5, algorithm=algorithms[0]).fit(new_data_frame)
        distances, indices = clf.kneighbors(new_data_frame)

    path_with_name = "C:/Users/Shantam Vijayputra/Desktop/intern/clf.pkl"
    _type = "wb"
    obj.save_clf(clf, path_with_name, _type)

    
