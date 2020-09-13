import os

import django

if __name__ == '__main__':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'CODE.settings'
    django.setup()

    from netdisc.models import Photo
    photoes = Photo.objects.all()
    print(photoes)
