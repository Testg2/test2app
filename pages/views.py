from django.shortcuts import render, get_object_or_404, redirect

from .models import Contact

# this is for to search multiple items
from django.db.models import Q

# using class based views | 2 types - list view and details view | we can use in django is by importing
# listview is use in index page | detail view is use in about page

from django.views.generic import ListView, DetailView


# for multiple search
from django.db.models import Q

# using generic class base view to create contact
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# create new user
from django.contrib.auth.forms import UserCreationForm
#
from django.urls import reverse_lazy

############# both allows user to login than use functionality ################

# for class based views
from django.contrib.auth.mixins import LoginRequiredMixin

# for method based views ( )
from django.contrib.auth.decorators import login_required


# using this message we can actually send message to templates
from django.contrib import messages


# ---------------------------------- function base view ----------------------------------

# Create your views here.
# def index(request):
#
#     all_contacts = Contact.objects.all()
#
#     context = {
#         'contacts': all_contacts
#     }
#     return render(request, 'pages/index.html', context)
#

#
# def about(request, id):
#
#     context = {
#         'contact': get_object_or_404(Contact, pk=id)
#     }
#
#     return render(request, 'pages/about.html', context)

@login_required
def search(request):

    if request.GET:
        store_search_items = request.GET['items']

        # search_results = Contact.objects.filter(name__icontains=store_search_items)

        search_results = Contact.objects.filter(
            Q(username__icontains=store_search_items) |
            Q(email__icontains=store_search_items) |
            Q(text_message__icontains=store_search_items) |
            Q(gender__icontains=store_search_items) |
            Q(phone__iexact=store_search_items)
        )

        context = {
            'store_search_items': store_search_items,
            'search_results': search_results.filter(manager=request.user),
        }

        return render(request, 'pages/search.html', context)
    else:
        return redirect('index')
# ---------------------------------- class base view ---------------------------------- #

class IndexListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = "pages/index.html"
    context_object_name = 'contacts'

    # it returns objects for all list of all contacts
    def get_queryset(self):
        # get all querysets and store in contacts variable
        contacts = super().get_queryset()
        return contacts.filter(manager=self.request.user)

# passing primary key directly in urls as pk
class AboutDetailView(LoginRequiredMixin, DetailView):
    model = Contact
    template_name = "pages/about.html"
    context_object_name = 'contact'

class AddNewView(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = "pages/add.html"
    fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'gender']
    # success_url = '/'

    # save value and redirect to individual page
    def form_valid( self, form):
        # not save n database
        instence = form.save(commit=False)
        instence.manager = self.request.user
        instence.save()

        # display success
        messages.success(self.request, 'Your Contact has been successfully created')

        return redirect('index')

class UpdateDetailView(LoginRequiredMixin, UpdateView):
    model = Contact
    template_name = "pages/update.html"
    fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'gender']
    success_url = '/'

    # save value and redirect to individual page
    def form_valid(self, form):
        instence = form.save()

        # display success
        messages.success(self.request, 'Your Contact has been successfully Updated')

        return redirect('about', instence.pk)


class DeleteDetailView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = 'pages/delete.html'
    success_url = '/'

    # this args and kwargs are use to pass additional argument
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Your contact has been successfully deleted')
        return super().delete(self, request, *args, **kwargs)


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('index')