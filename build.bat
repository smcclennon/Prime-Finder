@echo off
(
  make & make clean
  set foundErr=1
  if errorlevel 0 if not errorlevel 1 set "foundErr="
  if defined foundErr (
  (
  mingw32-make & mingw32-make clean
  set foundErr=1
  if errorlevel 0 if not errorlevel 1 set "foundErr="
  if defined foundErr echo Build complete
)
  )
)
timeout 3