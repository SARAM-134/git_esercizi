lista:list[str]=["web01","db01","cache01"]
print(lista)
lista.append("backup01")
print(lista)
lista.insert(0,"proxy01")
print(lista)
for x in lista:
    if x=="cache01":
        a=lista.index(x)
        lista.pop(a)
print( f"""
      Lista: {lista})
      Lunghezza: {len(lista)}
""")
     