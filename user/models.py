from django.db import models
from django.contrib.auth.models import AbstractUser


class Division(models.Model):
    name = models.CharField("Хэлтсийн нэр", max_length=255)
    tovchlol = models.CharField("Товчлол", max_length=10)
    salary_pack = models.IntegerField("Цалингийн багц")

    def __str__(self):
        return self.name


class User(AbstractUser):
    first_name = models.CharField("Нэр", max_length=30)
    last_name = models.CharField("Овог", max_length=30)
    salary = models.IntegerField("Үндсэн цалин", null=True)
    position = models.CharField("Албан тушаал", max_length=255)
    division = models.ForeignKey(Division, related_name='employees', on_delete=models.PROTECT)
    is_supervisor = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    def get_month_score(self, month):
        rating = self.ratings.filter(month__month=month).last()

        orating = self.my_ratings.filter(month__month=month).last()

        rating_score = rating.get_score() if rating else 0
        orating_score = orating.get_score() if orating else 0

        result = rating_score * 0.7 + orating_score * 0.3
        return result

    def get_month_rating_result(self, month):
        rating = self.ratings.filter(month__month=month).last()
        orating = self.my_ratings.filter(month__month=month).last()

        rating_result = rating.get_rating_result() if rating else [0, 0, 0, 0]
        orating_result = orating.get_rating_result() if orating else [0, 0, 0, 0]

        results = []

        for i in range(len(rating_result)):
            result = (rating_result[i] + orating_result[i]) / 2
            results.append(result)

        return results


class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Hr(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
