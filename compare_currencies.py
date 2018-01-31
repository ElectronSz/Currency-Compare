from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
from _datetime import datetime as d
import datetime as dt
from tabulate import tabulate as tbl
import _thread
import time

c = CurrencyRates()
b = BtcConverter()

date_obj = dt.datetime(d.now().year,d.now().month,d.now().day,d.now().hour,d.now().minute,d.now().second,d.now().microsecond)

USD = "USD"
GBP = "GBP"
ZAR = "ZAR"
EUR = "EUR"
AUD = "AUD"
SGD = "SGD"
CAD = "CAD"
CNY = "CNY"
JPY = "JPY"
NZD = "NZD"
INR = "INR"
CHF = "CHF"
MXN = "MXN"
BGN = "BGN"
HUF = "HUF"
MYR = "MYR"
HRK = "HRK"
THB = "THB"
NOK = "NOK"
PLN = "PLN"
CZK = "CZK"

print("\n*****************************************************************************************************************************************************")
print("***********Project Title: Currency Converter*********************************************************************************************************")
print("***********Project Date: 2018/01/31******************************************************************************************************************")
print("***********Project Author: ElectronSz****************************************************************************************************************")
print("***********Github: https://github.com/ElectronSz*****************************************************************************************************")
print("***********Project Version: 1.03*********************************************************************************************************************\n")
base_cur = input("Enter Your Base Currency(e.g USD): ")


tbl_data = [
    [c.get_rate(base_cur,USD,date_obj),c.get_rate(base_cur,GBP,date_obj),c.get_rate(base_cur,ZAR,date_obj),c.get_rate(base_cur,EUR,date_obj),
     c.get_rate(base_cur, AUD, date_obj),c.get_rate(base_cur,SGD,date_obj),c.get_rate(base_cur,CAD,date_obj),
     c.get_rate(base_cur, CNY, date_obj),c.get_rate(base_cur,JPY,date_obj),c.get_rate(base_cur,NZD,date_obj),
     c.get_rate(base_cur, INR, date_obj),c.get_rate(base_cur,CHF,date_obj),c.get_rate(base_cur,MXN,date_obj),
     c.get_rate(base_cur,BGN,date_obj),c.get_rate(base_cur,HUF,date_obj),c.get_rate(base_cur,MYR,date_obj),
     c.get_rate(base_cur,HRK,date_obj),c.get_rate(base_cur,THB,date_obj),c.get_rate(base_cur,NOK,date_obj),
     c.get_rate(base_cur,PLN,date_obj),c.get_rate(base_cur,CZK,date_obj)]
]

tbl_header = (USD,GBP,ZAR,EUR,AUD,SGD,CAD,CNY,JPY,NZD,INR,CHF,MXN,BGN,HUF,MYR,HRK,THB,NOK,PLN,CZK)

print(">>Table Results:")
print('>>Base Currency = ',base_cur)
print(tbl(tbl_data,tbl_header,tablefmt="fancy_grid"))
print(">>DOne loading table...")

print("\n::Lets Check Bitcoin now...!")
print("Bitcoin price for => ",base_cur)

print("1 BITCOIN = %(base)s %(price).2F" %{'base':base_cur,'price': b.get_latest_price(base_cur)})

print(">>Done checking bitcoin...")
print("Goodbye!")
print("PS, From [[[ElectronSz]]] :)")

