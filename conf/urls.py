from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from django.contrib import admin
admin.autodiscover()

from daraja.views import login_router

urlpatterns = patterns(
    '',
    url(r'^login_router$', login_router, name='home'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^billing/', include('ikwen.billing.urls', namespace='billing')),
    url(r'^cashout/', include('ikwen.cashout.urls', namespace='cashout')),
    url(r'^theming/', include('ikwen.theming.urls', namespace='theming')),
    url(r'^revival/', include('ikwen.revival.urls', namespace='revival')),

    url(r'^blog/', include('ikwen_webnode.blog.urls', namespace='blog')),
    url(r'^web/', include('ikwen_webnode.web.urls', namespace='web')),
    url(r'^items/', include('ikwen_webnode.items.urls', namespace='items')),
    url(r'^echo/', include('echo.urls', namespace='echo')),

    url(r'^', include('daraja.urls', namespace='daraja')),
    url(r'^', include('ikwen.core.urls', namespace='ikwen')),
)
