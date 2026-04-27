from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from blog.models import *
from . models import *
import openpyxl



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created. You can now login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        try:
            if u_form.is_valid and p_form.is_valid:
                u_form.save()
                p_form.save()
                messages.success(
                    request, f"Your account has been successfully Updated!")
                return redirect("profile")
        except Exception as e:
            messages.warning(request, f"{e}")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {"u_form": u_form, "p_form": p_form}
    return render(request, "users/profile.html", context)

@login_required
def follow_user(request, *args, **kwargs):
    id = request.POST.get('post_author_profile_id')
    profile = Profile.objects.get(id=id)
    profile.followed_by.add(request.user.profile)
    profile.save()
    return redirect('blog-home')

@login_required
def unfollow_user(request, *args, **kwargs):
    id = request.POST.get('post_author_profile_id')
    profile = Profile.objects.get(id=id)
    profile.followed_by.remove(request.user.profile)
    profile.save()
    return redirect('blog-home')

@login_required
def my_feed(request):
    posts = Post.objects.all()
    profiles = request.user.profile.follows.all()
    context = {
        'posts':posts,
        'profiles':profiles
    }
    return render(request, 'users/my_feed.html', context) 

@login_required
@permission_required('GET') 
def get_data(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="profile_data.xlsx"'

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Profile Data'

    profiles = Profile.objects.all()
    row_data = [
        ['Profile ID', 'Username', 'E-mail', 'Following']
    ]
    for profile in profiles:
        following_profiles = profile.follows.all()
        followed_usernames = []
        for following_profile in following_profiles:
            followed_usernames.append(following_profile.user.username)
        followed_usernames_str = ','.join(followed_usernames)

        row = [profile.id, profile.user.username, profile.user.email, followed_usernames_str]
        row_data.append(row)

    for line in row_data:
        ws.append(line)

    wb.save(response)
    return response

@login_required
def add_subscription(request, *args, **kwargs):
    id = request.POST.get('post_author_profile_id')
    prof = Profile.objects.get(id=id)
    request.user.profile.subscription.add(prof)
    return redirect('blog-home')

@login_required
def cancel_subscription(request, *args, **kwargs):
    id = request.POST.get('post_author_profile_id')
    prof = Profile.objects.get(id=id)
    request.user.profile.subscription.remove(prof)
    return redirect('blog-home')   

