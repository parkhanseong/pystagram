import logging

from django.shortcuts import render
from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# from pystagram.middlewares import HelloWorldError
from .models import Photo
from .models import Like
from rest_framework import serializers
from rest_framework import viewsets

logger = logging.getLogger('django')

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'image', 'content', 'created_at',)

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.order_by('-id')
    serializer_class = PhotoSerializer

def toppage(request):
    messages.info(request, '글 목록에 접근하셨습니다.')
    logger.warning('the toppage view is called')
    # raise HelloWorldError('에러 났음.')
    # return HttpResponse('hello world')

    photos = Photo.object.order_by('-updated_at')
    ctx={
    'object_list' : photos,
    }

    return render(request, 'toppage.html')

def view_photo(request, pk):

    photo = get_object_or_404(Photo, pk=pk)
    ctx = {
        'photo' : photo,
    }
    return render(request, 'view_photo.html', ctx)

@login_required
def like_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    like, is_created = Like.objects.get_or_create(
        user=request.user,
        photo=photo,
        #없을때는 defaults에 딕셔너리로 저장
        defaults={
            'user':request.user,
            'photo':photo,
            'status':True,
        }
    )
    if is_created is False:
        like.status = not like.status
        like.save()
        if like.status is True:
            messages.info(request, '좋아요 표식을 남겼습니다.')
        else:
            messages.info(request, '글 목록에 취소하셨습니다.')
    else:
        messages.info(request, '좋아요 표식을 남겼습니다.')

    return redirect('photos:view_photo', kwargs={'pk':photo.pk})
