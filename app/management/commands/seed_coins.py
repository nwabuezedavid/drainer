from django.core.management.base import BaseCommand
from app.models import Coin,wallet  
import requests
wallets = [
    {"name": "Trust Wallet", "link": "https://trustwallet.com", "logo": "https://img.logo.dev/trustwallet.com?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "MetaMask", "link": "https://metamask.io", "logo": "https://img.logo.dev/metamask.io?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Binance Wallet", "link": "https://www.binance.com", "logo": "https://img.logo.dev/binance.com?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "OKX Wallet", "link": "https://www.okx.com/web3", "logo": "https://img.logo.dev/okx.com?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Coinbase Wallet", "link": "https://www.coinbase.com/wallet", "logo": "https://img.logo.dev/coinbase.com?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Exodus Wallet", "link": "https://www.exodus.com", "logo": "https://img.logo.dev/exodus.com?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Ledger Live", "link": "https://www.ledger.com/ledger-live", "logo": "https://img.logo.dev/ledger.com?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Trezor Wallet", "link": "https://trezor.io", "logo": "https://img.logo.dev/trezor.io?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Huobi Wallet", "link": "https://www.huobi.com/wallet", "logo": "https://img.logo.dev/huobi.com?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Atomic Wallet", "link": "https://atomicwallet.io", "logo": "https://img.logo.dev/atomicwallet.io?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "MyEtherWallet", "link": "https://www.myetherwallet.com", "logo": "https://img.logo.dev/myetherwallet.com?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Coinomi Wallet", "link": "https://www.coinomi.com", "logo": "https://img.logo.dev/coinomi.com?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "SafePal Wallet", "link": "https://www.safepal.io", "logo": "https://img.logo.dev/safepal.io?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Math Wallet", "link": "https://mathwallet.org", "logo": "https://img.logo.dev/mathwallet.org?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "BitKeep Wallet", "link": "https://bitkeep.com", "logo": "https://img.logo.dev/bitkeep.com?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Argent Wallet", "link": "https://www.argent.xyz", "logo": "https://img.logo.dev/argent.xyz?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Rainbow Wallet", "link": "https://rainbow.me", "logo": "https://img.logo.dev/rainbow.me?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "AlphaWallet", "link": "https://alphawallet.com", "logo": "https://img.logo.dev/alphawallet.com?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "imToken", "link": "https://token.im", "logo": "https://img.logo.dev/token.im?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Trustee Wallet", "link": "https://trustee.com", "logo": "https://img.logo.dev/trustee.com?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "ZenGo Wallet", "link": "https://zengo.com", "logo": "https://img.logo.dev/zengo.com?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "CoolWallet S", "link": "https://www.coolwallet.io", "logo": "https://img.logo.dev/coolwallet.io?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Edge Wallet", "link": "https://edge.app", "logo": "https://img.logo.dev/edge.app?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Guarda Wallet", "link": "https://guarda.com", "logo": "https://img.logo.dev/guarda.com?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "TokenPocket", "link": "https://www.tokenpocket.pro", "logo": "https://img.logo.dev/tokenpocket.pro?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Coinbase Pro Wallet", "link": "https://pro.coinbase.com", "logo": "https://img.logo.dev/coinbase.com?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "BRD Wallet", "link": "https://brd.com", "logo": "https://img.logo.dev/brd.com?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Zerion Wallet", "link": "https://zerion.io", "logo": "https://img.logo.dev/zerion.io?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Paymium Wallet", "link": "https://www.paymium.com", "logo": "https://img.logo.dev/paymium.com?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Infinito Wallet", "link": "https://www.infinitowallet.io", "logo": "https://img.logo.dev/infinitowallet.io?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "ONTO Wallet", "link": "https://onto.app", "logo": "https://img.logo.dev/onto.app?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "D'Cent Wallet", "link": "https://www.dcentwallet.com", "logo": "https://img.logo.dev/dcentwallet.com?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Electrum Wallet", "link": "https://electrum.org", "logo": "https://img.logo.dev/electrum.org?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Coin98 Wallet", "link": "https://coin98.com/wallet", "logo": "https://img.logo.dev/coin98.com?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "MyCrypto Wallet", "link": "https://mycrypto.com", "logo": "https://img.logo.dev/mycrypto.com?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Tokenary Wallet", "link": "https://tokenary.io", "logo": "https://img.logo.dev/tokenary.io?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "BitKeep Mobile", "link": "https://bitkeep.com", "logo": "https://img.logo.dev/bitkeep.com?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "SafePal Mobile", "link": "https://www.safepal.io", "logo": "https://img.logo.dev/safepal.io?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Math Wallet Mobile", "link": "https://mathwallet.org", "logo": "https://img.logo.dev/mathwallet.org?token=pk_M_8OKJSSTmyAenmFPoETAA"},
    {"name": "Trustee Wallet Mobile", "link": "https://trustee.com", "logo": "https://img.logo.dev/trustee.com?token=pk_M_8OKJSSTmyAenmFPoETAA"}
]

class Command(BaseCommand):
    help = "Seed coins using CoinGecko API"

    def handle(self, *args, **kwargs):
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 50,
            "page": 1
        }

        response = requests.get(url, params=params)
        coins = response.json()

        for coin in coins:
            price_str = str(coin.get("current_price", "0"))

             
            objs, createds = wallet.objects.get_or_create(
                    name=coin["name"],
            )

            
            
            if not createds:
                objs.name = coin["name"]
                objs.save()

            self.stdout.write(f"{coin['name']} saved ✅")
        for coin in wallets:
             

            obj, created = Coin.objects.get_or_create(
                shortname=coin["name"],
                defaults={
                    "fullname": coin["name"],
                    "image": coin["logo"],
                    "traderate": 0
                }
            )
            

            # Optional: update existing coins
            if not created:
                obj.fullname = coin["name"]
                obj.image = coin["logo"]
                obj.traderate = 0
                obj.save()
            

            self.stdout.write(f"{coin['name']} saved ✅")

        self.stdout.write(self.style.SUCCESS("Seeding completed 🚀"))