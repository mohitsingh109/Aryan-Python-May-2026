# datetime module ==> read about this
#"""
#Stocks Data:
#Symbol
#AAPL ---> [{ "time": "29-May-2026 9:15 AM", "price": 15 }, {}, {}]
#MSFT --->  [{ "time": "29-May-2026 9:18 AM", "price": 45.6 }, {}, {}]


    #Please select your option
    #1) Add a stock data
    #2) View all stock data
   # 3) View all stock symbol
    #4) View given stock data by date range
    # 5 VIEW STOCK DATA BY PRICE RANGE
   # 5) exit


#1) Add a stock data
 #- user input stock symbol, time and price (No duplicate data)

#2) View all data for a given stock
    #- User will input a symbol, and you have to present in nicely
   # in print statement

#3) View all stock name

#4) View given stock data by date range
    #- User will input daterange & stock symbol

stock_data={}

def add_stock_data():
    global stock_data
    symbol = input("Enter stock symbol: ")
    time = input("Enter time: ")
    price = float(input("Enter price: "))
    if symbol in stock_data:
        for data in stock_data[symbol]:
            if data["time"] == time:
                print("Data already exists")
                return
        stock_data[symbol].append({"time": time, "price": price})
        print("Stock added successfully")
    else :
        stock_data[symbol] = [{"time": time, "price": price}]
        print("Stock symbol and data initialize successfully")

def view_all_stock_symbols():
    global stock_data
    for symbol in stock_data.keys():
        print(symbol)

def view_stock_data_by_symbol():
    global stock_data
    symbol = input("Enter stock symbol: ")
    if symbol not in stock_data:
        print("Invalid stock symbol")
        return
    for data in stock_data[symbol]:
        print(f"For the time of {data['time']} and price is {data['price']}")

def view_stock_data_by_price():
    global stock_data
    symbol =input("Enter stock symbol:")
    price_min = float(input("Enter min price:"))
    price_max = float(input("Enter max price:"))
    if symbol not in stock_data:
        print("Invalid stock symbol")
        return
    for data in stock_data[symbol]:
        if data["price"] >= price_min and data["price"]<= price_max :
            print(f"Price : {data["price"]}")




# def view_stock_data_by_date():
#     global stock_data
#     import datetime
#     id = input("Enter stock symbol: ")
#     for id in stock_data:
#         if
#



while True:
    print("\n")
    print("1.Add a stock data ")
    print("2.View all stock data")
    print("3.View all stock symbol")
    print("4.View all stock data by date range")
    print("5. exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_stock_data()
    elif choice == "2":
        view_stock_data_by_symbol()
    elif choice == "3":
        view_all_stock_symbols()
    elif choice == "4":
        print("In progress")
    elif choice == "5":
        print("exit")
        break
    else:
        print("Invalid choice")




