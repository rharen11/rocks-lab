from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

DAYS = (
  ('M', 'Monday'),
  ('T', 'Tuesday'),
  ('W', 'Wednesday'),
  ('Th', 'Thursday'),
  ('F', 'Friday'),
  ('S', 'Saturday'),
  ('Sun', 'Sunday')
)

class Painting(models.Model):
  title = models.CharField(max_length=100)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
      return reverse("paintings_detail", kwargs={"pk": self.id})

class Rock(models.Model):
  type = models.CharField(max_length=100)
  color = models.CharField(max_length=50)
  description = models.TextField(max_length=300)
  location = models.CharField(max_length=50)
  paintings = models.ManyToManyField(Painting)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.type

  def get_absolute_url(self):
      return reverse("rocks_detail", kwargs={"rock_id": self.id})

  # def cleaned_for_year(self):
  #   return self.cleaning_set.filter(cleaning.count() >= 12)

class Cleaning(models.Model):
  day = models.CharField(
    max_length=8,
    choices=DAYS,
    default=DAYS[0][0]
    )
  month = models.CharField(
    'Month Cleaned',
    max_length=8,
    )

  rock = models.ForeignKey(Rock, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_day_display()} in {self.month}"

  # class Meta:
  #   ordering = ['-date']
  


  