# -*- coding: utf-8 -*-
from django.test import TestCase

from .models import Lease

class TestLeaseModel(TestCase):

    def test_lease_creation(self):
        Lease = get_lease_model()
        # New lease created
        lease = Lease.objects.create(
            tenant_name="Test Tenant",
            property_owner_name="Test Property Owner",
            location_name="Testy Testas",
            signed_lease_date="2017-01-01",
            lease_term_in_months="24",
            size_of_space="1222",
            rent_price="5.54",
            lease_execution_date="2017-01-01",
            contingency_start_date="2017-01-01",
            contingency_end_date="2017-01-01",
            rent_commencement_date="2017-01-01",
            rent_rate_factor="1.0",
            occupancy_date="2017-01-01",
            landlord_broker="Test Landlord Broker",
            tenant_broker="Test Tenant Broker",
            lease_expiration_date="2017-01-01",
            contingencies="this is a list of test contingencies",
            deal_commission_rate="0.25",
            house_broker="Test House Broker",
            house_broker_commission_rate="0.4",
            outside_broker_commission_rate="0.4",
            commission_payout_terms="Test Commussuins payout terms",
            send_invoice_to="Send invoice to test",
            invoice_address="123 Test St",
            invoice_city="Testytown",
            invoice_state="NJ",
            invoice_zip="11111",
            invoice_phone="123-123-1234",
            contact_person="Test Contact",
            outside_broker_contact_address="123 Outside Broker Test St",
            outside_broker_contact_phone_number="011-44-987-987-9821",
            outside_broker_email_address="outside@brokertest.com",
            outside_broker_w9_on_file="False",
            notes="test notes",
            contingency_time_in_days="99",
            permit_type="Test Permit",
            )
        # Check that a Profile instance has been crated
        self.assertIsInstance(models.Lease)
        # Call the save method of the user to activate the signal
        # again, and check that it doesn't try to create another
        # profile instace
        lease.save()
        self.assertIsInstance(models.Lease)
