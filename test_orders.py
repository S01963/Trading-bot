import orders
import time
import MetaTrader5 as mt5

mt5.initialize()

orders.STOPLOSS = 100
orders.TAKEPROFIT = 500
orders.open_position("EURUSD", 0.01, "buy")
time.sleep(5)

orders.open_position("EURGBP", 0.01, "sell")