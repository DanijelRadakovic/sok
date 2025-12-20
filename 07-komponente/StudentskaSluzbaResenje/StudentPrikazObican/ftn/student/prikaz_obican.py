from ftn.sluzba.services.student import StudentPrikazBase


class StudentiPrikazObican(StudentPrikazBase):
    def identifier(self):
        return "StudentiPrikazObican"

    def name(self):
        return "Prikaz indeksa, imena i prezimena studenata"

    def prikazati_studente(self, lista_studenata):
        prikaz = "{:10}|{:40}|{:40}\n".format("Indeks", "Ime", "Prezime")
        for s in lista_studenata:
            prikaz += "{:10}|{:40}|{:40}\n".format(s.indeks, s.ime, s.prezime)
        return prikaz
