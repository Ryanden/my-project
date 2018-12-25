from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from .. import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('members.urls.views')),
    path('products/', include('products.urls.views')),
    path('calculator/', include('costcalculator.urls.views')),
    path('options/', include('product_options.urls.views')),
    path('store/', include('stores.urls.views')),
    path('company/', include('quality_test.urls.views')),
    path('', views.index, name='index')

]
urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
