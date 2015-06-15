from django.db import models

#full_name = models.CharField(max_length=120, blank=True, null=True)
#timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
class Cloth(models.Model):
	clothType = models.CharField(max_length=50, blank=False, null=False, primary_key=True)
	unitPrice = models.IntegerField()
	discount = models.IntegerField()
	sales = models.IntegerField()

	def __unicode__(self):
		return self.clothType

class ClothDetail(models.Model):
	orderId = models.IntegerField(primary_key=True)
	clothType = models.CharField(primary_key=True, max_length=50, blank=False, null=False)
	quantity = models.IntegerField()
	price = models.IntegerField()

	def __unicode__(self):
		return (self.orderId, self.clothType)

class Order(models.Model):
	orderId = models.IntegerField(primary_key=True)
	memo = models.CharField(max_length=200)
	customerId = models.IntegerField()
	state = models.IntegerField(default=0)
	sumPrice = models.IntegerField()
	addrId = models.IntegerField()
	createdAt = models.DateTimeField(auto_now_add=True, auto_now=False)
	bookTime = models.DateTimeField(auto_now_add=False, auto_now=False, null=False)
	collectTime = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
	finishTime = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
	backTime = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)

	def __unicode__(self):
		return str(self.orderId)

class Customer(models.Model):
	customerId = models.AutoField(primary_key=True)
	cellphone = models.CharField(max_length=15, blank=False, null=False, unique=True)
	firstName = models.CharField(max_length=16, blank=False,null=False)
	lastName = models.CharField(max_length=16, blank=False, null=False)
	password = models.CharField(max_length=64, blank=False, null=False)
	

	def __unicode__(self):
		return self.cellphone

class Address(models.Model):
	addressId = models.AutoField(primary_key=True)
	school = models.CharField(max_length=16)
	building = models.CharField(max_length=16)

	def __unicode__(self):
		return str(self.addressId)


