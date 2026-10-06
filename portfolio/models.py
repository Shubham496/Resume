from django.db import models


class Skill(models.Model):
    """A skill to display on the resume page."""
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default='General')
    level = models.PositiveSmallIntegerField(
        default=80,
        help_text='Proficiency 0–100'
    )
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f'{self.name} ({self.category})'


class Experience(models.Model):
    """A work-experience entry on the resume."""
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text='Leave blank for "Present"')
    description = models.TextField()
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order', '-start_date']

    def __str__(self):
        return f'{self.title} @ {self.company}'

    @property
    def duration(self):
        end = self.end_date.strftime('%b %Y') if self.end_date else 'Present'
        return f'{self.start_date.strftime("%b %Y")} – {end}'


class Education(models.Model):
    """An education entry on the resume."""
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year_end = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order', '-year_end']

    def __str__(self):
        return f'{self.degree} — {self.institution}'


class Project(models.Model):
    """A featured project shown on the landing page."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True)
    url = models.CharField(max_length=300, blank=True, help_text='Internal path or external URL')
    order = models.PositiveSmallIntegerField(default=0)
    is_featured = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
