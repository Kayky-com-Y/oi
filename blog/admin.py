from django.contrib import admin
from .models import Modalidade,Aluno,Curso
# Register your models here.
@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display=('nome',)
    search_fields=('nome',)
    list_filter=('nome',)

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display=('nome','email','telefone','data_nacimento')
    search_fields=('nome','email','telefone',)
    list_filter=('nome','email','telefone',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display=('nome','quantidade','descricao','modalidade')
    search_fields=('nome','quantidade','descricao','modalidade')
    list_filter=('nome','quantidade','descricao','modalidade')