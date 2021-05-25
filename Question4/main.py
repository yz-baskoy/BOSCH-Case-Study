from currency_rates import CURRENCY_RATES 
import tkinter as tk

total_used_coin = 2

class Wallet:
    def __init__(self, usd, btc, bch, ltc, xrp, eth):
        self.usd = usd
        self.btc = btc
        self.bch = bch
        self.ltc = ltc
        self.xrp = xrp
        self.eth = eth
    
    def displayWallet(self):
        print('usd:', self.usd, 'btc:',self.btc, 'bch:',self.bch, 
            'ltc:',self.ltc, 'eth:',self.xrp,'eth:',self.eth )
    
    def sellBtc(self):
        self.usd = self.usd + self.btc*CURRENCY_RATES[0]
        self.btc = self.btc - total_used_coin

    def sellBch(self):
        self.usd = self.usd + self.bch*CURRENCY_RATES[1]
        self.bch = self.bch - total_used_coin
    
    def sellLtc(self):
        self.usd = self.usd + self.ltc*CURRENCY_RATES[2]
        self.ltc = self.ltc - total_used_coin

    def sellXrp(self):
        self.usd = self.usd + self.ltc*CURRENCY_RATES[3]
        self.xrp = self.xrp - total_used_coin

    def sellEth(self):
        self.usd = self.usd + self.ltc*CURRENCY_RATES[4]
        self.eth = self.eth - total_used_coin

    def buyBtc(self):
        self.btc = self.btc + total_used_coin
        self.usd = self.usd - total_used_coin*CURRENCY_RATES[0]

    def buyBch(self):
        self.bch = self.bch + total_used_coin
        self.usd = self.usd - total_used_coin*CURRENCY_RATES[1]

    def buyLtc(self):
        self.ltc = self.ltc + total_used_coin
        self.usd = self.usd - total_used_coin*CURRENCY_RATES[2]

    def buyXrp(self):
        self.xrp = self.xrp + total_used_coin
        self.usd = self.usd - total_used_coin*CURRENCY_RATES[3]

    def buyEth(self):
        self.eth = self.eth + total_used_coin
        self.usd = self.usd - total_used_coin*CURRENCY_RATES[4]

myWallet = Wallet(100, 10, 300, 40, 20, 100)

myWallet.displayWallet() 

buyoperation_BTC = Wallet
buyoperation_BCH = Wallet
buyoperation_LTC = Wallet
buyoperation_XRP = Wallet
buyoperation_ETH = Wallet

selloperation_BTC = Wallet
selloperation_BCH = Wallet
selloperation_LTC = Wallet
selloperation_XRP = Wallet
selloperation_ETH = Wallet

myWallet.displayWallet() 
print('*******************')


# ********************GUI******************************
root = tk.Tk()
root.geometry('800x600')
root.resizable(True, True)
root.title('Crypto Currency Program')

# LABELS

label = tk.Label(
    root,
    text='BTC   BCH   LTC   XRP   ETH',
    font=("Helvetica", 20)
)

label2 = tk.Label(
    root,
    text = CURRENCY_RATES,
    font=("Helvetica", 18)
)

walletlabel = tk.Label(
    root,
    text = getattr(myWallet, 'usd'),
    font=("Helvetica", 18)
)

walletlabel.pack(ipadx=10, ipady=10)
label.pack(ipadx=10, ipady=10)
label2.pack(ipadx=10, ipady=10)

# USER INPUT

x = tk.IntVar()
number_of_input_coin = tk.Entry(textvariable=x)
number_of_input_coin.pack(ipadx=2, ipady=5)
a = int(str(number_of_input_coin.get()))


def add_total_used_coin():
    t = a
    return t
    total_used_coin = add_total_used_coin()

addButton = tk.Button(root,bg='green', text='add coin to trade')
addButton.pack(ipadx=6, ipady=6)

# SELL BUTTON CLICK FUNCTIONS
def sell_button_clicked():
    selloperation_BTC.sellBtc()

def sell_button_clicked1():
    selloperation_BCH.sellBch()

def sell_button_clicked2():
    selloperation_LTC.sellLtc()

def sell_button_clicked3():
    selloperation_XRP.sellXrp()

def sell_button_clicked4():
    selloperation_ETH.sellEth()

# BUY BUTTON CLICK FUNCTIONS
def buy_button_cliked1():
    buyoperation_BTC.buyBtc()
    
def buy_button_cliked2():
    buyoperation_BCH.buyBch()
    
def buy_button_cliked3():
    buyoperation_LTC.buyLtc()
    
def buy_button_cliked4():
    buyoperation_XRP.buyXrp()
    
def buy_button_cliked5():
    buyoperation_ETH.buyEth()
    


# SELL BUTTONS

sellBtcButton = tk.Button(root,bg='red', text='sell Btc', command=sell_button_clicked)
sellBtcButton.pack(ipadx=10, ipady=10)


sellBchButton = tk.Button(root,bg='red', text='sell Bch', command=sell_button_clicked1)
sellBchButton.pack(ipadx=10, ipady=10)


sellLtcButton = tk.Button(root,bg='red', text='sell Ltc', command=sell_button_clicked2)
sellLtcButton.pack(ipadx=10, ipady=10)


sellXrpButton = tk.Button(root,bg='red', text='sell Xrp', command=sell_button_clicked3)
sellXrpButton.pack(ipadx=10, ipady=10)


sellEthButton = tk.Button(root,bg='red', text='sell Eth', command=sell_button_clicked4)
sellEthButton.pack(ipadx=10, ipady=10)

# BUY BUTTONS

buyBtcButton = tk.Button(root, bg="blue", text='buy Btc', command=buy_button_cliked1)
buyBtcButton.pack(ipadx=10, ipady=10)

buyBchButton = tk.Button(root, bg="blue", text='buy Btc', command=buy_button_cliked2)
buyBchButton.pack(ipadx=10, ipady=10)

buyLtcButton = tk.Button(root, bg="blue", text='buy Btc', command=buy_button_cliked3)
buyLtcButton.pack(ipadx=10, ipady=10)

buyXrpButton = tk.Button(root, bg="blue", text='buy Btc', command=buy_button_cliked4)
buyXrpButton.pack(ipadx=10, ipady=10)

buyEthButton = tk.Button(root, bg="blue", text='buy Btc', command=buy_button_cliked5)
buyEthButton.pack(ipadx=10, ipady=10)

root.mainloop()

myWallet.displayWallet() 


 
