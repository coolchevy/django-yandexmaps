django-yandexmaps
=================

easy maps integration via yandex maps api


Installation
============

1. Add your YANDEXMAPS_API_KEY to settings.py http://api.yandex.ru/maps/form.xml/
2. Add 'yandex_maps' in INSTALLED_APPS


Usage
============

Template::
    {% load yandexmaps_tags %}
    {% yandex_map_by_address object.get_address object.title 500,300 %}

Demo
============

http://colorsound.com.ua/clubs/porter-pub-1/
