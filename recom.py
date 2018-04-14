# -*- Dataset encoding: Latin-1 -*-
"""
Created on Sat Apr 14 13:24:47 2018

@author: Shantam Vijayputra
"""

#importing library
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import pickle

#creating class
class Predict(object):

    #default path as null
    def __init__(self):
        self.path = None

    #static method to create set of elements in a column
    @staticmethod
    def createset(dataframe, colname):

        return set(dataframe[colname])
    
    #creating classmethod to load dataset
    @classmethod
    def loaddata(cls, path):

        return pd.read_csv(path, sep =",", encoding="latin-1", engine="python", dialect=None, na_filter=True)

    #classmethod to create dictionary
    @classmethod
    def proddict(cls, prod):
        dict = {}

        for i in range(len(prod)):
            dict[list(prod)[i]]= i+1

        return dict

    #classmethod to format price value into proper integer format
    @classmethod
    def intprice(cls, prices):
        for i in range(prices.shape[0]):
            if "," in str(prices[i]):
                prices[i] = int(prices[i].replace(",", ""))

        return prices

    #classmethod to save trained model
    @classmethod
    def save_clf(self, clf, path_with_name, _type, n):

        # dumping the data
        return pickle.dump(clf, open(path_with_name, _type), protocol = n)



if __name__=="__main__":

    #reating the object
    obj = Predict()
    
    #loading the pandas dataframe
    df = obj.loaddata("Book1.csv")
    
    #creating sets of each column for unique elements
    brands = obj.createset(df,'Brand')
    products = obj.createset(df,'Product')
    models = obj.createset(df,'model')
    colors = obj.createset(df,'Color')
    prices = df['Price']
    ratings =  df['Rating']

    #creating column wise dictionary to map each value
    brand_dict = obj.proddict(brands)
    products_dict = obj.proddict(products)
    models_dict = obj.proddict(models)
    colors_dict = obj.proddict(colors)
    prices = obj.intprice(prices)
    
    #list of dictionary
    dictlist = [brand_dict, products_dict, models_dict, colors_dict, prices, ratings]
  
    #new matrix in which algorithm is going to perform
    new_data_frame = np.zeros(df.shape)

    #mapping the values and copying to new matrix
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            if j <=3:
                new_data_frame[i][j] = dictlist[j][df.iloc[i][j]]
            else:
                new_data_frame[i][j] =  df.iloc[i][j]

    #list of algorithm that can be used
    algorithms = ["auto", "ball_tree", "kd_tree", "brute"]
    
    #testing with each algorithm
    for i in algorithms:

        clf = NearestNeighbors(n_neighbors=5, algorithm=algorithms[0]).fit(new_data_frame)
        distances, indices = clf.kneighbors(new_data_frame)
 
   #saving the trained classifier
    path_with_name = ["clf.pkl", "clf.sav"]
    _type = "wb"
    #obj.save_clf(clf, "clf.sav", _type, 2) #for python2
    obj.save_clf(clf, "clf.pkl", _type, 3) #for python3

###finished ###
