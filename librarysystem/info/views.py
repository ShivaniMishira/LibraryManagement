from django.shortcuts import render, redirect
from info.models import Books, Student,Issue,Sub,Post,Replie
from info.form import BookForm, StudentForm
from django.contrib import messages 
from datetime import date, timedelta,timezone
from django.shortcuts import get_object_or_404




# Create your views here.
def home(request):
    return render(request, 'home.html')

#singup
def sign_up_entry(request):
    return render(request , 'signup.html')


#signup
def sign_up_submit(request):
    if request.method == "POST":
        T1 =request.POST.get("name")
        T2 =request.POST.get("email")
        T3 =request.POST.get("password")

        if Student.objects.filter(name=T1).exists():
                print("username taken")
        elif Student.objects.filter(email=T2).exists():
                print('email exists')
        else:
            T = Student(name=T1, email=T2 ,password=T3)
            T.save()
    return render(request, 'signup.html' )


#signin
def sign_in_entry(request):
    return render (request, 'signin.html')

#signin
def sign_in_submit(request):
    if request.method == "POST":
        L1 = request.POST.get("name")
        L2 = request.POST.get("password")
        T1 = Student.objects.get(name=L1)
        a = T1.name
        b = T1.password
        c = T1.subscrib
        print("text = ",T1.id)
        if L1 == a:
            if L2 == b:
                request.session['stu'] = T1.id
                return render(request ,'prem.html')
        else:
            messages.info(request,"LogIn Failed")
    print("user id ",T1.id)    
    return render(request ,'prem.html')

def sub_exp(request):
    return render(request,'home.html')


# forget password funtion
def for_pass (request):
    if request. method == "POST":
        A1 = request.POST.get("name")
        A2 = request.POST.get("email")
        A4 = request.POST.get("newpass")
        A3 = Student.objects.get(name=A1)
        B1 = A3.name
        B2 = A3.email
        if A1 == B1 :
            if A2 == B2:
                A3.password = A4
                A3.save()
                messages.info(request,"Your Password Has Been Updated")
        else:
            messages.info(request,"Incorrect Entry")
    return render(request,'for_pass.html')


def student_profile(request):
    if 'stu' in request.session:
        stu_id = request.session['stu']
        A = Student.objects.filter(id=stu_id)
    return render(request, 'profile.html',{"A":A})

# student profile update function
def stu_edit(request):
        if request.method == "POST":
            sid = request.POST.get("update")
        A = Student.objects.get(id=sid)    
        context = {"A":A}
        return render(request, 'stu_update.html',context)

#student profile update function
def stu_update(request):
    if request.method == "POST":
        M = request.POST.get("user")
        M1 = request.POST.get("name")
        M2 = request.POST.get("email")
        M3 = request.POST.get("password")
        X1 = Student.objects.get(id=M)
        X1.name = M1
        X1.email = M2
        X1.password = M3
        X1.save()
        alert = True
    return render(request,'profile.html',{"alert":alert})

#signout
def sign_out(request):
    if 'stu' in request.session:
        request.session.flush()
    return redirect ('/')

# show Book Record
def book_show(request):
    data = Books.objects.all().values()
    return render(request, 'book_show.html', {'mybook':data})

# book record for user to issue books
def user_show(request):
    data = Books.objects.all()
    stu = request.session['stu']  
    context = {'stu':stu ,'mybook':data}
    return render(request, 'user_show.html',context)


#Book Update function
def book_edit(request,id):
    X = Books.objects.get(id=id)
    context={'X':X}
    return render(request, 'book_update.html',context)

# Book Update function
def book_update(request,id):
    if request.method == "POST":
        X1 = Books.objects.get(id=id)
        M1 = request.POST.get("name")
        M2 = request.POST.get("author")
        M3 = request.POST.get("publish")
        M4 = request.POST.get("category")
        M5 = request.POST.get("language")
        M6 = request.POST.get("stock")
        X1.name = M1
        X1.author = M2
        X1.publish = M3
        X1.category = M4
        X1.language = M5
        X1.stock = M6
        X1.save()
        X = Books.objects.all()
    return render(request, 'book_show.html', {'mydata':X})


# Add new Books to bookrecord
def book_add(request):
    if request.method == "POST":
        T1 = request.POST.get("name")
        T2 = request.POST.get("author")
        T3 = request.POST.get("publish")
        T4 = request.POST.get("category")
        T5 = request.POST.get("language")
        T6 = request.POST.get("stock")
        T = Books(name=T1, author=T2, publish=T3, category=T4, language=T5, stock=T6)
        T.save()
    return render(request, 'book_add.html')

# Delete Book
def book_delete(request,id):
    D = Books.objects.get(id=id)
    D.delete()
    return render(request, 'book_show.html')

# student book Issued function
def book_issued(request):
    if request.method == "POST":
        S2 = request.POST.get('user')
        U2 = request.POST.get('book')        
        B = Books.objects.get(id = int(U2))
        V = B.id
        B3 = B.name
        B2 = B.stock
        U = Student.objects.get(id = S2)
        V3 = U.id
        V2 = U.name
        U.issue = V
        U.bname = B3
        U1 = U.stock
        tday = date.today()
        exp = tday + timedelta(days=7)
        Issue.objects.create( Sname = V2,Sid = V3,Bname = B3,Bid = V,date=tday, expiry=exp)
        if int(U1) <  5:
            U1 = U1 + 1
            U.stock = U1
            U.save()
            if int(B2) > 0:
                B2 = int(B2) - 1
                B.stock = B2
                B.save()
            else:
                messages.info(request,"You have Reached Your Limit")
        J = Issue.objects.filter(Sid = V3)       
        return render (request, "issue_form.html",{"J":J})
    


# viwe book issued by student
def issue_show(request):
    if 'stu' in request.session:
        stu_id = request.session['stu']
        I = Student.objects.filter(id=stu_id)
        context = {'issue':I}
    return render(request,'issued.html',context)

#return book
def ret (request):
    return render(request,'return.html')

#book return show
def ret_show (request):
    V = Issue.objects.all()
    return render(request,"return.html",{"V":V})


# retun book function
def book_return(request):         
         if request.method == "POST":
             S2 = request.POST.get('user')
             U2 = request.POST.get('book')        
             B = Books.objects.get(id = U2)
             a = B.name
             b = B.id
             S = Student.objects.get(id = S2)
             s = S.id
             c = S.bname
             d = S.issue
             V = S.issue
             S1 = S.stock
             if int(S1) > 0:
                S1 = int(S1) - 1
                V = V - int(U2)
                S.issue = V
                S.stock = S1
                S.bname = 0
                S.save()
                i = Issue.objects.filter(Sid =  s)
                i.delete()
                if a == c:
                 if b == d:
                     B2 = B.stock    
                     B2 = B2 + 1
                     B.stock = B2
                     B.save()             
             else:
                 messages.info(request, "No Issued Books ")
         return render (request, "return.html")

# after book is issued student sees this page
def issue_form(request, slug, id):
    Issue=get_object_or_404(Issue, pk=id, slug=slug) 
    return render(request,'booking_detail.html',{'Issue': Issue})


# after login get membership page
def prem(request):
    return render(request,'prem.html')

# pyment for Subscribe plan
def sub (request):
    if request.method == "POST":
        q1 = request.POST.get("name")
        q2 = request.POST.get("card number")
        q3 = request.POST.get("plan")
        print("name--------------------------",q1)
        print("plan--------------------------",q3)
        #now = datetime.datetime.now()
        price=0
        if q3 == "Gold":
            dur = date.today() + timedelta(days=90)
            price=299
            A = Sub(Stu=q1, plan=q3 , price=price , Duration=dur)
            A.save()
        else:
            if q3 == "Silver":
                dur = date.today()+ timedelta(days=30)
                price=150
                A = Sub(Stu=q1, plan=q3 , price=price , Duration=dur)
                A.save()
            else:
                if q3 == "Platinum":
                    dur = date.today()  + timedelta(days=180)
                    price=599
                    A = Sub(Stu=q1, plan=q3 , price=price , Duration=dur)
                    A.save()
                else:
                    messages.info(request,"Error: somthing went wrong ")
        #Sub.objects.create(Stu=q1,price=price,plan=q3,Duration=dur)
        
    return render(request,'sub.html')


def forumadd(request):
    return render(request, 'forumadd.html')


def forum(request):
    if request.method=="POST":
        if 'stu' in request.session:
            stu_id = request.session['stu']
        S = Student.objects.get(id = stu_id)
        S1 = S.name
        content = request.POST.get('content','')
        post = Post(name_user=S1, post_content=content)
        post.save()
        alert = True
        return render(request, "forum.html", {'alert':alert})
    posts = Post.objects.filter().order_by('-timestamp')
    return render(request, "forum.html", {'posts':posts}) 

def reply(request,id):
    X = Post.objects.filter(id=id)
    context={'X':X}
    return render(request,'Discussion.html',context)

def discussion(request):
    if 'stu' in request.session:
            stu_id = request.session['stu']
    S = Student.objects.get(id = stu_id)
    S1 = S.name
    if request.method=="POST":
        desc = request.POST.get('desc','')
        post_id =request.POST.get('post_id','')
        post = Post.objects.filter(id=post_id).first()
        reply = Replie(name_user=S1, reply_content = desc, post=post)
        reply.save()
        return render(request, "Discussion.html")
# replie not showing up at discussion.html 
    replies = Replie.objects.filter(post=post).order_by('-timestamp')
    print("test-----------------",replies)
    return render(request, "Discussion.html", {'replies':replies})

def search(request):
    if request.method=="POST":
        S = request.POST.get("search")
        if Books.objects.filter(name=S):   
            con = Books.objects.filter(name=S)
            context={"con":con}             
            return render(request,'search.html',context)
    return render(request,'search.html')

def post_search(request):
    if request.method == "POST":
        S = request.POST.get("search")
        if Post.objects.filter(name_user=S):    
                con = Post.objects.filter(name_user=S)    
                context = {"con":con}     
                return render(request,'post_search.html',context)
    return render(request,'post_search.html')