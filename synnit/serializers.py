from django.contrib.auth.models import User 
from rest_framework.serializers import ModelSerializer 
from synnit.models import Synnintekija, Syntilaatu, TunnustettuSynti 


class Synnintekijazer(ModelSerializer):
    class Meta:
        model = Synnintekija
        exclude = ['id']


class Syntilaatuzer(ModelSerializer):
    class Meta:
        model = Syntilaatu
        fields = '__all__'


class TunnustettuSyntizer(ModelSerializer):
    class Meta:
        model = TunnustettuSynti
        exclude = ['id']
