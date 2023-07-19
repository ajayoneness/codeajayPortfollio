from django.shortcuts import render
from .models import yourDetails,ProfileImage,Resume,Educations,Expericence,Skills,portfolio,Clint,service,Blog,Contact


def index(request):

    usr = yourDetails.objects.get(id=1)
    profile = ProfileImage.objects.get(stu=usr)
    resumes = Resume.objects.get(stu=usr)
    edu = Educations.objects.filter(stu=usr)
    exp = Expericence.objects.filter(stu=usr)
    skills = Skills.objects.filter(stu=usr)
    folio = portfolio.objects.filter(stu=usr)
    clint =  Clint.objects.filter(stu=usr)
    blog =  Blog.objects.filter(stu=usr)

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        Contact(stu=usr,Name=name,Email=email,subject=subject,Message=message).save()
        

    cont = {
        'usr':usr,
        'profile':profile,
        'resume':resumes,
        'edu':edu,
        'exp':exp,
        'skills':skills,
        'folio':folio,
        'clint' : clint,
        'blog':blog,
    }


    return render(request,'index.html',cont)