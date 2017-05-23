from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()
import hello.views
from django.contrib.auth.views import *

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),

    # Login-Logout URLs
    url(r'^accounts/login/$', hello.views.login, name='login'),
    url(r'^accounts/login/update_list$', hello.views.update_list, name='update_list'),
    url(r'^accounts/logout/$', logout, {'next_page': 'index'}, name='logout'),
    #url(r'^accounts/loggedin/$', hello.views.loggedin, name='loggedin'),

    # Registration URLs
    url(r'^accounts/register/$', hello.views.registration_page, name='registration'),
    url(r'^accounts/register/complete/$', hello.views.registration_request, name='registration_request'),

    url(r'^info/$', hello.views.info, name='info'),

]
