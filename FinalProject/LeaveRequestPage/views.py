from django.shortcuts import render

# Create your views here.

def leave_request(request):
    return render(request, 'LeaveRequestPage.html')
