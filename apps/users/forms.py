from django.contrib.auth import get_user_model, forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
#from django.core.files.images import get_image_dimensions

User = get_user_model()

class AvatarFormMixin(object):

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        try:
            #w, h = get_image_dimensions(avatar)

            #validate dimensions
            #max_width = max_height = 100
            #if w > max_width or h > max_height:
            #    raise forms.ValidationError(
            #        f'Please use an image that is {max_width} x {max_height} pixels or smaller.'
            #    )

            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'jpg', 'gif', 'png']):
                raise forms.ValidationError(
                    f'Please use a JPEG, GIF or PNG image.'
                )

            #validate file size
            if len(avatar) > (200 * 1024):
                raise forms.ValidationError(
                    f'Avatar file size may not exceed 200k.'
                )

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar


class UserChangeForm(AvatarFormMixin, forms.UserChangeForm):

    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(AvatarFormMixin, forms.UserCreationForm):

    error_message = forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])