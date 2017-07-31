# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 22:00:04 2017

@author: hassan
"""
import pandas_datareader.oanda as oanda
import pandas_datareader.data as web
import quandl 
#import requests_cache
import datetime

#import matplotlib.pyplot as plt
#import datetime as dt
# Mehrzad
class IMarketData:
   
    def __init__(self,data_source,data_path,API_key=None):
        self.data_source=data_source
        self.data_path=data_path
        self.API_key=API_key
        self.expire_after = datetime.timedelta(days=3)
        self.session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=self.expire_after)



        
    def get_data(self,ticker_set,start_date,end_date=None):
        #expire_after = datetime.timedelta(days=3)
       # session = requests_cache.CachedSession(cache_name='cache', backend='sqlite',expire_after=expire_after)
        df_dic={}
        for ticker in ticker_set:
            df=web.DataReader(ticker,self.data_source,start_date,end_date)
            ticker=ticker.replace('/','_')
            df_dic.update({ticker:df})
        return df_dic
    
    def plot_data(self,df_dic):
        
        for key in df_dic:
            df_dic[key].plot(grid=True,title=key)
           
            
    def export_data(self,df_dic):
        for key in df_dic:
            df_dic[key].to_csv(path_or_buf=self.data_path+key+'.csv')

class MarketDataGoogle(IMarketData):
    def __init__(self,data_path):
        IMarketData.__init__(self,"google",data_path)       

class MarketDataFRED(IMarketData):
    def __init__(self,data_path):
        IMarketData.__init__(self,"fred",data_path)
        
class MarketDataOanda(IMarketData):
    def __init__(self,data_path):
        IMarketData.__init__(self,"oanda",data_path) 
    def get_data(self,ticker_set,start_date,end_date=None):
        df_dic={}
        for ticker in ticker_set:
            #quote_currency = "USD"
            #base_currency = ticker
            df=oanda.get_oanda_currency_historical_rates(start_date,end_date,base_currency=ticker) 
            #df=web.DataReader(ticker,self.data_source,start_date,end_date)
            df_dic.update({ticker:df})
        return df_dic
        
class MarketDataQuandl(IMarketData):
    def __init__(self,data_path):
        IMarketData.__init__(self,"quandl",data_path)
    def get_data(self,ticker_set,start_date,end_date=None):
        df_dic={}
        for ticker in ticker_set:
            df=quandl.get(ticker,start_date=start_date,end_date=end_date) 
            ticker=ticker.replace('/','_')
            df_dic.update({ticker:df})
        return df_dic
