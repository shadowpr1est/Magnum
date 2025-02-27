# Magnum

## Description
This is a rough (still working) copy of the magnum website.

## Features
1. View the list of products with the ability to filter by category
2. Search for products by name
3. Detailed product information
4. Adaptive interface using Bootstrap

## Navigation
1. Go to /products/ to view the list of products.
2. Click on the product to view the details.
3. You can manage products in the admin panel (/admin/).

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/shadowpr1est/magnum.git
    ```

2. Install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # for macOS and Linux
    venv\Scripts\activate  # for Windows
    pip install -r requirements.txt
    ```

3. Set up the database:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

5. Run the server:
    ```bash
    python manage.py runserver
    ```

The project is now available at http://127.0.0.1:8000/ or http://localhost:8000/

## Usage
Provide examples or screenshots of how to use the project.

## Contributing
Guidelines for contributing to the project.

## License
Specify the license under which the project is distributed.

## Acknowledgements
Acknowledge any libraries, tools, or individuals that contributed to the project.

## Contact
Provide contact information or links to the project's maintainers or community.
