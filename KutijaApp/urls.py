from django.conf.urls import patterns, include, url
import views
urlpatterns = patterns('',
	url(r'^$', views.home, name= "home"),

    #url(r'^lokacije/$', views.locations, name= "locations"),

    
    url(r'^admin/$', views.admin, name="admin"),
    url(r'^admin/addlocation/$', views.addlocation, name="addlocation"),

    #url(r'^cart/remove/$', views.removeFromCart, name="remove"),
    #url(r'^cart/checkout/$', views.checkout, name="checkout"),
    
    #url(r'^admin-login/$', views.adminLogin, name= "admin_login"),
    #url(r'^admin-panel/$', views.adminDashboard, name= 'admin'),
)