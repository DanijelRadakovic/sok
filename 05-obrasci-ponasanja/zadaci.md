# Obrasci ponasanja - zadaci za vežbanje

## Zadatak 1

Klasa `StudentskaSluzba` čuva studente sortirane po broju indeksa. Potrebno je prikazati studente sortirane po prezimenu
i imenu. Upotrebom `Strategy` dizajn obrasca napraviti metodu za prikaz sortirane liste pri čemu će algoritam za
sortiranje biti izmenjiv. Napraviti dve konkretne implementacije algoritma za sortiranje: `BubbleSort` i `QuickSort`.

**Napomena**: Nije potrebno zaista implementirati algoritme za sortiranje već je dovoljno
samo na konzoli ispisati koje sortiranje se obavlja.

## Zadatak 2

Simulator kotla za grejanje se, između ostalog, sastoji od klase `MeracPritiska` sa metodama: 
- `uzmi_pritisak() -> int`: koja vraća tekući pritisak u kotlu, 
- `podesi_pritisk(int)`: postavlja tekući pritisak.

Za prikaz pritiska zadužena je klasa `PritisakPrikaz`. Takod̄e, sigurnosni ventil, predstavljen klasom `SigurnosniVentil`,
treba da automatski reaguje kada pritisak u kotlu pred̄e unapred zadatu vrednost i da se otvori. 

Korišćenjem `Observer` dizajn obrasca simulirati rad kotla pri čemu će se iz test klase postavljati vrednost pritiska 
u kotlu dok će se pritisak prikazivati iz metoda klase `PritisakPrikaz` a otvaranje sigurnosnog ventila će biti 
prikazano iz metoda klase `SigurnosniVentil`. Svi prikazi treba da budu na konzoli.

## Zadatak 3

Klasa `StudentSelectionSort` definiše metodu `sort(lista_studenata) -> None` za sortiranje liste elemenata
tipa `Student`. Metoda `sort` je šablon metoda i koristi poziv metode `compare(student1,student2) -> int` da utvrdi
odnos izmed̄u `student1` i `student2`. Metoda `compare`:

- za `student1<student2` vraća `-1`,
- za `student1==student2` vraća `0` i
- za `student1>student2` vraća `1`.

Klasa Student ima atribute: `brojIndeksa: int`, `ime: str`, `prezime: str`.

Napisati klase:

- StudentSelectionSort,
- Student.

Sledeće klase nasleđuju `StudentSelectionSort` i redefinišu metodu `compare`:

- `StudentSortIndeks` - `compare` treba da poredi studente po broju indeksa,
- `StudentSortIme` - `compare` treba da poredi studente po imenu,
- `StudentSortPrezime` - `compare` treba da poredi studente po prezimenu.

Sortirati proizvoljan niz elemenata po sva tri kriterijuma. Ispisati sortiran niz na konzoli. Uraditi isti zadatak
primenom `strategy` dizajn šablona.