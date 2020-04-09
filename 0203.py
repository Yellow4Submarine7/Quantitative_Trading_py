#面向对象复习

from collections import namedtuple
from collections import OrderedDict
class StockTradeDays(object):
    def __init__(self,price_array,start_date,date_array=None):
        self.__price_array = price_array
        self.__date_array = self._init_days(start_date,date_array)
        self.__change_array = self.__init_change()
        self.stock_dict = self._init_stock_dict()
    def __init_change(self):


