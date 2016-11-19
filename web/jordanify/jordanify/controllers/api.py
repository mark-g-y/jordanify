import random
from django.http import JsonResponse


def jordanify_image(request):
    save_file(request.FILES['image'])
    return JsonResponse({'status':'success'})


def save_file(file):
    file_type = file.content_type.split('/')[1]
    name = random.getrandbits(128)
    with open('jordanify/static/uploads/' + str(name) + '.' + file_type, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
