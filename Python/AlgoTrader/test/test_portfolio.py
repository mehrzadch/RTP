# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 20:01:54 2017

@author: hassan
"""
import unittest 
import portfolio as pf
class Test_Portfolio(unittest.TestCase):
    
    def test1(self):
        as1=pf.Asset('db',10)
        as2=pf.Asset('cs',20)
        price=pf.MarketPrice({'db':2,'cs':3})
        port1=pf.Portfolio('ptest1',[as1,as2])
        res=port1.valuation(price)
        self.assertEqual(res[0],80)
        

if __name__ == '__main__':
   unittest.main()