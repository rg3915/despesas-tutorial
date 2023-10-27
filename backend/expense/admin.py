from django.contrib import admin

from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'value', 'status')
    # readonly_fields = ('slug', 'created', 'modified')
    # list_display_links = ('name',)
    search_fields = ('title',)
    list_filter = ('status',)
    # date_hierarchy = 'created'
    # ordering = ('-created',)
    # actions = ('',)

# admin.site.register(Expense)
