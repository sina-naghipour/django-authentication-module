import random
from django.core.management.base import BaseCommand
from faker import Faker
from products.models import Product, Review  # Replace with your actual app name

class Command(BaseCommand):
    help = 'Generates random data into Product and Review models.'
    
    def add_arguments(self, parser):
        parser.add_argument('--products', type=int, default=10, help='Number of generated products.')
        parser.add_argument('--reviews', type=int, default=15, help='Number of generated reviews.')
    
    def handle(self, *args, **options):
        fake = Faker()
        Faker.seed(46)  # For reproducible results
        
        product_count = options['products']
        review_count = options['reviews']
        
        # Clear existing data if needed (optional)
        # Product.objects.all().delete()
        # Review.objects.all().delete()
        
        # Create products
        created_products = []
        for _ in range(product_count):
            try:
                product = Product.objects.create(
                    name=fake.unique.word().title() + ' ' + fake.word().title(),
                    description=fake.paragraph(nb_sentences=6),
                    owner=fake.name(),
                    quantity=fake.random_int(min=5, max=120),
                )
                created_products.append(product)
                self.stdout.write(f'Created product: {product.name}')
            except Exception as e:
                self.stderr.write(f'Error creating product: {str(e)}')
                continue
        
        available_products = created_products if created_products else Product.objects.all()
        
        if not available_products:
            self.stderr.write('No products available to attach reviews!')
            return
        
        for _ in range(review_count):
            try:
                product = random.choice(available_products)
                review = Review.objects.create(
                    user_name=fake.name(),
                    stars=fake.random_int(min=1, max=5),
                    content=fake.paragraph(nb_sentences=3),
                    product=product,  # Pass the Product instance, not UUID
                )
                self.stdout.write(f'Created review for {product.name} by {review.user_name}')
            except Exception as e:
                self.stderr.write(f'Error creating review: {str(e)}')
                continue
            
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {len(created_products)} products and {review_count} reviews'
            )
        )