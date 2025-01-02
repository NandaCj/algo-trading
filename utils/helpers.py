import json
import pandas as pd
from configs.dev import logging as log, SHAREKHAN_SCRIPS, NIFTY_500_CSV


def get_sharekhan_scrip_codes():
    """
    :return: dict of sharekhan tradingSymbol : scripCode
    """
    print("getting sharekhan scrip codes...")
    with open(SHAREKHAN_SCRIPS, "r") as f:
        file_data = json.load(f)

    data = file_data["data"]
    sharekhan_scrips = {i["tradingSymbol"] : i["scripCode"] for i in data}

    print("sharekhan scrip codes retrieved...")
    return sharekhan_scrips


def get_nifty_500_list():
    """
    :return: returns list of stock_detail
    """
    print("getting sharekhan scrip codes...")
    df = pd.read_csv(NIFTY_500_CSV)
    return df["Symbol"].to_list()


def get_stocks_to_trade():
    sharekhan_scrip_codes = get_sharekhan_scrip_codes()
    nifty_500_list =get_nifty_500_list()
    return {k:v for k, v in sharekhan_scrip_codes.items() if k in nifty_500_list}



if __name__ == '__main__':
    res = get_stocks_to_trade()
    print(res)