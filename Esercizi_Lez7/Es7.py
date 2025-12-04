prodotti :list[dict]=[
{"nome": "Laptop", "prezzo": 899.99, "quantita": 5},
{"nome": "Mouse", "prezzo": 25.50, "quantita": 50},
{"nome": "Tastiera", "prezzo": 75.00, "quantita": 30},
{"nome": "Monitor", "prezzo": 299.99, "quantita": 15}
]
prezzi=[]
qt:list[int]=[]
inventario=0
for l in prodotti:
    for key,value in l.items():
        if key=="prezzo" and value>100:
            print(l)
        prezzo=l.get("prezzo")
        quantità=l.get("quantita")
        prezzi.append(prezzo)
        qt.append(quantità)
    for i in range(len(prezzi)):
        inventario=i*qt[i]+inventario
print(inventario)