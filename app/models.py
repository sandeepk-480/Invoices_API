from django.db import models


class Invoice(models.Model):
    date = models.DateTimeField(auto_now=True)
    customer_name = models.CharField(max_length=250)

    def __str__(self):
        return self.customer_name


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)