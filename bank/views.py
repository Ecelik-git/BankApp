from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Customer_Info


def home(request):
    return render(request, 'bank/home.html', {'title': 'home'})

class PostListView(ListView):
    model = Customer_Info
    template_name = 'bank/customer_page.html'
    context_object_name = 'customers'


    def get_queryset(self):
        return Customer_Info.objects.order_by('name')

class PostDetailView(DetailView):
    model = Customer_Info

    def customer_page(request):
        context = {
            'customers': Customer_Info.objects.all()
        }
        return render(request, 'bank/customer_page.html', {'title': 'Customer Detail'}, context)
def view(request):
    return render(request, "bank/customer_page.html", {'title': 'Customer Detail'})

class PostCreateView(CreateView):
    model = Customer_Info
    fields = ['name', 'lastname']

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Customer_Info
    fields = ['balance']

    def form_valid(self, form):
        form.instance.people = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.people:
            return True
        return False

def about(request):
    return render(request, 'bank/about.html', {'title': 'about'})

#username:hsteel email: hsteeltx@gmail.com, pass:hsteel12