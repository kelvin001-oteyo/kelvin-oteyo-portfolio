from django.db import models
from django.utils.text import slugify



class Update(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=300)
    content = models.TextField(blank=True)

    meta_description = models.CharField(
        max_length=160,
        blank=True,
        help_text="SEO description (max 160 characters)"
    )

    featured_image = models.ImageField(upload_to='updates/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)



    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        # Automatically generate slug from title if not provided
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            n = 1
            while Update.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{n}"
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


     

