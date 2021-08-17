from django.db import transaction
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

from .models import Photo


def list_photos(request):
    if request.method == 'GET':
        photos = Photo.objects.all().order_by('unsplash_id')
        return JsonResponse(list(map(lambda p: p.to_dict(), photos)), safe=False)

    return HttpResponseNotAllowed


@csrf_exempt
def like_photo(request, pk: int):
    if request.method == 'PATCH':
        with transaction.atomic():
            photo = Photo.objects.get(pk=pk)
            photo.add_like()
        return JsonResponse(photo.to_dict())

    return HttpResponseNotAllowed


@csrf_exempt
def dislike_photo(request, pk: int):
    if request.method == 'PATCH':
        with transaction.atomic():
            photo = Photo.objects.get(pk=pk)
            photo.add_dislike()
        return JsonResponse(photo.to_dict())

    return HttpResponseNotAllowed
