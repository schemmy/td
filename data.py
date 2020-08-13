import pandas as pd
import json
import logging
import talib


class StockHistory():

	def __init__(self, df, symb):

		self.o0 = df
		self.symb = symb


	def getSymb(self):

		return self.symb


	def getDf(self, begin, end):

		if begin == '' and end == '':
			return self.o0

		return self.o0[(self.o0['datetime'] >= begin) & (self.o0['datetime'] <= end)]


	def getHighestPrice(self, sinceIPO=False, daysBack=500, priceToUse='close'):

		if sinceIPO:
			return self.o0[priceToUse].max()

		if (len(self.o0) < daysBack):
			logging.warning('Stock does not have %d days since IPO.' %daysBack)

		return self.o0[priceToUse].iloc[-daysBack:].max()


	def getEMA(self, period=21, priceToUse='close'):

		colName = 'ema%d' %period
		if colName in self.o0.columns:
			return self.o0[colName]

		self.o0[colName] = talib.EMA(self.o0[priceToUse], timeperiod=period)
		return self.o0[colName]


	def getSMA(self, period=21, priceToUse='close'):
		
		colName = 'sma%d' %period
		if colName in self.o0.columns:
			return self.o0[colName]

		self.o0[colName] = talib.SMA(self.o0[priceToUse], timeperiod=period)
		return self.o0[colName]



