import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np


# Params
TICKER = 'SPY'
FAST = 10
SLOW = 27
LOOKBACK = 60 # periods, max available


def getData():
    df = yf.download(TICKER)
    df.columns = df.columns.get_level_values(0)
    return df.iloc[-LOOKBACK:,:]


# What do we want our strat to be

def addMovingAverages(df, fast, slow): 
    df[f'{FAST}_ma'] = df['Close'].rolling(fast).mean()
    df[f'{SLOW}_ma'] = df['Close'].rolling(slow).mean()
    plt.plot(df['Close'])
    plt.plot(df[f'{FAST}_ma'])
    plt.plot(df[f'{SLOW}_ma'])
    plt.legend(['Close', f'{FAST}_ma', f'{SLOW}_ma'])
    plt.title('Moving Avgs CrssOvrs '+ TICKER )
    return df.dropna()

def addStrat(df, fast,slow):
    df['Strategy'] = np.where(df[f'{fast}_ma'] > df[f'{slow}_ma'], 1, -1)
    df['Strategy'] = df['Strategy'].shift(1)
    return df


def testStrat(df, ticker, fast, slow):
    df['Asset Returns'] = (1 + df['Close'].pct_change()).cumprod() -1
    df['Strategy Returns'] = (1 + df['Close'].pct_change() * df['Strategy']).cumprod() - 1

    plt.figure()
    plt.plot(df['Asset Returns'])
    plt.plot(df['Strategy Returns'])
    plt.legend([f'{ticker} Cumulative Returns', f'{fast} - {slow} Crossover Strategy Returns'])
    plt.title('Moving Average Crossovers ' + TICKER)
    plt.show()
    return df.dropna()


df = yf.download(TICKER)
df = getData()
df = addMovingAverages(df, FAST, SLOW)
df = addStrat(df, FAST, SLOW)
df = testStrat(df, TICKER, FAST, SLOW)
print(df)