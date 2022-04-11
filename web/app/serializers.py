from django.contrib.auth.models import User, Group
from rest_framework import serializers
from web.app.models import Subproducto, Producto, Rubro


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('id','codigo', 'nombre', 'rubro_id')

class SubproductoSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Subproducto
        fields = ('id','codigo', 'nombre','descripcion','producto_id' ,'stock','precio','image','image2','image3')

class RubroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rubro
        fields = ('id','codigo', 'nombre','descripcion',"image")