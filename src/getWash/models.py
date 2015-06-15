from django.db import models

#full_name = models.CharField(max_length=120, blank=True, null=True)
#timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#updated = models.DateTimeField(auto_now_add=False, auto_now=True)
class Address(models.Model):
	addressId = models.AutoField(primary_key=True)
	school = models.CharField(max_length=16)
	building = models.CharField(max_length=16)

	def __unicode__(self):
		return str(self.addressId)

class Cloth(models.Model):
	clothType = models.CharField(max_length=50, blank=False, null=False, primary_key=True)
	unitPrice = models.IntegerField()
	sales = models.IntegerField()

	def __unicode__(self):
		return self.clothType

class Customer(models.Model):
	customerId = models.AutoField(primary_key=True)
	cellphone = models.CharField(max_length=15, blank=False, null=False, unique=True)
	firstName = models.CharField(max_length=16, blank=False,null=False)
	lastName = models.CharField(max_length=16, blank=False, null=False)
	password = models.CharField(max_length=64, blank=False, null=False)

	def __unicode__(self):
		return self.cellphone

class Order(models.Model):
	orderId = models.CharField(max_length=32, primary_key=True)
	memo = models.CharField(max_length=200, null=True)
	customer = models.ForeignKey(Customer)
	state = models.IntegerField(default=0)
	sumPrice = models.IntegerField()
	addr = models.ForeignKey(Address)
	createdAt = models.DateTimeField(auto_now_add=True, auto_now=False, null=False)
	bookTime = models.DateTimeField(auto_now_add=True, auto_now=False, null=False)
	collectTime = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	finishTime = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	backTime = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)

	def __unicode__(self):
		return str(self.orderId)
		
class ClothDetail(models.Model):
	order = models.ForeignKey(Order)
	clothType = models.ForeignKey(Cloth)
	quantity = models.IntegerField()

	class Meta:
		unique_together = ('clothType','order')

	def __unicode__(self):
		return (self.orderId, self.clothType)




