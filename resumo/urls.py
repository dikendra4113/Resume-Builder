from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from resumo import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url('resumo/', include('main_app.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url('', RedirectView.as_view(url='resumo/')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
