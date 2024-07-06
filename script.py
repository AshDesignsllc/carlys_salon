hairstyles = ["french bun", "pixie", "locs", "box braids", "silk press", "bob", "marley braids", "fade"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
  total_price += price
  print(price)
# print(total_price)

average_price = total_price / len(prices)
print("Average Haircut Price: $",  average_price)

new_prices = [price - 5 for price in prices]
print(new_prices)

total_revenue = 0

for i in range(len(hairstyles)):
  print(i)
  total_revenue += (prices[i] * last_week[i])

print("Total Revenue:",  total_revenue)

average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: $", average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]


print("Cuts under $30:", cuts_under_30)
print("Cuts under $30:", str(cuts_under_30).strip('[]').replace('\'', ''))