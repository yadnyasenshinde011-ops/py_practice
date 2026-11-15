sales = [12000, 45000, 18000, 55000, 32000, 9000]


low_sales=[]

for sale in sales:
    if sale < 20000:
        low_sales.append(sale)
print(low_sales)