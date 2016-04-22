from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from photos.urls import urlpatterns as photos_urls
from photos.views import PhotoViewSet

router = routers.DefaultRouter()
router.register(r'restapi', PhotoViewSet)

urlpatterns = [
    url(r'^photos/', include(photos_urls, namespace='photos')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT
)

#handler404 = 'photos.views.my_404' 404자 에러시 보내는 페이지 이렇게 만듦.
