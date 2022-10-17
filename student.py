import datetime

class Student(object):

    def __init__(self, vorname, nachname, matrikelnummer, geburtsdatum, noten = {}):
        self.vorname = vorname
        self.nachname = nachname
        self.matrikelnummer = matrikelnummer
        self.geburtsdatum = geburtsdatum
        self.noten = noten

    def __repr__(self):
        return f'Student(vorname={self.vorname}, nachname={self.nachname}, matrikelnummer={self.matrikelnummer}, geburtsdatum={self.geburtsdatum}, noten={self.noten})'

    def __str__(self):
        return f'Studierende Person mit Namen {self.vorname} {self.nachname}, geboren am {self.geburtsdatum}. Matrikelnummer: {self.matrikelnummer} mit folgenden Noten: {self.noten}'

    def note_eintragen(self, kurs, note):
        self.noten[kurs] = note

    def noten_berichten(self):
        print(f'{self.matrikelnummer}, Noten:')
        for kurs in self.noten:
            print(f'{kurs}: {self.noten[kurs]}')

    def noten_schummeln(self):
        anzahl = 0
        for kurs in self.noten:
            if self.noten[kurs] != 1.0:
                self.noten[kurs] = 1.0
                anzahl += 1
        return anzahl

s = Student('Max', 'Mustermann', 903172, datetime.datetime(1995, 9, 2))
s.note_eintragen('webpy',1.0)
s.note_eintragen('mathe2',1.3)
s.note_eintragen('mathe1',2.3)
s.note_eintragen('prom1',2.7)
print(s)
s.noten_berichten()
print(s.noten_schummeln())
print(s)