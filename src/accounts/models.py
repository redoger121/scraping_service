from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import UserManager
from django.db import models



class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user






class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=True, verbose_name='Администратор')
    city= models.ForeignKey('scraping.city', on_delete=models.SET_NULL, null=True, blank=True)
    language=models.ForeignKey('scraping.language', on_delete=models.SET_NULL, null=True, blank=True)
    send_email=models.BooleanField(default=True)

    objects=MyUserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    
    class Meta:
        verbose_name='Аккаунт'
        verbose_name_plural='Аккаунты'

    def __str__(self):
        return self.email


    def has_perm(self, perm, obj=None):
        return True


    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin