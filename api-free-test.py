import requests
import json

api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")

api = json.loads(api_request.content)

my_coins = [

	{	

	"symbol":'BTC',
	"coins_owned":2,
	"price_per_coin":10000
	},

	
	{	

	"symbol":'EOS',
	"coins_owned":100,
	"price_per_coin":5
	}
]

total_pl = 0

for i in range(0,10):
	for coin in my_coins:

		if api[i]['symbol']==coin["symbol"]:

			total_paid = coin["coins_owned"]*coin['price_per_coin']
			current_value = coin["coins_owned"]*float(api[i]['price_usd'])
			pl_per_coin =  float(api[i]['price_usd']) - coin['price_per_coin'] 
			total_pl_for_coin = pl_per_coin * coin["coins_owned"] 

			total_pl += total_pl_for_coin

			print("{0}-{1}: ${2}".format(api[i]['name'],api[i]['symbol'],api[i]['price_usd']))
			print("Number of Coins Owned:",coin['coins_owned'])
			print('Total Amount Paid:',"{0:.2f}".format(total_paid))
			print("Current Total Value:","{0:.2f}".format(current_value))
			print("Profit/Loss Per Coin:",pl_per_coin)
			print("Total Profit/Loss of this Coin:",total_pl_for_coin)
			print('-------------------------------')

print("Total Profit/Loss for portfolio:",)