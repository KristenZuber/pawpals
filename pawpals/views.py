from django.shortcuts import render
from.models import Review, Dog, Bunnie, Cat
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
ListView,
DetailView,
CreateView,
UpdateView,
DeleteView)

# Allows users to see dogs in a list format
class DogListView(ListView):
    model = Dog
    template_name = 'pawpals/dogs.html'
    context_object_name = 'dogs'

# Allows users to see Bunnies in a list format
class BunnyListView(ListView):
    model = Bunnie
    template_name = 'pawpals/bunnies.html'
    context_object_name = 'bunnies'

# Allows users to see cats in a list format
class CatListView(ListView):
    model = Cat
    template_name = 'pawpals/cats.html'
    context_object_name = 'cats'

# Allows users to see reviews in a list format
class ReviewListView(ListView):
    model = Review
    template_name = 'pawpals/reviews.html'
    context_object_name = 'reviews'
    ordering = ['-date']

# Allows users to click on individual reviews
class ReviewDetailView(DetailView):
    model = Review

# Allows users to create reviews
class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['title', 'content']
    success_url = '/reviews/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Allows users to update reviews (only if they wrote them)
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

# Allows users to delete reviews (only if they wrote them)
class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = '/reviews/'

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True
        return False

# Home
def home(request):
    return render(request, 'pawpals/home.html')

# Grabs all dog objects
def dogs(request):
    context = {
        'dogs': Dog.objects.all()
    }
    return render(request, 'pawpals/dogs.html', context)

# Grabs all cat objects
def cats(request):
    context = {
        'cats': Cat.objects.all()
    }
    return render(request, 'pawpals/cats.html', context)

# Grabs all bunny objects
def bunnies(request):
    context = {
        'bunnies': Bunnie.objects.all()
    }
    return render(request, 'pawpals/bunnies.html', context)

# Grabs all review objects
def review(request):
    context = {
        'reviews': Review.objects.all()
    }
    return render(request, 'pawpals/reviews.html', context)
