

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
  "user_id": "suvansh123",
  "type": "email",
  "subject": "Welcome",
  "message": "Messaage here!"
}
```
<img width="450" alt="image" src="https://github.com/user-attachments/assets/6b1069b2-7131-4ffa-b546-7abf1405db45" />
<img width="450" alt="image" src="https://github.com/user-attachments/assets/41ffc217-1a35-483a-abb9-2923f1a26213" />


### 2. Get User Notifications

**GET** `/users/{user_id}/notifications`

```bash
curl http://localhost:8000/users/user123/notifications
```
<img width="450" alt="image" src="https://github.com/user-attachments/assets/9ff23f7b-71dd-4110-838d-6dc3a0158f5a" />
<img width="450" alt="image" src="https://github.com/user-attachments/assets/bda3e919-b4d6-4b25-a487-e8a7300979da" />
<img width="450" alt="image" src="https://github.com/user-attachments/assets/599d2709-492b-4e8f-82dc-8fefe71fbc59" />


### 3. Post Create User 
```json
{
  "id": "suv123",
  "name": "Suvansh Choudhary,
  "email": "choudharysuvansh@gmail.com",
  "phone": "+1234567890"
}
```

**POST** `/users`

```bash
curl http://localhost:8000/users
```
<img width="450" alt="image" src="https://github.com/user-attachments/assets/7c70a4d6-7590-49b9-accb-27a83432fa1b" />
<img width="450" alt="image" src="https://github.com/user-attachments/assets/e8f9e203-3ee2-433c-8b61-b324fa4335eb" />

### 4. Get User 

**GET** `/users/{user_id}`

```bash
curl http://localhost:8000/users/suv123
```
<img width="450" alt="image" src="https://github.com/user-attachments/assets/33b1e0ce-d088-49b1-a81d-039d5ffbf0ea" />

### 5. Root 

**GET** `/`

```bash
curl http://localhost:8000/
```
<img width="450" alt="image" src="https://github.com/user-attachments/assets/6c8deeaa-10af-4032-88bc-8d13bb087fcd" />


---

## 🔍 Swagger UI – API Docs & Testing

<img width="450" alt="image" src="https://github.com/user-attachments/assets/cc175e6c-bb6c-418c-947d-59d1e264baf3" />


The FastAPI backend automatically generates interactive API documentation.

📚 **Visit:**
**[http://localhost:8000/docs](http://localhost:8000/docs)**

🧪 You can:

* Explore all available endpoints
* Test requests directly from the browser
* View request/response formats
* Validate payloads using examples

---

## RabbitMQ Management
<img width="470" alt="image" src="https://github.com/user-attachments/assets/936f627c-9faa-4a8a-a793-42aecf5441ef" />

<img width="470" alt="image" src="https://github.com/user-attachments/assets/6fc2c410-8d4c-4753-a0c3-ab294760f208" />

## Docker

<img width="470" alt="image" src="https://github.com/user-attachments/assets/c47de3be-8b10-45f1-bfd5-a7f7708d1ed0" />



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
