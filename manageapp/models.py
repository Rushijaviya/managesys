from django.db import models

# Create your models here.


class guard_reg(models.Model):
    
    uname=models.CharField(primary_key=True,max_length=20)
    fname=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=10)

    def __str__(self):
        return self.uname
    
class user_reg(models.Model):
    
    uname=models.CharField(max_length=20)
    fname=models.CharField(max_length=20)
    mname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    mobile=models.CharField(max_length=10)
    house=models.CharField(primary_key=True,max_length=10)
    Option=models.CharField(max_length=10)
    password=models.CharField(max_length=10)

    def __str__(self):
        return self.house


class SendRecieve(models.Model):
    sr=models.CharField(primary_key=True,max_length=50)

    def __str__(self):
        return self.sr
        
class Message(models.Model):
    sender = models.ForeignKey(SendRecieve, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(SendRecieve, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)



class rent(models.Model):
    Name=models.CharField(max_length=30)
    house=models.ForeignKey(user_reg,on_delete=models.CASCADE)
    Month=models.CharField(max_length=30)
    Amount=models.CharField(max_length=10)
    pmethod=models.CharField(max_length=30)

    def __str__(self):
        return self.Name

class maintain(models.Model):
    Name=models.CharField(max_length=30)
    house=models.ForeignKey(user_reg,on_delete=models.CASCADE)
    Month=models.CharField(max_length=30)
    Amount=models.CharField(max_length=10)
    pmethod=models.CharField(max_length=30)

    def __str__(self):
        return self.Name


class addevent(models.Model):
    NEvent=models.CharField(primary_key=True,max_length=50)
    DEvent=models.CharField(max_length=70)
    DateE=models.CharField(max_length=50)
    TEvent=models.CharField(max_length=50)
    Fund=models.CharField(max_length=50)
    Venue=models.CharField(max_length=50)

    def __str__(self):
        return self.NEvent

class complain(models.Model):
    Name=models.CharField(primary_key=True,max_length=50)
    ctitle=models.CharField(max_length=50)
    comp=models.CharField(max_length=70)

    def __str__(self):
        return self.Name

class guest(models.Model):
    VName=models.CharField(max_length=50)
    house=models.ForeignKey(user_reg,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=50)

    def __str__(self):
        return self.VName