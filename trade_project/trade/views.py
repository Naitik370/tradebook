from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Trade
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm, TradeForm

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', { 'form': form})   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('trade_list')
        else:
            return render(request, 'register.html', {'form': form})

def login_view(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('trade_list')
        
        form = LoginForm()
        return render(request,'login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                return redirect('trade_list')
        
        # either form not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'login.html',{'form': form})

def logout_view(request):
    logout(request)
    return redirect("login")
# trade/views.py (continued)


@login_required
def trade_list(request):
    trades = Trade.objects.filter(user=request.user)
    return render(request, "trade_list.html", {"trades": trades})

@login_required
def add_trade(request):
    if request.method == 'GET':
        trade = TradeForm()
        return render(request,'add_trade.html', {'trade': trade})
    if request.method == "POST":
        Ticker = request.POST["Ticker"]
        Quantity = request.POST["Quantity"]
        Entry = request.POST["Entry"]
        Exit = request.POST["Exit"]
        Date = request.POST["Date"]
        Trade.objects.create(user=request.user, Ticker=Ticker,Quantity=Quantity,Entry=Entry,Exit=Exit,Date=Date)
        return redirect("trade_list")
    return render(request, "add_trade.html")

