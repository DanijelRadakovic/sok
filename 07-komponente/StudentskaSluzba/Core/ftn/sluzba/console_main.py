from typing import List, Union
from importlib.metadata import entry_points

from ftn.sluzba.services.fakultet import (
    FakultetUcitatiBase,
    FakultetPrikazBase
)

def console_menu(**kwargs):
    plugini: List[Union[FakultetUcitatiBase, FakultetPrikazBase]] = \
        kwargs.get("fakultet_ucitavanje", []) + kwargs.get("fakultet_prikaz", [])
    if not plugini:
        print("Nije prepoznati nijedan plugin!")
        return
    greska = False
    poruka = None
    while True:
        print("-----------------------------------")
        if greska:
            print("Uneli ste pogresnu vrednost za opciju")
            greska = False
        if poruka:
            print(poruka)
        print("Izaberite broj opcije:")
        for i, plugin in enumerate(plugini):
            print(f"{i} {plugin.identifier()} {plugin.name()}")
        print(f"{len(plugini)} za izlaz")
        try:
            izbor = int(input("Unesite redni broj opcije:"))
        except:
            greska = True
            continue
        if izbor == len(plugini):
            return
        elif 0 <= izbor < len(plugini):
            poruka = izabrana_opcija(plugini[izbor], **kwargs)
        else:
            greska = True


def izabrana_opcija(plugin: Union[FakultetUcitatiBase, FakultetPrikazBase], **kwargs):
    try:
        if isinstance(plugin, FakultetUcitatiBase):
            fakulteti = kwargs["fakulteti"]
            pomocna_lista = plugin.ucitati_fakultete()
            del fakulteti[:]
            fakulteti.extend(pomocna_lista)
            return f"Ucitani fakulteti koristeci '{plugin.name()}' plugin\n"
        elif isinstance(plugin, FakultetPrikazBase):
            fakulteti = kwargs["fakulteti"]
            return plugin.prikazati_fakultete(fakulteti)
    except Exception as e:
        print(f"Error: {e}")


def load_plugins(oznaka):
    """
    Dinamicko prepoznavanje plagina na osnovu pripadajuce grupe.
    """
    plugins = []
    for ep in entry_points(group=oznaka):
        # Ucitavanje plagina.
        p = ep.load()
        print(f"{ep.name} {p}")
        # instanciranje odgovarajuce klase
        plugin = p()
        plugins.append(plugin)
    return plugins


def main():
    try:
        fakultet_ucitavanje = load_plugins("fakultet.ucitavanje")
        fakultet_prikaz = load_plugins("fakultet.prikaz")

    except Exception as e:
        print(f"Error: {e}")
        return

    try:
        console_menu(fakultet_ucitavanje=fakultet_ucitavanje,
                     fakultet_prikaz=fakultet_prikaz,
                     fakulteti=[])

    except Exception as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    main()
