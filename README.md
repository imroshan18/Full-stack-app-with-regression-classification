
# EventIntel Suite

### Full-Stack Machine Learning System for Event Risk & Attendance Forecasting

EventIntel Suite is a production-style full-stack machine learning application that supports data-driven decision-making for outdoor event planning.

The platform combines:

* Binary classification for feasibility assessment
* Regression modeling for attendance forecasting
* FastAPI backend for prediction serving
* Gradio-based interactive frontend
* Structured training and deployment workflow

This project demonstrates the integration of machine learning models into a deployable web-based system.

---

## Author

**imroshan18**

---

## Project Objective

Outdoor event planning involves uncertainty related to weather conditions and marketing impact. This system answers two critical operational questions:

1. Should the event proceed under forecasted conditions?
2. If approved, how many attendees can be expected?

By combining classification and regression models, the platform provides both strategic and quantitative insights.

---

## System Architecture

The application follows a decoupled full-stack architecture.

### 1. Machine Learning Layer

Two Decision Tree models are implemented using Scikit-learn:

* **Decision Tree Classifier**

  * Predicts whether the event is likely to succeed or be cancelled.

* **Decision Tree Regressor**

  * Estimates the number of expected attendees.

Both models are trained on structured environmental and marketing-related features.

---

### 2. Backend API (FastAPI)

FastAPI serves as the prediction interface:

* Loads serialized models
* Accepts feature inputs via REST endpoints
* Returns structured JSON responses
* Handles classification and regression simultaneously

This ensures scalability and clean separation between logic and presentation.

---

### 3. Frontend Dashboard (Gradio)

The frontend provides:

* Interactive sliders for numerical inputs
* Boolean toggle for weekend indicator
* Real-time prediction results
* User-friendly event analysis display

---

### 4. Service Orchestration

A unified runner script manages:

* Backend initialization
* Frontend launch
* Multi-process synchronization

This mirrors real-world microservice coordination.

---

## Feature Engineering

The synthetic dataset simulates practical event planning factors:

* **Temperature (°C)** – Expected event-day temperature
* **Rain Probability (%)** – Likelihood of precipitation
* **Social Media Reach** – Promotional campaign intensity
* **Is Weekend (0 or 1)** – Event scheduling timing

These features influence both feasibility and attendance outcomes.

---

## Technology Stack

| Layer                | Technology    |
| -------------------- | ------------- |
| ML Framework         | Scikit-learn  |
| Backend API          | FastAPI       |
| Frontend             | Gradio        |
| Data Handling        | Pandas, NumPy |
| Model Serialization  | Joblib        |
| Programming Language | Python 3.8+   |

---

## Installation & Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Train the Models

Before running the application, generate the trained models:

```bash
python train.py
```

This will:

* Create a synthetic dataset file
* Train both classification and regression models
* Save serialized models into the `models/` directory

---

### 3. Run the Application

Start both backend and frontend:

```bash
python run.py
```

---

### 4. Access the Dashboard

Open:

```
http://localhost:7860
```

---

## Application Workflow

1. Launch the system.
2. Input forecast parameters:

   * Temperature
   * Rain Probability
   * Social Media Reach
   * Weekend Indicator
3. Click “Analyze Event.”
4. View results:

   * Go / No-Go decision
   * Expected attendance number
   * Risk explanation message

---

## Output Description

### Classification Result

Binary output:

* **Approved (Go)**
* **Cancelled (No-Go)**

### Regression Result

Numerical forecast representing expected attendance.

### Contextual Insight

System-generated explanation based on input conditions.

---

## Project Structure

```
EventIntel-Suite/
│
├── main.py            # FastAPI backend
├── frontend.py        # Gradio interface
├── train.py           # Model training script
├── run.py             # Unified runner
├── requirements.txt
├── models/            # Serialized ML models
└── README.md
```

---

## Design Principles

* Clear separation of ML and API layers
* Reproducible training pipeline
* Modular architecture
* Full-stack integration
* Production-style deployment simulation

---

## Future Enhancements

* Replace synthetic dataset with real-world data
* Add model evaluation dashboard
* Integrate database for historical event tracking
* Deploy via Docker container
* Add user authentication
* Integrate weather API for live predictions

---

## Professional Positioning

This project demonstrates competency in:

* End-to-end ML deployment
* Full-stack application development
* REST API construction
* Model serialization and serving
* Decision tree implementation
* Feature engineering

