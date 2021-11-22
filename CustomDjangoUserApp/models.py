from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

## UserManager - used to control the creation of new users 
class UserManager(BaseUserManager):

    # Main function to create new users
    def create_user(self, email, password = None):
        if not email:
            raise ValueError('Users require an email.')
         
        user = self.model(
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    # function used to create new users with staff permissions
    def create_staffuser(self, email, password):

        user = self.create_user(
            email = email,
            password = password
        )
    
        user.staff = True
        user.save(using = self._db)
        return user

    # function used to create new users with admin level permissions
    def create_superuser(self, email, password):

        user = self.create_user(
            email = email,
            password = password,
        )
    
        user.staff = True
        user.admin = True
        user.save(using = self._db)
        return user

## User - custom model replacing the default Django User Model
class User(AbstractBaseUser):

    objects = UserManager()

    is_active = models.BooleanField(default = True)
    staff = models.BooleanField(default = False)
    admin = models.BooleanField(default = False)

    # Main fields to be used in the model
    email = models.EmailField(max_length = 255, blank = False, null = True, unique = True)

    # optional fields 


    # Modifying the behaviour of how the User model will work (compared to default)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [

    ]

    ## Setting up the functionality for within the django admin panel 
    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    # how the user will be referred to within the main listing page of users
    def __str__(self):
        return self.email
        
    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
