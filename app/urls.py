from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import  CarsListView, CreateCarsView, CarDetailView, CarUpdateView
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('new_car/', CreateCarsView.as_view(), name='new_car'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
