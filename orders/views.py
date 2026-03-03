from django.shortcuts import render, redirect
from .models import GroupBuy, OrderRecord
from django.contrib.auth.decorators import login_required

def index(request):
    groupbuys = GroupBuy.objects.all()

    return render(request, 'index.html', {
        'groupbuys': groupbuys
    })
    
def groupbuy_detail(request, id):
    groupbuy = GroupBuy.objects.get(id=id)

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('/login/')

        OrderRecord.objects.create(
            user=request.user,
            groupbuy=groupbuy,
            item_name=request.POST.get("item_name"),
            note=request.POST.get("note"),
            sweetness=request.POST.get("sweetness"),
            ice=request.POST.get("ice"),
            drink_name = request.POST.get('drink_name'),
        )
        return redirect('/groupbuy/' + str(id))

    orders = OrderRecord.objects.filter(groupbuy=groupbuy)

    return render(request, 'detail.html', {
        'groupbuy': groupbuy,
        'orders': orders,
    })

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def delete_order(request, order_id):
    order = get_object_or_404(OrderRecord, id=order_id)

    #只允許本人或管理員刪除
    if request.user == order.user or request.user.is_staff:
        groupbuy_id = order.groupbuy.id
        order.delete()
        return redirect('/groupbuy/' + str(groupbuy_id))

    return redirect('/')

@login_required
def delete_groupbuy(request, id):
    groupbuy = get_object_or_404(GroupBuy, id=id)

    if request.user.is_staff:
        groupbuy.delete()
        return redirect('/')

    return redirect('/')\

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def create_groupbuy(request):
    if request.method == "POST":
        GroupBuy.objects.create(
            owner=request.user,
            title=request.POST.get("title"),
            drink_mode=request.POST.get("drink_mode") == "on"
        )
        return redirect('/')

    return render(request, "create_groupbuy.html")