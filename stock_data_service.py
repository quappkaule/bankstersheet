import yfinance as yf
import pprint
import utils.hardening_methods as utils_hm


class StockDataService:
    stock_name = None
    stock_ticker = None

    def __init__(self, stock_name):
        if not utils_hm.validate_input(str, stock_name):
            print("ERROR: StockDataService for", stock_name, "not created. Please choose a valid stock_name like"
                                                             " \"msft\".")
            return
        self.stock_name = stock_name
        print("Establishing ticker for stock", stock_name)
        self.stock_ticker = yf.Ticker(stock_name)

    def get_stock_info(self):
        return self.stock_ticker.get_info()

    def get_stock_price(self):
        print("Try to access dollar stock price of", self.stock_name)
        return self.get_stock_info()['regularMarketPrice']


if __name__ == "__main__":
    stocks = 'msft'
    print("Getting data for", stocks)
    stock_data = StockDataService(stocks)
    # TODO // Extract into tests
    stock_data2 = StockDataService(1234)
    # TODO //
    print("Current price ", stock_data.get_stock_price(), "$")
    print("Detailed stock info:")
    pprint.pprint(stock_data.get_stock_info())
