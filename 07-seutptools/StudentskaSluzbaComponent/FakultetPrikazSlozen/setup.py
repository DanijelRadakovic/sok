from setuptools import setup, find_packages

setup(
    name="prikaz-fakultet-slozen",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['rs', 'rs.uns', 'rs.uns.ftn', 'rs.uns.ftn.fakultet'],
    # Grupa za prikazivanje fakulteta
    # `prikaz_slozen` alias se odnosi na
    # rs.uns.ftn.fakultet.prikaz_slozen:FakultetPrikazSlozen
    entry_points={
        'fakultet.prikaz':
            ['prikaz_slozen=rs.uns.ftn.fakultet.prikaz_slozen:FakultetPrikazSlozen'], },
    zip_safe=True
)
