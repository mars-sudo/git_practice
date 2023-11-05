from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model): #"Topic" is the name of this model
    """A topic the user is learning about."""
    text = models.CharField(max_length=200) # Attribute associated with this Model
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        """Return a string representation of the model."""
        return self.text
    
class Entry(models.Model): # "Entry" is the name of this model
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) 
    # the "topic" attribute for the "Entry" model. "foreign key" is a database term, it's a reference to another record in the database. 
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def _str_(self):
        """REturn a string representation of the model."""
        return f"{self.text[:50]}..."
        



