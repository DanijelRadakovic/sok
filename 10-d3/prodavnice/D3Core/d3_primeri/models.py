from django.db import models


class Prodavnica(models.Model):
    pib=models.CharField(max_length=20)
    naziv=models.CharField(max_length=50)
    adresa=models.CharField(max_length=40)
    broj_telefona=models.CharField('broj telefona',max_length=30)


    def __str__(self):
        return self.naziv

class Kategorija(models.Model):
    oznaka=models.CharField(max_length=20)
    naziv=models.CharField(max_length=50)

    def __str__(self):
        return self.naziv


class Artikal(models.Model):
    oznaka=models.CharField(max_length=20)
    naziv=models.CharField(max_length=50)
    opis=models.TextField(max_length=200)
    cena=models.DecimalField(max_digits=8,decimal_places=2)
    na_akciji=models.BooleanField('na akciji')
    kategorije=models.ManyToManyField(Kategorija)
    prodavnica=models.ForeignKey(Prodavnica,on_delete=models.CASCADE,related_name='artikli')

    def __str__(self):
        return self.naziv
