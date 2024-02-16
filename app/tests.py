from django.test import TestCase
from app.models import Invoice, InvoiceDetail
from django.urls import reverse
from rest_framework import status


class InvoiceTestCase(TestCase):
    def setUp(self):
        self.invoice = Invoice.objects.create(customer_name = "Testcase Customer")

    def test_invoice_list(self):
        url = reverse('invoice')  # name in urls
        response = self.client.get(url) # This will make as client is requesting
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.invoice.id)

    def test_invoice_ROD(self):
        url = reverse('invoice_rod', args=[self.invoice.id])  # name in urls
        response = self.client.get(url) # This will make as client is requesting
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.invoice.id)


class InvoiceDetailTestCase(TestCase):
    def setUp(self):
        self.invoice = Invoice.objects.create(customer_name="Testcase Customer")
        self.invoice_detail = InvoiceDetail.objects.create(invoice=self.invoice, description="Hello There", quantity=1, unit_price=1, price='34')

    def test_invoice_detail_list(self):
        url = reverse('invoice_detail')  # name in urls
        response = self.client.get(url) # This will make as client is requesting
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.invoice_detail.id)

    def test_invoice_detail_ROD(self):
        url = reverse('invoice_detail_rod', args=[self.invoice_detail.id])  # name in urls
        response = self.client.get(url) # This will make as client is requesting
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.invoice_detail.id)

