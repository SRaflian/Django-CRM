from .models import Record

def total_customers_context(request):
    total_count = Record.objects.count()
    return {'total_count': total_count}

def unique_states_count(request):
    # This line will give you a count of unique states.
    unique_states = Record.objects.values('state').distinct().count()
    return {'unique_states_count': unique_states}