from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.contrib.auth import get_user_model


class MainCaseViewSets(viewsets.ModelViewSet):
    queryset = MainCase.objects.all()
    serializer_class = MainCaseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['summ']
    search_fields = ['title']

class SimpleCaseViewSets(viewsets.ModelViewSet):
    queryset = SimpleCase.objects.all()
    serializer_class = SimpleCaseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['summ']
    search_fields = ['title']


class MainProcessorsViewSets(viewsets.ModelViewSet):
    queryset = MainProcessors.objects.all()
    serializer_class = MainProcessorsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SimpleProcessorsViewSets(viewsets.ModelViewSet):
    queryset = SimpleProcessors.objects.all()
    serializer_class = SimpleCaseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MainCoolingViewSets(viewsets.ModelViewSet):
    queryset = MainCooling.objects.all()
    serializer_class = MainCoolingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SimpleCoolingViewSets(viewsets.ModelViewSet):
    queryset = SimpleCooling.objects.all()
    serializer_class = SimpleCoolingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MainRamViewSets(viewsets.ModelViewSet):
    queryset = MainRam.objects.all()
    serializer_class = MainRamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SimpleRamViewSets(viewsets.ModelViewSet):
    queryset = SimpleRam.objects.all()
    serializer_class = SimpleRamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MainMother_boardViewSets(viewsets.ModelViewSet):
    queryset = MainMother_board.objects.all()
    serializer_class = MainMother_boardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SimpleMother_boardViewSets(viewsets.ModelViewSet):
    queryset = SimpleMother_board.objects.all()
    serializer_class = SimpleMother_boardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MainVideoCardViewSets(viewsets.ModelViewSet):
    queryset = MainVideoCard.objects.all()
    serializer_class = MainVideoCardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SimpleVideoCardViewSets(viewsets.ModelViewSet):
    queryset = SimpleVideoCard.objects.all()
    serializer_class = SimpleVideoCardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MainHddViewSets(viewsets.ModelViewSet):
    queryset = MainHdd.objects.all()
    serializer_class = MainHddSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SimpleHddViewSets(viewsets.ModelViewSet):
    queryset = SimpleHdd.objects.all()
    serializer_class = SimpleHddSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MainSsd1ViewSets(viewsets.ModelViewSet):
    queryset = MainSsd1.objects.all()
    serializer_class = MainSsd1Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SimpleSsd1ViewSets(viewsets.ModelViewSet):
    queryset = SimpleSsd1.objects.all()
    serializer_class = SimpleSsd1Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MainSsd2ViewSets(viewsets.ModelViewSet):
    queryset = MainSsd2.objects.all()
    serializer_class = MainSsd2Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SimpleSsd2ViewSets(viewsets.ModelViewSet):
    queryset = SimpleSsd2.objects.all()
    serializer_class = SimpleSsd2Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MainDVD_driveViewSets(viewsets.ModelViewSet):
    queryset = MainDVD_drive.objects.all()
    serializer_class = MainDVD_driveSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SimpleDVD_driveViewSets(viewsets.ModelViewSet):
    queryset = SimpleDVD_drive.objects.all()
    serializer_class = SimpleDVD_driveSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MainPower_supplyViewSets(viewsets.ModelViewSet):
    queryset = MainPower_supply.objects.all()
    serializer_class = MainPower_supplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SimplePower_supplyViewSets(viewsets.ModelViewSet):
    queryset = SimplePower_supply.objects.all()
    serializer_class = SimplePower_supplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MainWifi_adapterViewSets(viewsets.ModelViewSet):
    queryset = MainWifi_adapter.objects.all()
    serializer_class = MainWifi_adapterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SimpleWifi_adapterViewSets(viewsets.ModelViewSet):
    queryset = SimpleWifi_adapter.objects.all()
    serializer_class = SimpleWifi_adapterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MainSound_cardViewSets(viewsets.ModelViewSet):
    queryset = MainSound_card.objects.all()
    serializer_class = MainSound_cardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SimpleSound_cardViewSets(viewsets.ModelViewSet):
    queryset = SimpleSound_card.objects.all()
    serializer_class = SimpleSound_cardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MainOCViewSets(viewsets.ModelViewSet):
    queryset = MainOC.objects.all()
    serializer_class = MainOCSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SimpleOCViewSets(viewsets.ModelViewSet):
    queryset = SimpleOC.objects.all()
    serializer_class = SimpleOCSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MainMouseViewSets(viewsets.ModelViewSet):
    queryset = MainMouse.objects.all()
    serializer_class = MainMouseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SimpleMouseViewSets(viewsets.ModelViewSet):
    queryset = SimpleMouse.objects.all()
    serializer_class = SimpleMouseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MainKeyboardViewSets(viewsets.ModelViewSet):
    queryset = MainKeyboard.objects.all()
    serializer_class = MainKeyboardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SimpleKeyboardViewSets(viewsets.ModelViewSet):
    queryset = SimpleKeyboard.objects.all()
    serializer_class = SimpleKeyboardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MainMonitorViewSets(viewsets.ModelViewSet):
    queryset = MainMonitor.objects.all()
    serializer_class = MainMonitorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SimpleMonitorViewSets(viewsets.ModelViewSet):
    queryset = SimpleMonitor.objects.all()
    serializer_class = SimpleMonitorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MainHeadsetViewSets(viewsets.ModelViewSet):
    queryset = MainHeadset.objects.all()
    serializer_class = MainHeadsetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SimpleHeadsetViewSets(viewsets.ModelViewSet):
    queryset = SimpleHeadset.objects.all()
    serializer_class = SimpleHeadsetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


