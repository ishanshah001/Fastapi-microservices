# 🛵 Payment Microservices App (FastAPI + React + Redis + Redis Streams + Grafana)

## 📦 Overview
This is a **real-time, event-driven payment system** built with **FastAPI**, **React**, and **Redis**. It uses **Redis Streams** for inter-service communication and **RedisJSON** as a schemaless database. The system is designed for **high performance, scalability**, and **monitorability** using **Prometheus**.

---

## ⚙️ Features

### Backend (FastAPI + RedisJSON + Redis Streams)
- ✅ **Product and Order Placement API** with asynchronous background processing  
- 🧠 **Redis Streams** used for real-time order completion & inventory updates  
- 🚀 **RedisJSON** as schemaless NoSQL database (low latency, flexible schema)  
- 🔁 **Event-driven architecture**: loosely coupled microservices  
- 📉 **Grafana** for API and service performance monitoring  

### Frontend (React)
- 🎯 Lightweight and responsive UI built with React  
- 🔄 Live status tracking of orders  
- 🧼 Clean UI for placing orders  

---

## 🧰 Tech Stack

### Backend
- **FastAPI** – Python web framework  
- **Redis Streams** – Event bus (like Kafka)  
- **RedisJSON** – NoSQL database  
- **requests** – API calls between services  
- **Grafana** – Real-time visualization  

### Frontend
- **React** – UI development  
- **Axios** – API integration  
- **Tailwind CSS** – Styling  

---
## 🚀 Installation & Setup

### 🐍 Backend (FastAPI + Redis)

1️⃣ Clone the repository & navigate to backend:
```bash
git clone https://github.com/ishanshah001/Fastapi-microservices
cd /backend

2️⃣ Setup Environment Variables
Create a .env file in the backend directory with your Redis connection details:
REDDIS_ENDPOINT=localhost
REDDIS_PASSWORD=yourpassword
Replace localhost and yourpassword with your Redis server address and password.

3️⃣ Install Backend Dependencies
Make sure you have Python 3.8+ installed. Then run:
pip install -r requirements.txt

4️⃣ Run Backend API Servers
Start the FastAPI backend:

cd inventory
py main.py --port 8001

In a new terminal, start the Payment Service FastAPI backend:
cd ../payment
py main.py --port 8002

You should see both API servers running at:
Inventory API: http://localhost:8001
Payment API: http://localhost:8002

5️⃣Start Background Consumers
Open new terminal windows/tabs and run the consumers for each service:

Inventory Consumer:
python inventory/inventory_consumer.py

Payment Consumer:
python payment/payment_consumer.py

These consumers listen for order events and handle inventory and payment processing asynchronously.

6️⃣ Frontend Setup (React)
Navigate to the frontend directory:
cd ../frontend
Install dependencies:

npm install

Start the development server:
npm run dev

This will launch the frontend app, usually accessible at http://localhost:5173
