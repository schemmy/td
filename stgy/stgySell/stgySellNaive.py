from .stgySell import StgySell

class StgySellNaive(StgySell):

    def __init__(self, multiStockDTO, actionBook, balanceBook, lastDayIdx):

        StgySell.__init__(self, multiStockDTO, actionBook, balanceBook)
        self.name = 'StgySellNaive'
        self.lastDayIdx = lastDayIdx


    def shouldSell(self, symb, date, dateIdx):

        if self.lastDayIdx == dateIdx:
            return self.balanceBook.getSymbShares(symb)

        return 0


