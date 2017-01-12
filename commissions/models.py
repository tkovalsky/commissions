import datetime
from django.db import models
from django.urls import reverse

class Sale(models.Model):
    """
    Model representing the sale of a property
    """
    buyer_name = models.CharField(max_length=80, blank=True)
    seller_name = models.CharField(max_length=80, blank=True)
    location_name = models.CharField(max_length=120, blank=True)
    transaction_close_date = models.DateField("close date", blank=True, null=True)
    asking_price = models.DecimalField(decimal_places=2, null=False, blank=False, max_digits=20, default=0)
    contract_execution_date = models.DateField("contract signed on", blank=True, null=True)
    sellers_broker = models.CharField(max_length=80, blank=True)
    buyers_broker = models.CharField(max_length=80, blank=True)
    contingencies = models.TextField(max_length=1000, blank=True)
    closing_price = models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=20)
    house_commission_rate = models.DecimalField(decimal_places=4, default=1.000, max_digits=5)
    house_rep_commission_split_rate = models.DecimalField(decimal_places=4, max_digits=5, default=1.000)
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
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField("last modified", auto_now=True, auto_now_add=False)
    #listing_agent = models.ForeignKey('Users')

    def __str__(self):
        return self.location_name

    def get_absolute_url(self):
         """
         Returns the url to access a particular lease.
         """
         return reverse('sale-detail', args=[str(self.id)])

    @property
    def get_commissions_due_to_house(self):
        return self.house_commission_rate * self.asking_price

    @property
    def get_commissions_due_to_house_rep(self):
        return (self.house_commission_rate * self.asking_price ) * self.house_rep_commission_split_rate


    class Meta:
        ordering = ["location_name"]



class Lease(models.Model):
    """
    Model representing a signed lease
    """
    tenant_name = models.CharField(max_length=80, blank=True)
    property_owner_name = models.CharField(max_length=80)
    location_name = models.CharField(max_length=120)
    signed_lease_date = models.DateField(null=True, blank=True)
    lease_term_in_months = models.IntegerField("lease term", null=True, blank=True)
    size_of_transaction = models.IntegerField(null=True, blank=True, default=0)
    rent_price = models.DecimalField(decimal_places=2, max_digits=8)
    contract_execution_date = models.DateField(null=True, blank=True)
    free_rent_start_date = models.DateField(null=True, blank=True)
    free_rent_end_date = models.DateField(null=True, blank=True)
    due_diligence_start_date = models.DateField(null=True, blank=True)
    due_diligence_end_date = models.DateField(null=True, blank=True)
    rent_commencement_date = models.DateField(null=True, blank=True)
    rent_rate_factor = models.DecimalField(decimal_places=4, default=1, max_digits=5)
    occupancy_date = models.DateField(null=True, blank=True)
    landlord = models.CharField(max_length=80, blank=True)
    tenant_broker = models.CharField(max_length=80, blank=True)
    lease_expiration_date = models.DateField(null=True, blank=True)
    contingencies = models.TextField(max_length=1000, blank=True)
    house_commission_rate = models.DecimalField(decimal_places=4, default=1.000, max_digits=5)
    house_salesrep_commission_rate = models.DecimalField(decimal_places=4, null=True, blank=True, max_digits=5)
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
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField("last modified", auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.location_name

    def get_absolute_url(self):
         """
         Returns the url to access a particular lease.
         """
         return reverse('lease-detail', args=[str(self.id)])

    @property
    def get_aggregate_lease_commission(self):
        return float(self.size_of_transaction) * float(self.rent_price) * float((self.lease_term_in_months/12)) * float(self.house_commission_rate) * float(self.rent_rate_factor)

    @property
    def display_option(self):
        """
        creates a string for the lease option.  this is required to see the lease option in the admin (since its a many to many join)
        """
        return ', '.join([ option.start_date for option in self.option.all()[:25] ])
    #display_option.option_commencement_date = 'Option Start Date'


class Option(models.Model):
    """
    Model representing options on a lease
    """
    lease = models.ForeignKey('Lease', on_delete=models.CASCADE, null=True)
    option_terms = models.TextField(blank=True)
    option_notice_date = models.DateField(null=True, blank=True)
    option_commencement_date = models.DateField(null=True, blank=True)
    option_expiration_date = models.DateField(null=True, blank=True)
    increase_or_decrease_size = models.IntegerField(null=True, blank=True)
    increase_or_decrease_rent_rate_factor = models.DecimalField(decimal_places=4, default=1, max_digits=5)
    commission_rate = models.DecimalField(decimal_places=4, default=1.000, max_digits=5)
    option_contingencies = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s - %s' % (self.option_commencement_date, self.option_expiration_date)


'''
class Deal(models.Model):
    lease = models.ForeignKey('Lease', on_delete=models.SET_NULL, null=True)
    sale = models.ForeignKey('Sale', on_delete=models.SET_NULL, null=True)
    contact = models.ForeignKey('Contact', on_delete=models.SET_NULL, null=True)
    close_date = models.DateField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)
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

class Contact(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)
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
