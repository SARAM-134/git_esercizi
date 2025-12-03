voti:list[str]=[ 'A','B','A','C','B','A','D','B','C','A']
conteggio:dict[str:int]={
    'A':0,
    'B':0,
    'C':0,
    'D':0
}
for v in voti:
    if v=='A':
        conteggio['A']=conteggio['A']+1
    elif v=='B':
        conteggio['B']=conteggio['B']+1
    elif v=='D':
        conteggio['D']=conteggio['D']+1
    else:
        conteggio['C']=conteggio['C']+1
print(conteggio)