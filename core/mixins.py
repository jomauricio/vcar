from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class LoginRequiredAndIsOwnerMixin(LoginRequiredMixin, UserPassesTestMixin):
    owner_user_field = 'user'

    def test_func(self):
        user = getattr(self.get_object(), self.owner_user_field)
        return self.request.user == user
