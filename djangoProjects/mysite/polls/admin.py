
from django.contrib import admin
from polls.models import Poll,Choice, AdminPosts,UserPosts


class ChoiceInline(admin.StackedInline):
	model=Choice
	extra=3


class Poll_Admin(admin.ModelAdmin):
	fieldsets=[
			(None, {'fields': ['question']}),
			('Date information',{'fields': ['pub_date'], 'classes': ['collapse']}),
		  ]
	inlines=[ChoiceInline]
	list_display=('question','pub_date','display')
	list_filter=['pub_date']
	search_fields=['question']
	

class Admin_Posts(admin.ModelAdmin):
	fieldsets=[
			(None, {'fields':['subject']}),
			(None,{'fields':['post']}),
			('Date information',{'fields':['pub_date'],'classes':['collapse']}),
		  ]
	list_display=('subject','post','pub_date')
	list_filter=['pub_date']
	search_fields=['subject']

class User_Posts(admin.ModelAdmin):
	fieldsets=[
			(None, {'fields':['subject']}),
			(None,{'fields':['post']}),
			('Date information',{'fields':['pub_date']}),
			('User',{'fields':['username']})
		  ]

	list_display=('subject','post','username','pub_date')
	list_filter=['pub_date']
	search_fields=['subject']


admin.site.register(UserPosts,User_Posts)
admin.site.register(AdminPosts,Admin_Posts)
admin.site.register(Poll,Poll_Admin) 


