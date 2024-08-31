from django.db import models
import uuid
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from app.managers import UserManager

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
    premium = models.BooleanField(default=False, verbose_name='Премиум')
    premium_start = models.DateTimeField(null=True, blank=True, verbose_name='Дата начала премиума')
    premium_end = models.DateTimeField(null=True, blank=True, verbose_name='Дата окончания премиума')

    class Meta:
        abstract = True

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(_('username'), max_length=255, unique=True)
    email = models.EmailField(_('email address'),\
        null=True, blank=True)
    phone = models.CharField(_('phone number'), max_length=30,\
        null=True, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=False)
    is_staff = models.BooleanField(_('staff'), default=False)

    is_verified = models.BooleanField(_('verified'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        unique_together = ('username', 'email', 'phone')

# Профиль. Создается автоматически при регистрации пользователя.

class Profile(BaseModel):
    # Данные контактного лица
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Отчество')
    birth_date = models.DateField(blank=True, null=True, verbose_name='Дата рождения')

    # Данные юридического лица
    inn = models.CharField(max_length=12, null=True, blank=True, verbose_name='ИНН')
    kpp = models.CharField(max_length=9, null=True, blank=True, verbose_name='КПП')
    ogrn = models.CharField(max_length=15, null=True, blank=True, verbose_name='ОГРН')
    legal_address = models.CharField(max_length=255, null=True, blank=True, verbose_name='Юридический адрес')
    actual_address = models.CharField(max_length=255, null=True, blank=True, verbose_name='Фактический адрес')
    phone = models.CharField(max_length=30, null=True, blank=True, verbose_name='Телефон')
    email = models.EmailField(null=True, blank=True, verbose_name='Email')
    site = models.URLField(null=True, blank=True, verbose_name='Сайт')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    # Банковские реквизиты
    bank_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название банка')
    bank_bik = models.CharField(max_length=9, null=True, blank=True, verbose_name='БИК')
    bank_account = models.CharField(max_length=20, null=True, blank=True, verbose_name='Расчетный счет')
    bank_correspondent = models.CharField(max_length=20, null=True, blank=True, verbose_name='Корреспондентский счет')
    
    # Данные о премиуме
    products_limit = models.PositiveIntegerField(default=5, verbose_name='Лимит объявлений')
    products_count = models.PositiveIntegerField(default=0, verbose_name='Количество объявлений')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'