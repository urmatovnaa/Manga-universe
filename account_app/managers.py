from django.contrib.auth.base_user import BaseUserManager


class MyAccountManager(BaseUserManager):
    """
       Custom user model manager where email is the unique identifiers
       for authentication instead of usernames.
    """
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def get_default_profile_image():
    return "default/default_profile_image.jpeg"

