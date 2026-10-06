from django.db import models


class Skill(models.Model):
    """A skill to display on the resume page."""
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default='General')
    level = models.PositiveSmallIntegerField(
        default=85,
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


class Certification(models.Model):
    """Certifications earned."""
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField()
    credential_url = models.URLField(blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order', '-year']

    def __str__(self):
        return f'{self.title} ({self.issuer}, {self.year})'


class Project(models.Model):
    """Showcase project (BI, Power BI, Tableau, Excel, Data Engineering)."""
    TOOL_CHOICES = [
        ('powerbi', 'Power BI'),
        ('tableau', 'Tableau'),
        ('excel', 'Excel Model'),
        ('python', 'Python / Django'),
        ('sql', 'SQL / Data Warehouse'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    project_type = models.CharField(max_length=20, choices=TOOL_CHOICES, default='powerbi')
    summary = models.TextField()
    key_highlights = models.TextField(
        blank=True,
        help_text='Bullet points or details separated by newlines.'
    )
    image = models.ImageField(upload_to='projects/', blank=True)
    embed_url = models.TextField(
        blank=True,
        help_text='Tableau Public embed URL, Power BI iframe src, or OneDrive Excel embed link'
    )
    external_url = models.URLField(
        blank=True,
        help_text='Direct link to view/interact or download (Tableau Public / GitHub / Drive)'
    )
    download_file = models.FileField(
        upload_to='project_files/',
        blank=True,
        help_text='Attach .pbix, .twbx, or .xlsx file here'
    )
    order = models.PositiveSmallIntegerField(default=0)
    is_featured = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.title} [{self.get_project_type_display()}]'
