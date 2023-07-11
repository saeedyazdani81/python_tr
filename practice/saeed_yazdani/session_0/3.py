# تعریف دیکشنری از اسامی میوه‌ها به همراه قیمت
fruits = {
    "khiyar": 3,
    "golabi": 12,
    "sib": 9,
    "angoor": 10,
    "hendoone": 7,
    "ananas": 12
}

max_price = max(fruits.values())
max_fruits = [fruit for fruit, price in fruits.items() if price == max_price]

# محاسبه کمترین قیمت و مربوط به چه میوه‌هایی است
min_price = min(fruits.values())
min_fruits = [fruit for fruit, price in fruits.items() if price == min_price]

# محاسبه جمع قیمت تمام میوه‌ها
total_price = sum(fruits.values())

# محاسبه جمع قیمت میوه‌های کمتر از 10 دلار
less_than_10_price = sum(price for price in fruits.values() if price < 10)

# محاسبه میانگین قیمت میوه‌ها
average_price = total_price / len(fruits)

# محاسبه میانگین قیمت میوه‌های بالای 10 دلار
above_10_price = [price for price in fruits.values() if price > 10]
average_above_10 = sum(above_10_price) / len(above_10_price)

# پیدا کردن میوه‌های با قیمت برابر
equal_price_fruits = []
for fruit, price in fruits.items():
    if list(fruits.values()).count(price) > 1:
        equal_price_fruits.append(fruit)

# نمایش نتایج
print("max price :", max_price)
print("fruits with max price:", max_fruits)
print("lowest price :", min_price)
print("fruit with lowest price:", min_fruits)
print("total price of fruit:", total_price)
print("total price for fruits that whome lower than 10$  ", less_than_10_price)
print("average price :", average_price)
print("average price for fruits with price over 10$:", average_above_10)
print("fruits with equal price:", equal_price_fruits)
