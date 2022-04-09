from django.db import models
from django.contrib.auth.models import AbstractUser




class City(models.Model):
    name = models.CharField(verbose_name='название', max_length=20)

    def __str__(self):
        return self.name


class Hotels(models.Model):
    #country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название', max_length=60)
    address = models.CharField(verbose_name='адрес', max_length=100)
    website = models.CharField(verbose_name='сайт', max_length=100, blank=True)
    email = models.EmailField()
    telephone = models.IntegerField(verbose_name='телефон', null=True)
    coord_w = models.IntegerField(verbose_name='широта', null=True)
    coord_l = models.IntegerField(verbose_name='долгота', null=True)
    rating = models.IntegerField(verbose_name='рейтинг', null=True)

    def __str__(self):
        return f"{self.name} ({self.city.name})"


class Image(models.Model):
    hotels_images = models.ImageField(upload_to='hotels_images', blank=True)
    rooms_images = models.ImageField(upload_to='rooms_images', blank=True)


class HotelsImage(models.Model):
    hotels = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)


class Comforts(models.Model):
    parking = models.BooleanField(verbose_name='парковка', default=False)
    transfer = models.BooleanField(verbose_name='трансфер', default=False)
    meals = models.BooleanField(verbose_name='питание', default=False)
    animation = models.BooleanField(verbose_name='анимация', default=False)
    fitness = models.BooleanField(verbose_name='фитнес', default=False)
    pool = models.BooleanField(verbose_name='бассейн', default=False)
    beach = models.BooleanField(verbose_name='пляж', default=False)
    spa = models.BooleanField(verbose_name='спа-комплекс', default=False)
    animals = models.BooleanField(verbose_name='животные', default=False)
    wifi = models.BooleanField(verbose_name='wifi', default=False)
    medical = models.BooleanField(verbose_name='медуслуги', default=False)


class HotelsComforts(models.Model):
    hotels = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    comforts = models.ForeignKey(Comforts, on_delete=models.CASCADE)


class Rooms(models.Model):
    type = models.CharField(verbose_name='тип номера', max_length=20)
    price = models.DecimalField(verbose_name='цена номера', max_digits=11, decimal_places=2, default=0)
    image = models.ImageField(upload_to='rooms_images', blank=True)

    def __str__(self):
        return f"{self.type} ({self.price})"


class HotelsRooms(models.Model):
    hotels = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE)


class RoomsComforts(models.Model):
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    comforts = models.ForeignKey(Comforts, on_delete=models.CASCADE)


class RoomsImage(models.Model):
    hotels = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)


class UsersHotels(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)


class Offers(models.Model):
    hotels = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='цена', max_digits=11, decimal_places=2, default=0)
    date_begin = models.DateField(verbose_name='заезд')
    date_end = models.DateField(verbose_name='выезд')
    adults = models.IntegerField(verbose_name='взрослые', default=1)
    children = models.IntegerField(verbose_name='дети', default=0)

    def __str__(self):
        return f"{self.hotels.name} ({self.price})"


class Reservation(models.Model):
    users = models.ForeignKey(UsersHotels, on_delete=models.CASCADE)
    offers = models.ForeignKey(Offers, on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='комментарий', blank=True)
    code = models.CharField(verbose_name='номер брони', max_length=100)

    def __str__(self):
        return f"{self.users} ({self.code})"


class Persons(models.Model):
    last_name = models.CharField(verbose_name='фамилия', max_length=50)
    first_name = models.CharField(verbose_name='имя', max_length=50)
    middle_name = models.CharField(verbose_name='отчество', max_length=50, blank=True)
    birthday = models.DateField(verbose_name='день рождения')

    def __str__(self):
        return f"{self.last_name} {self.first_name} "


class ReservationPersons(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    persons = models.ForeignKey(Persons, on_delete=models.CASCADE)
