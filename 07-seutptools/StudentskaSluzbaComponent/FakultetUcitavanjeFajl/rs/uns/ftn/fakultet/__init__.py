# Ovaj deo koda je potreban da bi paket bio prijavljen
# kao namespace i deljen izmedju vise distribucija.
# Mora da se poklapa sa vrednostima namespace_pakages u setup.py modulu.
# Oficijalna dokumentacija:
#   https://setuptools.pypa.io/en/latest/pkg_resources.html#namespace-package-support
# Dodatno objasnjenje:
#   https://stackoverflow.com/questions/7785944/what-does-import-pkg-resources-declare-namespace-name-do

__import__('pkg_resources').declare_namespace(__name__)