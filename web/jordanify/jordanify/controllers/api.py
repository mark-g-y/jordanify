from django.http import JsonResponse

from jordanify import settings
from jordanify.lib import jordan, upload


def jordanify_image(request):
    file = request.FILES['image']
    if not upload.validate(file):
        return JsonResponse({'status':'error', 'description':'Either image is too large or not an image'})
    filepath = upload.save_file(request.FILES['image'])
    filepath = jordan.jordanify(filepath, settings.STATIC_URL + 'jordan.png')

    return JsonResponse({'status':'success', 'filepath':filepath})
