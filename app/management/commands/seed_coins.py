from django.core.management.base import BaseCommand
from app.models import Coin,wallet ,Coin2
import requests
domain_map = {
    'Unknown Wallet': None,
    'Safepal': 'safepal.io',
    'Trust': 'trustwallet.com',
    'Metamask': 'metamask.io',
    'Coinbase': 'coinbase.com',
    'Aktionariat': 'aktionariat.com',
    'Alice': 'alice.co',
    'Alpha Wallet': 'alphawallet.com',
    'Anchor': 'anchorprotocol.com',
    'Arculus': 'getarculus.com',
    'Argent': 'argent.xyz',
    'At Wallet': 'atwallet.io',
    'Atomic': 'atomicwallet.io',
    'Authereum': 'authereum.com',
    'Bakkt': 'bakkt.com',
    'Binance Smart Chain': 'binance.com',
    'Bit Keep': 'bitkeep.com',
    'Bit Pay': 'bitpay.com',
    'Blockchain': 'blockchain.com',
    'Bridge Wallet': 'mtpelerin.com',
    'Coin98': 'coin98.com',
    'Coinomi': 'coinomi.com',
    'Cool Wallet S': 'coolwallet.io',
    'Cosmostation': 'cosmostation.io',
    'Crypto com DeFi Wallet': 'crypto.com',
    'Cybavo Wallet': 'cybavo.com',
    'D Cent Biometric Wallet': 'dcentwallet.com',
    'D Cent Wallet': 'dcentwallet.com',
    'Dok Wallet': 'dokwallet.com',
    'Easy Pocket': 'easypocket.app',
    'Eidoo': 'eidoo.io',
    'Ellipal': 'ellipal.com',
    'Equal': 'equal.tech',
    'Exodus': 'exodus.com',
    'Fetch': 'fetch.ai',
    'Girin Wallet': 'girinlabs.com',
    'Gnosis Safe Multisig': 'safe.global',
    'Graph Protocol': 'thegraph.com',
    'Grid Plus': 'gridplus.io',
    'Harmony': 'harmony.one',
    'Huobi Wallet': 'htx.com',
    'Iconex': 'icon.foundation',
    'Infinito': 'infinitowallet.io',
    'Infinity Wallet': 'infinitywallet.io',
    'Karda Chain': 'kardiachain.io',
    'Keplr': 'keplr.app',
    'Keyring Pro': 'keyring.app',
    'Ledger Flex': 'ledger.com',
    'Ledger Live': 'ledger.com',
    'Ledger Nano S': 'ledger.com',
    'Ledger Nano S Plus': 'ledger.com',
    'Ledger Nano X': 'ledger.com',
    'Ledger Stax': 'ledger.com',
    'Lobstr': 'lobstr.co',
    'Loopring Wallet': 'loopring.io',
    'Maiar': 'maiar.com',
    'Math Wallet': 'mathwallet.org',
    'Meet One': 'meet.one',
    'Midas Wallet': 'midasprotocol.io',
    'Morix Wallet': 'morix.io',
    'Mykey': 'mykey.org',
    'Nash': 'nash.io',
    'Ngrave': 'ngrave.io',
    'Onto': 'onto.app',
    'Ownbit': 'ownbit.io',
    'Peak DeFi Wallet': 'peakdefi.com',
    'Phantom': 'phantom.app',
    'Pillar': 'pillarproject.io',
    'Qubic': 'qubic.org',
    'Rainbow': 'rainbow.me',
    'Spark Point': 'sparkpoint.io',
    'Spatium': 'spatium.net',
    'Tangem': 'tangem.com',
    'Token Pocket': 'tokenpocket.pro',
    'Tokenary': 'tokenary.io',
    'Torus': 'tor.us',
    'Trezor Model T': 'trezor.io',
    'Trust Vault': 'trustology.io',
    'Unstoppable Wallet': 'unstoppable.money',
    'Via Wallet': 'viawallet.com',
    'Vision': 'visionwallet.io',
    'Wallet Connect': 'walletconnect.com',
    'Wallet IO': 'wallet.io',
    'Walleth': 'walleth.org',
    'Wazirx': 'wazirx.com',
    'Xaman': 'xaman.app',
    'Xdc Wallet': 'xinfin.org',
    'Zel Core': 'zel.network',
}
def get_logo(name):
    domain = domain_map.get(name)

    if not domain:
        return "/default-wallet.png"  # fallback image

    return f"https://img.logo.dev/{domain}?token=pk_M_8OKJSSTmyAenmFPoETAA"
wallets = [
    {
        'name': name,
        'link': '#',
        'logo': get_logo(name)
    }
    for name in domain_map 
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
            obj, created = Coin2.objects.get_or_create( shortname=coin["symbol"].upper(),
                                                    defaults={ "fullname": coin["name"], 
                                                                "image": coin["image"], 
                                                                "traderate": price_str } )
             
            objs, createds = wallet.objects.get_or_create(
                    name=coin["name"],
            )

            
            if not created: 
                obj.fullname = coin["name"] 
                obj.image = coin["image"] 
                obj.traderate = price_str 
                obj.save()
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