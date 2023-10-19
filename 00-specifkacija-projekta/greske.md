# Česte greške u implementaciji projekta

## 1. Grešksa prilikom učitavanja plugin-a

![01.png](.docs/errors/01.png)

U slučaju da se paketi zovu identično u različitim pluginima, onda je potreban `namespace_packages`
parametar `setup` funkcije u kombinaciji sa `__import__('pkg_resources').declare_namespace(__name__)` u `__init__.py`.
Pogledati primer`StudentskaSluzbaComponent` sa vežbi 6.

Druga opcija je da se paketi u različitim pluginima različito zovu.
