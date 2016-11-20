from django.http import JsonResponse

from jordanify import settings
from jordanify.lib import jordan, upload


def jordanify_image(request):
    file = request.FILES['image']
    if not upload.validate(file):
        return JsonResponse({'status':'error', 'description':'Either image is too large or not an image'})
    filename = upload.save_file(request.FILES['image'])
    filepath = settings.STATICFILES_DIRS[0] + 'uploads/' + filename
    image = jordan.jordanify(filepath, settings.STATICFILES_DIRS[0] + 'images/jordan.png')
    image.save(filepath)

    return JsonResponse({'status':'success', 'filepath':settings.STATIC_URL + 'uploads/' + filename})
