from django.shortcuts import render
from django.views import generic

from .models import Sale
#from .models import Lease, Option, Contact, Deal



class SalesListView(generic.ListView):
    model = Sale

class SaleDetailView(generic.DetailView):
    model = Sale

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




'''
class AuthorListView(generic.ListView):
    model = Author
    queryset = Author.objects.order_by('last_name')

class AuthorDetailView(generic.DetailView):
    model = Author
    context_object_name = 'author'


'''
