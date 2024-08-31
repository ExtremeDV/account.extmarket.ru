from django.test import TestCase
from app.models import Category, Tags, Seller, Product, FeedbackSeller, FeedbackProduct, Certificates
from uuid import uuid4

class ModelsTestCase(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        self.tag = Tags.objects.create(name="New")
        self.seller = Seller.objects.create(
            name="Best Seller",
            description="Best products in town",
            about="We sell the best products",
            phone="1234567890",
            email="seller@example.com",
            address="123 Market St",
            site="http://example.com"
        )
        self.product = Product.objects.create(
            name="Smartphone",
            description="Latest model",
            price=999.99,
            count=10,
            category=self.category,
            seller=self.seller
        )
        self.product.tags.add(self.tag)
        self.feedback_seller = FeedbackSeller.objects.create(
            author="John Doe",
            seller=self.seller,
            name="John",
            text="Great seller!",
            rating=5
        )
        self.feedback_product = FeedbackProduct.objects.create(
            author="Jane Doe",
            product=self.product,
            name="Jane",
            text="Great product!",
            rating=5
        )
        self.certificate = Certificates.objects.create(
            product=self.product,
            name="Jane Doe",
            phone="1234567890",
            email="jane@example.com",
            date="2023-01-01",
            number="CERT123",
            status=True
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Electronics")

    def test_tag_creation(self):
        self.assertEqual(self.tag.name, "New")

    def test_seller_creation(self):
        self.assertEqual(self.seller.name, "Best Seller")
        self.assertEqual(self.seller.phone, "1234567890")

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Smartphone")
        self.assertEqual(self.product.price, 999.99)
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.seller, self.seller)
        self.assertIn(self.tag, self.product.tags.all())

    def test_feedback_seller_creation(self):
        self.assertEqual(self.feedback_seller.author, "John Doe")
        self.assertEqual(self.feedback_seller.seller, self.seller)
        self.assertEqual(self.feedback_seller.rating, 5)

    def test_feedback_product_creation(self):
        self.assertEqual(self.feedback_product.author, "Jane Doe")
        self.assertEqual(self.feedback_product.product, self.product)
        self.assertEqual(self.feedback_product.rating, 5)

    def test_certificate_creation(self):
        self.assertEqual(self.certificate.product, self.product)
        self.assertEqual(self.certificate.name, "Jane Doe")
        self.assertEqual(self.certificate.number, "CERT123")
        self.assertTrue(self.certificate.status)