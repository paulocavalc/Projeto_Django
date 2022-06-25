from django.contrib import admin
from app.models import Postagem

@admin.register(Postagem)
class Postagem(admin.ModelAdmin):
    list_display = ['titulo', 'conteudo', 'autor', 'criado_em']

# admin.site.register(Postagem)
