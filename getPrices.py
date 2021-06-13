import requests

url1 = "https://api.wazirx.com/api/v2/tickers" 								#Wazirx 

url2 = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr"		#coingecko

response_wzrx = requests.get(url1)
response_gecko = requests.get(url2)

#deserializing json response
data_wzrx = response_wzrx.json()		# A dict
data_gecko = response_gecko.json()		# A list of dict

# Get price and other information from data_gecko and data_wzrx
def showPrice(coin: str):

	# name = ""									name of coin
	# current_price = 0 						current_price of coin
	# ath = 0									All time high of coin
	# high_24 = 0								Last 24hr high
	# low_24 = 0 								Last 24hr low
	# image_link = ""

	# Using data_wzrx
	id = coin+"inr"
	temp_dict = data_wzrx[id]
	current_price = temp_dict["last"]
	high_24 = temp_dict["high"]
	low_24 = temp_dict["low"]

	#using data_gecko
	for i in data_gecko:
		if i["symbol"] == coin:
			ath = i["ath"]
			name = i["name"]
			image_link = i["image"]
			break

	response = f' Name = {name}, current price = {current_price}, all time high = {ath}, 24hr high = {high_24}, 24hr low = {low_24}'

	return response


	


