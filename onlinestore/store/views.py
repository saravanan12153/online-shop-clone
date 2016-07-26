# from django.shortcuts import render
from django.views.generic import TemplateView
# from django.template import RequestContext

# Create your views here.
# from models import Store, Product
from forms import RegistrationForm


class IndexView(TemplateView):
    """Landing page view."""

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """Return dictionary representing passed in context."""
        context = super(IndexView, self).get_context_data(**kwargs)
        context['registrationform'] = RegistrationForm()
        # context['loginform'] = LoginForm()
        return context


