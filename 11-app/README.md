

## Podesavanje projekta

Instalacija dev alata kako bi se omogućio development prilikom
razvoja aplikacije nad komponentama

```shell
pip install -r requirements.txt
```

Podesavanje aplikacije

```shell
pip install ./api ./core ./datasource-code ./datasource-db

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Rad sa migracijama

`python manage.py makemigrations` cuva migracije u `site-package/shop/db/migrations`
tako da ukoliko je neophodno obrisati migracije (i generistai ponovo) neopdho je 
obrisati fajl sa te lokacije.

### Napomena

Rad sa bazom koristeci Django biblioteku nije toliko nezavisan zbog samo
nacina funkcionisanja Django framework-a. Djano aplikacija je zbog toga 
"svesna" plugin-a za ucitanje iz baze tako sto smo morali da dodamo plugin
kao Django aplikaciju konfiguracijom `INSTALLED_APPS` sekciju ([ovde](django/sites/settings.py)).

Neko bolje resenje bi bilo da se koristi neka druga biblioteka za bazu i time
uspostavili kompletnu nezavisnost izmedju django aplikacije i plugin-a za 
ucitavanje iz baze.