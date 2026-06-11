products=[

{"name":"Product A","stock":5},

{"name":"Product B","stock":15},

{"name":"Product C","stock":25},

{"name":"Product D","stock":23},

{"name":"Product E","stock":8},
]

print("Product with stock less tahn 10")
for product in products:
    if product["stock"]<10:
        print(f"{product['name']}:{product['stock']} units")




