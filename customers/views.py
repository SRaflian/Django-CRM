from django.shortcuts import render, get_object_or_404, redirect
from .models import Record
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddRecordForm
from django.urls import reverse


# Create your views here.
@login_required
def Record_dashboard(request):
    records = Record.objects.all()  # Fetch all records from the database
    return render(request, 'customers/record-dashboard.html', {'records': records})

@login_required
def customer_record_view(request, id):
    record = get_object_or_404(Record, id=id)
    return render(request, 'customers/record/individual-record.html', {'record': record})

@login_required
def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				form.save()
				messages.success(request, "Record Added...")
				return redirect(reverse('record-dashboard'))
		return render(request, 'customers/add-record.html', {'form':form})

@login_required
def delete_record(request, id):
    if request.method == "POST":
        record = get_object_or_404(Record, id=id)
        record.delete()
        messages.success(request, "Record successfully deleted.")
        return redirect('record-dashboard')
    


