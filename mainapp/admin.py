from django.forms import ModelChoiceField, ModelForm
from django.contrib import admin

from .models import *



class ClothesAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='clothes'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SneakersAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='sneakers'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Clothes, ClothesAdmin)
admin.site.register(Sneakers, SneakersAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
