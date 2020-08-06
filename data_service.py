import yfinance as yf
import pprint


def get_stock_info(stock):
    print("Try to access stock data of %s ...", stock)
    stock_ticker = yf.Ticker(stock)
    return stock_ticker.info


if __name__ == "__main__":
    print("Starting data_service output main...")
    pprint.pprint(get_stock_info('msft'))
    print("... Stopping data_service output main")
