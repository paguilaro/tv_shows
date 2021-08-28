from django.db import models

# Create your models here.

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

    def __repr__(self) -> str:
        return f'{self.id}: {self.name}'
    