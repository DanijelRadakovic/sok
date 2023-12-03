import pkg_resources
from django.apps import AppConfig


class D3PrimeriConfig(AppConfig):
    name = 'd3_primeri'
    plugini_ucitavanje = []

    def ready(self):
        # Prilikom startovanja aplikacije, ucitavamo plugine na
        # vec poznati nacin.
        self.plugini_ucitavanje = load_plugins("prodavnica.ucitati")


def load_plugins(oznaka):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=oznaka):
        p = ep.load()
        print("{} {}".format(ep.name, p))
        plugin = p()
        plugins.append(plugin)
    return plugins
