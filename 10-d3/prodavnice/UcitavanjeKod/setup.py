from setuptools import setup, find_packages

setup(
    name="prodavnica-ucitavanje-kod",
    version="0.1",
    packages=find_packages(),
    install_requires=['d3-primeri>=0.1'],
    entry_points = {
        'prodavnica.ucitati':
            ['ucitavanje_kod=ucitavanje.kod.ucitavanje_kod:UcitatiProdavniceKod'],
    },
    zip_safe=True
)