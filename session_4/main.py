from trader import Trader
bot = Trader(5015577304 , 'MetaQuotes-Demo')
if bot.initialize_mt5():
	symbol = "EURUSD" #str
	lot = 0.01 
	position_type = 'buy'
	tm = 1
	numbers = 50
	start = 0
	# candles = bot.get_candles(symbol , tm , start, numbers)
	# bot.open_position(symbol, lot, 'buy')
	bot.close_positionByTicket(symbol , 50544852407)