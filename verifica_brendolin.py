tupla_consumi_energetici = (
    ("Milano", [
        ("gennaio", ("elettrico", 300)),
        ("gennaio", ("gas", 150)),
        ("febbraio", ("elettrico", 280)),
        ("febbraio", ("gas", 120)),
    ]),
    ("Brescia", [
        ("gennaio", ("elettrico", 280)),
        ("gennaio", ("gas", 140)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 130)),
    ]),
    ("Napoli", [
        ("gennaio", ("elettrico", 290)),
        ("gennaio", ("gas", 160)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 110)),
    ]),
    ("Torino", [
        ("gennaio", ("elettrico", 270)),
        ("gennaio", ("gas", 130)),
        ("febbraio", ("elettrico", 250)),
        ("febbraio", ("gas", 130)),
    ]),
)

def analizza_consumi_energetici(citta, risorsa):
    somma=0
    for risorsa in tupla_consumi_energetici:
        somma+=risorsa
        media_risorsa=somma/2
    max=0
    for risorsa in tupla_consumi_energetici:
        if risorsa>max:
            max+=risorsa
    min=1000
    for risorsa in tupla_consumi_energetici:
        if risorsa<min:
            min+=risorsa
    return(media_risorsa, max, min)

citta=str(input("Inserisci la citta che vuoi controllare: "))
risorsa=str(input("Inserisci la risorsa che vuoi controllare: "))
risultato_analisi = analizza_consumi_energetici("citta", "risorsa")
print(risultato_analisi(citta, risorsa))