from django.shortcuts import render
from django.http import HttpResponse
import boto3
def homepage(request):
    return render(request,'Commerce/homepage.html')
def su(request):
    if request.method=="POST":
        name = request.POST.get('username')
        phonenumber = request.POST.get('phonenumber')
        file=request.FILES.get('file_upload')
        import mysql.connector
        db = mysql.connector.connect(host="deployment.clm4ibgvdrzu.us-east-2.rds.amazonaws.com", passwd="Sadath8151",
                                     user="Sadath", database="Deployment")
        cursor = db.cursor()
        cursor.execute("insert into Test_collect(name,phone_number,image)values(%s,%s,%s)",
                       (name, phonenumber, file.name))
        db.commit()
        db.close()



        s3=boto3.client('s3',aws_access_key_id="AKIA5UUHTIOD2M724W6J",aws_secret_access_key="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")
        s3.put_object(Body=file,Key=str(file.name),Bucket="form-deployment")
        db.close()
        return render(request,'Commerce/suc.html')

