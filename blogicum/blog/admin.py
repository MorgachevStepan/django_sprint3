from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('is_published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_published', 'created_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'pub_date',
        'is_published',
        'created_at'
    )
    search_fields = ('title', 'text')
    list_filter = ('is_published', 'pub_date', 'created_at', 'category')
    autocomplete_fields = ('author', 'category', 'location')


class Meta:
    verbose_name = _('публикация')
    verbose_name_plural = _('Публикации')


Category._meta.verbose_name = _('категория')
Category._meta.verbose_name_plural = _('Категории')

Location._meta.verbose_name = _('местоположение')
Location._meta.verbose_name_plural = _('Местоположения')

Post._meta.verbose_name = _('публикация')
Post._meta.verbose_name_plural = _('Публикации')

Category._meta.get_field('is_published').verbose_name = _('Опубликовано')
Category._meta.get_field('title').verbose_name = _('Заголовок')
Category._meta.get_field('slug').verbose_name = _('Идентификатор')
Category._meta.get_field('description').verbose_name = _('Описание')
Category._meta.get_field('created_at').verbose_name = _('Добавлено')

Location._meta.get_field('is_published').verbose_name = _('Опубликовано')
Location._meta.get_field('name').verbose_name = _('Название места')
Location._meta.get_field('created_at').verbose_name = _('Добавлено')

Post._meta.get_field('is_published').verbose_name = _('Опубликовано')
Post._meta.get_field('title').verbose_name = _('Заголовок')
Post._meta.get_field('text').verbose_name = _('Текст')
Post._meta.get_field('pub_date').verbose_name = _('Дата и время публикации')
Post._meta.get_field('author').verbose_name = _('Автор публикации')
Post._meta.get_field('category').verbose_name = _('Категория')
Post._meta.get_field('location').verbose_name = _('Местоположение')
Post._meta.get_field('created_at').verbose_name = _('Добавлено')

Post._meta.get_field('is_published').help_text = _(
    'Снимите галочку, чтобы скрыть публикацию.'
)
Post._meta.get_field('pub_date').help_text = _(
    'Если установить дату и время в будущем — '
    'можно делать отложенные публикации.'
)
