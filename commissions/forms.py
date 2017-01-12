from django import forms
from django.forms import ModelForm

from .models import Lease, Sale, Option


class AddSaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['location_name', 'seller_name', 'asking_price', 'deal_commission_rate', 'transaction_close_date']
        labels = { 'transaction_close_date': ('Closing date'),
                    'deal_commission_rate': ('Deal commission'),}
        help_texts = { 'transaction_close_date': ('Enter the date of the closing.'), }




'''
from django.forms import ModelForm
from .models import BookInstance

class RenewBookModelForm(ModelForm):
    class Meta:
        model = BookInstance
        fields = ['due_back',]
        labels = { 'due_back': _('Renewal date'), }
        help_texts = { 'due_back': _('Enter a date between now and 4 weeks (default 3).'), }

        def clean_due_back(self):
            data = self.cleaned_data['renewal_date']

            #Check date is not in past.
            if data < datetime.date.today():
                raise ValidationError(_('Invalid date - renewal in past'))
            #Check date is in range librarian allowed to change (+4 weeks)
            if data > datetime.date.today() + datetime.timedelta(weeks=4):
                raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

            # Remember to always return the cleaned data.
            return data
'''




'''
        buyer_name = models.CharField(max_length=80, blank=True)
        contract_execution_date = models.DateField("contract signed on", blank=True, null=True)
        sellers_broker = models.CharField(max_length=80, blank=True)
        buyers_broker = models.CharField(max_length=80, blank=True)
        contingencies = models.TextField(max_length=1000, blank=True)
        closing_price = models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=20)
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
        date_modified = models.DateTimeField
'''
