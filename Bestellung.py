class Produkt:
    def __init__(self, Name, Preis, Bestand):
        self.Name = Name
        self.Preis = float(Preis)
        self.Bestand = int(Bestand)
    def geb_bestand(self):
        return self.Bestand
    def geb_name(self):
        return self.Name
    def geb_preis(self):
        return self.Preis
    def weniger(self, Menge):
        if Menge > self.Bestand:
            print("Zu viele Produkte")
            return False
        elif self.Bestand == 0:
            print("Produkt nicht verfügbar")
            return False
        else:
            self.Bestand -= Menge
            return True

class Kunde:
    def __init__(self, Name, shop):
        self.Name = Name
        self.wk = {} # Warenkorb
        self.shop = shop
    def einkaufen(self, Produkt, Menge):
        gefunden = False
        for object in self.wk:
            if object.geb_name() == Produkt:
                gefunden = True
                break
        if not gefunden:
             for objekt in self.shop.pl:
                if Produkt == objekt.geb_name():
                    erfolg = objekt.weniger(Menge)
                    if erfolg:
                        self.wk[objekt] = Menge
                    else:
                        print("Vorgang nicht möglich")
                else:
                    print("Produkt nicht gefunden")
        if gefunden:
            print("Produkt bereits im Warenkorb")
    def einkauf(self):
        D = {}
        for objekt, menge in self.wk.items():
            D[objekt.geb_name()] = menge
        return D
    def ändern(self, Produkt):
        for objekt in self.shop.pl:
            if Produkt == objekt.geb_name():
                del self.wk[objekt]
    def mehr(self, Produkt, Menge): # Zählt hier mehr dazu als er sollte
        for object, menge in self.wk.items():
            if Produkt == object.geb_name():
                erfolg = object.weniger(Menge)
                if erfolg:
                    self.wk[object] += Menge
    def bestellen(self):
        Gesamt = 0 # Unbedingt außerhalb der Schleife da er sonst: 1) Nach jedem Durchlauf auf 0 gesetzt wird und 2) falls nichts drin ist ein Fehler kommt
        for objekt, menge in self.wk.items():
            Zusatz = objekt.geb_preis() * menge
            Gesamt += Zusatz
        return Gesamt

class shop:
    def __init__(self):
        self.kl = [] # Kundenliste
        self.pl = [] # Produktliste -> Beide als Objekte darin gespeichert
    def neues_prod(self, Name, Preis, Bestand):
        self.pl.append(Produkt(Name, Preis, Bestand))
        return self.pl
    def check_verf(self, Produkt):
        gefunden = False
        for object in self.pl:
            if Produkt == object.geb_name():
                gefunden = True
                print(object.geb_bestand())
        if not gefunden:
            print("Produkt nicht gefunden")
    def zeige_prod(self):
        if self.pl:
            L = []
            for object in self.pl:
                L.append(object.geb_name())
            print(L) # Außerhalb der Schleife da ansonsten die Liste mehrfach printed wird
        else:
            print("Keine Produkte vorhanden")


