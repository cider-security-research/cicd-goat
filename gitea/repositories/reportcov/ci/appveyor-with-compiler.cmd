:: Very simple setup:
:: - if WINDOWS_SDK_VERSION is set then activate the SDK.
:: - disable the WDK if it's around.

SET COMMAND_TO_RUN=%*
SET WIN_SDK_ROOT=C:\Program Files\Microsoft SDKs\Windows
SET WIN_WDK="c:\Program Files (x86)\Windows Kits\10\Include\wdf"
ECHO SDK: %WINDOWS_SDK_VERSION% ARCH: %PYTHON_ARCH%

IF EXIST %WIN_WDK% (
    REM See: https://connect.microsoft.com/VisualStudio/feedback/details/1610302/
    REN %WIN_WDK% 0wdf
)
IF "%WINDOWS_SDK_VERSION%"=="" GOTO main

SET DISTUTILS_USE_SDK=1
SET MSSdk=1
"%WIN_SDK_ROOT%\%WINDOWS_SDK_VERSION%\Setup\WindowsSdkVer.exe" -q -version:%WINDOWS_SDK_VERSION%
CALL "%WIN_SDK_ROOT%\%WINDOWS_SDK_VERSION%\Bin\SetEnv.cmd" /x64 /release

:main
ECHO Executing: %COMMAND_TO_RUN%
CALL %COMMAND_TO_RUN% || EXIT 1
