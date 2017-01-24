from django.contrib import admin

from .models import Sale, Lease, Option, Term, Tenant, Location, BusinessType, Mandate
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
    model = Option

class LeaseTermInline(admin.TabularInline):
    model = Term


@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):

    list_filter = ['created']
    list_display = ['location_name','property_owner_name', 'tenant_name', 'size_of_space', 'rent_price', 'get_aggregate_lease_commission']
    fields = ['tenant_name','property_owner_name','location_name','size_of_space','rent_price', 'lease_term_in_months',
                ('signed_lease_date','rent_commencement_date', 'occupancy_date', 'lease_execution_date','lease_expiration_date',
                                        'contingency_start_date', 'contingency_end_date', ),
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

class MandateInline(admin.TabularInline):
    model = Mandate

class TenantInline(admin.TabularInline):
    model = Tenant


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    fields = ['name_of_company', 'notes']
    #inlines = [LocationInline,]
    #ERRORS: <class 'commissions.admin.LocationInline'>: (admin.E202) 'commissions.Location' has no ForeignKey to 'commissions.Tenant'.


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    fields = ['name_of_property', 'availability', 'property_type','property_owner', 'address', 'city', 'state', 'zip_code', 'notes']
    inlines = [TenantInline,]





@admin.register(BusinessType)
class BusinessTypeAdmin(admin.ModelAdmin):
    fields = ['name',]


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
