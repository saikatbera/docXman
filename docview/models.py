from django.db import models


# Create your models here.

class User(models.Model):
    full_name = models.CharField(max_length=30)
    email_id = models.EmailField(max_length=254)
    user_name = models.CharField(max_length=10)
    password = models.CharField(max_length=8)
    phone_no = models.CharField(max_length=10)
    signup_date = models.DateTimeField('Registered Date')

    def __str__(self):
        return self.user_name

class Document(models.Model):
    doc_name = models.CharField(max_length=40)
    doc_type = models.CharField(max_length=4, default='unknown')
    pub_date = models.DateTimeField()
    pub_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.doc_name
    
