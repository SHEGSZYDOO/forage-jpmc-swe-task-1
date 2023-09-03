################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(stock_name, bid_price, ask_price):
    # Calculate the price as the average of bid and ask prices
    price = (bid_price + ask_price) / 2.0
    return (stock_name, bid_price, ask_price, price)



def getRatio(price_a, price_b):
    # Calculate the ratio of stock A's price to stock B's price
    ratio = price_a / price_b
    return ratio



def main():
    stockA = "AAPL"
    stockB = "GOOG"
    
    # Example bid and ask prices for stock A and stock B
    bid_price_a = 150.0
    ask_price_a = 155.0
    bid_price_b = 1000.0
    ask_price_b = 1005.0
    
    # Get data points for stock A and stock B
    stockA_data = getDataPoint(stockA, bid_price_a, ask_price_a)
    stockB_data = getDataPoint(stockB, bid_price_b, ask_price_b)
    
    # Extract data
    stockA_name, stockA_bid, stockA_ask, stockA_price = stockA_data
    stockB_name, stockB_bid, stockB_ask, stockB_price = stockB_data
    
    # Calculate the ratio
    ratio = getRatio(stockA_price, stockB_price)
    
    # Print stock information, prices, and the ratio
    print("Stock A:", stockA_name)
    print("Bid Price for Stock A:", stockA_bid)
    print("Ask Price for Stock A:", stockA_ask)
    print("Price for Stock A:", stockA_price)
    print("\nStock B:", stockB_name)
    print("Bid Price for Stock B:", stockB_bid)
    print("Ask Price for Stock B:", stockB_ask)
    print("Price for Stock B:", stockB_price)
    print("\nRatio (Stock A / Stock B):", ratio)

if __name__ == "__main__":
    main()

