from django.db import models
from djmoney.models.fields import MoneyField

WINDOWS = "Windows"
MAC = "MacOS"
LINUX = "Linux"
DECK = "Steam Deck"

GAME = "Game"
SOFTWARE = "Software"


SYSTEMS_CHOICE = (
    (WINDOWS, "Windows"),
    (MAC, "MacOS"),
    (LINUX, "Linux"),
    (DECK, "Steam Deck"),
)

APP_TYPE_CHOICE = (
    (GAME, "Game"),
    (SOFTWARE, "Software"),
)


class Systems(models.Model):
    name = models.CharField(
        "System", max_length=63, choices=SYSTEMS_CHOICE, default="Windows", unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Systems"

        def __str__(self):
            return self.name


class LowestPrices(models.Model):
    balance = MoneyField(max_digits=14, decimal_places=2,
                         default_currency='USD')

    class Meta:
        ordering = ['balance']
        verbose_name_plural = "LowestPrices"

        def __str__(self):
            return self.name

class Prices(models.Model):
    balance = MoneyField(max_digits=14, decimal_places=2,
                         default_currency='USD')

    class Meta:
        ordering = ['balance']
        verbose_name_plural = "Prices"

        def __str__(self):
            return self.name

class Genres(models.Model):
    name = models.CharField("Genres",  max_length=63,
                            default="Indie", unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Genres"

        def __str__(self):
            return self.name


class Developers(models.Model):
    name = models.CharField("Name", max_length=63, unique=True)

    class Meta:
        ordering = ['name']

        def __str__(self):
            return self.name


class Publishers(models.Model):
    name = models.CharField("Name", max_length=63, unique=True)

    class Meta:
        ordering = ['name']

        def __str__(self):
            return self.name


class Games(models.Model):
    name = models.CharField("Name", max_length=255, unique=True)
    app_type = models.CharField(
        "APP Type",max_length=31, choices=APP_TYPE_CHOICE, default="Game", unique=True)
    link = models.URLField("URL", max_length=128, db_index=True, unique=True)
    genres = models.ManyToManyField(Genres)
    developers = models.ManyToManyField(Developers)
    publishers = models.ManyToManyField(Publishers)
    systems = models.ManyToManyField(Systems)
    published_at = models.TimeField("Published At")
    last_record = models.TimeField("Last Record Update", auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Games"

    def __str__(self):
        return self.name


class DLC(models.Model):
    name = models.CharField("Name", max_length=63, unique=True)
    game = models.ForeignKey(Games, on_delete=models.DO_NOTHING)
    link = models.URLField("URL", max_length=128, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "DLCs"

        def __str__(self):
            return self.name


class Bundle(models.Model):
    name = models.CharField("Name", max_length=63, unique=True)
    games = models.ForeignKey(Games, on_delete=models.DO_NOTHING)
    dlcs = models.ForeignKey(DLC, on_delete=models.DO_NOTHING)
    link = models.URLField("URL", max_length=128, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Bundles"

        def __str__(self):
            return self.name


class GameStore(models.Model):
    name = models.CharField("Name", max_length=63, unique=True)
    link = models.URLField("URL", max_length=128, db_index=True, unique=True)
    current_prices = models.ManyToManyField(Prices)
    lower_record_prices = models.ManyToManyField(LowestPrices)
    games = models.ManyToManyField(Games)
    dlc = models.ForeignKey("DLC",DLC)
    bundle = models.ForeignKey("Bundle",Bundle)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "GameStores"

        def __str__(self):
            return self.name
