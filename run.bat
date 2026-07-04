@echo off
title Job Acceptance Prediction System
color 0A

echo ================================================================================
echo                         🎯 JOB ACCEPTANCE PREDICTION SYSTEM
echo ================================================================================
echo.
echo  ╔══════════════════════════════════════════════════════════════════════════════╗
echo  ║                                                                              ║
echo  ║   🚀 Starting the Professional Dashboard...                                  ║
echo  ║   📊 AI-powered HR Analytics System                                           ║
echo  ║   🔮 Powered by Random Forest with 88.6%% Accuracy                            ║
echo  ║                                                                              ║
echo  ╚══════════════════════════════════════════════════════════════════════════════╝
echo.
echo.

echo [1/4] Navigating to project directory...
cd /d "D:\Job Application Pred"
echo ✅ Project directory: %cd%
echo.

echo [2/4] Checking Python 3.10 installation...
py -3.10 --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python 3.10 not found!
    echo.
    echo 🔧 Please install Python 3.10 from:
    echo    https://www.python.org/downloads/release/python-31011/
    echo.
    echo 📥 Download: python-3.10.11-amd64.exe
    echo.
    pause
    exit /b 1
)
echo ✅ Python 3.10 is installed
py -3.10 --version
echo.

echo [3/4] Installing required packages (this may take a moment)...
echo.
py -3.10 -m pip install --quiet streamlit pandas numpy scikit-learn matplotlib seaborn plotly joblib
echo ✅ All packages installed successfully!
echo.

echo [4/4] Starting Streamlit Dashboard...
echo.
echo ================================================================================
echo  🌐 Opening dashboard in your browser...
echo  📱 Local URL: http://localhost:8501
echo  🌍 Network URL: http://192.168.1.33:8501
echo  📊 Dashboard Features:
echo     • Real-time Job Acceptance Prediction
echo     • Interactive Analytics Dashboard
echo     • Advanced Data Explorer
echo  ⚡ Press Ctrl+C to stop the server
echo ================================================================================
echo.

py -3.10 -m streamlit run app.py --server.port 8501 --server.headless true --server.enableCORS false

pause