from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext
from oj.models import problem,solution
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from oj.forms import status_query
# Create your views here.

def problemlist(request):
	problems=[]
	problem_list=problem.objects.all()
	problem_pages=Paginator(problem_list,10)
	page=request.GET.get('page')
	try:
		problems=problem_pages.page(page)
	except PageNotAnInteger:
		problems=problem_pages.page(1)
	except EmptyPage:
		problems=problem_pages.page(paginator.num_pages)

	return render_to_response("problemlist.html",RequestContext(request,{"problems":problems}))

from django.http import Http404

def problem_show(request, id):
    try:
    	print id
        problems = problem.objects.get(problem_id=id)#focus the rename of the variable
    except:
        raise Http404
    return render_to_response("problem.html", RequestContext(request,{"problem": problems}))

 # def index(request):
 # 	return render_to_response("index.html")
from oj.forms import status_query
def status(request):
	if request.method=='POST':
		f=status_query(request.POST)
		if f.is_valid():
			pid=f.cleaned_data['problem_id']
			uid=f.cleaned_data['user_id']
			lang=f.cleaned_data['lang']
			result=f.cleaned_data['result']
	else:
		f=status_query()
		pid=None
		uid=None
		lang='A'
		result='A'
 	status_list=solution.objects.all()
 	if pid:
 		status_list=status_list.filter(problem_id=pid)
 	if uid:
 		status_list=status_list.filter(user_id=uid)
 	if lang!='A':		
 		status_list=status_list.filter(language=lang)
 	if result!='A':
 		status_list=status_list.filter(result=result)

 	status_pages=Paginator(status_list.order_by('-solution_id'),20)
 	page=request.GET.get('page')
 	try:
 		statuses=status_pages.page(page)
 	except PageNotAnInteger:
 		statuses=status_pages.page(1)
 	except EmptyPage:
 		statuses=status_pages.page(status_pages.num_pages)
 	return render_to_response("status.html",RequestContext(request,{"statuses":statuses,"form":f}))
# from django.contirb import auth 	
# def login(request):
# 	username=request.POST.get('username','')
# 	password=request.POST.get('password','')
# 	user=auth.authenticate(username=username,password=password)
# 	if user is not None and user.is_active:
# 		auth.login(request,user)
# 		pass
# 	else:
# 		pass
# 	return render_to_response("login.html")

# test
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from oj.forms import RegisterForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from oj.models import users
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
        	u=User()
        	u.username=form.cleaned_data['username']
        	upwd=form.cleaned_data['password']
        	u.set_password(upwd)
        	u.eamil=form.cleaned_data['email']
        	u.save()
        	uinfo=users()
        	uinfo.user=u
        	uinfo.team=form.cleaned_data['team']
        	uinfo.nickname=form.cleaned_data['nickname']
        	uinfo.motto=form.cleaned_data['motto']
        	uinfo.realname=form.cleaned_data['realname']
        	uinfo.studentid=form.cleaned_data['studentid']
        	uinfo.score1=0
        	uinfo.save()
        	u=authenticate(username=u.username,password=upwd)
        	login(request,u)
        	return HttpResponseRedirect('/oj/')

            # new_user = form.save()
            # return HttpResponseRedirect("/oj/")
    else:
        form = RegisterForm()
    return render_to_response("register.html", {'form': form})
from oj.forms import SignInForm

def sign_in(request):
	if request.method=='GET':
		sign = SignInForm(initial={'next_url':request.GET.get('next', '/')})
		return render_to_response('login.html',{'form':sign})
	else:
		sign=SignInForm(request.POST)
		if not sign.is_valid:
			return render_to_response("register.html",{'form':sign})
		upassword=sign.cleaned_data['password']
		uname=sign.cleaned_data['username']
		user=authenticate(username=uname,password=upassword)
		if user:
			if user.is_active:
				login(request,user)
				return render_to_response(request.POST['next_url'])
			else:
				return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect('/')
from forms import LoginForm

@login_required
def log_out(request):
	logout(request)
	return HttpResponseRedirect('oj/login/')


def LoginIn(request):
	if request.method=='GET':
		form=LoginForm()
		return render_to_response('login.html',RequestContext(request,{'form':form}))
	else:
		form=LoginForm(request.POST)
		if form.is_valid:
			username=request.POST.get('username','')
			password=request.POST.get('password','')
			user=authenticate(username=username,password=password)
			if user is not None and user.is_active:
				login(request,user)
				return render_to_response('index.html',RequestContext(request,{'form':form}))
			else:
				return render_to_response('login.html',RequestContext(request,{'form':form,'password_is_wrong':True}))
		else:
			return render_to_response('login.html',RequestContext(request,{'form':form}))

@login_required			
def profile(request):
	if request=="POST":
		username=request.user.username
		profile={}
		profile['username']=username
		return render_to_response('index.html',RequestContext(request,{'profile':profile}))


from oj.forms import ChangePasswordForm
@login_required
def changpwd(request):
	if request.method=='GET':
		form=ChangePasswordForm()
		return render_to_response('changepwd.html',RequestContext(request,{'form':form}))
	else:
		form=ChangePasswordForm(request.POST)
		if form.is_valid():
			username=request.user.username
			oldpassword=request.POST.get('oldpassword','')
			user=authenticate(username=username,password=oldpassword)
			if user is not None and user.is_active:
				newpassword=request.POST.get('NewPassword','')
				user.set_password(newpassword)
				user.save()
				return render_to_response('changepwd.html',RequestContext(request,{'is_changpwd':True}))
			else:
				return render_to_response('changepwd.html',RequestContext(request,{'form':form,'oldpassword_is_wrong':True}))
		else:
			return render_to_response('changepwd.html',RequestContext(request,{'form':form}))
from oj.models import contest,contest_problem
from datetime import datetime,timedelta
def contestlist(request):
	contest_list=contest.objects.all()
	now=datetime.now()
	# for items in contest_list:
	# 	if items.start_time>now:
	# 		status
	contest_pages=Paginator(contest_list.order_by('-contest_id'),10)
	page=request.GET.get('page')
	now=datetime.now()

	try:
		contests=contest_pages.page(page)
	except PageNotAnInteger:
		contests=contest_pages.page(1)
	except EmptyPage:
		contests=contest_pages.page(paginator.num_pages)
	return render_to_response("contestlist.html",RequestContext(request,{"contests":contests,"now":now}))
from string import letters

# class user_contest(object):
# 	"""docstring for user_contest"""
# 	def __init__(self, arg):
# 		super(user_contest, self).__init__()
# 		self.arg = arg
# 	int solved
# 	int penalty
# 	int submit
class user_contest(object):
	pass

def _cmp(u1, u2):
    if u1.solved < u2.solved:
        return 1
    elif u1.solved == u2.solved:
        if u1.penalty > u2.penalty:
            return 1
        else:
            return -1
    else:
        return -1

	
from oj.models import Contestant
def contest_show(request,id):
	try:
		contests=contest.objects.get(contest_id=id)		
	except:
		raise Http404
	problems_id=contest_problem.objects.filter(contest_id=id).order_by('num')
	total=problems_id.count()
	alpha=[]
	for i in range(total):
		
		alpha.append(str(65+i))
	problems=[]
	now=datetime.now()
	flag=False
	if(now<contests.start_time):
		flag=False;
	else:
		flag=True
	for pro in problems_id:
		try:
			xx=problem.objects.get(problem_id=pro.problem_id)
			problems.append(xx)
		except:
			raise Http404

	status_list=solution.objects.all()
	status_list=status_list.filter(contest_id=contests.contest_id)
	#standing implent
	# users=[status.user_id	for status in status_list]
	# users=set(users)
	# contest_user_list=[]
	# for i in users:
	# 	if not i in contest_user_list:
	# 		contest_user_list.append(i)
	cts = Contestant.objects.filter(contest_id=id)
	print cts
    # users = set([ct.user for ct in cts]) //so terrible bug!!!
 	users=[ct.user for ct in cts]
	for u in users:
		# x=u
		# u=user_contest()
		# u.username=x
		u.solved= 0
		u.penalty=datetime.now()-datetime.now()
		submit=[]
		for problemx in problems:
			if status_list.filter(user_id=u).filter(problem_id=problemx.problem_id).filter(result=4).exists():
				actime=status_list.filter(user_id=u).filter(problem_id=problemx.problem_id).filter(result=4).order_by('solution_id')[0].in_date
				actime=actime-contests.start_time
				u.solved+=1
				u.penalty+=actime
			else:
				actime=None
			trytime=status_list.filter(user_id=u).filter(problem_id=problemx.problem_id).exclude(result=4).count()
			u.penalty+=timedelta(minutes=trytime*20)
			submit.append((actime,trytime))#actime is the timeof ac trytime is the timesof submit
			u.submit=submit
		

	users.sort(cmp=_cmp)
	return render_to_response("contest.html",RequestContext(request,{"contest":contests,"problems":problems,"letters":letters,"now":now,"statuses":status_list,"standing":users,"flag":flag}))
from oj.forms import submitForm
@login_required
def submit(request,):
	pid=1000
	if request.GET.get('pid'):
		pid=request.GET.get('pid')
	if request.method=='POST':
		f=submitForm(request.POST)
		if f.is_valid():
			pid=f.cleaned_data['problem_id']
			try:
				p=problem.objects.get(problem_id=pid)	
			except:
				pid=1000
				f=submitForm(initial={'problem_id':pid})
				HttpResponseRedirect('/oj/submit')
				return render_to_response("submit.html",RequestContext(request,{"form":f,"pid":pid}))
			s=solution()
			code=source_code()
			x=solution.objects.order_by('-solution_id')[0].solution_id+1
			s.solution_id=x
			s.problem_id=pid
			s.user_id=request.user.username
			s.time=0
			s.memory=0
			s.in_date=datetime.now()
			s.result=0
			s.language=f.cleaned_data['lang']
			s.code_length=len(f.cleaned_data['code'])
			code.source=f.cleaned_data['code']
			code.solution_id=x
			s.valid=1
			s.num=-1
			s.judgetime=datetime.now()
			s.pass_rate=0.0
			s.save()
			code.save()
			return HttpResponseRedirect('/oj/status')
			return render_to_response("submit.html",RequestContext(request,{"form":f,"pid":pid}))
		else:
			return HttpResponseRedirect('/oj/submit')
	else:
		try:
			p=problem.objects.get(problem_id=pid)
		except:
			p=problem.objects.get(problem_id=1000)
		f=submitForm(initial={'problem_id':p.problem_id})
		return render_to_response('submit.html',RequestContext(request,{'form':f,"pid":pid}))


		
		
# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#         	u=User()
#         	u.username=form.cleaned_data['username']
#         	upwd=form.cleaned_data['password']
#         	u.set_password(upwd)
#         	u.eamil=form.cleaned_data['email']
#         	u.save()
#         	uinfo=users()
#         	uinfo.user=u
#         	uinfo.team=form.cleaned_data['team']
#         	uinfo.nickname=form.cleaned_data['nickname']
#         	uinfo.motto=form.cleaned_data['motto']
#         	uinfo.realname=form.cleaned_data['realname']
#         	uinfo.studentid=form.cleaned_data['studentid']
#         	uinfo.save()
#         	u=authenticate(username=u.username,password=upwd)
#         	login(request,u)
#         	return HttpResponseRedirect('/')

#             # new_user = form.save()
#             # return HttpResponseRedirect("/oj/")
#     else:
#         form = RegisterForm()
#     return render_to_response("register.html", {'form': form})
from oj.models import source_code
def code_show(request,id):
	try:
		code=source_code.objects.get(solution_id=id)
	except:
		raise Http404
	info=solution.objects.get(solution_id=id)
	return render_to_response("code.html",RequestContext(request,{"code":code,"solution":info}))


def index(request):
	return render_to_response("index.html",RequestContext(request));


def ranklist(request):
	ranklist=users.objects.all().order_by("-score1",'-solved','submit')
	ranklist_pages=Paginator(ranklist,25)
	page=request.GET.get('page')
	try:
		ranks=ranklist_pages.page(page)
	except PageNotAnInteger:
		ranks=ranklist_pages.page(1)
	except EmptyPage:
		ranks=ranklist_pages.page(paginator.num_pages)
	return render_to_response('ranklist.html',RequestContext(request,{'ranks':ranks}))
from oj.models import article
def userdetail(request,user_id):
	try:
		u=User.objects.get(username=user_id)
		u2=users.objects.get(user=u)
	except User.DoesNotExist:
		raise Http404
	solved_list=solution.objects.filter(user_id=user_id).filter(result=4).values('problem_id').distinct().all()
	article_list=article.objects.all().filter(user_id=u).order_by("-time")
	problem_list=problem.objects.values('problem_id').all()
	return  render_to_response('userdetail.html',RequestContext(request,{"solved_list":solved_list,'problem_list':problem_list,"userdetail":u,"uinfo":u2,"article_list":article_list}))
def update(request):
	s=solution()
	s.result=-1
	if request.method=="POST":
		sid=request.POST.get("sid")
	
		s=solution.objects.get(solution_id=sid)
		

	else:
		solution_id=request.GET.get("sid")
		try:
			s=solution.objects.all().filter(solution_id=sid)
		except:
			s.result=-3
	return render_to_response("update.html",RequestContext(request,{"result":s.result}))

def new_blog(request):
	return render_to_response("newblog.html",RequestContext(request))