from apps.models import Model


class Provinsi(Model):
    __table__ = 'scrape_bps'
    __primary_key__ = 'provinsi'
    __timestamps__ = False
