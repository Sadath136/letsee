from django.shortcuts import render
from django.http import HttpResponse
import boto3
from .models import Collect
def homepage(request):
    information = Collect.objects.all()
    context = {'info': information}
    return render(request,'Commerce/homepage.html',context)
def su(request):
    if request.method=="POST":
        name = request.POST.get('username')
        phonenumber = request.POST.get('phonenumber')
        file=request.FILES.get('file_upload')
        import mysql.connector
        db = mysql.connector.connect(host="deployment.clm4ibgvdrzu.us-east-2.rds.amazonaws.com", passwd="Sadath8151",
                                     user="Sadath", database="Deployment")
        cursor = db.cursor()
        cursor.execute('select * from Commerce_collect where phone_number=%s',(phonenumber,))
        details=cursor.fetchall()
        if details==[]:
            import mysql.connector
            db = mysql.connector.connect(host="deployment.clm4ibgvdrzu.us-east-2.rds.amazonaws.com", passwd="Sadath8151",
                                         user="Sadath", database="Deployment")
            cursor = db.cursor()
            cursor.execute("insert into Commerce_collect(name,phone_number,image)values(%s,%s,%s)",
                           (name, phonenumber, file.name))
            db.commit()
            db.close()
            import mysql.connector
            db = mysql.connector.connect(host="deployment.clm4ibgvdrzu.us-east-2.rds.amazonaws.com", passwd="Sadath8151",
                                         user="Sadath", database="Deployment")
            cursor = db.cursor()
            cursor.execute('select id from Commerce_collect where phone_number=%s and name=%s',(phonenumber,name))
            kp=cursor.fetchone()
            s3=boto3.client('s3',aws_access_key_id="AKIA5UUHTIOD2M724W6J",aws_secret_access_key="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")
            s3.put_object(Body=file,Key=str(*kp)+str(file.name),Bucket="form-deployment")
            db.close()
            import mysql.connector
            db = mysql.connector.connect(host="deployment.clm4ibgvdrzu.us-east-2.rds.amazonaws.com", passwd="Sadath8151",
                                         user="Sadath", database="Deployment")
            cursor = db.cursor()
            cursor.execute("update Commerce_collect set image=%s where id=%s",(str(*kp)+str(file.name),*kp))
            db.commit()
            db.close()
            return render(request,'Commerce/suc.html')
        else:
            return HttpResponse("<h1><i>this person has already been registered</i></h1>")
                    
