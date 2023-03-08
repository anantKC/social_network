from django.db import models
from django.contrib.auth.models import User
from django.views import generic

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
class ProfileView(generic.DetailView):
    model = Profile
    template_name = 'social_network_core_app/profile.html'

