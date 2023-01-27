from . import models
from rest_framework import serializers
from rest_framework import fields


class GameSerializer(serializers.ModelSerializer):
    name = fields.CharField(source="name", required=True)
    app_type = fields.CharField(source="app_type")
    link = fields.URLField(source="link")
    genres = serializers.RelatedField(many=True,source="genres",read_only=True)
    developers = serializers.RelatedField(many=True,source="developers",read_only=True)
    publishers = serializers.RelatedField(many=True,source="publishers",read_only=True)
    systems = serializers.RelatedField(many=True,source="systems",read_only=True)
    published_at = fields.TimeField(source="published_at")
    last_record = fields.TimeField(source="last_record")

    class Meta:
        model = models.Games
        fields = (
            'name',
            'app_type',
            'link',
            'genres',
            'developers',
            'publishers',
            'systems',
            'published_at',
            'last_record',
        )

        def __str__(self):
            return self.title


class DLCSerializer(serializers.ModelSerializer):
    name = fields.CharField(source="name",required=True)
    game = serializers.RelatedField(source="game",read_only=True)
    link = fields.URLField(source="link")

    class Meta:
        model = models.DLC
        fields = (
            'name',
            'game',
            'link',
        )

        def __str__(self):
            return self.name


class BundleSerializer(serializers.ModelSerializer):
    name = fields.CharField(source="name",required=True)
    games = serializers.RelatedField(source="name",read_only=True)
    dlcs = serializers.RelatedField(source="dlcs",read_only=True)
    link = fields.URLField(source="links")

    class Meta:
        model = models.Bundle
        fields = (
            'name',
            'games',
            'dlcs',
            'link',
        )

        def __str__(self):
            return self.name


class GameStoreSerializer(serializers.ModelSerializer):
    name = fields.CharField(source="name",required=True)
    link = fields.URLField(source="link")
    current_prices = serializers.RelatedField(many=True,source="current_prices",read_only=True)
    lower_record_prices = serializers.RelatedField(many=True,source="lower_record_prices",read_only=True)
    games = serializers.RelatedField(many=True,source="games",read_only=True)
    dlcs = serializers.RelatedField(source="dlcs",read_only=True)
    bundles = serializers.RelatedField(source="bundles",read_only=True)

    class Meta:
        model = models.GameStore
        fields = (
            'name',
            'link',
            'current_prices',
            'lower_record_prices',
            'games',
            'dlcs',
            'bundles',
        )

        def __str__(self):
            return self.name

        def __str__(self):
            return self.title
