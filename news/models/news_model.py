from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey(
        "users", on_delete=models.CASCADE, related_name="news"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="img/", blank=True, null=True)
    categories = models.ManyToManyField("categories", related_name="news")

    def __str__(self):
        return self.title
