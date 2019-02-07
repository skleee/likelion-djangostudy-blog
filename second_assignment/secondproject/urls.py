from django.contrib import admin
from django.urls import path, include # include: import path to another URLconf
from django.conf import settings
from django.conf.urls.static import static

import accounts.views
import blog.views
import portfolio.views # DONT FORGET!!!!!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.blog, name='home'),
    path('blog/', include('blog.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
