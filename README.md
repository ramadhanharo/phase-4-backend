#  Locavore API — Farmers Market & Food Vendor Finder

Locavore is a RESTful Flask API for discovering, reviewing, and managing local food vendors. Users can register, log in, add vendors, leave reviews, and manage their profiles.

---

##  Project Structure

locavore-backend/
│
├── app/
│ ├── init.py
│ ├── models.py
│ ├── controllers/
│ ├── routes/
│
├── migrations/
├── server.py
├── .env (optional)
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

##  Tech Stack

- **Backend:** Python, Flask, Flask SQLAlchemy
- **Database:** PostgreSQL
- **Auth:** JWT (JSON Web Tokens)
- **ORM & Migrations:** SQLAlchemy + Alembic
- **CORS:** Flask-CORS
- **Testing Tool:** Postman

---

##  Authentication

All protected routes require a valid JWT passed in the `Authorization` header:

Authorization: Bearer <your_token>

yaml
Copy
Edit

JWT is issued on successful login.

---

##  Setup Instructions

### 1. Clone the repo:

```bash
git clone git@github.com:ramadhanharo/phase-4-backend.git
cd locavore-backend
2. Create a virtual environment:
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
3. Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt

###4. Set up PostgreSQL:
sql
Copy
Edit
-- Login to psql:
sudo -u postgres psql

-- Create database:
CREATE DATABASE locavore_db;
5. Run migrations:
bash
Copy
Edit
flask db init     # Only once
flask db migrate -m "Initial"
flask db upgrade
6. Start the server:
bash
Copy
Edit
flask run
 API Endpoints
 ###Auth Routes


Method	Endpoint	Description	Auth
POST	/register	Register new user	❌
POST	/login	Login, returns token	❌

 ###Vendor Routes
Method	Endpoint	Description	Auth
GET	/vendors/	Get all vendors	✅
GET	/vendors/:id	Get vendor by ID	✅
POST	/vendors/	Create new vendor	✅
PUT	/vendors/:id	Update vendor (owner only)	✅
DELETE	/vendors/:id	Delete vendor (owner only)	✅

JSON Body for POST /vendors/:

json
Copy
Edit
{
  "name": "Organic Farm",
  "description": "Fresh vegetables and eggs",
  "location": "Nairobi"
}
### Review Routes
Method	Endpoint	Description	Auth
POST	/reviews/vendors/:vendor_id/reviews/	Create review	✅
PATCH	/reviews/reviews/:id/	Update review (owner)	✅
DELETE	/reviews/reviews/:id/	Delete review (owner)	✅

JSON Body for POST Review:

json
Copy
Edit
{
  "content": "Amazing produce!",
  "rating": 5
}

 Entity Relationship Diagram (ERD)
sql
Copy
Edit
User ───< Vendor ───< Review
A user can create many vendors.

A vendor can have many reviews.

Reviews are tied to both a user and a vendor.

### Features
JWT-based user registration/login

Full CRUD for vendors and reviews

Ownership-based permissions

Relational database with cascading deletes

Modular MVC structure

### Developer Notes
To inspect available routes:

bash
Copy
Edit
flask routes
To reset migrations:

bash
Copy
Edit
flask db downgrade base
rm -rf migrations/
flask db init
flask db migrate -m "fresh"
flask db upgrade

### Contributors
Ramadhan Haro — Backend Developer

Group 4 — Locavore Project Team

📝 License
This project is open-source and available under the MIT License.
