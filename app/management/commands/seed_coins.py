from django.core.management.base import BaseCommand
from app.models import Coin,wallet  
import requests


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

            obj, created = Coin.objects.get_or_create(
                shortname=coin["symbol"].upper(),
                defaults={
                    "fullname": coin["name"],
                    "image": coin["image"],
                    "traderate": price_str
                }
            )
            objs, createds = wallet.objects.get_or_create(
                    name=coin["name"],
            )

            # Optional: update existing coins
            if not created:
                obj.fullname = coin["name"]
                obj.image = coin["image"]
                obj.traderate = price_str
                obj.save()
            if not createds:
                objs.name = coin["name"]
                objs.save()

            self.stdout.write(f"{coin['name']} saved ✅")

        self.stdout.write(self.style.SUCCESS("Seeding completed 🚀"))