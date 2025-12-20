from ftn.sluzba.services.student import StudentPrikazBase


class StudentiPrikazSlozen(StudentPrikazBase):
    def identifier(self):
        return "StudentiPrikazSlozen"

    def name(self):
        return "Prikaz svih atributa studenata"

    def prikazati_studente(self, lista_studenata):
        prikaz = "{:10}|{:40}|{:40}|{:20}|{:40}\n".format("Indeks", "Ime", "Prezime", "Email", "Fakultet")
        for s in lista_studenata:
            prikaz += "{:10}|{:40}|{:40}|{:20}|{:40}\n".format(s.indeks, s.ime, s.prezime, s.email,
                                                               "" if s.fakultet is None else s.fakultet.naziv)
        return prikaz
