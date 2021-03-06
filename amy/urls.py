from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='dispatch')),
    path('workshops/admin/', admin.site.urls),
]
if settings.ENABLE_PYDATA:
    urlpatterns += [
        url(r'^workshops/', include('pydata.urls')),
    ]
urlpatterns += [
    url(r'^workshops/', include('workshops.urls')),
    # url(r'^account/', include('django.contrib.auth.urls')),

    # django views for authentication
    # taken in almost exact form from django.contrib.auth.views.urls:
    url(r'^account/login/$', auth_views.login,
        {"template_name": "account/login.html",
         "extra_context": {"title": "Log in"}}, name='login'),
    url(r'^account/logout/$', auth_views.logout,
        {"template_name": "account/logged_out.html"}, name='logout'),
    url(r'^account/password_reset/$',
        auth_views.password_reset,
        {"template_name": "account/password_reset.html"},
        name='password_reset'),
    url(r'^account/password_reset/done/$',
        auth_views.password_reset_done,
        {"template_name": "account/password_reset_done.html"},
        name='password_reset_done'),
    url(r'^account/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {"template_name": "account/password_reset_confirm.html"},
        name='password_reset_confirm'),
    url(r'^account/reset/done/$',
        auth_views.password_reset_complete,
        {"template_name": "account/password_reset_complete.html"},
        name='password_reset_complete'),

    # autocomplete lookups
    url(r'^select_lookups/', include('workshops.lookups')),

    # REST API v1
    url(r'^api/v1/', include('api.urls')),

    # external, anonuser-accessible forms
    url(r'^forms/', include('extforms.urls')),

    # Login with GitHub credentials
    url('', include('social_django.urls', namespace='social')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
