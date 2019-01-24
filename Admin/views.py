from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def admin_portal(request):
	return render(request,'Admin/admin_portal.html')

