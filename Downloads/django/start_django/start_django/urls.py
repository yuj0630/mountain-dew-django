from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views
from django.conf import settings
urlpatterns = [
    path('', include("map.urls")),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),

]
# 개발 환경에서는 static 파일 서빙을 위해 다음 코드를 추가합니다.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


