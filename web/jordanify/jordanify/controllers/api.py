from django.http import JsonResponse

from jordanify.lib import upload


def jordanify_image(request):
    file = request.FILES['image']
    if not upload.validate(file):
        return JsonResponse({'status':'error', 'description':'Either image is too large or not an image'})
    filepath = upload.save_file(request.FILES['image'])
    return JsonResponse({'status':'success', 'filepath':filepath})
