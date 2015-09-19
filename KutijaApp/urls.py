from django.conf.urls import patterns, include, url
import views
urlpatterns = patterns('',
	
    #url(r'^lokacije/$', views.locations, name= "locations"),
    
    url(r'^$', views.home, name= "home"),

    url(r'^admin/$', views.admin, name="admin"),
    url(r'^admin/addlocation/$', views.addlocation, name="addlocation"),
    url(r'^admin/addbox/$', views.addbox, name="addbox"),
    url(r'^admin/adduser/$', views.adduser, name="adduser"),
    
    url(r'^api/$', views.api, name="api"),

)