from setuptools import setup, find_packages
setup(
    name="ucitavanje-studenti-fajl",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['rs','rs.uns','rs.uns.ftn','rs.uns.ftn.studenti'],
    entry_points = {
        'student.ucitavanje':
            ['ucitavanje_fajl=rs.uns.ftn.studenti.ucitavanje_fajl:StudentiUcitavanjeFajl'],
    },
    data_files=[('fajlovi',['fajlovi/studenti.txt'])],
    zip_safe=False
)