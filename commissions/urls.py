from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
#    url(r'^contacts/$', views.ContactListView.as_view(), name='contacts'),
#    url(r'^contact/(?P<pk>\d+)$', views.ContactDetailView.as_view(), name='contact-detail'),
#    url(r'^leases/$', views.LeaseListView.as_view(), name='leases'),
#    url(r'^lease/(?P<pk>[0-9]+)/$', views.LeaseDetailView.as_view(), name='lease-detail'),
#    url(r'^deals/$', views.DealListView.as_view(), name='deals'),
#    url(r'^sale/(?P<pk>[0-9]+)/$', views.DealDetailView.as_view(), name='deal-detail'),
    url(r'^sales/$', views.SalesListView.as_view(), name='sales'),
    url(r'^sale/(?P<pk>[0-9]+)/$', views.SaleDetailView.as_view(), name='sale-detail'),
    url(r'^sale/create/$', views.SaleCreate.as_view(), name='sale_create'),
    url(r'^sale/(?P<pk>\d+)/update/$', views.SaleUpdate.as_view(), name='sale_update'),
    url(r'^sale/(?P<pk>\d+)/delete/$', views.SaleDelete.as_view(), name='sale_delete'),



]
