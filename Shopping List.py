#SHOPPING LIST PROGRAM

foods = []
prices = []
total = 0

while True:
    food = input("Enter your item (q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"How much is the {food} : $"))
        foods.append(food)
        prices.append(price)

print("________YOUR ITEMS________")

for food in foods:
    print(food)
for price in prices:
    total = total + price
    print(f"The total cost is ${total}")











