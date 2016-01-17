from django.conf.urls import url

from account import views

app_name = 'account'
urlpatterns = [
    url(r'^login/', views.login_user, name = 'Login'),
    url(r'^logout/', views.logout_user, name = 'Logout'),
]
