prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}

for key in prices:
    print
    key
    print
    "price: %s" % prices[key]
    print
    "stock: %s" % stock[key]
total = 0
for virus in prices:
    print
    virus, prices[virus] * stock[virus]

    total += prices[virus] * stock[virus]
print total