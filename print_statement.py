salaries = [25000, 42000, 18000, 55000, 32000, 60000, 22000]

high_salaries = []

for salary in salaries:
    if salary > 30000:
        high_salaries.append(salary)

print(high_salaries)



sales = [12000, 45000, 18000, 55000, 32000, 9000]

good_sales=[]

for sale in sales:
    if sale >= 30000:
        good_sales.append(sale)
print(good_sales)


sales = [12000, 45000, 18000, 55000, 32000, 9000]


low_sales=[]

for sale in sales:
    if sale < 20000:
        low_sales.append(sale)
print(low_sales)


salaries = [25000, 45000, 18000, 60000, 32000]

for salary in salaries:
    if salary >= 30000:
        print('High')
    else:
        print('Low')