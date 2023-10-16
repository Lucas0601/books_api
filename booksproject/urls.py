from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from books_api.views import UserBooks_APIView, GroupBooks_APIView
from books_api.urls import urlpatterns as books_api_urlpatterns

router = routers.DefaultRouter()
router.register(r'users', UserBooks_APIView)
router.register(r'groups', GroupBooks_APIView)

urlpatterns = [
    path('', include(router.urls)),
    path('books_api/', include(books_api_urlpatterns)),
    path('books_api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]