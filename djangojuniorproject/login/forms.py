from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password1',
            'password2',
        ]

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get("username")

        try:
            User.objects.get(username=username.lower())
        except ObjectDoesNotExist:
            pass
        else:
            self.add_error("username", "This username exists. Please, choose another one")

        return cleaned_data
