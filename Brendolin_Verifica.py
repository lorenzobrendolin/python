class Articolo: # 9:25 Spinarelli
  def __init__(self, codice, fornitore, marca, prezzo, quantita):
    self.codice = codice
    self.fornitore = fornitore
    self.marca = marca
    self.prezzo = prezzo
    self.quantita = quantita

  def scheda_articolo(self):
    return f"Codice:{self.codice}\nFornitore:{self.fornitore}\nMarca:{self.marca}\nPrezzo:{self.prezzo}\nQuantita:{self.quantita}"

  def modifica_scheda(self):
    scelta = int(input("Scegli cosa modificare: (1. Fornitore, 2. Marca, 3. Prezzo, 4. Quantita)"))
    if scelta == 1:
       fornitore = str("Inserisci il fornitore: ")
    if scelta == 2:
       marca = str("Inserisci la marca: ")
    if scelta == 3:
       prezzo = float("Inserisci il prezzo: ")
    if scelta == 4:
       quantita = int("Inserisci il fornitore: ")


class Televisore(Articolo): # 9:38 Spinarelli
    def __init__(self, codice, fornitore, marca, prezzo, quantita, pollici, tipo):
        super().__init__(codice, fornitore, marca, prezzo, quantita)
        self.pollici = pollici
        self.tipo = tipo

    def scheda_articolo(self):
      return f"Codice:{self.codice}\nFornitore:{self.fornitore}\nMarca:{self.marca}\nPrezzo:{self.prezzo}\nQuantita:{self.quantita}\nPollici:{self.pollici}\nTipo:{self.tipo}"


class Frigorifero(Articolo): # 9:42 Spinarelli
  def __init__(self, codice, fornitore, marca, prezzo, quantita, dimensioni, modello):
        super().__init__(codice, fornitore, marca, prezzo, quantita)
        self.dimensioni = dimensioni
        self.modello = modello

  def scheda_articolo(self):
    return f"Codice:{self.codice}\nFornitore:{self.fornitore}\nMarca:{self.marca}\nPrezzo:{self.prezzo}\nQuantita:{self.quantita}\nDimensioni:{self.dimensioni}\nModello:{self.modello}"


t1 = Televisore(1,"Fornitore 1","Sony",700,10,40,"Schermo piatto")
print(t1.scheda_articolo())


t1.modifica_scheda()
print(t1.scheda_articolo())


class Ordine(): # 10:25 Invernizzi
  def __init__(self, codice, data, piva, indirizzo):
    self.codice = codice
    self.data = data
    self.piva = piva
    self.indirizzo = indirizzo
    self.ordine = []

  def aggiungi_articolo(self,articolo):
    if isinstance(articolo, Televisore):
      tipo_articolo="televisore"
    elif isinstance(articolo, Frigorifero):
      tipo_articolo="frigorifero"
    self.ordine.append(articolo)
    print(f"Articolo {articolo.codice} aggiunto")

  def rimuovi_articolo(self, articolo):
    if articolo in self.articolo:
        self.ordine.remove(articolo)
        print(f"Articolo {articolo.codice} rimosso")
    else:
        print(f"Studente {articolo.codice} non esistente")

  def importo_ordine(self):
    for prodotto in self.ordine:
        importo += self.quantita(prodotto) * self.prezzo(prodotto)
        return importo

  def dettaglio_ordine(self):
    for prodotto in self.ordine:
            if isinstance(articolo, Televisore):
                sommaT += self.quantita(prodotto) * self.prezzo(prodotto)
            elif isinstance(articolo, Frigorifero):
               sommaF += self.quantita(prodotto) * self.prezzo(prodotto)
    return([self.sommaT, self.sommaF, self.sommaT+self.sommaF])


t2 = Televisore(2,"Fornitore 2","Samsung",1000,5,80,"Schermo curvo")
f1 = Frigorifero(3,"Fornitore 3","Bosch",750,12,'790x2000x600','Ultra')
f2 = Frigorifero(4,"Fornitore 4","Ariston",550,10,'590x1600x500','Medium')


ordine1=Ordine(1,"24/02/2022",'213143','Via della consegna 1')
ordine1.aggiungi_articolo(t1)
ordine1.aggiungi_articolo(t2)
ordine1.aggiungi_articolo(f1)
ordine1.aggiungi_articolo(f2)


ordine1.rimuovi_articolo(f2)
ordine1.rimuovi_articolo(f2)


ordine1.importo_ordine()


importi=ordine1.dettaglio_ordine()
print("--------------------------")
print(f"\nImporto televisori= {importi[0]}")
print(f"\nImporto frigoriferi= {importi[1]}")
print(f"\nImporto totale= {importi[2]}")


class Ordini(): # 11:00 Fine
  def __init__(self, nome_negozio, codice_negozio):
    self.nome_negozio = nome_negozio
    self.codice_negozio = codice_negozio
    self.ordini = []

  def aggiungi_ordine(self, ordine):
    for ordine in self.ordini:
            if ordine.codice == self.codice:
                ordine.aggiungi_ordine(ordine)
                return

  def rimuovi_ordine(self, ordine):
    for ordine in self.ordini:
            if ordine.codice == self.codice:
                self.ordini.remove(ordine)
                print(f"Ordine {ordine.codice} rimosso")
            else:
                print(f"Studente {articolo.codice} non esistente")

  def totale_ordini(self):
    for ordine in self.ordini:
        for prodotto in self.ordine:
                if isinstance(articolo, Televisore):
                    totT += self.quantita(prodotto) * self.prezzo(prodotto)
                elif isinstance(articolo, Frigorifero):
                    totF += self.quantita(prodotto) * self.prezzo(prodotto)
        return ([self.totT,self.totF, self.tot = self.sommaT+self.sommaF])
  

ordini_negozio=Ordini("Megastore vendita ",1)
ordini_negozio.aggiungi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)


ordini_negozio.aggiungi_ordine(ordine1)


t3 = Televisore(5,"Fornitore 5","LG",600,4,70,"Schermo curvo")
f3 = Frigorifero(6,"Fornitore 6","Bosch",450,10,'490x1000x400','Small')
ordine2=Ordine(2,"25/02/2022",'213113','Via della consegna 2')
ordine2.aggiungi_articolo(t3)
ordine2.aggiungi_articolo(f3)


ordini_negozio.aggiungi_ordine(ordine2)


importiTotali=ordini_negozio.totale_ordini()
print("--------------------------")
print(f"\nImporto totale televisori= {importiTotali[0]}")
print(f"\nImporto totale frigoriferi= {importiTotali[1]}")
print(f"\nImporto totale tutti gli ordini= {importiTotali[2]}")