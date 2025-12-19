from django.db import models
from django.urls import reverse

class Project(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    technologies = models.CharField(max_length=300, help_text="e.g., Django, Bootstrap, Python")
    image = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    github_link = models.URLField(blank=True)
    live_demo_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Project'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('portfolio: project_detail', arg = [self.id])

