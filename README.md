# Program for changing IP addresses on Windows

----
## Building exe file:
```shell
pyinstaller --uac-admin --noconsole --add-data="./main/scripts;./scripts/" --clean --onefile .\main\app.py
```
where:  
`--uac-admin` - run exe as admin  
`--onefile` - compile to single exe file  
`--add-data` - add additional files  
`--noconsole` - run without python console open  
`--clean` - delete previous build data  
