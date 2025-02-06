from django.db import models
from django.contrib.auth.models import AbstractUser

DEFAULT = 'profile_image/test.webp'

class User(AbstractUser):
    """    
    User model that sets the username to be the same as the email address.

    This model extends the built-in Custom ->  User model and ensures that the username field
    is set to the same value as the email field.

    Fields:
    - email: The unique email address of the user.
    - username: The username of the user (set to the email address).
    """
    bio = models.CharField('bio', max_length=255, null=True, blank=True)
    image = models.ImageField(
        'image', upload_to='profile_image/',
        default=DEFAULT,
        null=True, blank=True
    )
    email = models.EmailField("email address", blank=True, unique=True)
    
    

    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  

    def __str__(self):
        return self.username 