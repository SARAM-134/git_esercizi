def find(x:float, l:list[float])->bool:
    trovato:bool=False
    for i in l:
        if i==x:
            trovato=True
    return trovato
def conta_maggiori(x:float, l:list[float])->int:
    conteggio:int=0
    for i in l:
        if i>x:
            conteggio=conteggio+1
    return conteggio


prezzi:list[float]=[45.5,12.0,78.3,23.1,56.7]
copy:list[float]=sorted(prezzi)
minimo:float=min(prezzi)
massimo:int=max(prezzi)
y:float=23.1
if find(y,prezzi)==True:
    print("Trovato")
else:
    print( f" {y} non è nella lista")
t=50
print("Ci sono "+ str(conta_maggiori(t,prezzi))+" elementi maggiori di "+str(t))

