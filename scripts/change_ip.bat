@echo on
setlocal

SET INTERFACE="%4 %5"
SET IP_ADDR=%1
SET SUBNET=%2
SET GATEWAY=%3

REM "1" at end is for metric (better leave as is)
netsh interface ip set address name=%INTERFACE% static %IP_ADDR% %SUBNET% %GATEWAY% 1


endlocal
