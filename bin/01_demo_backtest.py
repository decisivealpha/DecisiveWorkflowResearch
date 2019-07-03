from backtesting import Backtest, Strategy
from backtesting.lib import crossover

from backtesting.test import SMA, GOOG

class SmaCross(Strategy):
    n1 = 10
    n2 = 30

    def init(self):
        self.sma1 = self.I(SMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()


if __name__ == '__main__':
    # Windows: avoid concurrent.futures.process.BrokenProcessPool by wrapping in this if __name__ section
    bt = Backtest(GOOG, SmaCross, cash=10000, commission=.002)

    output = bt.run()
    print(output)
    bt.optimize(n1=range(5, 20, 5),
                n2=range(10, 100, 10),)
    bt.plot()
