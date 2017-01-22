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
    url(r'^sale/create/$', views.SaleCreateView.as_view(), name='sale-create'),
    url(r'^sale/(?P<pk>\d+)/update/$', views.SaleUpdateView.as_view(), name='sale-update'),
    url(r'^sale/(?P<pk>\d+)/delete/$', views.SaleDeleteView.as_view(), name='sale-delete'),
    url(r'^leases/$', views.LeaseListView.as_view(), name='leases'),
    url(r'^lease/(?P<pk>[0-9]+)/$', views.LeaseDetailView.as_view(), name='lease-detail'),
    url(r'^lease/create/$', views.LeaseCreateView.as_view(), name='lease-create'),
    url(r'^lease/(?P<pk>\d+)/update/$', views.LeaseUpdateView.as_view(), name='lease-update'),
    url(r'^lease/(?P<pk>\d+)/delete/$', views.LeaseDeleteView.as_view(), name='lease-delete'),


    url(r'^location/create/$', views.AddLocationView.as_view(), name='location-create'),
    url(r'^location/(?P<pk>[0-9]+)/$', views.LocationDetailView.as_view(), name='location-detail'),
    url(r'^locations/$', views.LocationListView.as_view(), name='locations'),
    
]
