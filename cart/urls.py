
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.showCart, name='showCart'),
                  path('addCart/<int:id>', views.addCart, name='addCart'),
                  path('removeCart/<int:id>', views.removeCart, name='removeCart'),
                  path('complete/', views.paymentComplet, name='complete'),
                  path('paymentSucess/', views.paymentSucess, name='paymentSucess'),
                  #path('search', views.search, name='search'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
