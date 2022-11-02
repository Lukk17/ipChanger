@echo on
setlocal enabledelayedexpansion

SET INTERFACE="%4"
SET IP_ADDR=%1
SET SUBNET=%2
SET GATEWAY=%3

if not defined %~5 SET INTERFACE="%4 %5"
if not defined %~6 SET INTERFACE="%4 %5 %6"
if not defined %~7 SET INTERFACE="%4 %5 %6 %7"
if not defined %~8 SET INTERFACE="%4 %5 %6 %7 %8"
if not defined %~9 SET INTERFACE="%4 %5 %6 %7 %8 %9"

echo %INTERFACE%

:: "1" at end is for metric (better leave as is)
netsh interface ip set address name=%INTERFACE% static %IP_ADDR% %SUBNET% %GATEWAY% 1

endlocal
::pause
