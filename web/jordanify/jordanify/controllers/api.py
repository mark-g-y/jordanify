from django.http import JsonResponse

from jordanify import settings
from jordanify.lib import jordan, upload


def jordanify_image(request):
    file = request.FILES['image']
    if not upload.validate(file):
        return JsonResponse({'status':'error', 'description':'Either image is too large or not an image'})
    filename = upload.save_file(request.FILES['image'])
    jordan.jordanify(settings.STATIC_UPLOAD_URL + filename, settings.STATIC_URL + 'jordan.png')

    return JsonResponse({'status':'success', 'filepath':settings.STATIC_REL_UPLOAD_URL + filename})
