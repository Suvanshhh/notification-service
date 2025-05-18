

# 📬 Notification Service

A scalable microservice to send **email**, **SMS**, and **in-app notifications** to users. Supports queuing via RabbitMQ and MongoDB for persistence.

---

## 📌 Features

* ✅ REST API using **FastAPI**
* ✅ Notification types: **Email**, **SMS**, **In-App**
* ✅ Asynchronous processing via **RabbitMQ**
* ✅ MongoDB for storing notifications
* ✅ Auto-generated **Swagger UI** for API testing
* ✅ Dockerized and ready for deployment
* ✅ Clean modular code with best practices

---

## 🚀 API Endpoints

### 1. Send a Notification

**POST** `/notifications`

```json
{
  "user_id": "user123",
  "type": "email",
  "subject": "Welcome",
  "message": "Thanks for joining us!"
}
```

### 2. Get User Notifications

**GET** `/users/{user_id}/notifications`

```bash
curl http://localhost:8000/users/user123/notifications
```

---

## 🔍 Swagger UI – API Docs & Testing

The FastAPI backend automatically generates interactive API documentation.

📚 **Visit:**
**[http://localhost:8000/docs](http://localhost:8000/docs)**

🧪 You can:

* Explore all available endpoints
* Test requests directly from the browser
* View request/response formats
* Validate payloads using examples

---

## ⚙️ Technologies Used

* **FastAPI** – Backend framework
* **MongoDB** – Notification storage
* **RabbitMQ** – Queue for background task handling
* **Motor** – Async MongoDB driver
* **Pika** – RabbitMQ producer/consumer
* **Docker** – Containerized microservice

---

## 🧪 Setup Instructions

### 📁 Clone the Repository

```bash
git clone https://github.com/your-username/notification-service.git
cd notification-service
```

### 🐳 Run with Docker Compose

```bash
docker-compose up --build
```

It will start:

* FastAPI backend → `http://localhost:8000`
* Swagger UI → `http://localhost:8000/docs`
* RabbitMQ dashboard → `http://localhost:15672`
* MongoDB service → `localhost:27017`

**RabbitMQ Credentials:**

* Username: `guest`
* Password: `guest`

---

## 🧪 Sample Notification Payloads

### Email Notification

```json
{
  "user_id": "userno_1",
  "type": "email",
  "subject": "Verification",
  "message": "Your code is 123456"
}
```

### SMS Notification

```json
{
  "user_id": "userno_2",
  "type": "sms",
  "subject": "OTP",
  "message": "Your OTP is 987654"
}
```

### In-App Notification

```json
{
  "user_id": "userno_3",
  "type": "in-app",
  "subject": "New Message",
  "message": "You have a new message from Admin"
}
```

---

## 🧠 Assumptions Made

* User authentication is out of scope.
* Notification delivery is simulated (integrated Twilio, can integrate SendGrid, etc.).
* Retry mechanism is basic; can be extended for production.
* Focused on backend functionality; frontend optional.

---

## 🧰 Project Structure

```
.
├── app/
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── database.py
│   └── queue/
│       ├── producer.py
│       └── consumer.py
├── workers/
│   └── worker.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---
