# Razvoj komponenti u Python-u - Zadaci za vežbanje

## Zadatak 1

U primer sa vežbi dodati novi tip `Student` koji će definisati sledeće atribute:

- indeks (`string`),
- ime (`string`),
- prezime (`string`),
- email (`string`),
- fakultet (`Fakultet`).

Za definisanje atributa koristiti `property` dekorator. Napisati i odgovarajuće `set` metode
za koje se koristi `setter` dekorator, a koje će proveriti da li je prosleđen odgovarajući tip
vrednosti prilikom dodele vrednosti odgovarajućem atributu. Za proveru tipa `string` koristiti
python tip `str`.

## Zadatak 2

Dodati posebnu komponentu koja će učitavati studente iz fajla i posebnu komponentu koja će kreirati nove studente
direktno u kodu. Ove komponente treba da se registruju za oznaku `student.ucitati`. Core komponentu izmeniti da
prepoznaje komponente registrovane za oznaku `student.ucitati`. Pored metoda `identifier` i `name` za ove komponente
treba dodati i metodu `ucitati_studente(lista_fakulteta)` koja će biti pozvana iz core komponente.
Metoda `ucitati_studente(lista_fakulteta)` treba da vrati listu svih učitanih studenata.

## Zadatak 3

Dodati komponente za prikaz trenutno učitanih studenata. Ove komponente treba da se registruju za
oznaku `student.prikaz`. Core komponentu izmeniti da prepoznaje komponente registrovane za oznaku `student.prikaz`.
Pored metoda `identifier` i `name` za ove komponente treba dodati i metodu `prikazati_studente(lista_studenata)` koja će
biti pozvana iz core komponente. Metoda `prikazati_studente(lista_studenata)` treba da vrati vrednost tipa `string` koja
se može iskoristiti za prikaz korisniku. Za prikaz dodati dve posebne komponente:

- `StudentPrikazObican` - koja prikazuje vrednosti atributa indeks, ime i prezime za svakog studenta
- `StudentPrikazSlozen` - koja prikazuje vrednosti atributa indeks, ime, prezime, email i naziv fakulteta za svakog
  studenta