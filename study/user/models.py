from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManger(BaseUserManager):
    use_in_migrations = True

    def create_user(self, userID, password):
        user = self.model(
            userID = userID
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, userID, password):
        superuser = self.create_user(userID = userID, password = password)
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        
        return superuser
    
    
class User(AbstractBaseUser, PermissionsMixin):
    userID = models.CharField(max_length=50, unique = True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def is_staff(self):
        return self.is_admin
    
    objects = UserManger()

    USERNAME_FIELD = 'userID'

    class Meta:
        db_table = 'user'
