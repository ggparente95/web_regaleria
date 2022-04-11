from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from web.app.serializers import UserSerializer, GroupSerializer, SubproductoSerializer, ProductoSerializer, RubroSerializer
from web.app.models import Subproducto, Producto, Rubro


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SubproductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Subproducto.objects.all().order_by('nombre')
    serializer_class = SubproductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Producto.objects.all().order_by('nombre')
    serializer_class = ProductoSerializer

class RubroViewSet(viewsets.ModelViewSet):

    queryset = Rubro.objects.all().order_by('nombre')
    serializer_class = RubroSerializer