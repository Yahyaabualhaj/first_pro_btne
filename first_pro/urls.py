
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('proj_accounts/', include('proj_accounts.urls')),
    path('contacts/', include('contacts.urls')),

]
# + static(settings.MEDIA_URL,
#            document_root=settings.MEDIA_ROOT)

