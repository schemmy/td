import pandas as pd
from config.config import *
from dto import *

class DataLoader:

    def __init__(self, symbs, firstDay=''):

        self.symbs = symbs
        self.firstDay = firstDay


    def loadDailyData(self):

        dailyData = {}

        dailyDataPath = datapath / 'historical_daily/single/'
        loadFormat = {'open': 'float', 'high': 'float', 'low': 'float', 'close': 'float',
                           'datetime': 'str', 'symb': 'str'}

        logger.info('DataLoader: loading daily data...')

        lastDates = set()
        for idx, symb in enumerate(tqdm(self.symbs)):

            filePath = dailyDataPath / '{}.csv'.format(symb)
            if not path.exists(filePath):
                logger.warning('DataLoader: %s data not exist!' %symb)
                continue

            oSymb = pd.read_csv(filePath, dtype=loadFormat)

            sh = SingleStockDTO(oSymb, symb)
            if self.firstDay != '':
                sh.cutFromDate(self.firstDay) 

            lastDates.add(sh.getDf().iloc[-1]['datetime'])

            dailyData[symb] = sh

        if len(lastDates) == 1:
            logger.info('DataLoader: loading %d stocks, all good.' %(len(self.symbs)))
        else:
            logger.info('DataLoader: loading %d stocks, last date inconsistent!' %(len(self.symbs)))

        return MultiStockDTO(dailyData, self.firstDay)

