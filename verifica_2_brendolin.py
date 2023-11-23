tupla_partite = (
    ("SquadraA", "SquadraB", 3, 2),
    ("SquadraC", "SquadraD", 1, 1),
    ("SquadraB", "SquadraC", 2, 4),
    ("SquadraD", "SquadraA", 0, 3),
    ("SquadraB", "SquadraD", 1, 2),
)

def media_gol_partite(tupla_partite):
    gol=0
    for gol in tupla_partite:
        somma+=gol
        media_gol=somma/len(tupla_partite)
    print("La media dei gol in tutte le partite e: ",media_gol)

def media_gol_squadra(tupla_partite, squadra):
    squadra=str(input("Inserisci la squadra chevuoi ricercare: "))
    gol=0
    for gol in tupla_partite:
        somma+=gol
        gol_squadra=somma/len(tupla_partite)
    print("La media dei gol della squadra: ",squadra" e: ",gol_squadra)

def partita_con_piu_gol(tupla_partite):
    max_gol=0
    for gol in tupla_partite:
        if gol>max_gol:
            max_gol+=gol
    print("La partitacon più gol e: ",max_gol)

def partita_con_meno_gol(tupla_partite):
    min_gol=10
    for gol in tupla_partite:
        if gol<min_gol:
            min_gol+=gol
    print("La partitacon più gol e: ",min_gol)

def percentuale_vittorie_squadra(tupla_partite, squadra):
    squadra=str(input("Inserisci la squadra chevuoi ricercare: "))
    print("La percentuale di ittorie e: ",percentuale)

do {
    print("1. Visualizza la media gol partite \n 2. Visualizza la media gol squadra \n 3. Visualizza la partita con piu gol \n 4. Visualizza la partita con meno gol \n 5. Visualizza la percentuale vittorie squadra")
    scelta=int(input("Inserisci il numero della funzione che vuoi usare: "))
    if scelta==1:
        print(media_gol_partite(tupla_partite))
    if scelta==2:
        print(media_gol_squadra(tupla_partite, squadra))
    if scelta==3:
        print(partita_con_piu_gol(tupla_partite))
    if scelta==4:
        print(partita_con_meno_gol(tupla_partite))
    if scelta==5:
        print(percentuale_vittorie_squadra(tupla_partite, squadra))
} while (scelta!=0)