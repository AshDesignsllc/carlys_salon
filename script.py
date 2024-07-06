# List your initial variables

hairstyles = ["french bun", "pixie", "locs", "box braids", "silk press", "bob", "marley braids", "fade"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Step 1: Sum up all the prices of haircuts

total_price = 0
print("Current Prices")
for price in prices:
  total_price += price
  print("$", price)

print()

# Determine the average price of all the haircuts and print it as a string
  
average_price = total_price / len(prices)
print("Average Haircut Price: $",  average_price)

# The average price is too expensive so cut the prices to satisfy the client

new_prices = [price - 5 for price in prices]

formatted_prices = ', '.join(['${}'.format(price) for price in new_prices])
print("Lower prices:", formatted_prices)


# Determine the profability of the business with the new prices

total_revenue = 0

for i in range(len(hairstyles)):
  #print(i)
  total_revenue += (prices[i] * last_week[i])

print("Total Revenue:",  total_revenue)

average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: $", average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print("Cuts under $30:", str(cuts_under_30).strip('[]').replace('\'', ''))