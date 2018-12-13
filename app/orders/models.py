from django.db import models


class Order(models.Model):
    address1 = models.CharField(max_length=30)

    address2 = models.CharField(max_length=30)

    comment = models.TextField()

    requested_at = models.DateTimeField(auto_now_add=True)

    cancel_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.address1
