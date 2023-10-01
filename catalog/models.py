from django.db import models


class Category(models.Model):
    """Категория товара"""
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    """Продукт"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    preview = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    products = models.ManyToManyField(Product, related_name='versions', blank=True)
    version_number = models.CharField(max_length=50)
    version_name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.version_name}"
