from django import forms
# $jresult=Array($MSG_PD,$MSG_PR,$MSG_CI,$MSG_RJ,$MSG_AC,$MSG_PE,$MSG_WA,$MSG_TLE,$MSG_MLE,$MSG_OLE,$MSG_RE,$MSG_CE,$MSG_CO,$MSG_TR);
JUDGE_RESULT_CHOICES=(
	('A','All'),
	(0,'Wating'),
	(1,'Wating Rejudge'),
	(2,'Compiling'),
	(3,'Runing'),
	(4,'Accepted'),
	(5,'Presentation Error'),
	(6,'Wrong Answer'),
	(7,'Time Limit Exceeded'),
	(8,'Memory Limit Exceeded'),
	(9,'Output Limit Exceeded'),
	(10,"Runtime Exceeded"),
	(11,'Compile Error'),
	(12,'Compile OK'),
	(13,'TestRuning'),
	)
# JUDGE_RESULT_CHOICES = (, (1, 'Accepted'), (3, 'Compile Error'), (2, 'Presentation Error'), (4,'Wrong Answer'), (5,'Memory Limit Exceeded'), (6,'Time Limit Exceeded'), (7,'Output Limit Exceeded'), (8,'Runtime Error'), (9,'Restricted Function'), (10,'Abnormal Termination'), (11,'Internal Error'))
# $language_name=Array("C","C++","Pascal","Java","Ruby","Bash","Python","PHP","Perl","C#","Obj-C","FreeBasic","Other Language");
# LANG_CHOICES=(('A','--'),('C','C'),('C++','C++'),('Java','Java'))
LANG_CHOICES=(
	('A','All'),
	(0,'C'),
	(1,'C++'),
	(2,'Pascal'),
	(3,'Java'),
	)
LANG_SUBMIT=(
	(0,'C'),
	(1,'C++'),
	(2,'Pascal'),
	(3,'Java'),
	)
class status_query(forms.Form):
	problem_id=forms.IntegerField(required=False)
	user_id=forms.CharField(max_length=32,required=False)
	lang=forms.ChoiceField(choices=LANG_CHOICES,required=False)
	result=forms.ChoiceField(choices=JUDGE_RESULT_CHOICES,required=False)

from django.contrib.auth.models import User
class RegisterForm(forms.Form):
	username=forms.CharField(label="User Name",max_length=32)
	password=forms.CharField(label="password",max_length=32 ,widget=forms.widgets.PasswordInput)
	password2=forms.CharField(label="Password Confirm",max_length=32, widget=forms.widgets.PasswordInput)
	email=forms.EmailField(label='Email',required=False)
	team=forms.CharField(label="Team")
	nickname=forms.CharField(max_length=32)
	motto=forms.CharField(max_length=120,widget=forms.Textarea)
	realname=forms.CharField(max_length=32)
	
	studentid=forms.IntegerField()
	error_messages={
	 	'duplicate_username': ("A user with that username already exists."),
        'password_mismatch': ("The two password fields didn't match."),
	}
	def clean_username(self):
		username=self.cleaned_data["username"]
		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError(self.error_messages['duplicate_username'])
	def clean_password2(self):
		password1=self.cleaned_data.get("password","")
		password2=self.cleaned_data["password2"]
		if password1!=password2:
			raise forms.ValidationError(self.error_messages['password_mismatch'])
		return password2
class SignInForm(forms.Form):
	username=forms.CharField(max_length=32)		
	password=forms.CharField(max_length=32,widget=forms.widgets.PasswordInput)
	next_url=forms.CharField(widget=forms.widgets.HiddenInput)


from bootstrap_toolkit.widgets import BootstrapDateInput,BootstrapTextInput,BootstrapUneditableInput	
class LoginForm(forms.Form):
	username=forms.CharField(
		required=False,
		label='User Name',
		error_messages={'required':'Please Input Your username'},
		widget=forms.TextInput(
			attrs={
				'placeholder':u'User ID'
			}
		),
	)
	password=forms.CharField(
		required=True,
		label=u'Password',
		error_messages={'required':'Please Input your password'},
		widget=forms.PasswordInput(
			attrs={
				'placeholder':u'Password'
			}
		),
	)
	def clean(self):
		if not self.is_valid():
			raise forms.ValidationError(u"UserName and Password Must Be Put In")
		else:
			cleaned_data=super(LoginForm,self).clean()
class submitForm(forms.Form):
	problem_id=forms.IntegerField()
	lang=forms.ChoiceField(choices=LANG_SUBMIT)
	code=forms.CharField()


class ChangePasswordForm(forms.Form):
	oldpassword=forms.CharField(
		required=True,
		label='oldpassword',
		error_messages={'required':'Please Input Old Password'},
		widget=forms.PasswordInput(
			attrs={
				'placeholder':'oldpassword'
			}
			),
		)
	NewPassword=forms.CharField(
		required=True,
		label='newpassWord',
		error_messages={'required':'Please INpput new Password'},
		widget=forms.PasswordInput(
			attrs={
			'placeholder':'please Input Password'
			}
		),
	)
	ConfirmPassword=forms.CharField(
		required=True,
		label='Confirm Password',
		error_messages={'required':'Please INput Password Again'},
		widget=forms.PasswordInput(
			attrs={
			'placeholder':'Confirm Password'
			}
		),
	)
	def clean(self):
		if not self.is_valid():
			raise forms.ValidationError('all is must be input')
		elif self.cleaned_data['NewPassword']<>self.cleaned_data['ConfirmPassword']:
			raise forms.ValidationError('Password Confirm Failed')
		else:
			cleaned_data=super(ChangePasswordForm,self).clean()



