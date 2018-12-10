from django.http import HttpResponse
from django.shortcuts import render,  redirect
import spur
from . import ssh_run



def index(request):
    return render(request, 'django_ssh_public/index.html')


def server_information(request):

    if request.method == 'POST':

        try:
            ip_address = request.POST.get('ip_address')
            username = request.POST.get('username')
            password = request.POST.get('password')

            ssh_output_header, ssh_output_values = ssh_run.ssh_get(ip_address, username, password)

            return render(request, 'django_ssh_public/ssh_info.html', context = { 'header': ssh_output_header[0], 'values': ssh_output_values })
        except:
            print("ERROR ---------------> CHECK LOGS")
            return render(request, 'django_ssh_public/ssh_info_error.html')

    return redirect('/home/')
    