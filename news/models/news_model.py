from django.db import models
from news.validators import validate_date, validate_title


class News(models.Model):
    title = models.CharField(max_length=200, validators=[validate_title])
    content = models.TextField()
    author = models.ForeignKey(
        "Users",
        on_delete=models.CASCADE,
        related_name="news",
    )
    created_at = models.DateField(validators=[validate_date])
    image = models.ImageField(upload_to="img/", null=True, blank=True)
    categories = models.ManyToManyField(
        "Categories",
        related_name="news",
    )

    def __str__(self) -> str:
        return self.title
