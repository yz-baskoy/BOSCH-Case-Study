import pandas as pd
CURRENCY_RATES = {
    #
    #
}
my_dic = pd.read_excel('Crypto.xlsx', index_col=0).to_dict()

a = my_dic['Price']
print(type(a))

CURRENCY_RATES = list(a.values())
print(CURRENCY_RATES)

