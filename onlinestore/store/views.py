from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.template import RequestContext

# Create your views here.
from models import Store
from forms import RegistrationForm, LoginForm, StoreForm


class IndexView(TemplateView):
    """Landing page view."""

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """Return dictionary representing passed in context."""
        context = super(IndexView, self).get_context_data(**kwargs)
        context['registrationform'] = RegistrationForm()
        # context['loginform'] = LoginForm()
        return context


class RegistrationView(IndexView):

    form_class = RegistrationForm

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # save form data to the database
            new_user = form.save()

            # hash the password passed
            new_user.set_password(request.POST['password'])
            new_user.save()

            # authenticate new_user details and log them in
            new_user = authenticate(
                username=request.POST['username'],
                password=request.POST['password'])
            login(request, new_user)
            messages.success(
                request, "You've been successfully registered!")
            return redirect(
                '/stores',
                context_instance=RequestContext(request)
            )
        else:
            messages.error(
                request, 'Oops there was a problem on registration!')
            for error in form.errors.values():
                messages.add_message(request, messages.ERROR, error[0])
            return redirect(
                '/register',
                context_instance=RequestContext(request)
            )


class LoginView(IndexView):

    form_class = LoginForm

    def post(self, request, **kwargs):
        """Handle user login."""
        form = self.form_class(request.POST)
        if form.is_valid():
            current_user = authenticate(
                username=request.POST['username'],
                password=request.POST['password'])
            login(request, current_user)
            messages.success(
                request, 'Welcome back!!')
            return redirect(
                '/stores',
                context_instance=RequestContext(request)
            )
        else:
            messages.error(
                request, 'Incorrect username or password.')
            return redirect(
                '/login',
                context_instance=RequestContext(request)
            )


def storespage(request):
    stores = Store.objects.all()
    return render(request, 'stores.html', {'stores': stores})


def add_store(request):
    if request.method == "POST":
        form = StoreForm(request.POST)
        if form.is_valid():
            new_store = form.save(commit=False)
            new_store.owner = request.user
            new_store.save()
            return redirect('/stores')
    else:
        form = StoreForm()
    return render(request, 'stores.html', {'storeform': form})
