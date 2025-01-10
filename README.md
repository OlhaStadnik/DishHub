
# Dish Hub 

A Django-based web application for managing recipes, dishes, and cooks. This system allows users to create, update, and manage recipes while maintaining a database of cooks and their specialties.
[посилання на мій сайт](https://dishhub-h2kt.onrender.com/)
## Features

- User Authentication System
  - Custom user model (CookUser) with experience tracking
  - User registration and login
  - Profile management
  
- Recipe Management
  - Create, update, and delete dishes
  - Categorize dishes by types
  - Search functionality for dishes and dish types
  - Price management for dishes
  
- Cook Management
  - Track cook's experience
  - Associate cooks with dishes
  - View cook profiles and their specialties

## Technologies

- Python 3.x
- Django 5.1.3
- Bootstrap 4
- Crispy Forms
- PostgresSQL

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```
4. Set up environment variables:

Create a .env file in the root directory of the project.
Use the provided .env.sample as a template. Copy .env.sample to .env
Fill in the necessary values in the .env file, such as database credentials, 
Django settings, and any third-party API keys.
```bash
cp .env.sample .env
```

5. Apply migrations:

```bash
python manage.py migrate
```

5. Create a superuser:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

## Project Structure

- `accounts/` - Custom user management app
- `recipe_manager/` - Main app for recipe and dish management
- `templates/` - HTML templates
- `static/` - Static files (CSS, JavaScript, images)

## Usage

1. Register as a new cook or login with existing credentials
2. Create dish types to categorize your dishes
3. Add new dishes with descriptions and prices
4. Assign dishes to cooks
5. Browse and search through the recipe collection

## Admin Interface

Access the admin interface at `/admin` to manage:
- Users (Cooks)
- Dishes
- Dish Types

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

