from django.db import models


class Room(models.Model):
    number = models.IntegerField(default=None, null=False)
    available = models.BooleanField()
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='books', blank=False)
    # variations = models.OneToManyField(Variation)

    def __str__(self):
        return f"{self.number} {self.available}"

class Guest(models.Model):
    name = models.CharField(max_length=255,default=None, blank=False, null=False)
    email = models.EmailField(max_length=254,unique=True,null=False,blank=False)
    room = models.OneToOneField(Room,on_delete=models.CASCADE, related_name='guest', blank=False,null=False)

    def __str__(self):
        return self.name

# def validate_even(value):
#     if value % 2 != 0:
#         raise ValidationError(
#             _('%(value)s is not an even number'),
#             params={'value': value},
#         )