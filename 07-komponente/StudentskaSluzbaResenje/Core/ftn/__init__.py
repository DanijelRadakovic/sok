# Ovaj deo koda je potreban da bi paket bio prijavljen
# kao namespace i deljen izmedju vise distribucija.

__path__ = __import__('pkgutil').extend_path(__path__, __name__)
