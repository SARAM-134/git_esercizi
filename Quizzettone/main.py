print("Hello Quizzettone")
question="Qual è il tuo trapper preferito?"
answer_1="Sfera Ebbasta"
answer_2="DPG-777"
answer_3_="T3"
answer_4="T4"
def mostra_domanda() -> None:
    print(f"""question
    "A. "{answer_1}
    "B. "{answer_2}
    "C. "{answer_3_}
    "D. "{answer_4}""")
def raccogli_risposta() -> str:
    return input("Inserisci la tua risposta: ")

def valida_scelta(scelta:str)-> bool:
    scelta=scelta.upper()
    if scelta=="A" or scelta=="B" or scelta=="C" or scelta=="D":
        return True
    else:
        return False

def genera_feedback(scelta:str)->str:
    if scelta=="A":
        return "Hai indovinato"
    else:
        return "Non hai indovinato. Ritenta"
mostra_domanda()
risposta=raccogli_risposta()
print(valida_scelta(risposta))

