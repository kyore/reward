from datetime import datetime
from django.db import models

from user.models import User, Supervisor, Hr


class BaseRating(models.Model):
    CHOICES = (
        (1, 'Муу'),
        (2, 'Хангалтгүй'),
        (3, 'Дунд'),
        (4, 'Сайн'),
        (5, 'Маш сайн')
    )

    speed = models.PositiveSmallIntegerField("Ажлын хурд", choices=CHOICES)
    quality = models.PositiveSmallIntegerField("Ажлын чанар", choices=CHOICES)
    active = models.PositiveSmallIntegerField("Идэвхи санаачлага", choices=CHOICES)
    attitude = models.PositiveSmallIntegerField("Харилцаа хандлага", choices=CHOICES)

    month = models.DateField("Сар")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.month = datetime(year=self.month.year, month=self.month.month, day=1)
        super(BaseRating, self).save(**kwargs)

    def get_score(self):
        score = (self.speed + self.quality + self.active + self.attitude) / 20 * 100
        return score

    def get_rating_result(self):
        return [self.speed, self.quality, self.active, self.attitude]


class Rating(BaseRating):
    supervisor = models.ForeignKey(Supervisor, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)


class OwnRating(BaseRating):
    user = models.ForeignKey(User, related_name='my_ratings', on_delete=models.CASCADE)


class HRRating(models.Model):
    hr = models.ForeignKey(Hr, related_name='ratings', on_delete=models.CASCADE)
    employee = models.ForeignKey(User, related_name='hr_ratings', on_delete=models.CASCADE)

    latency = models.IntegerField()
    overtime = models.IntegerField()

    month = models.DateField()
