from django.shortcuts import render, get_object_or_404, redirect
from .models import Record
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddRecordForm
from django.urls import reverse
from django.shortcuts import render
from django.db.models.functions import ExtractMonth
from django.db.models import Count
import datetime


# Create your views here.
@login_required
def Record_dashboard(request):
    # Fetch all records from the database
    records = Record.objects.all()

    # Assuming you want the chart for the current year
    current_year = datetime.date.today().year
    monthly_customers = Record.objects.filter(created_at__year=current_year).annotate(month=ExtractMonth('created_at')).values('month').annotate(count=Count('id')).order_by('month')

    # Prepare data for Chart.js
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    customer_counts = [0] * 12  # Initialize a list of 12 zeros for each month
    for entry in monthly_customers:
        # Subtract 1 because JavaScript months are 0-indexed but Django gives 1-indexed months
        customer_counts[entry['month'] - 1] = entry['count']

    context = {
        'records': records,
        'months': months,
        'customer_counts': customer_counts,
    }
    return render(request, 'customers/record-dashboard.html', context)


@login_required
def Record_view(request):
    records = Record.objects.all()  # Fetch all records from the database
    return render(request, 'customers/record-view.html', {'records': records})


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
				return redirect(reverse('record-view'))
		return render(request, 'customers/add-record.html', {'form': form})


@login_required
def delete_record(request, id):
    if request.method == "POST":
        record = get_object_or_404(Record, id=id)
        record.delete()
        messages.success(request, "Record successfully deleted.")
        return redirect('record-view')


@login_required
def edit_record(request, id):
    record = get_object_or_404(Record, id=id)
    if request.method == "POST":
        form = AddRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record successfully updated.")
            return redirect('record-view')
    else:
        form = AddRecordForm(instance=record)
    return render(request, 'customers/record/edit-record.html', {'form': form, 'record_id': record.id})
