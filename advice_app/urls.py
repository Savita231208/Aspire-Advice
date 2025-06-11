from django.urls import path
from.import views , user_views
urlpatterns = [
    path("",views.home,name="home"),
    path("aboutus/",views.aboutus,name="about_us"),
    path("feedback/",views.feedback,name="feedback"),
    path("contactus/",views.contactus,name="contact_us"),
    path("student_login/",user_views.login,name="student_login"),
    path("user_registration/",user_views.registration,name="user_registration"),
    path("events/",views.event_update,name="events"),
    path("more_feedback/",views.more_feedback,name="more_feedback"),
    path("stu_registration/",user_views.stu_registration,name="stu_registration"),
    path("coun_login/",user_views.conlogin,name="coun_login"),
    path("student_home/",user_views.student_home,name="student_home"),
    path("coun_home/",user_views.coun_home,name="coun_home"),
    path("student_edit_profile/",user_views.student_edit_profile,name="student_edit_profile"),
    path("coun_edit_profile/",user_views.coun_edit_profile,name="coun_edit_profile"),
    path("add_tips/",user_views.add_tips,name="add_tips"),
    path("student_logout/",user_views.student_logout),
    path("coun_logout/",user_views.counsellor_logout),
    path("college/",views.view_college,name="College"),
    path("course/",views.course,name="Course"),
    path("tips/",views.tips,name="tips"),
    path("c_compose/",user_views.c_compose,name="compose"),
    path("c_inbox/",user_views.c_inbox,name="inbox"),
    path("s_compose/",user_views.s_compose,name="compose"),
    path("s_inbox/",user_views.s_inbox,name="inbox"),
    path("show_message/",user_views.showmessage,name="show_message"),
    path("appointment/",user_views.appointment,name="appointment"),
    path("pending_app/",user_views.pending_app,name="pending_app"),
    path("appo_status/",user_views.appo_status,name="appo_status"),
    path("confirm_app/",user_views.confirm_app,name="confirm_app"),



]