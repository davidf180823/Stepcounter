from datetime import date, datetime


class Schrittzähler:
    def __init__(self):
        self.datum = date.today()
        self.schritte = 0

    def schritte_hinzufügen(self, anzahl):
        self.schritte += anzahl

    def gesamtzahl_der_schritte(self):
        return f'{self.datum.strftime("%d.%m.%Y")}: {self.schritte} Schritte gegangen'

    def daten_speichern(self, dateipfad='schrittzählerdaten.txt'):
        with open(dateipfad, 'a') as datei:
            jetzt = datetime.now()
            datei.write(f'{jetzt.strftime("%H:%M:%S")} - {self.datum.strftime("%d.%m.%Y")}: {self.schritte}\n')

    @classmethod
    def daten_aus_datei_laden(cls, dateipfad='schrittzählerdaten.txt'):
        schrittzähler_liste = []
        with open(dateipfad, 'r') as datei:
            for zeile in datei:
                zeit_str, rest = zeile.strip().split(' - ')
                datum_str, schritte_text = zeile.strip().split(': ')
                datum = datetime.strptime(datum_str, "%d.%m.%Y").date()
                schritte = int(schritte_text.split()[0])
                schrittzähler = cls()
                schrittzähler.datum = datum
                schrittzähler.schritte = schritte
                schrittzähler_liste.append(schrittzähler)
        return schrittzähler_liste


# Benutzereingabe für die gelaufenen Schritte
def benutzereingabe_schritte():
    while True:
        try:
            schritte = int(input("Geben Sie die gelaufenen Schritte ein: "))
            return schritte
        except ValueError:
            print("Bitte geben Sie eine gültige ganze Zahl ein.")


# Funktion für die Benutzereingabe, ob das Programm beendet werden soll
def benutzereingabe_programm_beenden():
    antwort = input("Möchten Sie das Programm beenden? (ja/nein): ").lower()
    return antwort == "ja"


# Beispiel der Verwendung
if __name__ == "__main__":
    beenden = False

    while not beenden:
        # Ein Schrittzähler erstellen und Benutzereingabe für die gelaufenen Schritte abfragen
        schrittzähler1 = Schrittzähler()
        neue_schritte = benutzereingabe_schritte()
        schrittzähler1.schritte_hinzufügen(neue_schritte)

        # Daten in die Datei schreiben
        schrittzähler1.daten_speichern()

        # Gesamtzahl der gelaufenen Schritte für den Tag anzeigen
        print(schrittzähler1.gesamtzahl_der_schritte())

        # Benutzereingabe, ob das Programm beendet werden soll
        beenden = benutzereingabe_programm_beenden()
