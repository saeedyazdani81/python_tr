import MetaTrader5 as mt5

class Trader:
	def __init__(self, user_name , server ):
		self.user_name = user_name
		self.server = server
	def initialize_mt5(self):
		if not mt5.initialize(login=self.user_name , server=self.server):
			print("initialize faild." , mt5.last_error())
			quit()
		return True
	def get_terminal_info(self):
		return mt5.terminal_info()._asdict()
	def get_candles(self, symbol, tm, start, numbers):
		return mt5.copy_rates_from_pos(symbol, tm, start, numbers)
	


	def open_position(self, symbol:str, lot:float, position_type:str , deviation = 20):
		point = mt5.symbol_info(symbol).point
		if position_type == 'buy':
			position_type = mt5.ORDER_TYPE_BUY
			price = mt5.symbol_info_tick(symbol).ask
			tp = price + 100 * point
			sl = price - 100 * point
		elif position_type == 'sell':
			position_type = mt5.ORDER_TYPE_SELL
			price = mt5.symbol_info_tick(symbol).bid
			tp = price - 100 * point
			sl = price + 100 * point
		else:
			print("type is false")
			quit()
		request = {
		    "action": mt5.TRADE_ACTION_DEAL,
		    "symbol": symbol,
		    "volume": lot,
		    "type": position_type,
		    "price": price,
		    "sl":sl,
		    "tp":tp,
		    "deviation": deviation,
		    "magic": 234000,
		    "comment": "python script open",
		    "type_time": mt5.ORDER_TIME_GTC,
		    "type_filling": mt5.ORDER_FILLING_RETURN,
		}
		# send a trading request
		result = mt5.order_send(request)
		print(result)
	
	
	def close_positionByTicket(self,symbol, ticket):
		if mt5.Close(symbol, ticket = ticket):
			return True
		else:
			return False