from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from web.app import views
#from web.app.admin import admin_site
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'productos', views.SubproductoViewSet)
router.register(r'rubros', views.RubroViewSet)
router.register(r'tiposproductos', views.ProductoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]