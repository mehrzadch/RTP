# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 18:56:26 2017

@author: hassan
"""
import pandas as pd
import datetime as dt

class Portfolio:
    def __init__(self,name,asset_set):
        self.name=name
        self.asset_set=asset_set

    def valuation(self,market_price):
        value=0
        for asset in self.asset_set:
            value=value+market_price.price[asset.ticker]*asset.number
        return (value,market_price.unit,market_price.date)

class Asset:
    def __init__(self,ticker,number):
        self.ticker=ticker
        self.number=number


class MarketPrice:
     def __init__(self,price,date="current", unit="GBP"):
        self.price=price
        self.date=date
        self.unit=unit

        
    