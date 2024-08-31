from django.db import models
from uuid import uuid4

# Создайте здесь ваши модели.

class BaseModel(models.Model):
    """
    Базовая модель для всех моделей приложения.

    Атрибуты:
        created_at (DateTimeField): Дата и время создания записи.
        updated_at (DateTimeField): Дата и время последнего обновления записи.
        is_deleted (BooleanField): Флаг, указывающий на удаление записи.
        adwords (BooleanField): Флаг, указывающий на использование рекламы.
        adwords_start (DateTimeField): Дата начала рекламы.
        adwords_end (DateTimeField): Дата окончания рекламы.
        premium (BooleanField): Флаг, указывающий на использование премиум-функций.
        premium_start (DateTimeField): Дата начала премиум-функций.
        premium_end (DateTimeField): Дата окончания премиум-функций.
        show (BooleanField): Флаг, указывающий на необходимость показа записи.

    Метаданные:
        abstract (bool): Флаг, указывающий на абстрактность модели.
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_deleted = models.BooleanField(default=False, verbose_name='Удален')
    adwords = models.BooleanField(default=False, verbose_name='Реклама')
    adwords_start = models.DateTimeField(null=True, blank=True, verbose_name='Дата начала рекламы')
    adwords_end = models.DateTimeField(null=True, blank=True, verbose_name='Дата окончания рекламы')
    

    class Meta:
        abstract = True

class Category(models.Model):
    """
    Модель категории.

    Атрибуты:
        name (CharField): Название категории.

    Метаданные:
        verbose_name (str): Название модели в единственном числе.
        verbose_name_plural (str): Название модели во множественном числе.
    """
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Tags(models.Model):
    """
    Модель тега.

    Атрибуты:
        name (CharField): Название тега.

    Метаданные:
        verbose_name (str): Название модели в единственном числе.
        verbose_name_plural (str): Название модели во множественном числе.
    """
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name

class Seller(models.Model):
    """
    Модель продавца.

    Атрибуты:
        name (CharField): Название продавца.
        phone (CharField): Телефон продавца.
        email (EmailField): Электронная почта продавца.
        address (CharField): Адрес продавца.
        site (URLField): Сайт продавца.

    Метаданные:
        verbose_name (str): Название модели в единственном числе.
        verbose_name_plural (str): Название модели во множественном числе.
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    about = models.TextField(verbose_name='О продавце')
    logo = models.ImageField(upload_to='sellers/', verbose_name='Логотип', blank=True, null=True)
    image1 = models.ImageField(upload_to='sellers/', verbose_name='Изображение 1', blank=True, null=True)
    image2 = models.ImageField(upload_to='sellers/', verbose_name='Изображение 2', blank=True, null=True)
    image3 = models.ImageField(upload_to='sellers/', verbose_name='Изображение 3', blank=True, null=True)
    image4 = models.ImageField(upload_to='sellers/', verbose_name='Изображение 4', blank=True, null=True)
    image5 = models.ImageField(upload_to='sellers/', verbose_name='Изображение 5', blank=True, null=True)
    phone = models.CharField(max_length=255, verbose_name='Телефон')
    email = models.EmailField(max_length=255, verbose_name='Электронная почта')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    site = models.URLField(max_length=255, verbose_name='Сайт')
    social1 = models.URLField(max_length=255, verbose_name='Соцсеть 1', blank=True, null=True)
    social2 = models.URLField(max_length=255, verbose_name='Соцсеть 2', blank=True, null=True)
    social3 = models.URLField(max_length=255, verbose_name='Соцсеть 3', blank=True, null=True)
    social4 = models.URLField(max_length=255, verbose_name='Соцсеть 4', blank=True, null=True)
    view_count = models.IntegerField(verbose_name='Количество просмотров', default=0)

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'

    def __str__(self):
        return self.name

class Product(BaseModel):
    """
    Модель продукта.

    Атрибуты:
        name (CharField): Название продукта.
        description (TextField): Описание продукта.
        price (DecimalField): Цена продукта.
        count (IntegerField): Количество продукта.
        special_offer (BooleanField): Флаг, указывающий на наличие специального предложения.
        special_offer_start (DateTimeField): Дата начала специального предложения.
        special_offer_end (DateTimeField): Дата окончания специального предложения.
        special_offer_price (DecimalField): Цена специального предложения.
        special_offer_description (TextField): Описание специального предложения.
        category (ForeignKey): Категория продукта.
        tags (ManyToManyField): Теги продукта.
        seller (ForeignKey): Продавец продукта.
        image1 (ImageField): Изображение продукта.
        image2 (ImageField): Изображение продукта.
        image3 (ImageField): Изображение продукта.
        image4 (ImageField): Изображение продукта.
        image5 (ImageField): Изображение продукта.
        image6 (ImageField): Изображение продукта.
        image7 (ImageField): Изображение продукта.
        image8 (ImageField): Изображение продукта.
        image9 (ImageField): Изображение продукта.
        image10 (ImageField): Изображение продукта.

    Метаданные:
        verbose_name (str): Название модели в единственном числе.
        verbose_name_plural (str): Название модели во множественном числе.
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name='Название', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    characteristics = models.TextField(verbose_name='Характеристики', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', blank=True, null=True)
    count = models.IntegerField(verbose_name='Количество', blank=True, null=True)
    special_offer = models.BooleanField(default=False, verbose_name='Специальное предложение')
    special_offer_start = models.DateTimeField(null=True, blank=True, verbose_name='Дата начала специального предложения')
    special_offer_end = models.DateTimeField(null=True, blank=True, verbose_name='Дата окончания специального предложения')
    special_offer_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена специального предложения', blank=True, null=True)
    special_offer_description = models.TextField(verbose_name='Описание специального предложения', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория', blank=True, null=True)
    tags = models.ManyToManyField(Tags, related_name='products', verbose_name='Теги', blank=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='products', verbose_name='Продавец', blank=True, null=True)
    image1 = models.ImageField(upload_to='products/', verbose_name='Изображение 1', blank=True, null=True)
    image2 = models.ImageField(upload_to='products/', verbose_name='Изображение 2', blank=True, null=True)
    image3 = models.ImageField(upload_to='products/', verbose_name='Изображение 3', blank=True, null=True)
    image4 = models.ImageField(upload_to='products/', verbose_name='Изображение 4', blank=True, null=True)
    image5 = models.ImageField(upload_to='products/', verbose_name='Изображение 5', blank=True, null=True)
    image6 = models.ImageField(upload_to='products/', verbose_name='Изображение 6', blank=True, null=True)
    image7 = models.ImageField(upload_to='products/', verbose_name='Изображение 7', blank=True, null=True)
    image8 = models.ImageField(upload_to='products/', verbose_name='Изображение 8', blank=True, null=True)
    image9 = models.ImageField(upload_to='products/', verbose_name='Изображение 9', blank=True, null=True)
    image10 = models.ImageField(upload_to='products/', verbose_name='Изображение 10', blank=True, null=True)
    certificate_template = models.ImageField(upload_to='products/', verbose_name='Шаблон сертификата', blank=True, null=True)
    certificate_description = models.TextField(verbose_name='Описание сертификата', blank=True, null=True)
    certificate_langth_days = models.IntegerField(verbose_name='Срок действия сертификата (дней)', blank=True, null=True)
    return_policy = models.TextField(verbose_name='Политика возврата', blank=True, null=True)
    public_start = models.DateTimeField(null=True, blank=True, verbose_name='Дата начала публикации')
    public_length_days = models.IntegerField(verbose_name='Срок публикации (дней)', blank=True, null=True)
    public_end = models.DateTimeField(null=True, blank=True, verbose_name='Дата окончания публикации')
    view_count = models.IntegerField(verbose_name='Количество просмотров', default=0)
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

class FeedbackSeller(models.Model):
    """
    Модель отзыва о продавце.

    Атрибуты:
        author (CharField): Автор отзыва.
        seller (ForeignKey): Продавец.
        name (CharField): Имя пользователя.
        text (TextField): Текст отзыва.
        rating (IntegerField): Оценка продавца.
        image1 (ImageField): Изображение отзыва.
        image2 (ImageField): Изображение отзыва.
        image3 (ImageField): Изображение отзыва.
        image4 (ImageField): Изображение отзыва.
        image5 (ImageField): Изображение отзыва.

    Метаданные:
        verbose_name (str): Название модели в единственном числе.
        verbose_name_plural (str): Название модели во множественном числе.
    """
    author = models.CharField(max_length=255, verbose_name='Автор')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='feedbacks', verbose_name='Продавец')
    name = models.CharField(max_length=255, verbose_name='Имя пользователя')
    text = models.TextField(verbose_name='Текст отзыва')
    rating = models.IntegerField(verbose_name='Оценка продавца')
    image1 = models.ImageField(upload_to='feedbacks/', verbose_name='Изображение 1', blank=True, null=True)
    image2 = models.ImageField(upload_to='feedbacks/', verbose_name='Изображение 2', blank=True, null=True)
    image3 = models.ImageField(upload_to='feedbacks/', verbose_name='Изображение 3', blank=True, null=True)
    image4 = models.ImageField(upload_to='feedbacks/', verbose_name='Изображение 4', blank=True, null=True)
    image5 = models.ImageField(upload_to='feedbacks/', verbose_name='Изображение 5', blank=True, null=True)

    class Meta:
        verbose_name = 'Отзыв о продавце'
        verbose_name_plural = 'Отзывы о продавцах'

class FeedbackProduct(models.Model):
    """
    Модель отзыва о продукте.

    Атрибуты:
        author (CharField): Автор отзыва.
        product (ForeignKey): Продукт.
        name (CharField): Имя пользователя.
        text (TextField): Текст отзыва.
        rating (IntegerField): Оценка продукта.
        image1 (ImageField): Изображение отзыва.
        image2 (ImageField): Изображение отзыва.
        image3 (ImageField): Изображение отзыва.
        image4 (ImageField): Изображение отзыва.
        image5 (ImageField): Изображение отзыва.

    Метаданные:
        verbose_name (str): Название модели в единственном числе.
        verbose_name_plural (str): Название модели во множественном числе.
    """
    author = models.CharField(max_length=255, verbose_name='Автор')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='feedbacks', verbose_name='Продукт')
    name = models.CharField(max_length=255, verbose_name='Имя пользователя')
    text = models.TextField(verbose_name='Текст отзыва')
    rating = models.IntegerField(verbose_name='Оценка продукта')
    image1 = models.ImageField(upload_to='feedbacks/', verbose_name='Изображение 1', blank=True, null=True)
    image2 = models.ImageField(upload_to='feedbacks/', verbose_name='Изображение 2', blank=True, null=True)
    image3 = models.ImageField(upload_to='feedbacks/', verbose_name='Изображение 3', blank=True, null=True)
    image4 = models.ImageField(upload_to='feedbacks/', verbose_name='Изображение 4', blank=True, null=True)
    image5 = models.ImageField(upload_to='feedbacks/', verbose_name='Изображение 5', blank=True, null=True)

    class Meta:
        verbose_name = 'Отзыв о продукте'
        verbose_name_plural = 'Отзывы о продуктах'
    
class Certificates(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='certificates', verbose_name='Продукт')
    name = models.CharField(max_length=255, verbose_name='Имя пользователя')
    phone = models.CharField(max_length=255, verbose_name='Телефон')
    email = models.EmailField(max_length=255, verbose_name='Электронная почта')
    date = models.DateField(verbose_name='Дата')
    number = models.CharField(max_length=255, verbose_name='Номер сертификата')
    image = models.ImageField(upload_to='certificates/', verbose_name='Изображение сертификата')
    status = models.BooleanField(default=False, verbose_name='Статус')
    start = models.DateTimeField(null=True, blank=True, verbose_name='Дата начала')
    end = models.DateTimeField(null=True, blank=True, verbose_name='Дата окончания')
    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'
    def __str__(self):
        return self.number
    