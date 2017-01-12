import datetime
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import AddSaleForm

from .models import Sale, Lease, Option
#from .models Contact, Deal

class SalesListView(generic.ListView):
    model = Sale

class SaleDetailView(generic.DetailView):
    model = Sale



class SaleCreate(CreateView):
    model = Sale
    fields = '__all__'

class SaleUpdate(UpdateView):
    model = Sale
    fields = '__all__'

class SaleDelete(DeleteView):
    model = Sale
    success_url = reverse_lazy('sales')















def index(request):
    """
    View function for the home page of this site
    """
    #Generate counts for some main objects
#    num_deals=Deal.objects.all().count()
#    num_leases=Lease.objects.all().count()
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
        },
    )
