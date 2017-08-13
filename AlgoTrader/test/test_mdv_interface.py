# -*- coding: utf-8 -*-

import unittest 
import mdv_interface as mdv
#import datetime as dt
class TestMDVInterface(unittest.TestCase):
    
    def test_google(self):
        data_path="..\\DataBase\\HistoricalData\\Google\\"
        mkd=mdv.MarketDataGoogle(data_path)
        ticker_set=["BARC","HSBA",'STAN']
        start, end='2010-01-01','2015-01-01'
        dflist=mkd.get_data(ticker_set,start,end)
        #mkd.plot_data(dflist)
        mkd.export_data(dflist)
        return dflist
    def test_fred(self):
        data_path="..\\DataBase\\HistoricalData\\FRED\\"
        mkd=mdv.MarketDataFRED(data_path)
        ticker_set=["DEXUSEU","DEXUSUK",'DEXJPUS']
        start, end='2010-01-01','2015-01-01'
        dflist=mkd.get_data(ticker_set,start,end)
       # mkd.plot_data(dflist)
        mkd.export_data(dflist)
        return dflist
    
    def test_oanda(self):
        data_path="..\\DataBase\\HistoricalData\\Oanda\\"
        mkd=mdv.MarketDataOanda(data_path)
        ticker_set=["GBP","EUR",'JPY']
        start, end='2010-01-01','2015-01-01'
        dflist=mkd.get_data(ticker_set,start,end)
        #mkd.plot_data(dflist)
       # mkd.export_data(dflist)
        return dflist
    
    def test_Quandl(self):
        data_path="..\\DataBase\\HistoricalData\\Quandl\\"
        mkd=mdv.MarketDataQuandl(data_path)
        ticker_set=['FRED/GDP','LSE/HUKX','LSE/BARC']
        start, end='2010-01-01','2015-01-01'
        dflist=mkd.get_data(ticker_set,start,end)
        #mkd.plot_data(dflist)
        mkd.export_data(dflist)
        return dflist

if __name__ == '__main__':
    
 unittest.main()