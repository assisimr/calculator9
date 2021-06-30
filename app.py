#MODEL
#onePlusDaySales=150
one_plus_day_1_sales = 150
one_plus_day_2_sales = 250
one_plus_day_3_sales = 100

profits_to_amazon_from_one_plus = 200.27

discounts_from_sbi_to_one_plus = 3000.12

home_app_day_1_sales = 120
home_app_day_2_sales = 220
home_app_day_3_sales = 180

profits_to_amazon_from_home_app = 50

discounts_from_sbi_to_home_app = 3000.12

#CONTROLLER

total_one_plus_sales = one_plus_day_1_sales + one_plus_day_2_sales + one_plus_day_3_sales
total_home_app_sales = home_app_day_1_sales + home_app_day_2_sales + home_app_day_3_sales

net_one_plus_profits = total_one_plus_sales * profits_to_amazon_from_one_plus
net_home_app_profits = total_home_app_sales * profits_to_amazon_from_home_app

print("one_plus", net_one_plus_profits)
print("home_app", net_home_app_profits)

if net_one_plus_profits > net_home_app_profits:
    print("amazon_made_more_profits_on_one_plus_by", (net_one_plus_profits - net_home_app_profits))
else:
    print("home_app")
    
