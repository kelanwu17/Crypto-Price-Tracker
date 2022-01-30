import requests
import tkinter as tk
from datetime import datetime

crypto = input("What cryptocurrency would you like to track? ")


def trackBitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=" + crypto + "&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    price = response["USD"]
    time = datetime.now().strftime("%H:%M:%S")

    labelPrice.config(text = str(price) + " $")
    labelTime.config(text = "Updated at: " + time)

    canvas.after(500, trackBitcoin)
color = ""
if crypto == "btc":
     color = "gold"
elif crypto == "eth":
    color = "skyblue"
else:
    color = "darkgrey"

canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title("Crypto Tracker")
canvas.configure(background = color)
f1 = ("poppins", 24, "bold") #font
f2 = ("poppins", 22, "bold") #font
f3 = ("poppins", 18, "normal") #font

label = tk.Label(canvas, text = crypto.upper() + " PRICE", font = f1,background = color)
label.pack(pady = 20)

labelPrice = tk.Label(canvas, font = f2,background = color)
labelPrice.pack(pady = 20)

labelTime = tk.Label(canvas, font = f3,background = color)
labelTime.pack(pady = 20)

trackBitcoin()
canvas.mainloop()