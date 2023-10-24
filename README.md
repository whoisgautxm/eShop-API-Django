# E-Commerce API using Django

## Description

This project is an API for an e-commerce website developed using the Django web framework. The primary purpose of this project is to provide a robust and customizable backend for an e-commerce platform, enabling developers to build and extend their own online stores.

The API includes various features commonly found in e-commerce websites, such as user authentication, product management, shopping cart functionality, order processing, and more. It is designed to be flexible and easily extendable, making it suitable for both small and large e-commerce applications.

Mosh Hamedani's "Django for Beginners" course serves as the foundation for this project. By following Mosh's course, we ensure that the code adheres to best practices and industry standards, making it suitable for use in real-world applications.

## Features

- **User Authentication**: Allow users to sign up, log in, and manage their profiles.
- **Product Management**: Create, read, update, and delete product listings.
- **Shopping Cart**: Enable users to add products to their cart and place orders.
- **Order Processing**: Process and manage orders, including order history for users.
- **Payment Integration**: Implement payment gateways (e.g., Stripe, PayPal) for secure transactions.
- **Search and Filters**: Allow users to search for products and filter them based on various criteria.
- **Reviews and Ratings**: Enable users to leave reviews and ratings for products.
- **Admin Dashboard**: Provide an admin interface for managing users, products, and orders.

## Getting Started

Follow these steps to set up and run the project on your local machine.

1. **Clone the Repository**:

```git clone https://github.com/yourusername/e-commerce-api-django.git```

2. **Navigate to the Project Directory**:

```cd e-commerce-api-django```

3. **Create a Virtual Environment**:

Create a virtual environment for the project and activate it.

```python -m venv venv source venv/bin/activate # On Windows, use 'venv\Scripts\activate'```

4. **Install Dependencies**:

Install the project dependencies using pip.
```pip install -r requirements.txt```

5. **Run Migrations**:

Apply the database migrations to set up the initial database.

```python manage.py migrate```

6. **Create Superuser**:

Create an admin superuser account to access the admin dashboard.

```python manage.py createsuperuser```

7. **Run the Development Server**:

Start the development server.

```python manage.py runserver```

8. **Access the API**:

The API will be available at `http://localhost:8000/`. You can access the admin dashboard at `http://localhost:8000/admin/`.

## API Documentation

For detailed information on the API endpoints and usage, please refer to the API documentation. This documentation should be available at `/api/docs/` or `/api/swagger/` once the development server is running.

## Contribution

Contributions to this project are welcome. If you want to contribute, please follow the guidelines provided in the CONTRIBUTING.md file.

## License

This project is licensed under the [MIT License](LICENSE).
This format allows users to easily copy the commands and code snippets provided in the README.

