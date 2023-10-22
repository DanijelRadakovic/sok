# Kreacioni obrasci - zadaci za vežbanje

## Zadatak 1

Napraviti simulaciju upotrebe *Abstract Factory* dizajn obrasca na primeru *blockchain* aplikacije koja treba da omogući
komunikaciju sa sledećim mrežama: *Ethereum*, *Solana*, *Near*. Za komunikaciju ka bilo kojoj od mreža neophodni su:

- **Provider** - obezbeđuje čitanje podataka sa mreže.
    - `get_network()` - vraća naziv mreže.
    - `get_block_number()` - vraća 1 koji se inkrementira za 1 svakim pozivom metode.
- **Wallet** - obezbeđuje potpisivanje transakcija na osnovu privatnog kluča kao i njihovo slanje na mrežu.
    - `sign_transaction(tx)` - *hash*-uje proizvoljnu poruku (string) korišćenjem `sha256` *hash* funkcije. Pre
      *hash*-ovanja na poruku se dodaje naziv mreže kao prefix koja se dobija korišćenjem `Provider.get_network` metode.
    - `send_transaction(signed_tx)` - ispisuje na konzoli poruku u sledećem formatu: `Sending transaction: <tx>`.

Implementirati `Provider` i `Wallet` za sve 3 mreže i omogućiti njhivo kreiranje prateći sam dizajn obrasac. Poslati
sledeću poruku na sve 3 mreže radi upotrebe obrasca:

```text
The Times 03/Jan/2009 Chancellor on brink of second bailout for banks
```

## Zadatak 2

Potrebno je kreirati klasu `ComputerStore` koja u sebi sadrži kolekciju `Computer` objekata:

```
class Computer:
        def __init__(self, case, motherboard, cpu, memory, storage, gpu, price, additional_components=None):
        self.case = case
        self.motherboard = motherboard
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.gpu = gpu
        self.price = price
        self.additional_components = additional_components if additional_components else []

Computer("Basic Case", "Standard Motherboard", "Intel Core i5", "8GB RAM", "256GB SSD", "NVIDIA", $800, ["Keyboard", "Mouse", "Monitor"])
```

Dodati u `ComputerStorage` 10 obejkata klase `Computer` pričemu će se svaki naredni objekat razllikovati samo po jednom
atributu. Upotrebom *Prototype* dizajn obrasca pojednostaviti dodavanje tako što će prethodni objekat klonirati i
promeniti vrednost tog jednog atributa.

## Zadatak 3

Na programskom jeziku *Python* kreirati konvertor formata dokumenata. Delovi dokumenta
mogu biti sledećeg tipa:

- naslov
- podnaslov
- pasus
- nabrajanje
- definicija

*Director* kreira delove dokumenta na proizvoljan način pri čemu dokument može da sadrži više instanci istog tipa dela
dokumenta. Napraviti simulaciju konverzije u npr. *HTML*, i *Markdown* format. Posle kreiranja dokumenta *Director*
ispisuje dokument na konzoli. *Director* ne sme da sadrži referencu na konkretan *Builder*.
