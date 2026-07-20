@echo off

title GameSense AI


echo ===============================
echo Starting GameSense AI
echo ===============================


echo.
echo [1/3] Starting Backend...


start "GameSense Backend" cmd /k "cd /d D:\my\GameSense-AI\backend && python -m uvicorn main:app --reload --app-dir D:\my\GameSense-AI\backend"



timeout /t 5 >nul



echo.
echo [2/3] Starting Frontend...


start "GameSense Frontend" cmd /k "cd /d D:\my\GameSense-AI\frontend && npm run dev"



timeout /t 8 >nul



echo.
echo [3/3] Opening Browser...


start http://localhost:5173/


pause