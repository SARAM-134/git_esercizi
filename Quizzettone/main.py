import sys
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

def leggi_da_file(filep :str)->str:
    with open(filep) as file:
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
    domande_list: list[str]=[]
    with open("domande.txt","r") as f:
        for i in f:
            domande_list.append(i.strip())
    with open(domande_list[0],"r") as f:
        for i in f:
            print(i)

    """file_path= sys.argv[1]
    cont=leggi_da_file(file_path)
    index:int=estrai_index(cont)
    domanda=estrai_domanda(cont,index)
    risposta=estrai_risposta(cont,index)
    while True:
        mostra_domanda(domanda)
        risp=raccogli_risposta()
        print(risp)
        if valida_scelta(risp)==True:
            print(genera_feedback(risp,risposta))
        else:
            print("Inserisci solo la risposta tra le opzioni elencate")
        if is_corretta(risp,risposta):
            break"""

main()