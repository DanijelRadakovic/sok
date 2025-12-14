from flask import Flask, render_template, request, redirect, url_for
from util import *
from models import Prodavnica, Artikal, podaci

app = Flask(__name__)
app.config['APP_NAME'] = 'Evidencija prodavnica'


@app.route('/')
def index():
    return render_template('index.html', title=app.config['APP_NAME'])


@app.route('/kategorije/')
def lista_kategorija():
    return render_template('lista_kategorija.html', title='Kategorije', kategorije=podaci['kategorije'])


@app.route('/prodavnice')
def lista_prodavnica():
    return render_template('lista_prodavnica.html', title='Prodavnice', prodavnice=podaci['prodavnice'])


@app.route('/prodavnice/brisanje/<pib>')
def brisanje_prodavnice(pib):
    podaci['prodavnice'] = [p for p in podaci['prodavnice'] if p.pib != pib]
    return redirect(url_for('lista_prodavnica'))


@app.route('/prodavnice/unos')
@app.route('/prodavnice/unos/<pib>')
def unos_prodavnice(pib=None):
    """
    Parametar **pib** je opcioni kako be se napravila razlika izmedju kreiranja i izmene prodavnice.
    Prilikom izmene mora da se prosledi **pib** kako bi se polja popunila postojecim vrednostima odabrane prodavnice.
    """
    if request.method == 'GET':
        if pib is None:
            return render_template('unos_prodavnice.html', title=app.config['APP_NAME'])
        else:
            prodavnica = next((p for p in podaci['prodavnice'] if p.pib == pib), None)
            if not prodavnica:
                return redirect(url_for('lista_prodavnica'))  # handles 404

            return render_template('unos_prodavnice.html',
                                   title=app.config['APP_NAME'],
                                   stari_pib=prodavnica.pib,
                                   pib=prodavnica.pib,
                                   naziv=prodavnica.naziv,
                                   adresa=prodavnica.adresa,
                                   broj_telefona=prodavnica.broj_telefona)


@app.route('/prodavnice', methods=['POST'])
def prodavnice():
    """
    Okida da se preko forme koja sluzi za dodavanje i izmenu prodavnice.
    Razlika izmedju dodavanja i izmene je u tome sto kod izmene postoji
    field **stari_pib** koji cuva pib koji je bio pre izmene s obzirom na
    to da se pib moze menjati.

    Ukoliko je kreiranje ili izmena prodavnice uspesna, preusemerava se na stranicu
    na kojoj se prikazuju sve prodavnice. U suprotnom prikazuje postojecu stranicu
    sa greskama nastale prilikom unosa.
    """
    prodavnice = podaci['prodavnice']

    greska_pib = None
    greska_naziv = None
    greska_adresa = None
    greska_broj_telefona = None

    form_pib = request.form.get('pib', '').strip()
    naziv = request.form.get('naziv', '').strip()
    adresa = request.form.get('adresa', '').strip()
    broj_telefona = request.form.get('broj_telefona', '').strip()
    stari_pib = request.form.get('stari_pib')

    if not form_pib:
        greska_pib = 'Morate uneti pib'
    if not naziv:
        greska_naziv = 'Morate uneti naziv'
    if not adresa:
        greska_adresa = 'Morate uneti adresu'
    if not broj_telefona:
        greska_broj_telefona = 'Morate uneti broj telefona'

    if not greska_pib:
        postojeca_prodavnica = next((p for p in prodavnice if p.pib == form_pib), None)

        if postojeca_prodavnica:
            if stari_pib:
                if postojeca_prodavnica.pib != stari_pib:
                    greska_pib = 'Prodavnica sa tom vrednoscu pib-a vec postoji'
            else:
                greska_pib = 'Prodavnica sa tom vrednoscu pib-a vec postoji'

    if not any([greska_pib, greska_naziv, greska_adresa, greska_broj_telefona]):
        if not stari_pib:
            prodavnice.append(Prodavnica(pib=form_pib, naziv=naziv, adresa=adresa, broj_telefona=broj_telefona))
        else:
            prodavnica = next((p for p in prodavnice if p.pib == stari_pib), None)
            if prodavnica:
                prodavnica.pib = form_pib
                prodavnica.naziv = naziv
                prodavnica.adresa = adresa
                prodavnica.broj_telefona = broj_telefona
        return redirect(url_for('lista_prodavnica'))

    return render_template("unos_prodavnice.html",
                           title=app.config['APP_NAME'],
                           greska_pib=greska_pib,
                           greska_naziv=greska_naziv,
                           greska_adresa=greska_adresa,
                           greska_broj_telefona=greska_broj_telefona,
                           pib=form_pib,
                           naziv=naziv,
                           adresa=adresa,
                           broj_telefona=broj_telefona,
                           stari_pib=stari_pib)


@app.route('/artikli')
def lista_artikala():
    return render_template('lista_artikala.html', title='Artikli', artikli=podaci['artikli'])


@app.route('/artikli/brisanje/<oznaka>?')
def brisanje_artikla(oznaka):
    podaci['artikli'] = [a for a in podaci['artikli'] if a.oznaka != oznaka]
    return redirect(url_for('lista_artikala'))


@app.route('/artikli/unos')
@app.route('/artikli/unos/<oznaka>')
def unos_artikla(oznaka=None):
    """
    Parametar **oznaka** je opcioni kako be se napravila razlika izmedju kreiranja i izmene artikla.
    Prilikom izmene mora da se prosledi **oznaka** kako bi se polja popunila postojecim vrednostima odabranog artikla.
    """
    prodavnice = podaci['prodavnice']
    kategorije = podaci['kategorije']
    artikli = podaci['artikli']

    greska_artikli = None
    greska_lista_kategorije = None

    if not prodavnice:
        greska_artikli = 'Da biste mogli da unosite Artikle morate uneti bar jednu prodavnicu.'
    if not kategorije:
        greska_lista_kategorije = 'Da biste mogli da unosite Artikle morate uneti bar jednu kategoriju.'

    if greska_artikli or greska_lista_kategorije:
        return render_template('unos_artikla.html',
                               title=app.config['APP_NAME'],
                               greska_artikli=greska_artikli,
                               greska_lista_kategorije=greska_lista_kategorije)

    if oznaka is None:
        return render_template('unos_artikla.html',
                               title=app.config['APP_NAME'],
                               prodavnice=prodavnice,
                               lista_kategorija=kategorije)
    else:
        artikal = next((a for a in artikli if a.oznaka == oznaka), None)
        if not artikal:
            return redirect(url_for('lista_artikala'))  # handles 404
        stara_oznaka = oznaka
        return render_template('unos_artikla.html',
                               title=app.config['APP_NAME'],
                               stara_oznaka=stara_oznaka,
                               oznaka=artikal.oznaka,
                               naziv=artikal.naziv,
                               opis=artikal.opis,
                               cena=artikal.cena,
                               na_akciji=artikal.na_akciji,
                               kategorije=artikal.kategorije,
                               prodavnica=artikal.prodavnica,
                               prodavnice=prodavnice,
                               lista_kategorija=kategorije)


@app.route('/artikli', methods=['POST'])
def artikli():
    """
    Okida da se preko forme koja sluzi za dodavanje i izmenu prodavnice.
    Razlika izmedju dodavanja i izmene je u tome sto kod izmene postoji
    field **stara_oznaka** koji cuva oznaku atikla koja je bila pre izmene s
    obzirom na to da se oznaka moze menjati.

    Ukoliko je kreiranje ili izmena artikla uspesna, preusemerava na stranicu
    na kojoj se prikazuju svi artikli. U suprotnom prikazuje postojecu stranicu
    sa greskama nastale prilikom unosa.
    """

    prodavnice = podaci['prodavnice']
    kategorije = podaci['kategorije']
    artikli = podaci['artikli']

    # Initialize error vars
    greska_oznaka = None
    greska_naziv = None
    greska_opis = None
    greska_cena = None
    greska_na_akciji = None
    greska_kategorije = None
    greska_prodavnica = None

    form_oznaka = request.form.get('oznaka', '').strip()
    naziv = request.form.get('naziv', '').strip()
    opis = request.form.get('opis', '').strip()
    stara_oznaka = request.form.get('stara_oznaka')

    raw_cena = request.form.get('cena', '')
    cena, cena_converted = convert_to_float(raw_cena)

    raw_akcija = request.form.get('na_akciji')
    na_akciji = True if raw_akcija else False

    oznake_kategorija = request.form.getlist('kategorije')
    prodavnica_pib = request.form.get('prodavnica', '').strip()

    if not form_oznaka:
        greska_oznaka = "Morate uneti oznaku"
    if not naziv:
        greska_naziv = "Morate uneti naziv"
    if not opis:
        greska_opis = "Morate uneti opis"
    if not raw_cena:
        greska_cena = "Morate uneti cenu"

    if not oznake_kategorija:
        greska_kategorije = "Morate izabrati kategorije"
    if not prodavnica_pib:
        greska_prodavnica = "Morate izabrati prodavnicu"

    if not cena_converted:
        greska_cena = "Morate uneti decimalnu vrednost za cenu"

    selektovana_prodavnica = None
    if not greska_prodavnica:
        prodavnica = next((p for p in prodavnice if p.pib == prodavnica_pib), None)
        if prodavnica:
            selektovana_prodavnica = prodavnica
        else:
            greska_prodavnica = "Izabrana prodavnica ne postoji"

    if not greska_oznaka:
        postojeci_artikal = next((a for a in artikli if a.oznaka == form_oznaka), None)

        if postojeci_artikal:
            if stara_oznaka:
                if postojeci_artikal.oznaka != stara_oznaka:
                    greska_oznaka = "Artikal sa tom vrednoscu oznake vec postoji"
            else:
                greska_oznaka = "Artikal sa tom vrednoscu oznake vec postoji"

    selektovane_kategorije = []
    for oznaka_kategorije in oznake_kategorija:
        kategorija = next((k for k in kategorije if k.oznaka == oznaka_kategorije), None)
        if kategorija:
            selektovane_kategorije.append(kategorija)

    if len(selektovane_kategorije) == 0:
        greska_kategorije = "Morate izabrati kategoriju"

    if not any([greska_oznaka, greska_naziv, greska_opis, greska_cena,
                greska_na_akciji, greska_kategorije, greska_prodavnica]):

        if not stara_oznaka:
            artikli.append(
                Artikal(oznaka=form_oznaka,
                        naziv=naziv,
                        opis=opis,
                        cena=cena,
                        na_akciji=na_akciji,
                        prodavnica=selektovana_prodavnica,
                        kategorije=selektovane_kategorije)
            )
        else:

            artikal = next((a for a in artikli if a.oznaka == stara_oznaka), None)
            if artikal:
                artikal.oznaka = form_oznaka
                artikal.naziv = naziv
                artikal.opis = opis
                artikal.cena = cena
                artikal.na_akciji = na_akciji
                artikal.prodavnica = selektovana_prodavnica
                artikal.kategorije = selektovane_kategorije

        return redirect(url_for('lista_artikala'))

    return render_template("unos_artikla.html",
                           title=app.config['APP_NAME'],
                           greska_oznaka=greska_oznaka,
                           greska_naziv=greska_naziv,
                           greska_opis=greska_opis,
                           greska_cena=greska_cena,
                           greska_na_akciji=greska_na_akciji,
                           greska_kategorije=greska_kategorije,
                           greska_prodavnica=greska_prodavnica,
                           oznaka=form_oznaka,
                           naziv=naziv,
                           opis=opis,
                           cena=cena,
                           na_akciji=na_akciji,
                           stara_oznaka=stara_oznaka,
                           kategorije=selektovane_kategorije,
                           prodavnica=selektovana_prodavnica,
                           prodavnice=prodavnice,
                           lista_kategorija=kategorije)


if __name__ == '__main__':
    app.run(debug=True)
