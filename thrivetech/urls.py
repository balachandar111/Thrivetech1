from django.contrib import admin
from django.urls import path
from thriveapp import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('WhoWeAre/',views.whoweare,name='whoweare'),
    path('Migration/',views.migration,name='migration'),
    path('Career/',views.career,name='career'),
    path('Helpdesk/',views.helpdesk,name='helpdesk'),
    path('Customersupport/',views.customersupport,name='customersupport'),
    path('Uiux/',views.uiux,name='uiux'),
    path('Website/',views.website,name='website'),
    path('Forge/',views.forge,name='forge'),
     path('Form/',views.form,name='form'),
    
    
]