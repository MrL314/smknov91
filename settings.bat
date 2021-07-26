@echo OFF

SET python_cmd="python"










REM ======= DONT TOUCH ANYTHING BELOW HERE =======



SET sett_clld=%1
if "%sett_clld%"=="" goto :ps
goto :endif

:ps
pause

:endif

SET sett_clld=""