from django.shortcuts import render
from .models import Record
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Record_dashboard(request):
    records = Record.objects.all()  # Fetch all records from the database
    return render(request, 'users/record-dashboard.html', {'records': records})