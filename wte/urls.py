from django.conf.urls import include, url
from django.contrib import admin
from account import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'wte.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^restaurant/', include('restaurant.urls')),
    url(r'^login/', views.login_user, name = 'Login'),
    url(r'^logout/', views.logout_user, name = 'Logout'),
]
