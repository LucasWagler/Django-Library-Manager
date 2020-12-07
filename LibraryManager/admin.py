from django.contrib import admin

from .models import Author, Book, BookBranchCopies, Branch, Department, Employee
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    # fields = ['name', 'country']
    list_display = ('name', 'country')
    search_fields = ['name', 'country']

class BookBranchCopiesInline(admin.TabularInline):
    model = BookBranchCopies
    extra = 1
    

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    list_filter = ['price']
    search_fields = ['title', 'author__name', 'author__country']
    inlines = [BookBranchCopiesInline]
    # fields = ['image_tag']
    # readonly_fields = ['image_tag']

class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'phone']
    search_fields = ['name', 'city', 'phone']

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'budget']
    search_fields = ['name']
    # filter by budget

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user', 'department', 'branch']
    search_fields = ['name', 'department__name', 'branch__name', 'email']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)

admin.AdminSite.site_header = 'Aesop Bookstore'
admin.AdminSite.site_title = 'Aesop Bookstore'
admin.AdminSite.site_url = '/admin'
admin.AdminSite.index_title = 'Bookstore Administration'
