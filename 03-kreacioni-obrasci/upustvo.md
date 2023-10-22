# Kreacioni obrasci

Diagrami obrasaca su dostupni [ovde](https://www.igordejanovic.net/courses/sok/02-kreacioni/).

## Singleton

*Singleton* obrazac mora da obezbediti jednu instancu objekta u kompletnom sistemu. Iako je njegova implementacija
jednostavna treba voditi računa kada se koristi u konkuretnom programirnaju da bude *thread-safe*
([python implementacija](primeri/singleton.py)).
Takođe, obratiti pažnj da li biblioteke koje obezbeđuju jednu istancu objekta da li su *thread-safe* ukoliko se
primenjuje konkuretno programiranje.

## Prototype

*Prototype* treba da obezbedi kopiju objekta. Prilikom implementacije treba obratit panžnju na `deep` i `shallow` načina
kopiranja. U *Python*-y se treba obratiti pažnju kako se prenose `muttable` i `inmuttable`. `Muttable` objekti se
moraju uvek kopirati koristeći `deep copy` kopiranje. `Inmuttable` objekti nemaju potrebe da se kopiraju s obzirom na to
da ih interpreter kopira u *runtime*-u ukoliko se objekat menja.

## Builder

Pored klasične implementacije *Builder* obrasca (koji obuhvata koncepte *Director*, *ConcreateBuilder* itd.), postoji i
i jednostavnija verzija *Builder* obrasca koji olaksava rad sa objektima koji imaju veliki broj parametara u
konstruktoru ([python implementacija](primeri/builder.py)). U konkretnom primeru *Builder* je ujedno i *Director* i
uvodi sledeće benefite:

- **Kreiranje kompleksnih objekata**: Kada trebate da kreirate objekat sa mnogo opcionih parametara ili konfiguracija,
  konstruktor sa dugom listom parametara može postati nepraktičan i težak za korišćenje. Builder omogućava da definišene
  parametre konstuktora koji imaju konkretnu vrednost.

- **Kombinacije parametara**: Neki objekti mogu imati više validnih konfiguracija, i neki parametri ne moraju biti
  prisutni u svakoj kombinaciji. Builder može obezbediti da se specificiraju samo parametri koji su relevantni za
  određeni objekat koji želite da kreirate.

- **Čitljivost**: Dug i komplikovan poziv konstruktora može otežati čitanje i razumevanje koda. *Builder* može
  poboljšati čitljivost koda tako što razbija proces konstrukcije u niz metoda, svaka sa smislenim imenom.

- **Nepromenjivost**: *Builder* se često koristi za kreiranje nepromenljivih objekata, što može biti važno za očuvanje
  integriteta podataka i izbegavanje neočekivanih sporednih efekata.

- **Fleksibilnost**: *Builder* se može promeniti ili proširiti proces konstrukcije bez menjanja koda klijenta koji
  koristi *Builder*. Ovo olakšava prilagođavanje promenama u strukturi ili ponašanju objekta.

Ova implemntacija se često koristi, tako da postoje biblioteke koje na gotovo nude ovu
implementaciju: [Lombok](https://projectlombok.org/features/Builder) za Javu.