from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
class RegisterView(CreateView):
    template_name = "users/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["username"].widget.attrs.update(
            {
                "class": "block text-gray-700 text-sm font-bold mb-2 w-full p-2 border border-gray-300 rounded"
            }
        )
        form.fields["password1"].widget.attrs.update(
            {
                "class": "block text-gray-700 text-sm font-bold mb-2 w-full p-2 border border-gray-300 rounded"
            }
        )
        form.fields["password2"].widget.attrs.update(
            {
                "class": "block text-gray-700 text-sm font-bold mb-2 w-full p-2 border border-gray-300 rounded"
            }
        )
        return form
