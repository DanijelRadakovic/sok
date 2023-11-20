from setuptools import setup, find_packages

setup(
    # naziv komponente prilikom instaliranja
    name="studentska-sluzba-core",
    # verzija komponente
    version="0.1",
    # Distribucija svih paketa koji se nalaze u `.` direktorijumu.
    # Moguce je izabrate samo neke pakete i dati ih u vidu liste.
    packages=find_packages(),
    # Paketi rs, rs.uns i rs.uns.ftn su zajednicki za vise distribucija
    # (npr. Core, FakultetPrikazObican, FakultetPrikazSlozen, ...).
    # Da bismo izbegli clashing i omogucili deljenje potpaketa i modula
    # ovih paketa na vise distribucija, potrebno je definisati namespace-ove.
    # Takodje, `__init__.py` moduli ova tri paketa moraju sadrzati poziv
    # declare_namespace() funkcije.
    namespace_packages=['rs', 'rs.uns', 'rs.uns.ftn'],
    # Sta ova distribucija (komponenta) nudi ostalim komponentama na koriscenje.
    # Na ovaj nacin radimo export FakultetPrikazBase i FakultetUcitavanjeBase
    # apstraktnih servisa.
    provides=['rs.uns.ftn.studentska.sluzba.services',
              ],
    # Koje su ulazne tacke u nasu komponentu?
    # Ova komponenta se korista kao skripta iz konzole (terminala),
    # the pripada grupi `console_scripts`.
    # Ovoj komponenti dodeljujemo alias `sluzba_main` kojim mozemo pozvati
    # rs.uns.ftn.studentska.sluzba.console_main:main funckije iz CLI-a
    # upotrebno alias (tj. $ sluzba_main)
    entry_points={
        'console_scripts':
            ['sluzba_main=rs.uns.ftn.studentska.sluzba.console_main:main'],
    },
    # Da li je u redu da se nasa komponente spakuje u zip arhivu.
    zip_safe=True
)
