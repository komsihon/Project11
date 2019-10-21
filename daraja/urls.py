
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

from daraja.views import Home, RegisteredCompanyList, DeployCloud, ChangeProfile, Dashboard, CompanyList, \
    SuccessfulDeployment, ViewProfile, login_router, DaraList, DaraRequestList, Configuration, InviteDara

urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^for-businesses$', Home.as_view(), name='for_businesses'),
    url(r'^invitation/(?P<ikwen_name>[-\w]+)$', InviteDara.as_view(), name='invite_dara'),

    url(r'^configuration$', Configuration.as_view(), name='configuration'),
    url(r'^daraRequestList$', DaraRequestList.as_view(), name='dara_request_list'),
    url(r'^daraList$', permission_required('daraja.ik_manage_daraja')(DaraList.as_view()), name='dara_list'),

    url(r'^companies$', RegisteredCompanyList.as_view(), name='registered_company_list'),
    url(r'^deploy$', login_required(DeployCloud.as_view()), name='deploy_cloud'),
    url(r'^successfulDeployment/(?P<ikwen_name>[-\w]+)$', login_required(SuccessfulDeployment.as_view()), name='successful_deployment'),

    url(r'^login_router$', login_router, name='login_router'),
    url(r'^dashboard/$', login_required(Dashboard.as_view()), name='dashboard'),
    url(r'^profile/$', login_required(ChangeProfile.as_view()), name='change_profile'),
    url(r'^companies/$', login_required(CompanyList.as_view()), name='company_list'),

    url(r'^profile/(?P<dara_name>[-\w]+)/$', ViewProfile.as_view(), name='view_profile'),
)
