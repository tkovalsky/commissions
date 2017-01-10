from django.db import models
from django.urls import reverse

class sale(models.Model):
    """
    Model representing the sale of a property
    """
    buyer_name = models.CharField(max_length=80)
    seller_name = models.CharField(max_length=80)
    location_name = models.CharField(max_length=120, help_text="Enter the name of the property, e.g. the shopping center name")
    transaction_close_date = models.DateField("close date", null=True, blank=True)
    asking_price = models.DecimalField(decimal_places=2)
    contract_execution_date = models.DateField("contract signed on", null=True, blank=True)
    sellers_broker = models.CharField(max_length=80)
    buyers_broker = models.CharField(max_length=80)
    contingencies = models.TextField("deal contingencies", max_length=1000, blank=True, null=True)
    closing_price = models.DecimalField(decimal_places=2)
    house_commission_rate = models.DecimalField(decimal_places=3, max=1, default=1.000)
    house_rep_commission_split_rate = models.DecimalField(decimal_places=4, max=1)
    outside_broker_commission_rate = models.DecimalField(decimal_places=3, max=.9999, default=0)
    commission_due_date = models.DateField("commission paid on", null=True, blank=True)
    commission_payout_terms = models.TextField("deal contingencies", max_length=1000, blank=True, null=True)
    send_invoice_to = models.CharField(max_length=120)
    invoice_address = models.CharField(max_length=100)
    invoice_phone = models.CharField(max_length=15)
    invoice_city = models.CharField(max_length=30)
    invoice_state = models.CharField(max_length=20)
    invoice_zip = models.CharField(max_length=12)
    contact_person = models.CharField(max_length=80)
    outside_broker_contact = models.CharField(max_length=80)
    outside_broker_contact_address = models.CharField(max_length=100)
    outside_broker_contact_phone_number = models.CharField(max_length=15)
    outside_broker_email_address = models.EmailField()
    outside_broker_w9_on_file = models.BooleanField(default=False)
    notes = models.TextField()
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField("last modified", auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.location_name

    def get_absolute_url(self):
         """
         Returns the url to access a particular lease.
         """
         return reverse('sale-detail', args=[str(self.id)])

    class Meta:
        ordering = ["transaction_close_date"]



class lease(models.Model):
    """
    Model representing a signed lease
    """
    tenant_name = models.CharField(max_length=80)
    property_owner_name = models.CharField(max_length=80)
    location_name = models.CharField(max_length=120)
    signed_lease_date = models.DateField(null=True, blank=True)
    lease_term_in_months = models.IntegerField("lease term", max_length=4, max=1200)
    size_of_transaction = models.IntegerField()
    rent_price = models.DecimalField(decimal_places=2)
    contract_execution_date = models.DateField("contract signed on", null=True, blank=True)
    free_rent_start_date = models.DateField(null=True, blank=True)
    free_rent_end_date = models.DateField(null=True, blank=True)
    due_diligence_rent_start_date = models.DateField(null=True, blank=True)
    due_diligence_end_date = models.DateField(null=True, blank=True)
    contract_execution_date = models.DateField(null=True, blank=True)
    rent_commencement_date = models.DateField(null=True, blank=True)
    rent_rate_factor = models.DecimalField(decimal_places=4, default=1, max=100)
    occupancy_date = models.DateField(null=True, blank=True)
    landlord = models.CharField(max_length=80)
    tenant_broker = models.CharField(max_length=80)
    lease_expiration_date = models.DateField(null=True, blank=True)
    contingencies = models.TextField("deal contingencies", max_length=1000, blank=True, null=True)
    house_commission_rate = models.DecimalField(decimal_places=3, max=1, default=1.000)
    house_salesrep_commission_rate = models.DecimalField(decimal_places=2)
    outside_broker_commission_rate = models.DecimalField(decimal_places=3)
    commission_payout_terms = models.TextField("deal contingencies", max_length=1000, blank=True, null=True)
    send_invoice_to = models.CharField(max_length=120)
    invoice_address = models.CharField(max_length=100)
    invoice_city = models.CharField(max_length=30)
    invoice_state = models.CharField(max_length=20)
    invoice_zip = models.CharField(max_length=12)
    invoice_phone = models.CharField(max_length=15)
    contact_person = models.CharField(max_length=80)
    outside_broker_contact = models.CharField(max_length=80)
    outside_broker_contact_address = models.CharField(max_length=100)
    outside_broker_contact_phone_number = models.CharField(max_length=15)
    outside_broker_email_address = models.EmailField()
    outside_broker_w9_on_file = models.BooleanField(default=False)
    notes = models.TextField()
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField("last modified", auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.location_name

    def get_absolute_url(self):
         """
         Returns the url to access a particular lease.
         """
         return reverse('lease-detail', args=[str(self.id)])

    def display_option(self):
        """
        creates a string for the lease option.  this is required to see the lease option in the admin (since its a many to many join)
        """
        return ', '.join([ option.rent_commencement_date for option in self.option.all()[:25] ])
    display_genre.short_description = 'Option Start Dates'


class option(models.Model):
    """
    Model representing options on a lease
    """
    lease = models.ForeignKey('Lease', null=True)
    option_terms = models.TextField()
    number_of_lease_options = models.IntegerField()
    option_notice_date = models.DateField(null=True, blank=True)
    option_commencement_date =
    option_expiration_date = models.DateField(null=True, blank=True)
    increase_or_decrease_size = models.IntegerField()
    increase_or_decrease_rent_rate = models.IntegerField()
    increase_or_decrease_commission_rate = models.IntegerField()
    option_contingencies = models.TextField
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField("last modified", auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s (%s)' % (self.id, self.lease.tenant_name)



class deal(models.Model):
    lease = models.ForeignKey('Lease', on_delete=models.SET_NULL, null=True))
    sale = models.ForeignKey('Sale', on_delete=models.SET_NULL, null=True))
    contact = models.ForeignKey('Contact', on_delete=models.SET_NULL, null=True))
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

class contact(models.Model):
    name = models.CharField(null=False, blank=False)
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
