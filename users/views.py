from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from.forms import UserRegistrationForm, UserUpdateForm, UserApplyForm
from django.contrib.auth.decorators import login_required
from.models import Apply

# Allows users to register,
# and gives a success message if they successfully registered
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created!')
            return redirect('pawpals-home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

#Allows users to update their profile only if they are logged in
@login_required
def profile(request):
    u_form = UserUpdateForm()

    context = {
        'u_form': u_form
    }
    return render(request, 'users/profile.html', context)

#Allows users to submit an application only if they are logged in.
# Otherwise, they are redirected to the log in page
@login_required
def apply(request):
    form = UserApplyForm(request.POST)
    if form.is_valid():
        form.save()
        first_name = form.cleaned_data.get('first_name')
        messages.success(request, f'Thanks for applying { first_name }!')
        return redirect('pawpals-home')
    else:
        form = UserApplyForm()
    return render(request, 'users/apply.html', {'form': form})
