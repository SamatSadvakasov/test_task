
---

# Advertisements API

This is a Django and Django Rest Framework (DRF) project that provides a RESTful API for managing advertisements. It allows you to create, read, update, and delete advertisements, as well as view the list of advertisements.

## Features

- Create new advertisements with title, description, city, and category.
- List all advertisements with their details, including city and category names.
- View a single advertisement's details and increment its view count.
- Update and delete existing advertisements.
- Utilizes Django Admin for easy data management.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Django and Django Rest Framework installed
- Docker (optional, for containerization)

## Setup

1. Clone the repository to your local machine:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```bash
   cd advert_project
   ```

3. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser for accessing the Django Admin:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the Django Admin at `http://localhost:8000/admin/` to add categories, cities, and advertisements.

## Usage

### API Endpoints

- List all advertisements: `/api/advert-list/` (GET)
- Create a new advertisement: `/api/advert-list/` (POST)
- Retrieve, update, or delete a single advertisement: `/api/advert/{id}/` (GET, PUT, DELETE)

### Example API Requests

**List all advertisements:**

```bash
curl http://localhost:8000/api/advert-list/
```

**Create a new advertisement:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"title": "New Ad", "description": "Description of the new ad", "city": 1, "category": 1}' http://localhost:8000/api/advert-list/
```

**Retrieve a single advertisement:**

```bash
curl http://localhost:8000/api/advert/{id}/
```

**Update a single advertisement:**

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Ad", "description": "Updated description"}' http://localhost:8000/api/advert/{id}/
```

**Delete a single advertisement:**

```bash
curl -X DELETE http://localhost:8000/api/advert/{id}/
```

## Docker (Optional)

To run the project in a Docker container, follow these steps:

1. Build the Docker image:

   ```bash
   docker build -t advert_app .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 8000:8000 advert_app
   ```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README with additional information or specific instructions based on your project's requirements.