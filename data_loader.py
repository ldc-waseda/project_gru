import os
import pickle
import numpy as np
import pandas as pd
import random
from sklearn.model_selection import train_test_split
from global_param import *
class DataLoader():
    def __init__(self,):
        self.processed_data = None
        pass
    def transfer2pixel(self,):
        '''
        input: original pos file
        input size: len x [frame, id, pos_y, pos_x]
        return: pixeled pos file
        return size: len x [frame, id, pos_y, pos_x]
        '''
        pass

    def transfer2image(self):
        '''
        input: pixeled pos file
        input size: len x [frame, id, pos_y, pos_x]
        return: pixeled pos file
        return size: len x [frame, id, [image_H,image_W]]
        '''
        pass

    def split_dataset(self):
        '''
        input: self.processed_data
        input size: len x [20 x [id, x, y]]
        return:
        '''
        X = self.processed_data[:, 0:8]
        y = self.processed_data[:, 8::]
        X_t, X_v, y_t, y_v = train_test_split(X,y,test_size=0.1)
        X_train, X_test, y_train, y_test = train_test_split(X_t,y_t,test_size=0.3)
        return X_train, y_train, X_test, y_test, X_v, y_v

    def load_preprocess(self,data_file):
        print("Loading dataset: ", DEMO_DATASET)
        print("Loading data from file path ", data_file)
        f = open(data_file, 'rb')
        self.raw_data = pickle.load(f)
        f.close()