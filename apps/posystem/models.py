from __future__ import unicode_literals
from django.utils.datastructures import MultiValueDictKeyError
from ..login_app.models import Club
from django.db import models
import re
import bcrypt
from django import forms
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class VendorManager(models.Manager):
    def registerVendor(self, postData):
        results = {'status': True, 'errors': [], 'user': None}
        if len(postData['vendor_name']) < 2:
            results['status'] = False
            results['errors'].append('Vendor Name Must be at Least 2 Character.')
        if len(postData['vendor_address']) < 10:
            results['status'] = False
            results['errors'].append('Vendor Address Must be at Least 10 Characters.')
        if len(postData['vendor_city']) < 1:
            results['status'] = False
            results['errors'].append('Vendor City Must be at Least 1 Characters.')
        if len(postData['vendor_state']) < 1:
            results['status'] = False
            results['errors'].append('Vendor State Must be at Least 1 Characters.')
        if len(postData['vendor_zip']) < 1:
            results['status'] = False
            results['errors'].append('Vendor Zip Code Must be at Least 1 Characters.')
        if len(postData['vendor_phone']) < 8:
            results['status'] = False
            results['errors'].append('Vendor Phont Must be at Least 8 Characters.')

        return results

    def createVendor(self, postData, club_id):
        user = Vendor.objects.create(
            vendor_name=postData['vendor_name'],vendor_address=postData['vendor_address'],vendor_city=postData['vendor_city'],vendor_state=postData['vendor_state'],
            vendor_zip=postData['vendor_zip'],vendor_phone=postData['vendor_phone'],vendor_fax=postData['vendor_fax'],vendorclub = Club.objects.get(id = club_id),
            vendorclubid = club_id)
        return user

@python_2_unicode_compatible
class Vendor(models.Model):
    vendor_name = models.CharField(max_length=30)
    vendor_address = models.CharField(max_length=100)
    vendor_city = models.CharField(max_length=30)
    vendor_state = models.CharField(max_length=30)
    vendor_zip = models.IntegerField()
    vendor_phone = models.CharField(max_length=30)
    vendor_fax = models.CharField(max_length=30)
    vendorclub = models.ForeignKey(Club, on_delete=models.CASCADE)
    vendorclubid = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = VendorManager()

    def __str__(self):
        return self.vendor_name

class ProductManager(models.Manager):
    def registerProduct(self, postData):
        results = {'status': True, 'errors': [], 'user': None}
        if len(postData['quantity']) < 1 or len(postData['quantity']) > 5:
            results['status'] = False
            results['errors'].append('Quantity Must be at Least 1.')
        if len(postData['product_number']) < 2 or len(postData['product_number']) > 15:
            results['status'] = False
            results['errors'].append('Product Number Must be at Least 2 Characters.')
        if len(postData['product_description']) < 3  or len(postData['product_description']) > 200:
            results['status'] = False
            results['errors'].append('Product Description Must be at Least 3 Characters and Shorter than 200 Characters.')
        # if len(postData['unit_cost']) < 3  or len(postData['unit_cost']) > 10 or postData['unit_cost'] != 0.00:
        if postData['unit_cost'] < 1:
            results['status'] = False
            results['errors'].append('Unit Cost Must be at Least 1 Characters.')
        print results
        return results

    def createProduct(self, postData, club_id):
        quantity = float(postData['quantity'])
        unitcost = float(postData['unit_cost'])
        user = Product.objects.create(
            product_quantity=quantity, product_number=postData['product_number'], product_description=postData['product_description'], unit_cost=unitcost,
            final_cost=(quantity*unitcost), votes=0, status='5 Votes Needed', productclub = Club.objects.get(id = club_id),
                productclubid = club_id, productvendor = Vendor.objects.get(id = postData['vendor']),)
        return user

@python_2_unicode_compatible
class Product(models.Model):
    product_quantity = models.IntegerField()
    product_number = models.CharField(max_length=25)
    product_description = models.CharField(max_length=200)
    unit_cost = models.FloatField(max_length=20)
    final_cost = models.CharField(max_length=20)
    votes = models.IntegerField()
    voters = models.ManyToManyField('login_app.User', related_name="voters")
    status = models.CharField(max_length=25)
    productclub = models.ForeignKey(Club, on_delete=models.CASCADE)
    productvendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    productclubid = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ProductManager()

    def __str__(self):
        return self.product_description
