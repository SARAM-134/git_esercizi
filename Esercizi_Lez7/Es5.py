utenti:dict[str:str]={
    "alice":"admin",
    "bob":"user",
    "charlie":"guest"
}
trovato:bool=False
for key,values in utenti.items():
    print( f"""
    Username: {key}
    Ruolo:    {values}
          """)
    if  key=='bob':
        trovato=True

print(f"Bob presente:{trovato}")
print(utenti.keys())
print(utenti.values())