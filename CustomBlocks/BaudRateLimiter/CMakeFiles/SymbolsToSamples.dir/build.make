# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/xongile/Lab-Project/CustomBlocks/BaudRateLimiter

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/xongile/Lab-Project/CustomBlocks/BaudRateLimiter

# Include any dependencies generated for this target.
include CMakeFiles/SymbolsToSamples.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/SymbolsToSamples.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/SymbolsToSamples.dir/flags.make

SymbolsToSamplesDocs.cpp: SymbolsToSamples.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/xongile/Lab-Project/CustomBlocks/BaudRateLimiter/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating SymbolsToSamplesDocs.cpp"
	./PothosUtil.sh --doc-parse SymbolsToSamples.cpp --output /home/xongile/Lab-Project/CustomBlocks/BaudRateLimiter/SymbolsToSamplesDocs.cpp

CMakeFiles/SymbolsToSamples.dir/SymbolsToSamples.cpp.o: CMakeFiles/SymbolsToSamples.dir/flags.make
CMakeFiles/SymbolsToSamples.dir/SymbolsToSamples.cpp.o: SymbolsToSamples.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xongile/Lab-Project/CustomBlocks/BaudRateLimiter/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/SymbolsToSamples.dir/SymbolsToSamples.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/SymbolsToSamples.dir/SymbolsToSamples.cpp.o -c /home/xongile/Lab-Project/CustomBlocks/BaudRateLimiter/SymbolsToSamples.cpp

CMakeFiles/SymbolsToSamples.dir/SymbolsToSamples.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/SymbolsToSamples.dir/SymbolsToSamples.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xongile/Lab-Project/CustomBlocks/BaudRateLimiter/SymbolsToSamples.cpp > CMakeFiles/SymbolsToSamples.dir/SymbolsToSamples.cpp.i

CMakeFiles/SymbolsToSamples.dir/SymbolsToSamples.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/SymbolsToSamples.dir/SymbolsToSamples.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xongile/Lab-Project/CustomBlocks/BaudRateLimiter/SymbolsToSamples.cpp -o CMakeFiles/SymbolsToSamples.dir/SymbolsToSamples.cpp.s

CMakeFiles/SymbolsToSamples.dir/SymbolsToSamples.cpp.o.requires:

.PHONY : CMakeFiles/SymbolsToSamples.dir/SymbolsToSamples.cpp.o.requires

CMakeFiles/SymbolsToSamples.dir/SymbolsToSamples.cpp.o.provides: CMakeFiles/SymbolsToSamples.dir/SymbolsToSamples.cpp.o.requires
	$(MAKE) -f CMakeFiles/SymbolsToSamples.dir/build.make CMakeFiles/SymbolsToSamples.dir/SymbolsToSamples.cpp.o.provides.build
.PHONY : CMakeFiles/SymbolsToSamples.dir/SymbolsToSamples.cpp.o.provides

CMakeFiles/SymbolsToSamples.dir/SymbolsToSamples.cpp.o.provides.build: CMakeFiles/SymbolsToSamples.dir/SymbolsToSamples.cpp.o


CMakeFiles/SymbolsToSamples.dir/SymbolsToSamplesDocs.cpp.o: CMakeFiles/SymbolsToSamples.dir/flags.make
CMakeFiles/SymbolsToSamples.dir/SymbolsToSamplesDocs.cpp.o: SymbolsToSamplesDocs.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xongile/Lab-Project/CustomBlocks/BaudRateLimiter/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/SymbolsToSamples.dir/SymbolsToSamplesDocs.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/SymbolsToSamples.dir/SymbolsToSamplesDocs.cpp.o -c /home/xongile/Lab-Project/CustomBlocks/BaudRateLimiter/SymbolsToSamplesDocs.cpp

CMakeFiles/SymbolsToSamples.dir/SymbolsToSamplesDocs.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/SymbolsToSamples.dir/SymbolsToSamplesDocs.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xongile/Lab-Project/CustomBlocks/BaudRateLimiter/SymbolsToSamplesDocs.cpp > CMakeFiles/SymbolsToSamples.dir/SymbolsToSamplesDocs.cpp.i

CMakeFiles/SymbolsToSamples.dir/SymbolsToSamplesDocs.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/SymbolsToSamples.dir/SymbolsToSamplesDocs.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xongile/Lab-Project/CustomBlocks/BaudRateLimiter/SymbolsToSamplesDocs.cpp -o CMakeFiles/SymbolsToSamples.dir/SymbolsToSamplesDocs.cpp.s

CMakeFiles/SymbolsToSamples.dir/SymbolsToSamplesDocs.cpp.o.requires:

.PHONY : CMakeFiles/SymbolsToSamples.dir/SymbolsToSamplesDocs.cpp.o.requires

CMakeFiles/SymbolsToSamples.dir/SymbolsToSamplesDocs.cpp.o.provides: CMakeFiles/SymbolsToSamples.dir/SymbolsToSamplesDocs.cpp.o.requires
	$(MAKE) -f CMakeFiles/SymbolsToSamples.dir/build.make CMakeFiles/SymbolsToSamples.dir/SymbolsToSamplesDocs.cpp.o.provides.build
.PHONY : CMakeFiles/SymbolsToSamples.dir/SymbolsToSamplesDocs.cpp.o.provides

CMakeFiles/SymbolsToSamples.dir/SymbolsToSamplesDocs.cpp.o.provides.build: CMakeFiles/SymbolsToSamples.dir/SymbolsToSamplesDocs.cpp.o


# Object files for target SymbolsToSamples
SymbolsToSamples_OBJECTS = \
"CMakeFiles/SymbolsToSamples.dir/SymbolsToSamples.cpp.o" \
"CMakeFiles/SymbolsToSamples.dir/SymbolsToSamplesDocs.cpp.o"

# External object files for target SymbolsToSamples
SymbolsToSamples_EXTERNAL_OBJECTS =

libSymbolsToSamples.so: CMakeFiles/SymbolsToSamples.dir/SymbolsToSamples.cpp.o
libSymbolsToSamples.so: CMakeFiles/SymbolsToSamples.dir/SymbolsToSamplesDocs.cpp.o
libSymbolsToSamples.so: CMakeFiles/SymbolsToSamples.dir/build.make
libSymbolsToSamples.so: /usr/lib/x86_64-linux-gnu/libPothos.so
libSymbolsToSamples.so: /usr/lib/libPocoUtil.so.50
libSymbolsToSamples.so: /usr/lib/libPocoXML.so.50
libSymbolsToSamples.so: /usr/lib/libPocoNet.so.50
libSymbolsToSamples.so: /usr/lib/x86_64-linux-gnu/libexpat.so
libSymbolsToSamples.so: /usr/lib/libPocoJSON.so.50
libSymbolsToSamples.so: /usr/lib/libPocoFoundation.so.50
libSymbolsToSamples.so: /usr/lib/x86_64-linux-gnu/libpcre.so
libSymbolsToSamples.so: /usr/lib/x86_64-linux-gnu/libz.so
libSymbolsToSamples.so: CMakeFiles/SymbolsToSamples.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/xongile/Lab-Project/CustomBlocks/BaudRateLimiter/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX shared module libSymbolsToSamples.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/SymbolsToSamples.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/SymbolsToSamples.dir/build: libSymbolsToSamples.so

.PHONY : CMakeFiles/SymbolsToSamples.dir/build

CMakeFiles/SymbolsToSamples.dir/requires: CMakeFiles/SymbolsToSamples.dir/SymbolsToSamples.cpp.o.requires
CMakeFiles/SymbolsToSamples.dir/requires: CMakeFiles/SymbolsToSamples.dir/SymbolsToSamplesDocs.cpp.o.requires

.PHONY : CMakeFiles/SymbolsToSamples.dir/requires

CMakeFiles/SymbolsToSamples.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/SymbolsToSamples.dir/cmake_clean.cmake
.PHONY : CMakeFiles/SymbolsToSamples.dir/clean

CMakeFiles/SymbolsToSamples.dir/depend: SymbolsToSamplesDocs.cpp
	cd /home/xongile/Lab-Project/CustomBlocks/BaudRateLimiter && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/xongile/Lab-Project/CustomBlocks/BaudRateLimiter /home/xongile/Lab-Project/CustomBlocks/BaudRateLimiter /home/xongile/Lab-Project/CustomBlocks/BaudRateLimiter /home/xongile/Lab-Project/CustomBlocks/BaudRateLimiter /home/xongile/Lab-Project/CustomBlocks/BaudRateLimiter/CMakeFiles/SymbolsToSamples.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/SymbolsToSamples.dir/depend

