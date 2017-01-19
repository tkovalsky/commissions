import datetime

from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.urls import reverse

from . import managers

#you can define a list of validations in a file (e.g. validators.py) and import it here, then add as an argument to the model
#from .validators import validate_content


class Sale(TimeStampedModel):
    """
    Model representing the sale of a property
    """
    buyer_name = models.CharField(max_length=80, blank=True)
    #***buyer_name = models.CharField(max_length=80, validators=[validate_content]) ***this will call the validate_content function above
    seller_name = models.CharField(max_length=80, blank=True)
    location_name = models.CharField(max_length=120, blank=True)
    transaction_close_date = models.DateField("close date", blank=True, null=True)
    asking_price = models.DecimalField(decimal_places=2, null=False, blank=False, max_digits=20, default=0)
    contract_execution_date = models.DateField("contract signed on", blank=True, null=True)
    sellers_broker = models.CharField(max_length=80, blank=True)
    buyers_broker = models.CharField(max_length=80, blank=True)
    house_broker = models.CharField(max_length=80, blank=True)
    contingencies = models.TextField(max_length=1000, blank=True)
    closing_price = models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=20, default=0)
    deal_commission_rate = models.DecimalField(decimal_places=4, default=1.000, max_digits=5)
    house_rep_commission_split_rate = models.DecimalField(decimal_places=4, max_digits=5, default=1)
    outside_broker_commission_rate = models.DecimalField(decimal_places=4, default=0, max_digits=5)
    commission_due_date = models.DateField("commission paid on", blank=True, null=True)
    commission_payout_terms = models.TextField(max_length=1000, blank=True)
    send_invoice_to = models.CharField(max_length=120, blank=True)
    invoice_address = models.CharField(max_length=100, blank=True)
    invoice_phone = models.CharField(max_length=15, blank=True)
    invoice_city = models.CharField(max_length=30, blank=True)
    invoice_state = models.CharField(max_length=20, blank=True)
    invoice_zip = models.CharField(max_length=12, blank=True)
    contact_person = models.CharField(max_length=80, blank=True)
    outside_broker_contact = models.CharField(max_length=80, blank=True)
    outside_broker_contact_address = models.CharField(max_length=100, blank=True)
    outside_broker_contact_phone_number = models.CharField(max_length=15, blank=True)
    outside_broker_email_address = models.EmailField(blank=True)
    outside_broker_w9_on_file = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

    def __str__(self):
        return self.location_name

    def get_absolute_url(self):
         """
         Returns the url to access a particular lease.
         """
         return reverse('sale-detail', args=[str(self.id)])

    @property
    def get_commissions_due_to_house(self):
        return self.deal_commission_rate * self.asking_price

    @property
    def get_commissions_due_to_house_rep(self):
        return (self.deal_commission_rate * self.asking_price ) * self.house_rep_commission_split_rate


    class Meta:
        ordering = ["location_name"]



class Lease(TimeStampedModel):
    """
    Model representing a signed lease
    """
    tenant_name = models.CharField(max_length=80, blank=True)
    property_owner_name = models.CharField(max_length=80)
    location_name = models.CharField(max_length=120)
    signed_lease_date = models.DateField(null=True, blank=True)
    lease_term_in_months = models.IntegerField("lease term", null=True, blank=True)
    size_of_space = models.IntegerField(null=True, blank=True, default=0)
    rent_price = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    lease_execution_date = models.DateField(null=True, blank=True)
    contingency_start_date = models.DateField(null=True, blank=True)
    contingency_end_date = models.DateField(null=True, blank=True)
    rent_commencement_date = models.DateField(null=True, blank=True)
    rent_rate_factor = models.DecimalField(decimal_places=4, default=1, max_digits=5)
    occupancy_date = models.DateField(null=True, blank=True)
    landlord_broker = models.CharField(max_length=80, blank=True)
    tenant_broker = models.CharField(max_length=80, blank=True)
    lease_expiration_date = models.DateField(null=True, blank=True)
    contingencies = models.TextField(max_length=1000, blank=True)
    deal_commission_rate = models.DecimalField(decimal_places=4, default=0, max_digits=5)
    house_broker = models.CharField(max_length=80, blank=True)
    house_broker_commission_rate = models.DecimalField(decimal_places=4, null=True, blank=True, max_digits=5, default=0)
    outside_broker_commission_rate = models.DecimalField(decimal_places=4, null=True, blank=True, max_digits=5, default=0)
    commission_payout_terms = models.TextField(max_length=1000, blank=True)
    send_invoice_to = models.CharField(max_length=120, blank=True)
    invoice_address = models.CharField(max_length=100, blank=True)
    invoice_city = models.CharField(max_length=30, blank=True)
    invoice_state = models.CharField(max_length=20, blank=True)
    invoice_zip = models.CharField(max_length=12, blank=True)
    invoice_phone = models.CharField(max_length=15, blank=True)
    contact_person = models.CharField(max_length=80, blank=True)
    outside_broker_contact = models.CharField(max_length=80, blank=True)
    outside_broker_contact_address = models.CharField(max_length=100, blank=True)
    outside_broker_contact_phone_number = models.CharField(max_length=15, blank=True)
    outside_broker_email_address = models.EmailField(blank=True)
    outside_broker_w9_on_file = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    contingency_time_in_days = models.IntegerField(null=True, blank=True, default=0)
    permit_type = models.CharField(max_length=100, blank=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

    objects = managers.LeaseManager()

    def __str__(self):
        return self.location_name

    def get_absolute_url(self):
         """
         Returns the url to access a particular lease.
         """
         return reverse('lease-detail', args=[str(self.id)])


    @property
    def get_aggregate_lease_commission(self):
        return float(self.size_of_space) * float(self.rent_price) * float((self.lease_term_in_months/12)) * float(self.deal_commission_rate) * float(self.rent_rate_factor)

    @property
    def display_option(self):
        """
        creates a string for the lease option.  this is required to see the lease option in the admin (since its a many to many join)
        """
        return ', '.join([ option.start_date for option in self.option.all()[:25] ])
    #display_option.option_commencement_date = 'Option Start Date'

    class Meta:
        verbose_name = ("Lease")
        verbose_name_plural = ("Leases")
        ordering = ("-created",)

class LeaseTerm(TimeStampedModel):
    """
    Model representing terms on a lease
    """
    lease = models.ForeignKey('Lease', on_delete=models.CASCADE, null=True)
    option_terms = models.TextField(blank=True)
    term_start_date = models.DateField(null=True, blank=True)
    term_end_date = models.DateField(null=True, blank=True)
    commission_rate = models.DecimalField(decimal_places=4, default=0, max_digits=5)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return '%s - %s' % (self.term_start_date, self.term_end_date)



class LeaseOption(models.Model):
    """
    Model representing options on a lease
    """
    lease = models.ForeignKey('Lease', on_delete=models.CASCADE, null=True)
    terms = models.TextField(blank=True)
    notice_date = models.DateField(null=True, blank=True)
    commencement_date = models.DateField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    size = models.IntegerField(null=True, blank=True, default=0)
    commission_rate = models.DecimalField(decimal_places=4, default=0, max_digits=5)
    contingencies = models.TextField(blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s - %s' % (self.option_commencement_date, self.option_expiration_date)


class Location(TimeStampedModel):
    property_owner_name = models.CharField(max_length=80)  #refactor to contacts model
    name = models.CharField(max_length=120, null=True, blank=True)
    address = models.CharField(max_length=120, null=True, blank=True)
    term_of_agreement = models.IntegerField(null=True, blank=True, default=0)
    invoice_contact_name = models.CharField(max_length=120, null=True, blank=True)
    invoice_billing_address = models.CharField(max_length=120, null=True, blank=True)
    invoice_billing_city = models.CharField(max_length=30, null=True, blank=True)
    invoice_billing_state = models.CharField(max_length=30, null=True, blank=True)
    invoice_billing_zip = models.CharField(max_length=10, null=True, blank=True)
    listing_execution_date = models.DateField(null=True, blank=True)
    listing_expiration_date = models.DateField(null=True, blank=True)

    LOCATION_AVAILABILITY = (
        ('a', 'Available'),
        ('l', 'For Lease'),
        ('s', 'For Sale'),
        ('b', 'Sublet'),
    )

    availability = models.CharField(max_length=1, choices=LOCATION_AVAILABILITY, blank=True, default='a', help_text="Location status")

    LISTING_STATUS = (
        ('n', 'New'),
        ('a', 'Approved'),
        ('r', 'Rejected'),
    )

    listing_status = models.CharField(max_length=2, choices=LISTING_STATUS, blank=True, default='n', help_text="Location status")

    LOCATION_TYPE = (
        ('nc', 'Not Classified'),
        ('p', 'Pad'),
        ('b', 'Bank'),
        ('l', 'Land'),
    )

    location_type = models.CharField(max_length=2, choices=LOCATION_TYPE, blank=True, default='nc', help_text="Property type")
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'space'
        verbose_name_plural = 'spaces'

    def __str__(self):
        return self.name_of_business


class TenantRep(TimeStampedModel):
    """
    Model representing a tenant rep deal
    """
    locations = models.ForeignKey('Location', blank=True, null=True)
    name_of_business = models.CharField(max_length=80, blank=True)
    business_type_tags = models.ManyToManyField('BusinessType', help_text="Select the types of businesses that represent the tenant")
    contact = models.CharField(max_length=80, blank=True)
    notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField("last modified", auto_now=True, auto_now_add=False)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)


    def __str__(self):
        return self.name_of_business

    def get_absolute_url(self):
         """
         Returns the url to access a particular tenant.
         """
         return reverse('tenant-detail', args=[str(self.id)])

    class Meta:
        ordering = ('name_of_business',)

    @property
    def display_business_type_tags(self):
        """
        creates a string for the business types.  this is required to see the types in the admin (since its a many to many join)
        """
        return ', '.join([ businesstype.name for businesstype in self.businesstype.all()[:25] ])




class BusinessType(TimeStampedModel):
    """
    Model representing the types of businesses for tenants
    """
    name = models.CharField(max_length=100, help_text="Enter the type of business")

    def __str__(self):
        return self.name

'''
Updated this a little but is not implemented.

class Deal(models.Model):
    lease = models.ForeignKey('Lease', on_delete=models.SET_NULL, null=True)
    sale = models.ForeignKey('Sale', on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    broker_name = models.CharField(max_length=80, blank=True)
    tenant_name = models.CharField(max_length=80, blank=True)
    tenant_dba_name = models.CharField(max_length=80, blank=True)
    close_date = models.DateField(blank=True, null=True)
    DEAL_STATUS = (
        ('new', 'New'),
        ('prospect', 'Prospect'),
        ('loi_signed', 'LOI Signed'),
        ('contract_signed', 'Available'),
        ('closed', 'Closed'),
        ('invoiced', 'Invoiced'),
        ('in_collections', 'In Collections'),
    )
    size_of_space = models.IntegerField("lease term", null=True, blank=True)
    status = models.CharField(max_length=25, choices=DEAL_STATUS, blank=True, default='new', help_text="Deal closing status")
    annualized_rent = models.DecimalField(decimal_places=2, null=False, blank=False, max_digits=20, default=0)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField("last modified", auto_now=True, auto_now_add=False)

    def get_absolute_url(self):
        """
        Returns the url to access a partcular deal
        """
        return reverse('deal-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s, %s' % (self.id, self.close_date)

    class Meta:
        ordering = ["-close_date"]


#future implementation to make activity of a location
#class Activity(models.Model):
#    status = models.CharField(max_length=25, choices=Location_STATUS, blank=True, default='new', help_text="Location status")







class Contact(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField("last modified", auto_now=True, auto_now_add=False)

    def get_absolute_url(self):
        """
        Returns the url to access a partcular contact
        """
        return reverse('contact-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s, %s' % (self.name, self.email)
'''



'''
best practice for order of model content
class MyModel(models.Model):
    # Relations
    # Attributes - Mandatory
    # Attributes - Optional
    # Object Manager
    # Custom Properties
    # Methods
    # Meta and String

'''
