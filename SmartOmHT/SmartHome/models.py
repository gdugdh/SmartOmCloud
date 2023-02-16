import uuid

from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth import get_user_model


class Home(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="homes")
	name = models.CharField("Имя", max_length=256)

	def __str__(self):
		return f"{user.username}: {self.name}"


# class Device(models.Model):
# 	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="devices")
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')


class DeviceType(models.Model):
	name = models.CharField("Название", max_length=256)

	def __str__(self):
		return f"Тип устройства: {self.name}"


class DeviceModel(models.Model):
	name = models.CharField("Название", max_length=256)

	def __str__(self):
		return f"Модель устройства: {self.name}"


class DevicePLC(models.Model):
	code = models.UUIDField("Код устройства", default = uuid.uuid4)
	device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
	device_model = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
	name = models.CharField("Название", max_length=256, default="SmartPLC")
	description = models.TextField("Описание")

	def __str__(self):
		return f"(SmartPLC): {self.id}"


class DataPLC(models.Model):
	device = models.ForeignKey(DevicePLC, on_delete=models.CASCADE, related_name="data_plc")
	datetime = models.DateTimeField("Время получения данных")
	temperature = models.IntegerField("Температура")
	humidity = models.IntegerField("Влажность")

	def __str__(self):
		return f"(SmartPLC) temperature: {self.temperature} |  humidity: {self.humidity}"
