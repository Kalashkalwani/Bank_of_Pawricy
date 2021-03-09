from django.shortcuts import render,redirect
from django.http import HttpResponse
from bank.models import Accounts,Transactions
from datetime import datetime
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request,"index.html")


def transaction(request):
    trans = Transactions.objects.all().order_by('-sno')
    params = {"trans":trans}
    return render(request,"transaction.html",params)

def newtransaction(request):
    acc = Accounts.objects.all()
    params = {"acc":acc}

    if request.method == "POST":
        sender = request.POST.get("sender")
        receiver = request.POST.get("receiver")
        Amount = request.POST.get("Amount")
        status = False

        if int(sender) > 0 and int(receiver) > 0:
            sender_acc = Accounts.objects.get(sno = sender)
            receiver_acc = Accounts.objects.get(sno = receiver)
            if float(sender_acc.Balance) > float(Amount): 
                sender_acc.Balance = float(sender_acc.Balance) - float(Amount)
                receiver_acc.Balance = float(receiver_acc.Balance) + float(Amount)
                sender_acc.save()
                receiver_acc.save()
                status = True
                t = Transactions(sender_acc =sender_acc,receiver_acc=receiver_acc,Amount=Amount,status=status,date=datetime.now() )
                t.save()
                return redirect("/transaction")
            
            else:
                messages.info(request, 'Insufficient Balance ')
                t = Transactions(sender_acc =sender_acc,receiver_acc=receiver_acc,Amount=Amount,status=status,date=datetime.now() )
                t.save()
                return render(request,"newtransaction.html",params)
            
        elif int(sender) == 0 and int(receiver):
            messages.warning(request, 'Enter Sender ')

        elif int(receiver) == 0 and int(sender):
            messages.warning(request, 'Enter Receiver ')
            
        else:
            messages.warning(request, 'Enter Correct users ')
      

    return render(request,"newtransaction.html",params)


def transfer(request,x):
    x  = Accounts.objects.get(sno=x)
    acc = Accounts.objects.all()
    params = {"acc":acc,"x":x}
    return render(request,"newtransaction.html",params)


def accounts(request):
    acc = Accounts.objects.all()
    params = {"acc":acc}

    if request.method == "POST":
        x = request.POST.get("transfer")
        return redirect("/transfer_"+x)
    return render(request,"account.html",params)