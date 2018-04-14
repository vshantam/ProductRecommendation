# -*- Dataste encoding: utf-8 -*-
"""
Created on Sat Apr 14 18:07:52 2018

@author: Shantam Vijayputra
"""
import pickle
import pandas as pd
import math
import sys
from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format

class Main(object):
    
    def __init__(self):
        self.path_with_name = None
        
    @staticmethod
    def loadclf(path_with_name):
        _type = "rb"
        return pickle.load(open(path_with_name,_type))
    
    @staticmethod
    def loaddf(path):
        return pd.read_csv(path, encoding="latin-1", engine="python", dialect=None, sep=",")

    @classmethod
    def proddict(cls, prod):
        dict = {}

        for i in range(len(prod)):
            dict[list(prod)[i]]= i+1
        return dict

     
        
if __name__ == "__main__":

    init(strip=not sys.stdout.isatty()) 
    cprint(figlet_format('P R S!', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])
    print("## Product  Recommendor     System!##\n")
 
    obj = Main()
    
    df = obj.loaddf("Book1.csv")
    print("Please provide the product details that you liked in a single line seperated by space in the following order:\n1.Brand\n2.Product\n3.Model\n4.Color\n5.Price\n6.Rating\n");
    print("E.g.")
    print(df.head(n = 5))
    print("\nPlease Make sure that  you spell correctly and the product details must be available in our dataset.\n")
    print("Enter your Response: ")

    while(True):
        
        response = input().strip().split(" ")
    
        if len(response) != 6:
            print({}.format("Response is not propper"))
        
        else:
            break
        
        
    try:
        try:
            
            brand_dict = {'Brand1': 1, 'Brand2': 3, 'Brand3': 4, 'Brand4': 2, 'Brand5': 5}
            colors_dict = {'Black': 4, 'Grey': 3, 'PInk': 1, 'Silver': 5, 'White': 2}
            products_dict = {'Camera': 2, 'Lens': 3, 'Mobile': 4, 'T.V': 1}
            models_dict = obj.proddict(set(df['model']))
            
        except Exception as e:
            print("Dictionary Failure!")
            print({}.format(str(e)))
        
        brand = brand_dict[response[0]];
        product = products_dict[response[1]];
        model = models_dict[response[2]];
        color = colors_dict[response[3]];
        
        if "," in response[4]:
            price = math.ceil(int((response[4].replace("," , ""))))
        else:
            price = math.ceil(int((response[4])))
            
        rating = float(response[5])
        
        clf = pickle.load(open("clf.pkl","rb"))
        
        index = clf.kneighbors([[brand, product, model, color, price, rating]], int(input("No. of recomendations:").strip()), return_distance=False)
        
        for i in index[0]:
            print(list(df.iloc[i]))
            
    except KeyError as k:
        print({}.format(str(k)))
        
    print("Finished procedure")

            
        
            
