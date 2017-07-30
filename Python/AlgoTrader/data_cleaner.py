# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 22:58:46 2017

@author: hassan
"""

import pandas as pd
import configuration as conf

def load_data():
    dt=pd.read_csv(conf.hs_data+"\YHOO.csv")
    return dt
def clean_data(dt):
    pass
def update_hsDatabase(df):
    pd.to_csv(df)
