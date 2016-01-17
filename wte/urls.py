from django.conf.urls import include, url
from django.contrib import admin
from restaurant import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'wte.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^restaurant/', include('restaurant.urls')),
    url(r'^', include('account.urls')),
    url(r'^$', views.get_next, name = 'next'),
]
