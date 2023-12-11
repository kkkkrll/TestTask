from django.db import models


class Contract(models.Model):
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)


class CreditOrder(models.Model):
    contract = models.OneToOneField(
        Contract, verbose_name='Contract', on_delete=models.CASCADE, null=False, related_name='credit_order'
    )
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)


class Manufacturer(models.Model):
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)


class Product(models.Model):
    credit_order = models.ForeignKey(
        CreditOrder, verbose_name='CreditOrder', on_delete=models.CASCADE, related_name='products'
    )
    manufacturer = models.ForeignKey(
        Manufacturer, verbose_name='Manufacturer', on_delete=models.CASCADE, related_name='products'
    )
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)

# Task 2

# Product.objects.filter(credit_order__contract_id=32812)
# .values('manufacturer')
# .annotate(count=Count('manufacturer'))
# .values_list('manufacturer', flat=True)
