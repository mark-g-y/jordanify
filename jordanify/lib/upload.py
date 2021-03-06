import random

from jordanify import settings


def validate(file):
    content_type = file.content_type.split('/')[0]
    if content_type in settings.CONTENT_TYPES and file._size < settings.MAX_UPLOAD_SIZE:
        return True
    return False


def save_file(file):
    file_type = file.content_type.split('/')[1]
    name = str(random.getrandbits(128)) + '.' + file_type
    with open(settings.STATICFILES_DIRS[0] + 'uploads/' + name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return name
            