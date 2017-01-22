from django import forms
from django.forms import inlineformset_factory, ModelForm
from .models import Lease, Sale, Option, Location, Tenant, Term


class AddSaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['location_name', 'seller_name', 'asking_price',
                                                'deal_commission_rate',
                                                'transaction_close_date'
                ]
        labels = { 'transaction_close_date': ('Closing date'),
                    'deal_commission_rate': ('Deal commission'),
                }
        help_texts = { 'transaction_close_date': ('Enter the date of the closing.'), }


class AddLeaseForm(forms.ModelForm):
    content = forms.CharField(label='',
                widget=forms.Textarea(
                        attrs={'placeholder': "Your message",
                            "class": "form-control"}
                    ))
    class Meta:
        model = Lease
        fields = ['location_name', 'property_owner_name', 'rent_price', 'deal_commission_rate', 'size_of_space', ]
        labels = { 'contract_execution_date': ('Contract signed on'),
                    'deal_commission_rate': ('Deal commission'),}
        help_texts = { 'contract_execution_date': ('Enter the date of the closing.'), }

    def clean_location_name(self, *args, **kwargs):
        location_name = self.cleaned_data.get("location_name")
        if content == "abc":
            raise forms.ValidationError("Cannot be ABC")
        return content

#Search is not yet implemented
class SearchForm(forms.Form):
    search_text = forms.CharField()


class AddLocationForm(forms.ModelForm):
    name_of_company = forms.CharField(max_length=30, required=False)

    class Meta:
        model = Location
        fields = ('name_of_property', 'address')

    def save(self, commit=True):
        location = super(LocationForm, self).save(commit=False)
        tenant = Tenant(name=self.cleaned_data['name_of_company'])

        location.save()
        location.tenant = tenant
        if commit:
            tenant.save()
        return location


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
