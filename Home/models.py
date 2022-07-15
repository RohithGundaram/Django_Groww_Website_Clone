from django.db import models

# Create your models here.
class Orders(models.Model):
    CustomerID = models.IntegerField()
    CustomerName = models.CharField(max_length=50)
    OrderNo = models.AutoField
    ShareName = models.CharField(max_length=50)
    Buy_SellPrice = models.IntegerField()
    NumberOfShares = models.IntegerField()
    OrderDate = models.DateField()
    OrderTime = models.TimeField()

    def __str__(self):
        a = str(str(self.CustomerID)+"_Amount_Rs."+str(self.Buy_SellPrice*self.NumberOfShares)+"/-_"+self.ShareName+"_"+str(self.CustomerName)+"_"+str(self.OrderDate)+"_"+str(self.OrderTime))
        return a 