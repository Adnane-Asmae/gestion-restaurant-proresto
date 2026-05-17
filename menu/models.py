from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    ordre = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordre', 'nom']

    def __str__(self):
        return self.nom

class Plat(models.Model):
    PAYS_CHOICES = [
        ('maroc', 'Maroc'),
        ('espagne', 'Espagne'),
        ('italie', 'Italie'),
        ('japon', 'Japon'),
        ('chine', 'Chine'),
    ]
    
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='plats', null=True, blank=True)
    nom = models.CharField(max_length=100)
    pays = models.CharField(max_length=20, choices=PAYS_CHOICES, default='maroc')
    image = models.ImageField(upload_to='plats/', blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True)
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nom

    @property
    def get_image(self):
        if self.image:
            return self.image.url
        elif self.image_url:
            return self.image_url
        return None