from django.contrib import admin

# Register your models here.
from .models import User,Document 
class UserAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,              {'fields':['user_name','password']}),
        ('User Information',{'fields':['full_name','email_id','phone_no']}),
        ('Date Information',{'fields':['signup_date']}),
    ]
    list_display = ('user_name','password', 'full_name', 'email_id', 'phone_no','signup_date')
    list_filter = ['full_name','signup_date']
    search_fields = ['full_name']

class DocumentAdmin(admin.ModelAdmin):
    fieldsets=[
        ('Document Information',{'fields':['doc_name','doc_type','pub_by']}),
        ('Date Information',{'fields':['pub_date']}),
    ]
    list_display = ('doc_name','doc_type','pub_by','pub_date')
    list_filter = ['doc_name','doc_type','pub_date']
    search_fields = ['doc_name','doc_type']
#class 
admin.site.register(User,UserAdmin)
admin.site.register(Document,DocumentAdmin)
