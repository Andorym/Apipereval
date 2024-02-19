from django.db import models

class User(models.Model):
    name = models.CharField(max_length=25)
    second_name = models.CharField(max_length=25)
    otc = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'pass_user'


class Pass(models.Model):
    ADDED_STATUS = [
        ('new', 'new data'),
        ('pending', 'The data is being processed'),
        ('accepted', 'Processing is successful'),
        ('rejected', 'The data is not accepted'),
    ]

    created = models.DateTimeField(auto_now_add=True)
    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.CharField(max_length=255, blank=True)
    add_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=ADDED_STATUS, default='new')
    coordinates = models.ForeignKey('Coordinates', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.ForeignKey('Level', blank=True, on_delete=models.PROTECT)

    class Meta:
        db_table = 'pass_pass'

class Coordinates(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

    class Meta:
        db_table = 'pass_coordinates'


class Level(models.Model):
    winter_level = models.CharField(max_length=5, blank=True)
    summer_level = models.CharField(max_length=5, blank=True)
    autumn_level = models.CharField(max_length=5, blank=True)
    spring_level = models.CharField(max_length=5, blank=True)

    class Meta:
        db_table = 'pass_level'
        ordering = [-1]


class Images(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=35)
    data = models.BinaryField()
    passes = models.ForeignKey(Pass, related_name='images', on_delete=models.CASCADE)

    class Meta:
        db_table = 'pass_images'