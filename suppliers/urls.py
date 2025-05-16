from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Supplier app adminpage"
admin.site.site_title = "Supplier app adminpage"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]
