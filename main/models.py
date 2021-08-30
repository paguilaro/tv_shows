from django.db import models

# Create your models here.

class UsersManagers(models.Manager):

    def basic_validator(self, postData):
        errors = {}

        if len(postData['name']) < 4:
            errors["name"] = "El nombre de usuario debe tener al menos 4 letras"

        if len(postData['email']) < 4:
            errors ["email"] = "El email de usuario debe tener al menos 4 letras"

        if len(postData['password']) < 6:
            errors ["password"] = "La contrasena de usuario debe tener al menos 6 letras"

        if postData['password'] != postData['password_confirm']:
            errors ["password"] = "Ambas contrasenas deben ser iguales"

        return errors


class Network(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # authors
    def __repr__(self) -> str:
        return f'{self.id}: {self.name}'
    #el self id corresponde a la llave con que se accederá en el shell 

class Show(models.Model): 
    title = models.CharField(max_length=255)
    network = models.ForeignKey(Network,  related_name="shows", on_delete = models.CASCADE)
    # esta linea queda asi
    release_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # authors
    def __repr__(self) -> str:
        return f'{self.id}: {self.title}'
    #el self id corresponde a la llave con que se accederá en el shell 

class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    allowed = models.BooleanField(default=True)
    avatar = models.URLField(
        default='https://images.all-free-download.com/images/graphiclarge/persona_avatar_2_144024.jpg'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UsersManagers()

    def __repr__(self) -> str:
        return f'{self.id}: {self.name}'

    