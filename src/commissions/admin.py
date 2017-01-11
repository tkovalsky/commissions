from django.contrib import admin

from .models import Sale, Lease
#Option, Contact, Deal


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_filter = ['date_added']
    list_display = ['location_name','buyer_name', 'seller_name','asking_price', 'get_commissions_due_to_house', 'get_commissions_due_to_house_rep']
    fields = ['location_name','property_owner_name', 'seller_name', 'size_of_transaction'
                'asking_price','closing_price',
                ('transaction_close_date', 'contract_execution_date', 'commission_due_date'),
                ('sellers_broker', 'buyers_broker'),
                ('house_commission_rate', 'house_rep_commission_split_rate'),
                ('outside_broker_contact','outside_broker_w9_on_file', 'outside_broker_email_address',
                                        'outside_broker_commission_rate', 'outside_broker_contact_address',
                                        'outside_broker_contact_phone_number'),
                ('contingencies', 'commission_payout_terms',),
                ('send_invoice_to', 'invoice_address', 'invoice_phone', 'invoice_city', 'invoice_state',
                                        'invoice_zip','contact_person', ),
                'notes',
    ]


@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_filter = ['date_added']
    list_display = ['location_name','property_owner_name', 'tenant_name', 'size_of_transaction', 'rent_price', 'get_aggregate_lease_commission']
    fields = ['location_name','size_of_transaction','rent_price', 'lease_term_in_months',
                ('signed_lease_date', 'contract_execution_date', 'free_rent_start_date', 'free_rent_end_date', 'due_diligence_start_date',
                                    'due_diligence_end_date', 'rent_commencement_date', 'occupancy_date', 'lease_expiration_date'),
                ('rent_rate_factor', 'house_commission_rate', 'house_salesrep_commission_rate',
                                    'commission_payout_terms',),
                ('landlord', 'tenant_broker'),
                #('sellers_broker', 'buyers_broker'),
                #('house_commission_rate', 'house_rep_commission_split_rate'),
                ('outside_broker_contact','outside_broker_w9_on_file', 'outside_broker_email_address',
                                        'outside_broker_commission_rate', 'outside_broker_contact_address',
                                        'outside_broker_contact_phone_number'),
                #('contingencies', 'commission_payout_terms',),
                ('send_invoice_to', 'invoice_address', 'invoice_phone', 'invoice_city', 'invoice_state',
                                        'invoice_zip','contact_person', ),
                'notes',
                'contingencies'
    ]






#@admin.register(Option)
#class OptionAdmin(admin.ModelAdmin):
#    pass

#class LeaseOptionInstanceInline(admin.TabularInline):
#    model = Option

#@admin.register(Lease)
#class LeaseAdmin(admin.ModelAdmin):
#    exclude = ('date_added', 'date_modified',)
#    inlines = [LeaseOptionInstanceInline]





'''
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
