from datetime import datetime

from djongo import models as mongo_models


class Email(mongo_models.Model):
    id = mongo_models.ObjectIdField(max_length=25)
    name = mongo_models.CharField(max_length=100)
    email = mongo_models.EmailField(max_length=100)
    subscription_date = mongo_models.DateTimeField(default=datetime.now())
    print("w modelu email", flush=True)

    def __str__(self):
        return self.email
