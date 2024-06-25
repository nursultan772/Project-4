from django.db import models

class User(models.Model):
    user = models.CharField(max_length=50)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class MainProcessors(models.Model):
    title = models.CharField(max_length=48, verbose_name="Тип процессора")

    def __str__(self):
        return self.title

class SimpleProcessors(models.Model):
    title = models.CharField(max_length=60)
    summ = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    processors = models.ForeignKey(MainProcessors, related_name='processors', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class MainCooling(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title

class SimpleCooling(models.Model):
    title = models.CharField(max_length=60)
    summ = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    cooling = models.ForeignKey(MainCooling, related_name='cooling', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class MainMother_board(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class SimpleMother_board(models.Model):
    title = models.CharField(max_length=60)
    summ = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    motherboard = models.ForeignKey(MainMother_board, related_name='mother_board', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class MainRam(models.Model):
    title = models.CharField(max_length=28)

    def __str__(self):
        return self.title

class SimpleRam(models.Model):
    title = models.CharField(max_length=80)
    summ = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    ram = models.ForeignKey(MainRam, related_name='ram', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class MainVideoCard(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class SimpleVideoCard(models.Model):
    title = models.CharField(max_length=60)
    summ = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    video_card = models.ForeignKey(MainVideoCard, related_name='video_card', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class MainHdd(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title

class SimpleHdd(models.Model):
    title = models.CharField(max_length=60)
    summ = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    hdd = models.ForeignKey(MainHdd, related_name='hdd', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class MainSsd1(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class SimpleSsd1(models.Model):
    title = models.CharField(max_length=60)
    summ = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    ssd1 = models.ForeignKey(MainSsd1, related_name='ssd1', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class MainSsd2(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class SimpleSsd2(models.Model):
    title = models.CharField(max_length=60)
    summ = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    ssd2 = models.ForeignKey(MainSsd2, related_name='ssd2', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class MainDVD_drive(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class SimpleDVD_drive(models.Model):
    title = models.CharField(max_length=60)
    summ = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    dvd_drive = models.ForeignKey(MainDVD_drive, related_name='dvd_drive', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class MainCase(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class SimpleCase(models.Model):
    title = models.CharField(max_length=60)
    summ = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    case = models.ForeignKey(MainCase, related_name='case', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class MainPower_supply(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class SimplePower_supply(models.Model):
    title = models.CharField(max_length=60)
    summ = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    power_supply = models.ForeignKey(MainPower_supply, related_name='power_supply', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class MainWifi_adapter(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class SimpleWifi_adapter(models.Model):
    title = models.CharField(max_length=60)
    summ = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    wifi_adapter = models.ForeignKey(MainWifi_adapter, related_name='wifi_adapter', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class MainSound_card(models.Model):
    title = models.CharField(max_length=60,)

    def __str__(self):
        return self.title


class SimpleSound_card(models.Model):
    title = models.CharField(max_length=60)
    summ = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    sound_card = models.ForeignKey(MainSound_card, related_name='sound_card', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class MainOC(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class SimpleOC(models.Model):
    title = models.CharField(max_length=60)
    summ = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    oc = models.ForeignKey(MainOC, related_name='oc', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class MainMouse(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class SimpleMouse(models.Model):
    title = models.CharField(max_length=60)
    summ = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    mouse = models.ForeignKey(MainMouse, related_name='mouse', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class MainKeyboard(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class SimpleKeyboard(models.Model):
    title = models.CharField(max_length=60)
    summ = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    keyboard = models.ForeignKey(MainKeyboard, related_name='keyboard', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class MainMonitor(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class SimpleMonitor(models.Model):
    title = models.CharField(max_length=60)
    summ = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    monitor = models.ForeignKey(MainMonitor, related_name='monitor', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class MainHeadset(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class SimpleHeadset(models.Model):
    title = models.CharField(max_length=60)
    summ = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    headset = models.ForeignKey(MainHeadset, related_name='headset', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


