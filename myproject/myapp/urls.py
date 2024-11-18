from django.contrib import admin
from django.urls import path
from myapp.views.views import home,about

urlpatterns =[
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about),
]
