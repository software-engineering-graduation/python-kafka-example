# RabbitMQ with Python

## Overview

This project demonstrates the use of RabbitMQ with Python, showcasing two message handling patterns: 
- **Pub/Sub (Publisher/Subscriber)**
- **Queue-based messaging**.

Using **Docker** to set up **RabbitMQ** and its management interface. Python scripts are provided to simulate the interaction with the RabbitMQ message broker for both pub/sub and queue-based communication.

## Project Structure

```
.
├── README.md
├── docker-compose.yml
├── rabbit-pub_sub
│   ├── pub.py          # Publisher script
│   └── sub.py          # Subscriber script
├── rabbit-queue
│   ├── consumer.py     # Consumer script
│   └── producer.py     # Producer script
└── requirements.txt    # Python dependencies
```

## Getting Started

### 1. Set up RabbitMQ with Docker

The provided `docker-compose.yml` file launches a RabbitMQ container with the management interface.

To start the container:
```bash
docker-compose up -d
```

This will:
- Launch RabbitMQ on port **5672** (for messaging).
- Make the RabbitMQ management UI available on **port 15672**.

### 2. Install Dependencies

Before running the Python scripts, install the necessary dependencies:
```bash
pip install -r requirements.txt
```

### 3. Pub/Sub Model

#### Publisher

The publisher script (`pub.py`) announces new flavors by sending messages to a topic exchange named `flavors`.

Run the publisher:
```bash
python rabbit-pub_sub/pub.py
```

#### Subscriber

The subscriber script (`sub.py`) listens for new flavor announcements by consuming messages from the `flavors` exchange.

Run the subscriber:
```bash
python rabbit-pub_sub/sub.py
```

### 4. Queue-Based Messaging

#### Producer

The producer script (`producer.py`) sends new ice cream orders to a queue named `sorvete_queue`.

Run the producer:
```bash
python rabbit-queue/producer.py
```

#### Consumer

The consumer script (`consumer.py`) listens to the `sorvete_queue` and processes orders.

Run the consumer:
```bash
python rabbit-queue/consumer.py
```