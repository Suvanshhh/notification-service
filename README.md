Great! Now that your project is pushed to GitHub, here’s a **step-by-step guide** you can share in your `README.md` or with collaborators so anyone can clone and run it locally using Docker:

---

## 🚀 How to Clone and Run the Notification Service

### 🔗 1. Clone the Repository

```bash
git clone https://github.com/Suvanshhh/notification-service.git
cd notification-service
```

---

### 🐳 2. Install Docker & Docker Compose

Make sure [Docker](https://docs.docker.com/get-docker/) and Docker Compose are installed and running on your machine.

---

### 🛠️ 3. Create an `.env` File

Create a `.env` file in the root directory and add environment variables if required. For example:

```env
RABBITMQ_HOST=rabbitmq
RABBITMQ_PORT=5672
POSTGRES_DB=notifications
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
```

(Ensure your code references these environment variables.)

---

### 📦 4. Build and Run the App

Run this command from the root of the project:

```bash
docker-compose up --build
```

This will start:

* 🐘 PostgreSQL (on port `5432`)
* 🐇 RabbitMQ (on ports `5672` and `15672` for the dashboard)
* ⚡ FastAPI Web Server (on port `8000`)
* 🛠️ Background Worker (consumes tasks from RabbitMQ)

---

### 🌐 5. Access the Services

* **FastAPI Docs (Swagger UI)**: [http://localhost:8000/docs](http://localhost:8000/docs)
* **RabbitMQ Dashboard**: [http://localhost:15672](http://localhost:15672)
  (Default username/password: `guest` / `guest`)

---

### 📬 6. Testing the API

You can send a `POST` request to:

```
POST http://localhost:8000/notifications
```

With JSON body:

```json
{
  "user_id": "user123",
  "type": "email",
  "subject": "Hello",
  "message": "This is a test notification"
}
```

---

### ✅ Bonus: Sample CURL Request

```bash
curl -X POST http://localhost:8000/notifications \
  -H "Content-Type: application/json" \
  -d '{"user_id": "user123", "type": "email", "subject": "Test", "message": "This is a test"}'
```

---

Let me know if you'd like to **add a frontend** or host the app on **Render, Railway, or Vercel**. I can help set that up too!
