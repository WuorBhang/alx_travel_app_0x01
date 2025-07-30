# ALX Travel App - Backend API (0x01)

A robust, scalable backend API for a travel listing and booking platform built with **Django** and **Django REST Framework (DRF)**. This project enables users to manage listings, book stays, and review properties through a clean, documented RESTful API.

> ✅ **Task 0 & 1 Complete**  
> API Development, ViewSets, Router, Swagger Docs, Manual Review Ready

---

## 🌍 Project Overview

**ALX Travel App** is a full-featured API backend that allows:
- Hosts to **create and manage property listings** (hotels, apartments, villas, etc.)
- Guests to **book accommodations** with date validation and pricing
- Users to **leave reviews and ratings**
- All data accessible via a **well-documented REST API**

This version (`0x01`) introduces:
- `ModelViewSet` for Listings and Bookings
- RESTful routing using `DefaultRouter`
- Interactive API documentation with **Swagger UI** via `drf-spectacular`
- CORS, authentication, filtering, and pagination
- Ready for frontend integration (React, Vue, etc.)

---

## 🚀 Features

- **Listings Management**
  - CRUD operations for property listings
  - Supports multiple types: Hotel, Apartment, Villa, etc.
  - Amenities tracking (ManyToMany relationship)
  - Availability date range

- **Booking System**
  - Date validation (check-in < check-out)
  - Guest count vs. max capacity
  - Auto-calculated total price
  - User-specific booking access

- **Reviews & Ratings**
  - 1–5 star ratings
  - One review per user per listing
  - Average rating computed via annotation

- **API & Documentation**
  - RESTful endpoints under `/api/`
  - JWT or Session authentication
  - Filterable, searchable, paginated responses
  - Interactive Swagger UI at `/api/docs/`

- **Security & Best Practices**
  - Environment variables via `.env`
  - PostgreSQL database
  - CORS protection
  - Input validation and error handling

---

## 🛠 Tech Stack

| Layer     | Technology                          |
|-----------|-------------------------------------|
| Backend   | Python 3.10+, Django 4.2+           |
| API       | Django REST Framework (DRF)         |
| Database  | PostgreSQL (with `dj_database_url`) |
| Auth      | DRF TokenAuthentication + SessionAuth |
| Docs      | `drf-spectacular` (Swagger UI)      |
| CORS      | `django-cors-headers`               |
| Filtering | `django-filter`, search, ordering   |
| Deployment Ready | Redis, Celery (future use)  |

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/WuorBhang/alx_travel_app_0x01.git
cd alx_travel_app_0x01
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file and add:

```env
SECRET_KEY=your-django-secret-key-here
DEBUG=True
DB_NAME=alx_travel_db
DB_USER=postgres
DB_PASSWORD=1234
DB_HOST=localhost
DB_PORT=5432
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Run the Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run the Server

```bash
python manage.py runserver
```

---

## 🌐 API Endpoints

All endpoints are available under `/api/`.

### 🔹 Listings
- `GET /api/listings/` – List all listings (filterable by `?location=`)
- `POST /api/listings/` – Create a new listing
- `GET /api/listings/<id>/` – Get listing details
- `PUT /api/listings/<id>/` – Update listing
- `DELETE /api/listings/<id>/` – Delete listing

### 🔹 Bookings
- `GET /api/bookings/` – List all bookings
- `POST /api/bookings/` – Create a new booking
- `GET /api/bookings/<id>/` – Get booking details
- `PUT /api/bookings/<id>/` – Update booking
- `DELETE /api/bookings/<id>/` – Delete booking

### 🔹 Reviews
- `GET /api/reviews/` – List all reviews
- `POST /api/reviews/` – Create a new review
- `GET /api/reviews/<id>/` – Get review details
- `PUT /api/reviews/<id>/` – Update review
- `DELETE /api/reviews/<id>/` – Delete review

### 🔹 API Documentation
- 🔗 Swagger UI: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
- 📄 OpenAPI Schema: [http://127.0.0.1:8000/api/schema/](http://127.0.0.1:8000/api/schema/)

---

## 🔐 Authentication

### Session Authentication
Use `/admin/` to log in, then use Swagger UI with session.

### Token Authentication
Generate a token:

```bash
python manage.py shell
```

```python
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
token = Token.objects.create(user=User.objects.get(username='youruser'))
print(token.key)
```

Then add header in Postman/Swagger:

```
Authorization: Token <token>
```

---

## 🧪 Testing with Postman

Example:

```http
POST /api/bookings/
{
  "listing": 1,
  "check_in": "2025-04-01",
  "check_out": "2025-04-05",
  "guests": 2
}

GET /api/listings/?location=Nairobi
```

> Note: `POST`, `PUT`, and `DELETE` on `/api/listings/` require admin or staff permissions.

---

## 📂 Project Structure

```bash
alx_travel_app_0x01/
├── alx_travel_app/
│   ├── settings.py
│   ├── urls.py          # Main URLs with /api/ and /api/docs/
│   └── wsgi.py
├── listings/
│   ├── models.py        # Listing, Booking, Review
│   ├── serializers.py   # DRF Serializers
│   ├── views.py         # ModelViewSets
│   └── urls.py          # App-level router
├── manage.py
├── requirements.txt
└── .env.example         # Example environment file
```

---

## 📄 License

This project is licensed under the MIT License.

---

## 👥 Authors

- GitHub: [@WuorBhang](https://github.com/WuorBhang)
- Email: [uhuribhang211@gmail.com](mailto:uhuribhang211@gmail.com)

---

## 📬 Feedback & Contributions

Contributions, issues, and feature requests are welcome!  
Feel free to open issues or reach out via the email above.
