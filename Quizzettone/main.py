print("Hello Quizzettone")
question="Qual è il tuo trapper preferito?"
answer_1="Sfera Ebbasta"
answer_2="DPG-777"
answer_3_="T3"
answer_4="T4 "
def mostra_domanda(domanda:str) -> None:
    print(domanda)

def raccogli_risposta() -> str:
    return input("Inserisci la tua risposta: ")

def valida_scelta(scelta:str)-> bool:
    scelta=scelta.upper()
    if scelta=="A" or scelta=="B" or scelta=="C" or scelta=="D":
        return True
    else:
        return False

def genera_feedback(scelta:str,risp_esatta:str)->str:
    if scelta==risp_esatta:
        return "Hai indovinato"
    else:
        return "Non hai indovinato. Ritenta"
    

def leggi_da_file()->str:
    with open("domanda1.txt") as file:
        cont=file.read()
    return cont
            
def estrai_domanda(contenuto:str,index:int)->str:
    domanda=contenuto[0:index]
    return domanda

def estrai_risposta(contenuto:str, index:int)->str:
    risposta=contenuto[index+1:index+2]
    return risposta
def estrai_index(contenuto:str)->int:
    return contenuto.index('£')
def is_corretta(scelta,risposta_esatta)->bool:
    return scelta==risposta_esatta
def main():
    cont=leggi_da_file()
    index:int=estrai_index(cont)
    domanda=estrai_domanda(cont,index)
    risposta=estrai_risposta(cont,index)
    while True:
        mostra_domanda(domanda)
        risp=raccogli_risposta()
        print(risp)
        if valida_scelta(risp)==True:
            print(genera_feedback(risp,risposta))
        if is_corretta(risp,risposta):
            break
    

main()