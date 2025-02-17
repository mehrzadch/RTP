# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 16:12:16 2017

@author: hassan
"""

import numpy as np
import pandas as pd

def create_sharpe_ratio(returns, periods=252,interest_rate=0):
    """
    Create the Sharpe ratio for the strategy, based on a
    Parameters:
    returns - A pandas Series representing period percentage returns.
    periods - Daily (252), Hourly (252*6.5), Minutely(252*6.5*60) etc.
    """
    return (np.sqrt(periods) * (np.mean(returns))-interest_rate) / np.std(returns)

def create_drawdowns(pnl):
    """
    Calculate the largest peak-to-trough drawdown of the PnL curve
    as well as the duration of the drawdown. Requires that the
    pnl_returns is a pandas Series.
    Parameters:
    pnl - A pandas Series representing period percentage returns.
    Returns:
    drawdown, duration - Highest peak-to-trough drawdown and duration.
    """
    # Calculate the cumulative returns curve
    # and set up the High Water Mark
    hwm = [0]
    
    # Create the drawdown and duration series
    idx = pnl.index
    drawdown = pd.Series(index = idx)
    duration = pd.Series(index = idx)
    
    # Loop over the index range
    for t in range(1, len(idx)):
        hwm.append(max(hwm[t-1], pnl[t]))
        drawdown[t]= (hwm[t]-pnl[t])
        duration[t]= (0 if drawdown[t] == 0 else duration[t-1]+1)
    return drawdown, drawdown.max(), duration.max()