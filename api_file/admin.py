from django.contrib import admin
from .models import CsvModel
from django.utils.safestring import mark_safe


# Register your models here.
# class CsvAdmin(admin.ModelAdmin):
#     list_display = ('csv_fields', 'get_csv',)
#     list_display_links = ('csv_fields',)
#     list_editable = ('csv_fields',)
#     fields = ('csv_fields', 'get_csv',)
#     readonly_fields = ('get_csv',)
#
#     def get_csv(self, obj):
#         if obj.csv_fields:
#             return mark_safe(f'<csv src="{obj.csv_fields.url}" width="80px"')
#         else:
#             return 'Нет файла'
#
#     get_csv.short_description = 'Файл'


admin.site.register(CsvModel)
