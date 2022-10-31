@echo on
setlocal

SET INTERFACE="%4 %5"
SET IP_ADDR=%1
SET SUBNET=%2
SET GATEWAY=%3

netsh interface ip set address name=%INTERFACE% static %IP_ADDR% %SUBNET% %GATEWAY%

endlocal

