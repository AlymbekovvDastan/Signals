from django.db import models

class Job(models.Model):
    company = models.CharField(max_length=255, blank=False)
    company_email = models.CharField(max_length=255, blank=False)
    title = models.CharField(max_length=255, blank=False)
    details = models.CharField(max_length=255, blank=False)
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    email = models.CharField(max_length=255, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class Subscription(models.Model):
    email = models.CharField(max_length=255, blank=False)
    user = models.ForeignKey(Subscriber, related_name='subscriptions', on_delete=models.CASCADE)
    job = models.ForeignKey(Job, related_name='jobs', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
