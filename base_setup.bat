@echo OFF

CALL settings.bat 1


%python_cmd% hex2bin_fixed.py game.hex

CALL reset_sram.bat 1

copy "Super Mario Kart (USA).sfc" "TEMP.TMP" >NUL

echo [INFO] Applying step 1 of patch
flips.exe "NovFix.bps" "Super Mario Kart (USA).sfc"

copy "Super Mario Kart (USA).sfc" "FIX2.bps" >NUL
copy "game.hex.bin" "TEST.sfc" >NUL

echo [INFO] Applying step 2 of patch
flips.exe "FIX2.bps" "TEST.sfc"

del "FIX2.bps"

del "Super Mario Kart (USA).sfc"

copy "TEMP.TMP" "Super Mario Kart (USA).sfc" >NUL

del "TEMP.TMP"

copy "TEST.sfc" "Nov91.sfc" >NUL

del "TEST.sfc"

pause