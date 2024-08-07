from django.db import models

# Create your models here.

class BaseModel(models.Model):
    """
    Базовая модель для всех моделей приложения.

    Атрибуты:
        created_at (DateTimeField): Дата и время создания записи.
        updated_at (DateTimeField): Дата и время последнего обновления записи.
        is_deleted (BooleanField): Флаг, указывающий на удаление записи.
        show (BooleanField): Флаг, указывающий на необходимость показа записи.

    Метаданные:
        abstract (bool): Флаг, указывающий на абстрактность модели.
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_deleted = models.BooleanField(default=False, verbose_name='Удален')
    show = models.BooleanField(default=True, verbose_name='Показывать')

    class Meta:
        abstract = True