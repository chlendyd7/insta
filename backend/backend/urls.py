from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # 미디어 경로 요청 시 setting.media_root에서 찾겠다

    import debug_toolbar
    urlpatterns+=[
        path('__debug__/', include(debug_toolbar.urls)),
    ]