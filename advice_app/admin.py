from django.contrib import admin

from.models import FeedBack,Contact,Event,Counsellor,Course,College,Tip,Message,Appointment, Student


class FeedBack_Admin(admin.ModelAdmin):

    list_display = ('name','email','remarks','ratings')

class Contact_Admin(admin.ModelAdmin):

    list_display = ('name','email','phone','date')

class Counsellor_Admin(admin.ModelAdmin):

    list_display = ('c_name','c_email','c_phone','c_city') 

class Appointment_Admin(admin.ModelAdmin):
    list_display = ('cou_detail','stu_detail')   

class Student_Admin(admin.ModelAdmin):
    list_display = ('st_name','st_email','st_name','st_city')
    search_fields = ('st_city',)

class Coun_Admin(admin.ModelAdmin):
    list_display =('c_id','c_name','c_city','c_phone')


# Register your models here.
admin.site.register(FeedBack,FeedBack_Admin)
admin.site.register(Contact,Contact_Admin)
admin.site.register(Event)
admin.site.register(Counsellor,Counsellor_Admin)
admin.site.register(Course)
admin.site.register(Student,Student_Admin)
admin.site.register(College)
admin.site.register(Tip)
admin.site.register(Message)
admin.site.register(Appointment,Appointment_Admin)

admin.site.site_header = "Aspire Advice Admin Dashboard"
admin.site.site_title = "Aspire Advice"
admin.site.index_title = "Welcome to Aspire Advice"


