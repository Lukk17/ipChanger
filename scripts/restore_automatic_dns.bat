@echo on
setlocal

SET INTERFACE="%1 %2"

netsh interface ip set dns name=%INTERFACE% dhcp

endlocal
pause
