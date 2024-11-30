from django.shortcuts import render, redirect
from .models import Member, Program
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import ContactForm, JoinRequestForm




def sports(request):
    return render(request, 'club/sports.html')


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return HttpResponse(f"Thank you {name}, we have received your message.")
    else:
        form = ContactForm()

    return render(request, 'club/contact_us.html', {'form': form})


def home(request):
    return render(request, 'club/home.html')


@login_required
def dashboard(request):
    members = Member.objects.all()  # Fetch all members
    recent_members = members.order_by('-id')[:5]  # Fetch the 5 most recent members
    context = {
        'members': members,
        'recent_members': recent_members,
        'club_accounts': "Details about club accounts (to be updated)",
        'management_team': "Details about management team (to be updated)",
    }
    return render(request, 'club/dashboard.html', context)


def register(request):
    if request.method == 'POST':
        form = JoinRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JoinRequestForm()

    return render(request, 'club/register.html', {'form': form})


def member_list(request):
    members = Member.objects.all()
    paginator = Paginator(members, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'club/member_list.html', {'page_obj': page_obj})


def program_list(request):
    return render(request, 'club/program_list.html')


