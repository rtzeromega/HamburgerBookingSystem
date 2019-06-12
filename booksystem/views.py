from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Create, Store, Cart, Like
from .forms import UserForm,CreateForm, StoreForm, CartForm, LikeForm
from django.http import HttpResponseRedirect

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def index(request):
    return render(request, 'booksystem/index.html')


# 登录
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None:  # 登录成功
            if user.is_active:  # 加载订票页面
                login(request, user)
                context = {'username': request.user.username}
                return render(request, 'booksystem/buy.html', context)
            else:
                return render(request, 'booksystem/login.html', {'error_message': 'Your account has been disabled'})
        else:  # 登录失败
            return render(request, 'booksystem/login.html', {'error_message': 'Invalid login'})
    return render(request, 'booksystem/login.html')


# 退出登录
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {"form": form}
    return render(request, 'booksystem/login.html', context)


# 注册
def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                context = {'username': request.user.username}
                return render(request, 'booksystem/buy.html', context)  # 注册成功直接render buy页面
    context = {"form": form}
    return render(request, 'booksystem/register.html', context)


def user_info(request):
    if not request.user.is_authenticated():
        return render(request, 'booksystem/login.html')
    else:
        my_cart = Cart.objects.filter(user=request.user)
        my_like = Like.objects.filter(user=request.user)
        create_result = Create.objects.filter(user=request.user)
        return render(request, 'booksystem/user_info.html', {
            'username': request.user.username,
            'create_result': create_result,
            'my_cart': my_cart,
            'my_like': my_like})


def buy(request):
    if not request.user.is_authenticated():
        return render(request, 'booksystem/login.html')
    else:
        store_result = Store.objects.all()
        create_result = Create.objects.all()
        return render(request, 'booksystem/buy.html', {
            'username': request.user.username,
            'store_result': store_result,
            'create_result': create_result})


def detail(request, store_id):
    if not request.user.is_authenticated():
        return render(request, 'booksystem/login.html')
    else:
        store = get_object_or_404(Store, pk=store_id)
        form = LikeForm(request.POST or None)
        if form.is_valid():
            like = form.save(commit=False)
            like.user = request.user
            like.food = store
            like.comment = form.cleaned_data['comment']
            like.save()
        like_result = Like.objects.filter(food=store)
        return render(request, 'booksystem/detail.html', {
            'store': store,
            'like_result':like_result,
            'form':form,
            'username': request.user.username})


def book(request, store_id):
    store = Store.objects.get(pk=store_id)
    store.quantity -= 1
    store.save()
    cart = Cart(user=request.user, food=store) # 存储数据
    cart.save()
    return HttpResponseRedirect('/booksystem/buy')


def refund(request, cart_id):
    cart = Cart.objects.get(pk=cart_id)
    store = Store.objects.get(pk=cart.food_id)
    store.quantity += 1
    store.save()
    cart.save()
    cart.delete()
    return HttpResponseRedirect('/booksystem/user_info')


def refund_like(request, like_id):
    like = Like.objects.get(pk=like_id)
    like.save()
    like.delete()
    return HttpResponseRedirect('/booksystem/user_info')


def create(request):
    if not request.user.is_authenticated():
        return render(request, 'booksystem/login.html')
    else:
        form = CreateForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            create = form.save(commit=False)
            create.user = request.user
            create.create_logo = request.FILES['create_logo']
            file_type = create.create_logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'create': create,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'booksystem/create.html', context)
            create.save()
            return render(request, 'booksystem/buy.html')
        context = {
            "form": form,
        }
        return render(request, 'booksystem/create.html', context)


def delete(request, create_id):
    create = Create.objects.get(pk=create_id)
    create.delete()
    create_result = Create.objects.filter(user=request.user)
    return render(request, 'booksystem/user_info.html', {'create_result': create_result})