import datetime
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin #TODO
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.forms import modelformset_factory
from django.forms.utils import ErrorList
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import AddSaleForm, AddLeaseForm, CreateTenantRepForm

from .models import Sale, Lease, LeaseOption, Location, LeaseTerm

#from .models Contact, Deal


def lease_formset_view(request):
    LeaseModelFormset = modelformset_factory(Lease, fields=['location_name',
                                                            'term_start_date'],
                                                            extra=2)
    formset = LeaseModelFormset(request.POST or None)
    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)
    context = {
        "formset": formset
    }
    return render(request, "lease_formset_view.html", context)

#Views for sale transactions
class SalesListView(generic.ListView):
    model = Sale

    def get_context_data(self, *args, **kwargs):
        context = super(SalesListView, self).get_context_data(*args, **kwargs)

class SaleDetailView(generic.DetailView):
    model = Sale

class SaleCreateView(CreateView):
    #can use fields or form_class
    #form_class = AddSaleForm
    model = Sale
    fields = '__all__'

class SaleUpdateView(UpdateView):
    model = Sale
    fields = '__all__'

class SaleDeleteView(DeleteView):
    model = Sale
    success_url = reverse_lazy('sales')


#Views for lease transactions
class LeaseListView(generic.ListView):
    model = Lease

class LeaseDetailView(generic.DetailView):
    model = Lease

class LeaseCreateView(CreateView):
    model = Lease
    fields = '__all__'


'''
function based view used to create custom form for tenant reps
'''
def create_tenant_rep(request):
    form_class = CreateTenantRepForm

    return render(request, 'commissions/create_tenant_rep.html', { 'form': form_class,
    })


class LeaseUpdateView(UpdateView):
    model = Lease
    fields = '__all__'

class LeaseDeleteView(DeleteView):
    model = Lease
    success_url = reverse_lazy('leases')


class SearchView(generic.ListView):

    def get_querset(self, *args, **kwargs):
        queryset = Sale.objects.all() + Lease.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            queryset = queryset.filter(content__icontains=query)
        return queryset










def index(request):
    """
    View function for the home page of this site
    """
    #Generate counts for some main objects
#    num_deals=Deal.objects.all().count()
    num_leases=Lease.objects.all().count()
    num_sales=Sale.objects.all().count()
#    num_options=Option.objects.all().count()
#    num_contacts=Contacts.objects.all().count()
    # Available books (status = 'a')
    #num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    #num_authors=Author.objects.count() #'All' is implied by default

    #Render the html template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={
            'num_sales':num_sales,
            'num_leases':num_leases,
        },
    )
