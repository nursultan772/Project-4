from rest_framework import serializers
from .models import *


class MainProcessorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainProcessors
        fields = '__all__'


class SimpleProcessorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleProcessors
        fields = '__all__'


class MainCoolingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCooling
        fields = '__all__'
        

class SimpleCoolingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleCooling
        fields = '__all__'


class MainMother_boardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainMother_board
        fields = '__all__'


class SimpleMother_boardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleMother_board
        fields = '__all__'


class MainRamSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainRam
        fields = '__all__'

class SimpleRamSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleRam
        fields = '__all__'


class MainVideoCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainVideoCard
        fields = '__all__'


class SimpleVideoCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleVideoCard
        fields = '__all__'


class MainCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCase
        fields = '__all__'

class SimpleCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleCase
        fields = '__all__'


class MainHddSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainHdd
        fields = '__all__'


class SimpleHddSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleHdd
        fields = '__all__'


class MainSsd1Serializer(serializers.ModelSerializer):
    class Meta:
        model = MainSsd1
        fields = '__all__'


class SimpleSsd1Serializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleSsd1
        fields = '__all__'


class MainSsd2Serializer(serializers.ModelSerializer):
    class Meta:
        model = MainSsd2
        fields = '__all__'


class SimpleSsd2Serializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleSsd2
        fields = '__all__'


class MainDVD_driveSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainDVD_drive
        fields = '__all__'


class SimpleDVD_driveSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleDVD_drive
        fields = '__all__'


class MainPower_supplySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPower_supply
        fields = '__all__'


class SimplePower_supplySerializer(serializers.ModelSerializer):
    class Meta:
        model = SimplePower_supply
        fields = '__all__'


class MainWifi_adapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainWifi_adapter
        fields = '__all__'


class SimpleWifi_adapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleWifi_adapter
        fields = '__all__'


class MainSound_cardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSound_card
        fields = '__all__'


class SimpleSound_cardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleSound_card
        fields = '__all__'


class MainOCSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainOC
        fields = '__all__'


class SimpleOCSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleOC
        fields = '__all__'


class MainMouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainMouse
        fields = '__all__'


class SimpleMouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleMouse
        fields = '__all__'


class MainKeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainKeyboard
        fields = '__all__'


class SimpleKeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleKeyboard
        fields = '__all__'


class MainMonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainMonitor
        fields = '__all__'


class SimpleMonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleMonitor
        fields = '__all__'


class MainHeadsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainHeadset
        fields = '__all__'


class SimpleHeadsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleHeadset
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'