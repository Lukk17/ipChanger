@echo on
setlocal

SET INTERFACE="%1 %2"

netsh interface ip set address name=%INTERFACE% dhcp

endlocal
pause
