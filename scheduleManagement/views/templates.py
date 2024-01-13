from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomeRequestHandler(LoginRequiredMixin, TemplateView):
    template_name = "home.html"


class UserRequestHandler(LoginRequiredMixin, TemplateView):
    template_name = "account/profile.html"
