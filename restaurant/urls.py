from django.conf.urls import url

from restaurant import views

app_name = 'restaurant'
urlpatterns = [
    # Examples:
    # url(r'^$', 'wte.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.viewAll, name='viewAll'),
    url(r'^calc/$', views.calc, name='calc'),
    url(r'^next/$', views.get_next, name='next'),
    url(r'^array/$', views.get_array, name='array'),
    url(r'^add/$', views.add_restaurant, name='addRestaurant')
]
