from django.contrib import admin

# Register your models here.
from .models import User, Table ,Plat,Commande # add table,user

admin.site.register(User) #Enregistrement du modèle user
admin.site.register(Table) 
admin.site.register(Plat)  
admin.site.register(Commande)
