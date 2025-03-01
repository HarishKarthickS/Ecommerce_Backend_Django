# E-Commerce API with Django and PostgreSQL

## 📌 Project Overview
This is a fully functional **E-Commerce REST API** built using **Django REST Framework** and **PostgreSQL (via NeonDB)**. The API supports:
- **User authentication** (registration with automatic JWT token generation, login, and token refreshing)
- **Product management** (CRUD operations for products)
- **Order management** (placing, retrieving, and managing orders)
- **JWT-based authentication** for secure API access

## 🚀 Features
✅ **User Registration & Login** (with JWT token response)  
✅ **Secure Authentication** (using Simple JWT)  
✅ **CRUD Operations for Products**  
✅ **Order Management System**  
✅ **PostgreSQL Database (via NeonDB)**  
✅ **RESTful API Structure**  
✅ **Environment Variable Support** (via `python-decouple` and `.env` file)  
✅ **Well-structured Code with Django Best Practices**  

## 📂 Project Structure
```
ecommerce_project/
├── .env                  # Environment variables
├── .gitignore            # Git ignore file
├── manage.py             # Django management script
├── ecommerce_project/    # Main Django project
│   ├── __init__.py
│   ├── settings.py       # Django settings (NeonDB integrated)
│   ├── urls.py
│   └── wsgi.py
└── api/                  # Main API app
    ├── __init__.py
    ├── admin.py          # Admin panel setup
    ├── models.py         # Database models
    ├── serializers.py    # API serializers
    ├── views.py          # API views (business logic)
    └── urls.py           # API routes
```

## 🛠 Installation & Setup
### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/ecommerce-api.git
cd ecommerce-api
```

### Step 2: Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```
If you don’t have a `requirements.txt` file, install dependencies manually:
```bash
pip install django djangorestframework psycopg2-binary djangorestframework-simplejwt python-decouple dj-database-url
```

### Step 4: Set Up Environment Variables
Create a `.env` file in the root directory and add the following:
```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgresql://your_neondb_user:your_neondb_password@your_neondb_host/your_neondb_name?sslmode=require
```

### Step 5: Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create a Superuser (Admin)
```bash
python manage.py createsuperuser
```
Follow the prompts to set up your admin user.

### Step 7: Run the Server
```bash
python manage.py runserver
```
The API is now running at **http://127.0.0.1:8000/** 🎉

## 🔑 API Endpoints
### 🏷 Authentication
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/api/register/` | Register a new user (returns JWT tokens) |
| POST | `/api/login/` | Obtain access & refresh JWT tokens |
| POST | `/api/token/refresh/` | Refresh access token |

### 📦 Product Management
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/api/products/` | List all products |
| POST | `/api/products/` | Create a new product (requires authentication) |
| GET | `/api/products/{id}/` | Retrieve product details |
| PUT | `/api/products/{id}/` | Update a product (requires authentication) |
| DELETE | `/api/products/{id}/` | Delete a product (requires authentication) |

### 🛒 Order Management
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/api/orders/` | List user’s orders (authentication required) |
| POST | `/api/orders/` | Place a new order |

## 🔥 Example Requests
### 1️⃣ User Registration & Get Token
**Request:**
```json
{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepassword",
    "password2": "securepassword"
}
```
**Response:**
```json
{
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}
```

### 2️⃣ Create a Product
**Request:** (Requires authentication, add `Authorization: Bearer <access_token>` header)
```json
{
    "name": "Smartphone",
    "description": "A high-end smartphone with AI features",
    "price": 799.99,
    "category": "Electronics"
}
```

### 3️⃣ Place an Order
**Request:**
```json
{
    "order_items": [
        { "product_id": 1, "quantity": 2 }
    ]
}
```
**Response:**
```json
{
    "id": 1,
    "user": 1,
    "order_items": [
        { "product": { "id": 1, "name": "Smartphone", "price": 799.99 }, "quantity": 2 }
    ],
    "total": 1599.98,
    "status": "Pending",
    "created_at": "2025-03-01T12:00:00Z"
}
```

## 🛠 Future Enhancements
📌 **Stripe Payment Integration**  
📌 **User Roles (Admin, Seller, Buyer)**  
📌 **Search & Filtering for Products**  
📌 **Unit Testing for API**  

## 🤝 Contributing
Pull requests are welcome! Feel free to submit issues and suggestions.

## 📜 License
MIT License. Feel free to use and modify this project.

---
**Enjoy coding! 🚀🔥**

