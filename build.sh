#!/bin/sh
# Primer++
# github.com/smcclennon/Primer
# Tested with MacOS Catalina 10.15.4 with Apple clang 11.0.3

echo Warning: This build command has only been tested on MacOS Catalina 10.15.4 with Apple clang 11.0.3
echo This is MacOS only and may not work on other versions of MacOS (and/or) Apple clang
echo Building...
# chmod +x build.sh
gcc++ Primer++.cpp -o Primer++ -std=c++17
echo Build complete!
./Primer++