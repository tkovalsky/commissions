from django.contrib import admin

from .models import Sale, Lease, LeaseOption, LeaseTerm, TenantRep, Location, BusinessType
#, Contact, Deal


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_filter = ['created']
    list_display = ['location_name','buyer_name', 'seller_name','asking_price', 'get_commissions_due_to_house', 'get_commissions_due_to_house_rep']
    fields = ['location_name','seller_name','closing_price', 'added_by',
                ('transaction_close_date', 'contract_execution_date', 'commission_due_date'),
                ('sellers_broker', 'buyers_broker'),
                ('deal_commission_rate', 'house_rep_commission_split_rate'),
                ('outside_broker_contact','outside_broker_w9_on_file', 'outside_broker_email_address',
                                        'outside_broker_commission_rate', 'outside_broker_contact_address',
                                        'outside_broker_contact_phone_number'),
                ('contingencies', 'commission_payout_terms',),
                ('send_invoice_to', 'invoice_address', 'invoice_phone', 'invoice_city', 'invoice_state',
                                        'invoice_zip','contact_person', ),
                'notes',
    ]

    extra = 1

class LeaseOptionInline(admin.TabularInline):
    model = LeaseOption

class LeaseTermInline(admin.TabularInline):
    model = LeaseTerm


@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):

    list_filter = ['created']
    list_display = ['location_name','property_owner_name', 'tenant_name', 'size_of_space', 'rent_price', 'get_aggregate_lease_commission']
    fields = ['location_name','size_of_space','rent_price', 'lease_term_in_months','term_start_date', 'term_end_date',
                ('signed_lease_date','rent_commencement_date', 'occupancy_date', 'lease_expiration_date'),
                ('rent_rate_factor', 'deal_commission_rate','commission_payout_terms',),
                ('tenant_broker'),
                ('outside_broker_contact','outside_broker_w9_on_file', 'outside_broker_email_address',
                                        'outside_broker_commission_rate', 'outside_broker_contact_address',
                                        'outside_broker_contact_phone_number'),
                ('send_invoice_to', 'invoice_address', 'invoice_phone', 'invoice_city', 'invoice_state',
                                        'invoice_zip','contact_person', ),
                'notes',
                'contingencies'
                ]
    inlines = [LeaseOptionInline, LeaseTermInline]
    extra = 1

#This tabular inline was not working in the TenantRepAdmin
class LocationInline(admin.TabularInline):
    model = Location

@admin.register(TenantRep)
class TenantRepAdmin(admin.ModelAdmin):
    exclude = ['date_modified','created']
    extra = 1


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    exclude = ['date_modified','created']
    extra = 1





@admin.register(BusinessType)
class BusinessTypeAdmin(admin.ModelAdmin):
    exclude = ['date_modified', 'created']
    extra = 1


'''
Below is an example of a good way to write the fieldset codes

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    """
    You can add "sections" to group related model information within the detail form, using the fieldsets attribute.
    Each section has its own title (or None, if you don't want a title)
    """

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        })
     )



admin.site.register(Language)
'''
