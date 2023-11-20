from setuptools import setup, find_packages

setup(
    name="ucitavanje-fakultet-kod",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['rs', 'rs.uns', 'rs.uns.ftn', 'rs.uns.ftn.fakultet'],
    # Grupa za pothranjivanje fakulteta.
    # `ucitavanje_kod` je alias za klasu FakultetUcitavanjeKod
    entry_points={
        'fakultet.ucitavanje':
            ['ucitavanje_kod=rs.uns.ftn.fakultet.ucitavanje_kod:FakultetUcitavanjeKod'],
    },
    zip_safe=True
)
