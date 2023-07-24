from django.shortcuts import redirect, render,HttpResponse
from message_app.models import Msg
# Create your views here.
def create(request):
    if request.method=='GET': 
        #print("request is:",request.method )
        return render(request,'create.html') 
    else:
  
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']

       
       #insert record into database table
        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
        m.save()
        #return HttpResponse("data inserted seccessfully")
        return redirect('/dashboard')
  
def dashboard(request):

    m=Msg.objects.all()
    #print(m)
    context={}
    context['data']=m
    #return HttpResponse("data fetched from database")
    return render(request,'dashboard.html',context)

def delete(request,rid):
    #print("id to be delete",rid)
    m=Msg.objects.filter(id=rid)
    print(m)
    m.delete()
    return redirect('/dashboard')
    #return HttpResponse("id to be delete: "+rid)
def edit(request,rid):
    #print("id to br edited: "+rid)
    #return HttpResponse("id to be edited: "+rid)
    if  request.method=='GET':
        m=Msg.objects.get(id=rid)
        print(m)
        context={}
        context['data']=m
        return render(request,'edit.html',context)
    else:
        #submit updated form
        un=request.POST['uname']
        umail=request.POST['uemail']
        umob=request.POST['mobile']
        umsg=request.POST['msg']
        m=Msg.objects.filter(id=rid)
        m.update(name=un,email=umail,mobile=umob,msg=umsg)
        return redirect('/dashboard')
       # print(un)
        #print(umail)
        #print(umob)
        #print(umsg)
        #return HttpResponse("Record Updated")
