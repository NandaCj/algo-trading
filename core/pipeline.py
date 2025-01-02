import time

from . import pipeline_configs as p_configs
from configs.dev import logging as log
from .modules.readers import yahoo_finance as yf
from utils.helpers import get_stocks_to_trade
import apache_beam as beam


class GetStockToTrade(beam.DoFn):

    def process(self, ele):
        """

        :yields: tuple of stock nse code and sharekhan scrip code
        """
        stocks_to_trade = get_stocks_to_trade()
        for stock, code in stocks_to_trade.items():
            yield {"stock": stock, "code": code}



class GetStockDataFromYahooApi(beam.DoFn):

    def process(self, ele, *args, **kwargs):
        """
        :param ele:
        :param args:
        :param kwargs:
        :return: req_data =  {
            "timestamp": datetime.now(),
            "price": data["currentPrice"],
            "dayLow": data["dayLow"],
            "dayHigh": data["dayHigh"]
        }
        """
        stock = ele["stock"]
        live_price_dict = yf.get_live_price(stock=stock + ".NS")

        print(f"retrieved live price for {stock} : {live_price_dict}")

        yield stock, live_price_dict


if __name__ == '__main__':
    obj = GetStockDataFromYahooApi().process(ele = ("ITC", 1660))