# Product Segmentation App

This Django application allows users to segment products based on price and size dynamically. Users can define the number of segments using a range filter, enabling a tailored view of products according to their preferences.

## Features
- Dynamic segmentation of products by price and size.
- Create, read, update, and delete products.
- Built-in admin interface for managing product data.

## Installation
1. Clone the repository.
2. Install requirements: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Create sample products: `python manage.py loaddata sample_products.json`
5. Start the server: `python manage.py runserver` 

## Usage
Access the app at `http://localhost:8000/products/` to view and filter products.
