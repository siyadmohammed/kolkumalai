from django.urls import path
from.import views
urlpatterns=[
    path('',views.index),
    path('contact/',views.contact),
    path('registernew/',views.registernew),
    path('kolukkumalaiadv/',views.adminlogin),
    path('adminlogincheck/',views.adminlogincheck),
    path('admin_homepage/',views.adminhomepage),
    path('savedbookings/',views.savedbookings),
    path('checkavailability/',views.checkavailability),
    path('viewbookings/',views.viewbooking),
    path('savedguestenquiry/',views.savedguestmessage),
    path('viewguestenquiry/',views.viewguestmessage),
]