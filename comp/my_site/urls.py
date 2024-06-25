from django.urls import path, include
from .views import *

urlpatterns = [

    path('accounts/',include('allauth.urls')),


    path('main_cases/', MainCaseViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='main_case_list'),
    path('main_cases/<int:pk>/',MainCaseViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='main_case_detail'),

    path('simple_cases/', SimpleCaseViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='simple_case_list'),
    path('simple_cases/<int:pk>/', SimpleCaseViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='simple_case_detail'),

    path('main_processors/', MainProcessorsViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='main_processors_list'),
    path('main_processers/<int:pk>/', MainProcessorsViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='main_processors_detail'),

    path('simple_processors/', SimpleProcessorsViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='simple_processors_list'),
    path('simple_processors/<int:pk>/', SimpleProcessorsViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='simple_processors_detail'),

    path('main_coolings/', MainCoolingViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='main_cooling_list'),
    path('main_coolings/<int:pk>/', MainCoolingViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='main_cooling_detail'),

    path('simple_coolings/', SimpleCoolingViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='simple_cooling_list'),
    path('simple_coolings/<int:pk>/', SimpleCoolingViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='simple_cooling_detail'),

    path('main_rams/', MainRamViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='main_ram_list'),
    path('main_rams/<int:pk>/', MainRamViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='main_ram_detail'),

    path('simple_rams/', SimpleRamViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='simple_ram_list'),
    path('simple_rams/<int:pk>/', SimpleRamViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='simple_ram_detail'),

    path('main_mother_boards/', MainMother_boardViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='main_mother_board_list'),
    path('main_mother_boards/<int:pk>/', MainMother_boardViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='main_mother_board_detail'),

    path('simple_mother_boards/', SimpleMother_boardViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='simple_mother_board_list'),
    path('simple_mother_boards/<int:pk>/', SimpleMother_boardViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='simple_mother_board_detail'),

    path('main_video_cards/', MainVideoCardViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='main_video_card_list'),
    path('main_video_card/<int:pk>/', MainVideoCardViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='main_video_card_detail'),

    path('simple_video_cards/', SimpleVideoCardViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='simple_video_card_list'),
    path('simple_video_card/<int:pk>/', SimpleVideoCardViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='simple_video_card_detail'),

    path('main_hdd/', MainHddViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='main_hdd_list'),
    path('main_hdd/<int:pk>/', MainHddViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='main_hdd_detail'),

    path('simple_hdd/', SimpleHddViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='simple_hdd_list'),
    path('simple_hdd/<int:pk>/', SimpleHddViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='simple_hdd_detail'),

    path('main_ssd1/', MainSsd1ViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='main_ssd1_list'),
    path('main_ssd1/<int:pk>/', MainSsd1ViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='main_ssd1_detail'),

    path('simple_ssd1/', SimpleSsd1ViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='simple_ssd1_list'),
    path('simple_ssd1/<int:pk>/', SimpleSsd1ViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='simple_ssd1_detail'),

    path('main_ssd2/', MainSsd2ViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='main_ssd2_list'),
    path('main_ssd2/<int:pk>/', MainSsd2ViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='main_ssd2_detail'),

    path('simple_ssd2/', SimpleSsd2ViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='simple_ssd2_list'),
    path('simple_ssd2/<int:pk>/', SimpleSsd2ViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='simple_ssd2_detail'),

    path('main_dvd_drives/', MainDVD_driveViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='main_dvd_drive_list'),
    path('main_dvd_drives/<int:pk>/', MainDVD_driveViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='main_dvd_drive_detail'),

    path('simple_dvd_drives/', SimpleDVD_driveViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='simple_dvd_drive_list'),
    path('simple_dvd_drives/<int:pk>/', SimpleDVD_driveViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='simple_dvd_drive_detail'),

    path('main_power_supplys/', MainPower_supplyViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='main_power_supply_list'),
    path('main_power_supplys/<int:pk>/', MainPower_supplyViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='main_power_supply_detail'),

    path('simple_power_supplys/', SimplePower_supplyViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='simple_power_supply_list'),
    path('simple_power_supplys/<int:pk>/', SimplePower_supplyViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='simple_power_supply_detail'),

    path('main_wifi_adapters/', MainWifi_adapterViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='main_wifi_adapter_list'),
    path('main_wifi_adaters/<int:pk>/', MainWifi_adapterViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='main_wifi_adapter_detail'),

    path('simple_wifi_adapters/', SimpleWifi_adapterViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='simple_wifi_adapter_list'),
    path('simple_wifi_adapter/<int:pk>/', SimpleWifi_adapterViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='simple_wifi_adapter_detail'),

    path('main_sound_cards/', MainSound_cardViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='main_sound_card_list'),
    path('main_sound_cards/<int:pk>/', MainSound_cardViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='main_sound_card_detail'),

    path('simple_sound_card/', SimpleSound_cardViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='simple_sound_card_list'),
    path('simple_sound_cards/<int:pk>/', SimpleSound_cardViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='simple_sound_card_detail'),

    path('main_ocs/', MainOCViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='main_oc_list'),
    path('main_ocs/<int:pk>/', MainOCViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='main_oc_detail'),

    path('simple_ocs/', SimpleOCViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='simple_oc_list'),
    path('simple_ocs/<int:pk>/', SimpleOCViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='simple_oc_detail'),

    path('main_mouses/', MainMouseViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='main_mouse_list'),
    path('main_mouses/<int:pk>/', MainMouseViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='main_mouses_detail'),

    path('simple_mouses/', SimpleMouseViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='simple_mouse_list'),
    path('simple_mouses/<int:pk>/', SimpleMouseViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='simple_mouse_detail'),

    path('main_keyboard/', MainKeyboardViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='main_keyboard_list'),
    path('main_keyboard/<int:pk>/', MainKeyboardViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='main_keyboard_detail'),

    path('simple_keyboards/', SimpleKeyboardViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='simple_keyboard_list'),
    path('simple_keyboards/<int:pk>/', SimpleKeyboardViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='simple_keyboard_detail'),

    path('main_monitors/', MainMonitorViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='main_monitor_list'),
    path('main_monitors/<int:pk>/', MainMonitorViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='main_monitor_detail'),

    path('simple_monitors/', SimpleMonitorViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='simple_monitor_list'),
    path('simple_monitors/<int:pk>/', SimpleMonitorViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='simple_monitor_detail'),

    path('main_headsets/', MainHeadsetViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='main_headset_list'),
    path('main_headsets/<int:pk>/', MainHeadsetViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='main_headset_detail'),

    path('simple_headsets/', SimpleHeadsetViewSets.as_view({'get': 'list', 'post': 'create'}),
        name='simple_headset_list'),
    path('simple_headsets/<int:pk>/', SimpleHeadsetViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='simple_headset_detail'),

]