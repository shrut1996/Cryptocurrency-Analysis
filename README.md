# Cryptocurrency analysis

Cryptocurrencies are nowadays starting to be seen by investors as a new asset class despite being said it to be in a bubble by many experts from big financial institutions. Many questions are being asked like how do Bitcoin markets behave? What are the causes of the sudden spikes and dips in cryptocurrency values? Are the markets for different altcoins inseparably linked or largely independent? How can we predict what will happen next? 
Well this project analyses the behaviour of cryptocurrencies (only bitcoin has been looked upon till now) and tries to mine any relations between the various global financial instruments. Further using these correlations, I have tried to forecast the bitcoin to usd price based on historical values. However, in general I can claim, through the findings of this project, that bitcoins have a very negligible dependency or even influence in this context on other securities.

## Aim

Collecting and analysing market data, retrieved using the yahoo finance API, with the help of visualisations. Finding any relation between cryptocurrencies and among the rest of the asset classes then forecasting its value using regression techniques.

## Findings

* Correlation between Bitcoin and some top market indices

| Market Index    | Factor        |
| :-------------: |:-------------:|
| NIKKEI          | 0.1308        |
| EURONEXT        | 0.1549        |
| NASDAQ          | 0.2719        |
| FTSE            | 0.3467        |
| SSE             | 0.0564        |
| NYSE            | 0.0711        |


* Correlation between Bitcoin and some safe haven assets

| Asset              | Factor        |
| :----------------: |:-------------:|
| GOLD               |  0.2077       |
| CHINA Internet ETF |  0.0964       |
| FIDELIY MF         |  0.1665       |
| COLUMBIA MF        |  0.1565       |
| GLOBAL EX-US PROP. | -0.0291       |

## References

> https://www.signalplot.com/what-is-bitcoins-correlation-with-other-financial-assets/

> Financial dataset collected from https://finance.yahoo.com
