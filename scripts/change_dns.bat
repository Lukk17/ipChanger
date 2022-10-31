@echo on
setlocal

SET INTERFACE="%2 %3"
SET GATEWAY=%1

netsh interface ip set dns name=%INTERFACE% static %GATEWAY%

endlocal

