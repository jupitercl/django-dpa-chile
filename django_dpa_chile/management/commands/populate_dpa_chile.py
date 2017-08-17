# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urllib3
import json
from bunch import bunchify
from django.core.management.base import BaseCommand, CommandError
from django_dpa_chile.models import Region, Provincia, Comuna

safe_ascci = {'\xc1': 'Á', '\xc9': 'É', '\xcd': 'Í', '\xd3': 'Ó', '\xda': 'Ú',
              '\xdc': 'U', '\xd1': 'Ñ', '\xc7': 'C', '\xed': 'i', '\xf3': 'o',
              '\xf1': 'ñ', '\xe7': 'c', '\xba': '', '\xb0': '', '\xe1': 'á',
              '\xe2': 'a', '\xe3': 'a', '\xe4': 'a', '\xe5': 'a', '\xe8': 'e',
              '\xe9': 'é', '\xea': 'e', '\xeb': 'e', '\xec': 'i', '\xed': 'í',
              '\xee': 'i', '\xef': 'i', '\xf2': 'o', '\xf3': 'ó', '\xf4': 'o',
              '\xf5': 'o', '\xf0': 'o', '\xf9': 'u', '\xfa': 'u', '\xfb': 'u',
              '\xfc': 'u', '\xe5': 'a'}


class Command(BaseCommand):
    help = 'Populate Political-Administrative Division of Chile'

    def handle(self, *args, **options):
        urllib3.disable_warnings()
        http = urllib3.PoolManager()

        r = http.request('GET', 'https://apis.modernizacion.cl/dpa/regiones')
        j = json.loads(r.data)
        regiones = bunchify(j)

        for region in regiones:
            self.stdout.write(self.style.SUCCESS('Region: {}'.format(region.nombre)))
            try:
                fields = {'tipo': region.tipo,
                          'nombre': region.nombre,
                          'lat': str(region.lat),
                          'lng': str(region.lng),
                          'url': region.url}

                obj, created = Region.objects.update_or_create(
                    codigo=region.codigo, defaults=fields)

                self.provincia(obj, http)
            except Exception as e:
                raise CommandError('Fail populate - Exception: {}'.format(e))

        self.stdout.write(
            self.style.SUCCESS('Successfully populate dpa chile'))

    def provincia(self, region, http):
        p = http.request(
            'GET',
            'https://apis.modernizacion.cl/dpa/regiones/{}/provincias'.format(region.codigo))
        j = json.loads(p.data)
        provincias = bunchify(j)
        for provincia in provincias:
            self.stdout.write(self.style.SUCCESS('Provincia: {}'.format(provincia.nombre)))
            try:
                fields = {'tipo': provincia.tipo,
                          'nombre': provincia.nombre,
                          'lat': str(provincia.lat),
                          'lng': str(provincia.lng),
                          'url': provincia.url,
                          'region': region}

                obj, created = Provincia.objects.update_or_create(
                    codigo=provincia.codigo, defaults=fields)

                self.comunas(obj, http)
            except Exception as e:
                raise CommandError('Fail populate - Exception: {}'.format(e))

    def comunas(self, provincia, http):
        c = http.request(
            'GET',
            'https://apis.modernizacion.cl/dpa/regiones/{}/provincias/{}/comunas'.format(provincia.region.codigo,
                                                                                         provincia.codigo))
        j = json.loads(c.data)
        comunas = bunchify(j)
        for comuna in comunas:
            self.stdout.write(self.style.SUCCESS('Comuna: {}'.format(comuna.nombre)))
            try:
                fields = {'tipo': comuna.tipo,
                          'nombre': comuna.nombre,
                          'lat': str(comuna.lat),
                          'lng': str(comuna.lng),
                          'url': comuna.url,
                          'provincia': provincia}

                obj, created = Comuna.objects.update_or_create(
                    codigo=comuna.codigo, defaults=fields)

            except Exception as e:
                raise CommandError('Fail populate - Exception: {}'.format(e))
