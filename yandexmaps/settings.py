from django.conf import settings

DEFAULT_WIDTH = getattr(settings, 'YANDEXMAPS_DEFAULT_WIDTH', 300)
DEFAULT_HEIGHT = getattr(settings, 'YANDEXMAPS_DEFAULT_HEIGHT', 300)

DEFAULT_LAT = getattr(settings, 'YANDEXMAPS_DEFAULT_LAT', 50.4300647)
DEFAULT_LNG = getattr(settings, 'YANDEXMAPS_DEFAULT_LNG', 30.5201912)

YANDEXMAPS_API_KEY = getattr(settings, 'YANDEXMAPS_API_KEY', None)
