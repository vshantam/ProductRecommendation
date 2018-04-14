#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Sat Apr 14 18:07:52 2018

@author: Shantam Vijayputra
"""

#importing the libraries
import pickle
import pandas as pd
import math
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

#creating class
class Main(object):

    #initialising path with null
    def __init__(self):
        self.path_with_name = None

    #static method to load classifier
    @staticmethod
    def loadclf(path_with_name):
        _type = 'rb'
        return pickle.load(open(path_with_name, _type))

    #static method to load dataframe
    @staticmethod
    def loaddf(path):
        return pd.read_csv(path, encoding='latin-1', engine='python',
                           dialect=None, sep=',')
    
    #creating dictionary to map elements in the coloumn
    @classmethod
    def proddict(cls, prod):
        dict = {}

        for i in range(len(prod)):
            dict[list(prod)[i]] = i + 1
        return dict


if __name__ == '__main__':

    #Ascii art 
    init(strip=not sys.stdout.isatty())
    
    cprint(figlet_format('P R S!', font='starwars'), 'yellow', 'on_red'
           , attrs=['bold'])
    
    #Abbreviation Printing
    print ('## Product  Recommender     System!##\n')

    #creating he object and instantiate it
    obj = Main()
    
    #loading the pandas dataframe
    df = obj.loaddf('Book1.csv')

    #printing the instruction to input
    print ("Please provide the product details that you liked in a single line seperated by space in the following order:\n1.Brand\n2.Product\n3.Model\n4.Color\n5.Price\n6.Rating\n")

    #printing the examples
    print ('E.g.')

    print (df.head(n=5))
    
    #displaying the spelling warning
    print ('''
Please Make sure that  you spell correctly and the product details must be available in our dataset.
''')
    
    #asking for response
    print ('Enter your Response: ')
 
    #running through infinite loop until there is 6 inputs in the response. exactly 6 input is must.
    while True:
        
        #using exceptional handeling to get respone for either python2 and python3 version
        try:
            response = input().strip().split(' ')
        except:
            response = raw_input().strip().split(' ')
        
        #checking the response is propper or not
        if len(response) != 6:
            print ('Response is not propper')
        else:
            break
    #exceptional handeling to create dictionary and map using unique numbers
    try:
        try:

            brand_dict = {
                'Brand1': 1,
                'Brand2': 3,
                'Brand3': 4,
                'Brand4': 2,
                'Brand5': 5,
                }

            colors_dict = {
                'Black': 4,
                'Grey': 3,
                'PInk': 1,
                'Silver': 5,
                'White': 2,
                }

            products_dict = {
                'Camera': 2,
                'Lens': 3,
                'Mobile': 4,
                'T.V': 1,
                }

            models_dict = obj.proddict(set(df['model']))

        except Exception as e:

            print ('Dictionary Failure!')
            print ({}.format(str(e)))

        #variables 
        brand = brand_dict[response[0]]
        product = products_dict[response[1]]
        model = models_dict[response[2]]
        color = colors_dict[response[3]]

        #filter the price because money can be in 13,490 or 13490.we want only float or integer no string or special charecters.
        if ',' in response[4]:
            price = math.ceil(int(response[4].replace(',', '')))
        else:
            price = math.ceil(int(response[4]))

        rating = float(response[5])

        #using exceptional handeling to load trained classifier using python 2 or python3 .
        try:
	    # .pkl extension for python3
              clf = pickle.load(open('clf.pkl', 'rb'))

        except:
            # .sav function for python2
              clf = pickle.load(open('clf.sav', 'rb'))
        
        #creating index to be fitted in the trained classifier and asking for number of recommendations.
        index = clf.kneighbors([[
            brand,
            product,
            model,
            color,
            price,
            rating,
            ]], int(input('No. of recomendations:')),
                return_distance=False)

        #displaying the order and format for the output
        print ('''
Brand \t Product \t Model \t Color \tPrice \t Rating
''')
        #displaying  n recomendations
        for i in index[0]:
            list1 = list(df.iloc[i])
            list2 = [str(x).encode('utf-8','ignore') for x in list1]
            #print (list2)#for python2
            print(list1)#for python3

    except KeyError as  k:

        print ({}.format(str(k)))

    #finished.
    print ('Finished procedure')


			
