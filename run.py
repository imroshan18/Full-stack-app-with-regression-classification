import subprocess
import time
import sys
import os

def run_app():
    print("🚀 Starting SmartEvent Pro System...")
    
    # 1. Start FastAPI Backend
    print("Starting FastAPI Backend (Port 8000)...")
    backend_process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    
    # Wait for backend to start
    time.sleep(3)
    
    # Check if backend is running
    if backend_process.poll() is not None:
        print("❌ Failed to start FastAPI Backend.")
        output, _ = backend_process.communicate()
        print(output)
        return

    # 2. Start Gradio Frontend
    print("Starting Gradio Frontend (Port 7860)...")
    frontend_process = subprocess.Popen(
        [sys.executable, "frontend.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    
    print("\n✅ System is up and running!")
    print("👉 Backend: http://localhost:8000")
    print("👉 Frontend: http://localhost:7860")
    print("\nPress Ctrl+C to stop both servers.")
    
    try:
        while True:
            # Print output from processes to console
            line_b = backend_process.stdout.readline()
            if line_b:
                print(f"[Backend] {line_b.strip()}")
            
            line_f = frontend_process.stdout.readline()
            if line_f:
                print(f"[Frontend] {line_f.strip()}")
                
            if backend_process.poll() is not None or frontend_process.poll() is not None:
                break
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n🛑 Shutting down servers...")
        backend_process.terminate()
        frontend_process.terminate()
        print("Cleanup complete.")

if __name__ == "__main__":
    run_app()
