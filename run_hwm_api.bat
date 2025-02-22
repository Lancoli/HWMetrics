@echo off
setlocal
:: This command runs the executable as administrator
powershell -Command "Start-Process 'C:\Users\david\Downloads\openhardwaremonitor-v0.9.6\OpenHardwareMonitor\OpenHardwareMonitor.exe' -Verb runAs"
