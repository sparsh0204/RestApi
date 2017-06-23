from django.conf.urls import url, include
from django.contrib import admin
from api import views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'data', views.Datatablelist)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^register/$', views.CreateUserView.as_view(), name='user'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
