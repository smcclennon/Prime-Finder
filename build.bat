:: Primer++
:: github.com/smcclennon/Primer

@echo off
set "source_file=Primer++.cpp"
set "resource_file=Primer++.o"
set "output_file=Primer++.exe"

echo Building %output_file%...
g++ "%source_file%" "%resource_file%" -o "%output_file%" --static -pedantic -Wall -Wextra -Wcast-align -Wcast-qual -Wctor-dtor-privacy -Wdisabled-optimization -Wformat=2 -Winit-self -Wlogical-op -Wmissing-declarations -Wmissing-include-dirs -Wnoexcept -Wold-style-cast -Woverloaded-virtual -Wredundant-decls -Wshadow -Wsign-conversion -Wsign-promo -Wstrict-null-sentinel -Wstrict-overflow=5 -Wswitch-default -Wundef -Werror -Wno-unused
echo Build complete!
timeout 3