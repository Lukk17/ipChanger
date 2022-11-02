@echo on
setlocal

SET INTERFACE="%1"

if not defined %~2 SET INTERFACE="%1 %2"
if not defined %~3 SET INTERFACE="%1 %2 %3"
if not defined %~4 SET INTERFACE="%1 %2 %3 %4"
if not defined %~5 SET INTERFACE="%1 %2 %3 %4 %5"
if not defined %~6 SET INTERFACE="%1 %2 %3 %4 %5 %6"
if not defined %~7 SET INTERFACE="%1 %2 %3 %4 %5 %6 %7"
if not defined %~8 SET INTERFACE="%1 %2 %3 %4 %5 %6 %7 %8"
if not defined %~9 SET INTERFACE="%1 %2 %3 %4 %5 %6 %7 %8 %9"

netsh interface ip set dns name=%INTERFACE% dhcp

endlocal
