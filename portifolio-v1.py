from tkinter import *
import requests
import json

def my_portfolio():

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
		},

		{	

		"symbol":'XMR',
		"coins_owned":50,
		"price_per_coin":40.5
		},


		{	

		"symbol":'ETH',
		"coins_owned":100,
		"price_per_coin":270
		},


		{	

		"symbol":'LTC',
		"coins_owned":30,
		"price_per_coin":25
		}
	]

	total_pl = 0
	coin_row = 1

	for i in range(0,100):
		for coin in my_coins:

			if api[i]['symbol']==coin["symbol"]:

				total_paid = coin["coins_owned"]*coin['price_per_coin']
				current_value = coin["coins_owned"]*float(api[i]['price_usd'])
				pl_per_coin =  float(api[i]['price_usd']) - coin['price_per_coin'] 
				total_pl_for_coin = pl_per_coin * coin["coins_owned"] 

				total_pl += total_pl_for_coin

				# print("{0}-{1}: ${2}".format(api[i]['name'],api[i]['symbol'],api[i]['price_usd']))
				# print("Number of Coins Owned:",coin['coins_owned'])
				# print('Total Amount Paid:',"{0:.2f}".format(total_paid))
				# print("Current Total Value:","{0:.2f}".format(current_value))
				# print("Profit/Loss Per Coin:",pl_per_coin)
				# print("Total Profit/Loss of this Coin:",total_pl_for_coin)
				# print('-------------------------------')

				name_label = Label(gui, text = api[i]['name'], bg="black", fg='white',font="Lato 12", padx='5', pady='5',borderwidth=2,relief = 'groove')
				name_label.grid(row=coin_row, column=0, sticky=N+S+E+W)

				price_label = Label(gui, text = api[i]['price_usd'] , bg="grey", fg='white',font="Lato 12", padx='5', pady='5',borderwidth=2,relief = 'groove')
				price_label.grid(row=coin_row, column=1, sticky=N+S+E+W)

				num_coins_label = Label(gui, text = coin['coins_owned'], bg="black", fg='white',font="Lato 12", padx='5', pady='5',borderwidth=2,relief = 'groove')
				num_coins_label.grid(row=coin_row, column=2, sticky=N+S+E+W)

				amount_paid_label = Label(gui, text = "{0:.2f}".format(total_paid), bg="grey", fg='white',font="Lato 12", padx='5', pady='5',borderwidth=2,relief = 'groove')
				amount_paid_label.grid(row=coin_row, column=3, sticky=N+S+E+W)

				current_val_label = Label(gui, text = "{0:.2f}".format(current_value), bg="black", fg='white',font="Lato 12", padx='5', pady='5',borderwidth=2,relief = 'groove')
				current_val_label.grid(row=coin_row, column=4, sticky=N+S+E+W)

				pl_per_coin_label = Label(gui, text =pl_per_coin , bg="grey", fg='white',font="Lato 12", padx='5', pady='5',borderwidth=2,relief = 'groove')
				pl_per_coin_label.grid(row=coin_row, column=5, sticky=N+S+E+W)

				total_pl_for_coin_label = Label(gui, text = total_pl_for_coin, bg="black", fg='white',font="Lato 12", padx='5', pady='5',borderwidth=2,relief = 'groove')
				total_pl_for_coin_label.grid(row=coin_row, column=6, sticky=N+S+E+W)

				coin_row += 1


	api = ""

	total_pl_label = Label(gui, text = total_pl, bg="cyan", fg='white', font="Lato 12 bold", padx='5', pady='5',borderwidth=2,relief = 'groove')
	total_pl_label.grid(row=coin_row, column=6, sticky=N+S+E+W)

	#button to refresh: but API refreshes every 5 Minutes: so refresh time dictated by api
	update_button = Button(gui, command=my_portfolio , text = "Refresh", bg="cyan", fg='white', font="Lato 12 bold", padx='5', pady='5',borderwidth=2,relief = 'groove')
	update_button.grid(row=coin_row+1, column=6, sticky=N+S+E+W)


gui = Tk()
gui.title("Cryptocurrency Portfolio")


name_label = Label(gui, text = "Coin Name", bg="cyan", fg='white', font="Lato 12 bold", padx='5', pady='5',borderwidth=2,relief = 'groove')
name_label.grid(row=0, column=0, sticky=N+S+E+W)

price_label = Label(gui, text = "Price", bg="cyan", fg='white', font="Lato 12 bold", padx='5', pady='5',borderwidth=2,relief = 'groove')
price_label.grid(row=0, column=1, sticky=N+S+E+W)

num_coins_label = Label(gui, text = "Coins Owned", bg="cyan", fg='white', font="Lato 12 bold", padx='5', pady='5',borderwidth=2,relief = 'groove')
num_coins_label.grid(row=0, column=2, sticky=N+S+E+W)

amount_paid_label = Label(gui, text = "Total Amount Paid", bg="cyan", fg='white', font="Lato 12 bold", padx='5', pady='5',borderwidth=2,relief = 'groove')
amount_paid_label.grid(row=0, column=3, sticky=N+S+E+W)

current_val_label = Label(gui, text = "Current Value", bg="cyan", fg='white', font="Lato 12 bold", padx='5', pady='5',borderwidth=2,relief = 'groove')
current_val_label.grid(row=0, column=4, sticky=N+S+E+W)

pl_per_coin_label = Label(gui, text = "Profit/Loss Per Coin", bg="cyan", fg='white', font="Lato 12 bold", padx='5', pady='5',borderwidth=2,relief = 'groove')
pl_per_coin_label.grid(row=0, column=5, sticky=N+S+E+W)

total_pl_label = Label(gui, text = "Total Profit/Loss", bg="cyan", fg='white', font="Lato 12 bold", padx='5', pady='5',borderwidth=2,relief = 'groove')
total_pl_label.grid(row=0, column=6, sticky=N+S+E+W)


#bitcoin.pack()  auto aligns the bitcoin label

my_portfolio()

gui.mainloop()

print("Program Completed")
