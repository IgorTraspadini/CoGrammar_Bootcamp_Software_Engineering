# Created by IgorCT - Dez_2024

# menu list
menu = ['latte','expresso','double expresso','cake slice','hot chocolate','sandwich',]

# stock dictionary
stock = {'latte': 2,
         'expresso': 10,
         'double expresso': 20,
         'cake slice': 8,
         'hot chocolate': 15,
         'sandwich': 12}

# price dictionary
price = {'latte': 3.5,
         'expresso': 2,
         'double expresso': 2.5,
         'cake slice': 5,
         'hot chocolate': 4,
         'sandwich': 3.5}

# Calculate the total stock and print out.
total_stock = sum([ stock[item] * price[item]  for item in menu])
print("################## Total Stock Value Report #################")
print(f'Total stock value: £{total_stock}')
