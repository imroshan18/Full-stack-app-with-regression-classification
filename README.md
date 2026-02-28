# SmartEvent Pro: Integrated Event Risk and Attendance Prediction System

## Overview
SmartEvent Pro is a comprehensive full-stack machine learning application designed to optimize outdoor event planning. The system addresses two primary operational questions for event organizers:
1. **Feasibility (Classification):** Should the event proceed given the forecasted weather conditions?
2. **Attendance (Regression):** If the event proceeds, how many attendees are expected to arrive?

By combining a Decision Tree Classifier and a Decision Tree Regressor, the system provides a unified decision-making tool that bridges risk management with resource allocation.

## Technical Architecture
The application is built using a modern decoupled architecture:
*   **Machine Learning Engine:** Scikit-learn implementation of Decision Tree algorithms for both binary classification and continuous regression tasks.
*   **Backend API:** FastAPI provides a high-performance RESTful interface for serving model predictions.
*   **Frontend Interface:** Gradio-based dashboard offering an intuitive user experience for parameter input and visualization of results.
*   **Integration Layer:** A multi-process manager that synchronizes the backend and frontend services.

## Dataset and Features
The models are trained on a synthetic dataset designed to mirror real-world environmental and promotional influences:
*   **Temperature (°C):** Numerical value representing the forecasted event temperature.
*   **Rain Probability (%):** Numerical value (0-100) representing the likelihood of precipitation.
*   **Social Media Reach:** Numerical value representing the scale of the marketing effort.
*   **Is Weekend:** Boolean indicator (0 or 1) representing the timing of the event.

## Installation and Setup

### Prerequisites
*   Python 3.8 or higher
*   Git (for version control)

### Step 1: Install Dependencies
Download the necessary libraries using the provided requirements file:
```bash
pip install -r requirements.txt
```

### Step 2: Model Training
The models must be trained before the first execution to generate the serialized model files:
```bash
python train.py
```
This script will generate `smartevent_data.csv` and save the serialized models in the `models/` directory.

### Step 3: Launch the Application
Execute the unified runner script to start both the FastAPI backend and the Gradio frontend:
```bash
python run.py
```

## Operation Guide
1. Launch the application as described above.
2. Access the frontend dashboard at `http://localhost:7860`.
3. Adjust the sliders for Temperature, Rain Probability, and Social Media Reach.
4. Toggle the Weekend checkbox according to the planned event date.
5. Click **Analyze Event** to retrieve the dual-model prediction.
6. The "Event Status" box will indicate the Go/No-Go decision, while the "Expected Attendance" box provides the numerical forecast for planning.

## System Outputs
*   **Classification Output:** A binary status of "Success" (Go) or "Cancelled" (No-Go).
*   **Regression Output:** A non-negative integer representing the estimated turnout.
*   **Risk Message:** A context-aware explanation of the prediction (e.g., weather warnings or favorable conditions).
