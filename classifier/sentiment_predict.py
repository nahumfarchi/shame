# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 10:13:03 2018

@author: nafarchi
"""

import pickle
from sentiment_train import *

def predict(sentences, model_path):
    """ 
    Returns a list of sentiment predictions using the model given in model_path.
    0 is a negative sentiment,
    1 is a positive sentiment.
    """
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
        labels = model.predict(sentences)
        return ['neg' if l==1 else 'pos' for l in labels]

if __name__ == '__main__':
    MODEL_PATH = '..\\models\\kaggle-toxic-comments-00.pickle'
    SENTENCES = ['You are stupid', 
                 'You suck', 
                 'Fat idiot', 
                 'You are a bitch!',
                 'Oshri is a traitor!',
                 'Happy birthday!', 
                 'You are the greatest', 
                 'That''s awesome',
                 'Fuck you son of a bitch']
    labels = predict(SENTENCES, MODEL_PATH)
    print("labels : {}".format(labels))
    
        
    