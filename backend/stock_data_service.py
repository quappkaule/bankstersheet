import pprint
import utils.hardening_methods as utils_hm
import backend.yahoo_finance as yf


class StockDataService:
    stock_name = ""
    stock_ticker = None
    api_name = ""

    def __init__(self, stock_name, api_name="yahoo"):
        if not utils_hm.valid_input(str, stock_name, api_name):
            print("ERROR: StockDataService object for", stock_name, "not created. Please choose a valid stock_name like"
                                                                    " \"msft\".")
            return
        self.stock_name = stock_name
        self.api_name = api_name
        if api_name == "yahoo":
            print("Establishing yahoo ticker for stock", stock_name)
            self.stock_ticker = yf.YahooStocks(stock_name)
        elif api_name == "google":
            # TODO // implement google finance API connection
            print("Establishing google finance ticker for stock", stock_name)
        else:
            print("ERROR: StockDataService object for", stock_name, "and", api_name, "not created. Please choose a "
                                                                                     "valid API to get the stock data"
                                                                                     "from, like \"yahoo\".")
            return

    def get_stock_info(self):
        return self.stock_ticker.get_stock_info()

    def get_stock_price(self):
        return self.stock_ticker.get_stock_price()

    def get_stock_history(self, period="1mo", interval="1d", start=None, end=None, prepost=False, actions=True,
                          auto_adjust=True, back_adjust=False, proxy=None, rounding=True, tz=None, **kwargs):
        if self.api_name == "yahoo":
            return self.stock_ticker.get_stock_history(period, interval, start, end, prepost, actions, auto_adjust,
                                                       back_adjust, proxy, rounding, tz, **kwargs)


if __name__ == "__main__":
    # TODO // Extract main function into tests
    stocks = 'msft'
    print("Getting data for", stocks)
    stock_data = StockDataService(stocks)
    # TODO // Extract into tests
    stock_data2 = StockDataService(1234)
    # TODO //
    print("Current price ", stock_data.get_stock_price(), "$")
    print("Detailed stock info:")
    pprint.pprint(stock_data.get_stock_info())
    print("Stock history for 3 months:")
    pprint.pprint(stock_data.get_stock_history(period="3mo"))
    # TODO // Extract into tests
    pprint.pprint(stock_data.get_stock_history(period=3))
    pprint.pprint(stock_data.get_stock_history(rounding="3"))
    # TODO //
