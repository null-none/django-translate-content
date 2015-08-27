# -*- coding: utf-8 -*- 

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from yandex_translate import YandexTranslate

from .models import Page


class Command(BaseCommand):
    help = 'Translate content'

    def handle(self, *args, **options):
        translate = YandexTranslate(settings.YANDEX_TRANSLATE_KEY)
        objects = Page.objects.all()
        for item in objects:
            print('Translate:', translate.translate(item.text, 'ru-en')) 
        self.stdout.write('Finished translate')