import gradio as gr
import requests
import json

# API URL
API_URL = "http://localhost:8000/predict"

def predict_event(temp, rain_prob, social_reach, is_weekend):
    # Convert checkbox to int
    is_weekend_int = 1 if is_weekend else 0
    
    # Prepare payload
    payload = {
        "temp": temp,
        "rain_prob": rain_prob,
        "social_reach": social_reach,
        "is_weekend": is_weekend_int
    }
    
    try:
        # Call FastAPI backend
        response = requests.post(API_URL, json=payload)
        result = response.json()
        
        status = result['status']
        attendance = result['attendance']
        message = result['message']
        
        # Determine color/style based on status
        color = "🟢" if status == "Success" else "🔴"
        
        return (
            f"{color} {status}", 
            f"{attendance} People",
            message
        )
    except Exception as e:
        return "Error", "Error", f"Could not connect to backend: {str(e)}"

# Define the custom CSS for a premium look
custom_css = """
.container { 
    max-width: 900px; 
    margin: auto; 
    padding-top: 2rem;
}
.header {
    text-align: center;
    margin-bottom: 2rem;
    color: #2D3748;
}
.output-box {
    border-radius: 12px;
    padding: 20px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
}
"""

with gr.Blocks(css=custom_css, title="SmartEvent Pro") as demo:
    gr.Markdown(
        """
        # 📅 SmartEvent Pro
        ### The AI-Powered Outdoor Event Optimizer
        *Optimize your event planning with combined Classification (Risk) and Regression (Attendance) models.*
        """
    )
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 🛠️ Event Parameters")
            temp = gr.Slider(minimum=5, maximum=40, value=22, label="🌡️ Temperature (°C)")
            rain_prob = gr.Slider(minimum=0, maximum=100, value=15, label="🌧️ Rain Probability (%)")
            social_reach = gr.Slider(minimum=50, maximum=5000, value=500, label="📢 Social Media Reach")
            is_weekend = gr.Checkbox(label="🗓️ Is it a Weekend?", value=True)
            submit_btn = gr.Button("Analyze Event", variant="primary")
            
        with gr.Column(scale=1):
            gr.Markdown("### 📊 AI Predictions")
            with gr.Group():
                status_out = gr.Textbox(label="Event Status (Classification)", interactive=False)
                attendance_out = gr.Textbox(label="Expected Attendance (Regression)", interactive=False)
                message_out = gr.Markdown("Click 'Analyze Event' to see results.")
                
    submit_btn.click(
        fn=predict_event,
        inputs=[temp, rain_prob, social_reach, is_weekend],
        outputs=[status_out, attendance_out, message_out]
    )
    
    gr.Examples(
        examples=[
            [25, 10, 800, True],
            [12, 60, 400, False],
            [30, 5, 2000, True],
            [8, 20, 300, False]
        ],
        inputs=[temp, rain_prob, social_reach, is_weekend]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
