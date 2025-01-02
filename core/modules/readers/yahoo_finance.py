import json

import yfinance as yf
from datetime import datetime

def get_live_price(stock, return_all=False):
    try:
        stock = yf.Ticker(stock)
        data = stock.info

        req_data =  {
            "timestamp": datetime.now(),
            "price": data["currentPrice"],
            "dayLow": data["dayLow"],
            "dayHigh": data["dayHigh"]
        }

        return data if return_all else req_data

    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return None


if __name__ == '__main__':
    from configs.dev import BASE_DIR
    data = get_live_price("ITC.NS", return_all=True)
    file_name = f"{BASE_DIR}/test_cases/samples/yahoo_finance_ticket_info.json"
    with open(file_name, "w") as json_file:
        json.dump(data, json_file, indent=4)