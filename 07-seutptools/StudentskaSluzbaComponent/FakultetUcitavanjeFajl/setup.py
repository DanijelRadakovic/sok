from setuptools import setup, find_packages

setup(
    name="ucitavanje-fakultet-fajl",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['rs', 'rs.uns', 'rs.uns.ftn', 'rs.uns.ftn.fakultet'],
    # Grupa za ucitavanje fakulteta
    # Alias `ucitavanje_fajil` se odnosi na rs.uns.ftn.fakultet.ucitavanje_fajl:FakultetUcitavanjeFajl
    entry_points={
        'fakultet.ucitavanje':
            ['ucitavanje_fajl=rs.uns.ftn.fakultet.ucitavanje_fajl:FakultetUcitavanjeFajl'],
    },
    # Propratni fajlovi koje treba instalirati zajedno sa distribucijom kompnente.
    # Specificiramo direktnorijume u koje treba instalirati odgovarajuce fajlove
    # pomocu parova (direktorijum, putanje_do_fajla).
    # Vise na: https://docs.python.org/3/distutils/setupscript.html#installing-additional-files
    data_files=[('fajlovi', ['fajlovi/fakulteti.txt'])],
    # Ovu komponentu ne treba spakovati u .zip arhivu, kako bi se omogucio pristup
    # fajlovima iz `data_files`.
    zip_safe=False
)
