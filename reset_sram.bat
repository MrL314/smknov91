@echo OFF

echo [INFO] RESETTING SRAM FILE.

SET reset_clld=%1

CALL settings.bat 1

%python_cmd% drv_data.py


if "%reset_clld%"=="" goto :ps
goto :endif

:ps
pause

:endif

SET reset_clld=""