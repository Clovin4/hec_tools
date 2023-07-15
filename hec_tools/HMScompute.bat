set "HMS=C:\Program Files\HEC\HEC-HMS\4.9"
set "PATH=%HMS%\bin\gdal;%PATH%"
set "GDAL_DRIVER_PATH=%HMS%\bin\gdal\gdalplugins"
set "GDAL_DATA=%HMS%\bin\gdal\gdal-data"
set "PROJ_LIB=%HMS%\bin\gdal\projlib"

set "CLASSPATH=%HMS%\hms.jar;%HMS%\lib\*"
C:\jython2.7.3\bin\jython.exe -Djava.library.path="%HMS%\bin;%HMS%\bin\gdal" HMScompute.py %1 %2