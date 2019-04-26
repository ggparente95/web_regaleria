from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from .models import Producto, Subproducto, Rubro

class ProductoAdmin(admin.ModelAdmin):
    
    list_display = ('codigo','nombre')


class SubproductoAdmin(admin.ModelAdmin):
    
    list_display = ('codigo','nombre','producto','stock','precio')

class RubroAdmin(admin.ModelAdmin):

    list_display = ('codigo','nombre')

class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('Blanqueria BIEN BLANQUITO')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('Administracion')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Sitio de Administracion')

admin_site = MyAdminSite()

admin_site.register(Producto, ProductoAdmin)
admin_site.register(Subproducto, SubproductoAdmin)
admin_site.register(Rubro, RubroAdmin)
