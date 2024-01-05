from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomeRequestHandler(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
    redirect_field_name = "redirect_to"


class UserRequestHandler(LoginRequiredMixin, TemplateView):
    template_name = "account/profile.html"
