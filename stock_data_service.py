import yfinance as yf
import pprint
import utils.hardening_methods as utils_hm


class StockDataService:
    stock_name = None
    stock_ticker = None

    def __init__(self, stock_name):
        if not utils_hm.valid_input(str, stock_name):
            print("ERROR: StockDataService object for", stock_name, "not created. Please choose a valid stock_name like"
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

    def get_stock_history(self, period="1mo", interval="1d", start=None, end=None, prepost=False, actions=True,
                          auto_adjust=True, back_adjust=False, proxy=None, rounding=True, tz=None, **kwargs):
        if not utils_hm.valid_input(str, period, interval):
            print("ERROR: No stock history for", self.stock_name, "retrieved. Please choose valid \"period\" and "
                                                                  "\"interval\" strings, like \"period=3mo\".")
            return
        if not utils_hm.valid_input(bool, prepost, actions, auto_adjust, back_adjust, rounding):
            print("ERROR: No stock history for", self.stock_name, "retrieved. Please choose valid bool values for "
                                                                  "\"prepost\", \"actions\", \"auto_adjust\", "
                                                                  "\"back_adjust\" or \"rounding\".")
            return
        return self.stock_ticker.history(period=period, interval=interval, start=start, end=end, prepost=prepost,
                                         actions=actions, auto_adjust=auto_adjust, back_adjust=back_adjust, proxy=proxy,
                                         rounding=rounding, tz=tz, **kwargs)


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
    print("Stock history for 3 months:")
    pprint.pprint(stock_data.get_stock_history(period="3mo"))
    # TODO // Extract into tests
    pprint.pprint(stock_data.get_stock_history(period=3))
    pprint.pprint(stock_data.get_stock_history(rounding="3"))
    # TODO //
