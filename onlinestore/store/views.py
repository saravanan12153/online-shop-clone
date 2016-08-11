from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.template import RequestContext

# Create your views here.
from models import Store, Product
from forms import RegistrationForm, LoginForm, StoreForm, ProductForm


class IndexView(TemplateView):
    """Landing page view."""

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """Return dictionary representing passed in context."""
        context = super(IndexView, self).get_context_data(**kwargs)
        context['registrationform'] = RegistrationForm()
        context['loginform'] = LoginForm()
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
                '/stores/',
                context_instance=RequestContext(request)
            )
        else:
            messages.error(
                request, 'Incorrect username or password.')
            return redirect(
                '/login',
                context_instance=RequestContext(request)
            )


class AddStore(TemplateView):
    """View for creation on a new store and viewing all stores."""

    template_name = 'stores.html'
    form_class = StoreForm

    def get_context_data(self, **kwargs):
        """Return dictionary representing passed in context."""
        context = super(AddStore, self).get_context_data(**kwargs)
        context['stores'] = Store.objects.all()
        context['username'] = self.request.user.username
        context['addstoreform'] = StoreForm()
        return context

    def post(self, request, **kwargs):
        """Method for creation of new store."""
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            new_store = form.save(commit=False)
            new_store.owner = self.request.user
            new_store.save()
            messages.success(
                request, 'New Store added successfully!')
            return redirect(
                '/stores/',
                context_instance=RequestContext(request)
            )
        else:
            messages.error(
                request, 'Error at creation!')
            return redirect(
                '/stores/',
                context_instance=RequestContext(request)
            )


class StoreEditsView(TemplateView):
    """Handle edition of stores created."""

    def post(self, request, **kwargs):
        store = Store.objects.filter(id=kwargs['pk'],
                                     owner=self.request.user).first()
        store.store_name = request.POST.get('name')
        store.picture = request.POST.get('picture')
        store.save()
        messages.success(request, 'Store name successfully updated.')
        return redirect(
            '/stores/',
            context_instance=RequestContext(request))


class StoreDeleteView(TemplateView):
    """Handle store deletion."""

    def get(self, request, **kwargs):
        """Handle store deletion."""
        store = Store.objects.filter(id=kwargs['pk']).first()
        store.delete()
        messages.success(request, 'Store deleted.')
        return redirect(
            '/stores/',
            context_instance=RequestContext(request))


class ProductsView(TemplateView):
    """View for addition and viewing all products in a store."""

    template_name = 'products.html'
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        """Pass in data in a dictionary to the template view."""
        context = super(ProductsView, self).get_context_data(**kwargs)
        context['store'] = Store.objects.get(id=kwargs['pk'])
        context['products'] = Product.objects.filter(store=kwargs['pk'])
        context['productform'] = ProductForm()
        return context

    def post(self, request, **kwargs):
        """Handle creation of a new product."""
        form = self.form_class(request.POST, request.FILES)
        store = Store.objects.get(id=kwargs['pk'])
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.store = store
            new_product.save()
            messages.success(request, 'Product successfully added.')
            return redirect(
                '/stores/' + kwargs['pk'] + '/products/',
                context_instance=RequestContext(request))
        else:
            messages.error(
                request, 'Something went wrong. :-(')
            return redirect(
                '/stores/' + kwargs['pk'] + '/products/',
                context_instance=RequestContext(request))


class ProductEditsView(TemplateView):
    """Handle edition of stores created."""

    def post(self, request, **kwargs):
        product = Product.objects.filter(
            id=kwargs['pk'], store=kwargs['store_id']).first()
        product.product_name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.picture = request.POST.get('picture')
        product.save()
        messages.success(request, 'Product name successfully updated.')
        return redirect(
            '/stores/' + kwargs['store_id'] + '/products/',
            context_instance=RequestContext(request))


class ProductDeleteView(TemplateView):
    """Handle product deletion."""

    def get(self, request, **kwargs):
        """Handle product deletion."""
        product = Product.objects.filter(
            id=kwargs['pk'], store=kwargs['store_id']).first()
        product.delete()
        messages.success(request, 'Store deleted.')
        return redirect(
            '/stores/' + kwargs['store_id'] + '/products/',
            context_instance=RequestContext(request))


def logout(request):
    """Log user out of the system."""
    auth_logout(request)
    return redirect('/')
