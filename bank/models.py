from django.db import models

# Create your models here.

class Accounts(models.Model):
    sno = models.IntegerField(primary_key=True)
    Account_no = models.CharField(max_length=30,unique=True)
    Name = models.CharField(max_length=50)
    email = models.EmailField()
    Balance = models.DecimalField(max_digits=14,decimal_places=2)


    def __str__(self):
        return self.Name + " (" + self.Account_no +")"


class Transactions(models.Model):
    sno = models.AutoField(primary_key=True)
    sender_acc = models.ForeignKey(Accounts, on_delete=models.CASCADE, related_name='sender')
    receiver_acc =models.ForeignKey(Accounts, on_delete=models.CASCADE,related_name='receiver' )
    Amount = models.DecimalField(max_digits=14,decimal_places=2)
    status = models.BooleanField()
    date = models.DateTimeField(auto_now=True)






