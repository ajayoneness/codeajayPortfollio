from django.db import models


class yourDetails(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    degree = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    birthday = models.DateField(blank=True,null=True)
    emailid =  models.EmailField(null=True, blank=True)
    address = models.TextField( max_length=500, blank=True,null=True)
    experienceYear = models.CharField(max_length=10, blank=True, null=True)

class ProfileImage(models.Model):
    stu = models.OneToOneField(yourDetails,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Profile_image',  blank=True, null=True)
    image2 = models.ImageField(upload_to='Profile_image',  blank=True, null=True)

class Resume(models.Model):
    stu = models.OneToOneField(yourDetails,on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resume',  blank=True, null=True)
    

class Educations(models.Model):
    stu = models.ForeignKey(yourDetails,on_delete=models.CASCADE)
    degree_name  = models.CharField(max_length=100, blank=True,null=True)
    UniversityName = models.CharField(max_length=250, blank=True,null=True)
    startyear = models.IntegerField()
    passingyear   = models.IntegerField()
    gradepointsgained = models.DecimalField(decimal_places=2, max_digits=5)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    Decription = models.TextField(max_length=500, blank=True, null=True)


class Expericence(models.Model):
    stu = models.ForeignKey(yourDetails,on_delete=models.CASCADE)
    post = models.CharField(max_length=100, blank=True,null=True)
    company_name  = models.CharField(max_length=250, blank=True,null=True)
    Duration = models.IntegerField()
    Decription = models.TextField(max_length=500, blank=True, null=True)


class Skills(models.Model):
    stu = models.ForeignKey(yourDetails,on_delete=models.CASCADE)
    skillname = models.CharField(max_length=50, blank=True,null=True)
    #rate yourself out of 100
    rate = models.IntegerField()


class service(models.Model):
    stu = models.ForeignKey(yourDetails,on_delete=models.CASCADE)
    sevicename = models.CharField(max_length=50, blank=True,null=True)
    shortDecription = models.TextField(max_length=250, blank=True, null=True)
    fullDecription = models.TextField(max_length=1000, blank=True, null=True)


class portfolio(models.Model):
    stu = models.ForeignKey(yourDetails,on_delete=models.CASCADE)
    title = models.CharField(max_length=64,null=True,blank=True)
    image = models.ImageField(upload_to='portfolioImg', blank=True, null=True)
    video = models.FileField(upload_to='portfolioVideo', blank=True, null=True)
    shortDecription = models.TextField(max_length=250, blank=True, null=True)
    fullDecription = models.TextField(max_length=1000, blank=True, null=True)

class Clint(models.Model):
    stu = models.ForeignKey(yourDetails,on_delete=models.CASCADE)
    name = models.CharField(max_length=30,blank=True,null=True)
    email = models.EmailField()
    message = models.TextField(max_length=500, null=True,blank=True)
    image = models.ImageField(upload_to='clintImg', blank=True, null=True)
    profession = models.CharField(max_length=50,null=True,blank=True)

class Blog(models.Model):
    stu = models.ForeignKey(yourDetails,on_delete=models.CASCADE)
    title = models.CharField(max_length=64,null=True,blank=True)
    image = models.ImageField(upload_to='blogImg', blank=True, null=True)
    shortDecription = models.TextField(max_length=250, blank=True, null=True)
    fullDecription = models.TextField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Contact(models.Model) : 
    stu = models.ForeignKey(yourDetails,on_delete=models.CASCADE)
    Name = models.CharField( max_length = 70, blank=True, null=True)
    Email = models.EmailField ()
    subject = models.CharField(max_length=100,blank=True,null=True)
    Message = models.TextField (max_length = 800 ,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)






