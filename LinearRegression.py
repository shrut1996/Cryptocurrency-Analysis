#!/usr/bin/python

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from quandl import get


def run_ordinary_least_squares(dates, prices):
    exponent = 2
    intercept = np.column_stack((dates, prices ** exponent))
    constant = sm.add_constant(intercept)
    regression = sm.OLS(prices, constant).fit()
    print(regression.summary())
    return regression


def plot_regression_line(regression):
    fig, ax = plt.subplots(figsize=(20,10))
    ax.plot(dates, prices, 'r-', label="Values ")
    ax.plot(dates, regression.fittedvalues, 'b--', label="Regression line ")
    plt.xlabel('Time')
    plt.ylabel('Normalized Values')
    ax.legend(loc='best')
    plt.grid(True)
    plt.show()


btc = get("BITFINEX/BTCUSD", authtoken="sff8MFpE7wRPc3cz5q3Y")
dates = np.arange(1, btc.index.nunique() + 1, 1)
prices = btc['Mid'].values

regression = run_ordinary_least_squares(dates, prices)
plot_regression_line(regression)
