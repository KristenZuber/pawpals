from django.shortcuts import render
from.models import Review, Dog, Bunnie, Cat
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
ListView,
DetailView,
CreateView,
UpdateView,
DeleteView)

# Create your views here.
class DogListView(ListView):
    model = Dog
    template_name = 'pawpals/dogs.html'
    context_object_name = 'dogs'

class BunnyListView(ListView):
    model = Bunnie
    template_name = 'pawpals/bunnies.html'
    context_object_name = 'bunnies'

class CatListView(ListView):
    model = Cat
    template_name = 'pawpals/cats.html'
    context_object_name = 'cats'

class ReviewListView(ListView):
    model = Review
    template_name = 'pawpals/reviews.html'
    context_object_name = 'reviews'
    ordering = ['-date']

class ReviewDetailView(DetailView):
    model = Review

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['title', 'content']
    success_url = '/reviews/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['title', 'content']
    success_url = '/reviews/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True
        return False

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = '/reviews/'

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True
        return False

def home(request):
    return render(request, 'pawpals/home.html')

def dogs(request):
    context = {
        'dogs': Dog.objects.all()
    }
    return render(request, 'pawpals/dogs.html', context)
    # return render(request, 'pawpals/dogs.html', {'title': 'Dogs'})

def cats(request):
    context = {
        'cats': Cat.objects.all()
    }
    return render(request, 'pawpals/cats.html', context)

def bunnies(request):
    context = {
        'bunnies': Bunnie.objects.all()
    }
    return render(request, 'pawpals/bunnies.html', context)

def review(request):
    context = {
        'reviews': Review.objects.all()
    }
    return render(request, 'pawpals/reviews.html', context)
