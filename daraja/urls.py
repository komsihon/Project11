
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

from ikwen.cashout.views import Payments, manage_payment_address, request_cash_out

from daraja.views import Home, RegisteredCompanyList, DeployCloud, ChangeProfile, Dashboard, CompanyList, \
    SuccessfulDeployment, ViewProfile, login_router, DaraList, DaraRequestList, Configuration, InviteDara

urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^for-businesses$', Home.as_view(), name='for_businesses'),
    url(r'^invitation/(?P<ikwen_name>[-\w]+)$', InviteDara.as_view(), name='invite_dara'),
    url(r'^companies$', RegisteredCompanyList.as_view(), name='registered_company_list'),
    url(r'^deploy$', login_required(DeployCloud.as_view()), name='deploy_cloud'),
    url(r'^successfulDeployment/(?P<ikwen_name>[-\w]+)$', login_required(SuccessfulDeployment.as_view()), name='successful_deployment'),
    url(r'^profile/(?P<dara_name>[-\w]+)/$', ViewProfile.as_view(), name='view_profile'),

    url(r'^configuration$', permission_required('daraja.ik_manage_daraja')(Configuration.as_view()), name='configuration'),
    url(r'^daraRequestList$', permission_required('daraja.ik_manage_daraja')(DaraRequestList.as_view()), name='dara_request_list'),
    url(r'^daraList$', permission_required('daraja.ik_manage_daraja')(DaraList.as_view()), name='dara_list'),

    url(r'^login_router$', login_router, name='login_router'),
    url(r'^dashboard/$', login_required(Dashboard.as_view()), name='dashboard'),
    url(r'^profile/$', login_required(ChangeProfile.as_view()), name='change_profile'),
    url(r'^companies/$', login_required(CompanyList.as_view()), name='company_list'),
    url(r'^wallet/$', login_required(Payments.as_view()), name='wallet'),
    url(r'^manage_payment_address/$', manage_payment_address, name='manage_payment_address'),
    url(r'^request_cash_out/$', request_cash_out, name='request_cash_out'),
)
