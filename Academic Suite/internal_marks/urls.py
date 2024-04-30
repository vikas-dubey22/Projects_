"""
URL configuration for internal_marks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import  views,hod,staff_views,student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE,name='base'),

    path('', views.LOGIN,name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='Logout'),

    path('Profile', views.PROFILE,name='profile'),
    path('Profile/update', views.PROFILE_UPDATE,name='profile_update'),
    path('hod/home', hod.home,name='hod_home'),
    path('hod/student/add', hod.ADD_STUDENT,name='add_student'),
    path('hod/student/view', hod.VIEW_STUDENT,name='view_student'),
    path('hod/course/add', hod.ADD_COURSE,name='add_course'),
    path('hod/student/edit/<str:id>', hod.EDIT_STUDENT,name='edit_student'),
    path('hod/student/update', hod.UPDATE_STUDENT,name='update_student'),
    path('hod/student/delete/<str:admin>',hod.DELETE_STUDENT,name='delete_student'),
    path('hod/course/view', hod.VIEW_COURSE,name='view_course'),
    path('hod/course/edit/<str:id>', hod.EDIT_COURSE,name='edit_course'),
    path('hod/course/update', hod.UPDATE_COURSE,name='update_course'),
    path('hod/course/delete/<str:id>',hod.DELETE_COURSE, name='delete_course'),

    path('hod/Staff/add',hod.ADD_STAFF,name='add_staff'),
    path('hod/Staff/view', hod.VIEW_STAFF,name='view_staff'),
    path('hod/Staff/edit/<str:id>', hod.EDIT_STAFF,name='edit_staff'),
    path('hod/Staff/update', hod.UPDATE_STAFF,name='update_staff'),
    path('hod/Staff/delete/<str:admin>',hod.DELETE_STAFF,name='delete_staff'),

    path('hod/Subject/add',hod.ADD_SUBJECT,name='add_subject'),
    path('hod/Subject/view', hod.VIEW_SUBJECT,name='view_subject'),
    path('hod/Subject/edit/<str:id>', hod.EDIT_SUBJECT,name='edit_subject'),
    path('hod/Subject/update', hod.UPDATE_SUBJECT,name='update_subject'),
    path('hod/Subject/delete/<str:id>', hod.DELETE_SUBJECT,name='delete_subject'),

    path('hod/Session/add',hod.ADD_SESSION,name='add_session'),
    path('hod/Session/view', hod.VIEW_SESSION,name='view_session'),
    path('hod/Session/edit/<str:id>', hod.EDIT_SESSION,name='edit_session'),
    path('hod/Session/update', hod.UPDATE_SESSION,name='update_session'),
    path('hod/Session/delete/<str:id>', hod.DELETE_SESSION,name='delete_session'),
    path('hod/Staff/Send_Notification',hod.STAFF_SEND_NOTIFICATION,name='staff_notification'),
    path('hod/Staff/save_notification', hod.SAVE_NOTIFICATION, name='save_staff_notification'),
    path('hod/Staff/leave_view',hod.STAFF_LEAVE_VIEW,name="staff_leave_view"),
    path('hod/Staff/approve_view/<str:id>', hod.STAFF_APPROVE, name='staff_approve_leave'),
    path('hod/Staff/reject_view/<str:id>', hod.STAFF_REJECT, name='staff_reject_leave'),
    

    path('hod/student/send_notification',hod.STUDENT_NOTIFICATION,name='student_send_notification'),
    path('hod/student/save_notification',hod.STUDENT_SAVE_NOTIFICATION,name='save_stud_notification'),

    path('hod/view/attendance',hod.VIEW_ATTEND,name='view_attendance'),


   path('hod/Staff/feed',hod.STAFF_FEED_REPLY,name='staff_feed'),
   path('hod/Staff/feed/save',hod.STAFF_REPLY_SAVE,name='staff_reply_save'),
   path('hod/Staff/feed/delete/<int:feedback_id>/', hod.STAFF_DELETE_FEEDBACK, name='staff_delete_feedback'),
   path('hod/student/feedback/delete/<int:feedback_id>/', hod.STUD_DELETE_FEEDBACK, name='student_delete_feedback'),
   path('hod/student/feedback',hod.STUD_FEED,name='get_student_feed'),

   path('hod/student/feedback/save',hod.STUD_SAVE_FEED,name='get_reply_save'),
    

   path('hod/student/leave_view',hod.STUD_LEAVE_VIEW,name='get_student_leave_view'),
   path('hod/student/approve_leave/<str:id>',hod.STUD_APPROVE,name='stud_approve_leave'),
   path('hod/student/reject_leave/<str:id>',hod.STUD_REJECT,name='stud_reject_leave'),

   #Staff
   path('staff/home',staff_views.HOME,name='staff_home'),
   path('staff/notifications',staff_views.NOTIFICATIONS,name='notifications'),
   path('staff/mark_as_done/<str:status>',staff_views.STAFF_NOTIFICATION_MARK_AS_DONE,name="notification_done"),
   path('staff/apply_leave',staff_views.STAFF_APPLY_LEAVE,name='staff_apply_leave'),
   path('staff/apply_leave_save',staff_views.STAFF_SAVE,name='staff_save'),
   path('staff/feedback',staff_views.STAFF_FEEDBACK,name='staff_feedback'),
   path('staff/feedback/save',staff_views.STAFF_SAVE_FEEDBACK,name='staff_feed_save'),
   path('staff/take_attendance',staff_views.STAFF_TAKE_ATTENDANCE,name='take_attendance'),
   path('staff/save_attendance',staff_views.STAFF_STORE_ATTENDANCE,name='staff_save_attendance'),
   path('staff/view_attendance',staff_views.STAFF_GET_ATTENDANCE,name='staff_view_attendance'),

   path('staff/add/result',staff_views.STAFF_ADD_MARKS,name='staff_add_result'),

   path('staff/save/result',staff_views.STAFF_SAVE_RES,name='staff_save_result'),

   #student
   path('student/home',student_views.STUDENT_HOME,name='student_home'),

   path('student/dashboard',student_views.STUD_DASH,name='student_dashboard'),
   
   path('student/notifications',student_views.STUDENT_NOTIFICATIONS,name='stud_notification'),
   
   path('student/feed',student_views.STUDENT_FEED,name='student_feedback'),
   path('student/feed/save',student_views.STUDENT_FEED_SAVE,name='student_feedback_save'),


   path('student/apply_leave',student_views.STUDENT_APPLY_FOR_LEAVE,name='student_apply_leave'),

   path('student/leave_save',student_views.STUDENTLEAVE_SAVE,name='student_leave_save'),
   
   path('student/view_attendance',student_views.STUDENT_SEE_ATTENDANCE,name='student_view_attendance'),

   path('student/view_result',student_views.VIEW_RES,name='view_result'),
   path('student/mark_done/<str:status>',student_views.STUDENT_NOTIFICATION_MARK_DONE,name='stud_notification_mark_done'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
