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
CMAKE_SOURCE_DIR = /home/xongile/Lab-Project/CustomBlocks/CCEncoder

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/xongile/Lab-Project/CustomBlocks/CCEncoder

# Include any dependencies generated for this target.
include CMakeFiles/CCEncoder.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/CCEncoder.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/CCEncoder.dir/flags.make

CCEncoderDocs.cpp: CCEncoder.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/xongile/Lab-Project/CustomBlocks/CCEncoder/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating CCEncoderDocs.cpp"
	./PothosUtil.sh --doc-parse CCEncoder.cpp --output /home/xongile/Lab-Project/CustomBlocks/CCEncoder/CCEncoderDocs.cpp

CMakeFiles/CCEncoder.dir/CCEncoder.cpp.o: CMakeFiles/CCEncoder.dir/flags.make
CMakeFiles/CCEncoder.dir/CCEncoder.cpp.o: CCEncoder.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xongile/Lab-Project/CustomBlocks/CCEncoder/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/CCEncoder.dir/CCEncoder.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/CCEncoder.dir/CCEncoder.cpp.o -c /home/xongile/Lab-Project/CustomBlocks/CCEncoder/CCEncoder.cpp

CMakeFiles/CCEncoder.dir/CCEncoder.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/CCEncoder.dir/CCEncoder.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xongile/Lab-Project/CustomBlocks/CCEncoder/CCEncoder.cpp > CMakeFiles/CCEncoder.dir/CCEncoder.cpp.i

CMakeFiles/CCEncoder.dir/CCEncoder.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/CCEncoder.dir/CCEncoder.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xongile/Lab-Project/CustomBlocks/CCEncoder/CCEncoder.cpp -o CMakeFiles/CCEncoder.dir/CCEncoder.cpp.s

CMakeFiles/CCEncoder.dir/CCEncoder.cpp.o.requires:

.PHONY : CMakeFiles/CCEncoder.dir/CCEncoder.cpp.o.requires

CMakeFiles/CCEncoder.dir/CCEncoder.cpp.o.provides: CMakeFiles/CCEncoder.dir/CCEncoder.cpp.o.requires
	$(MAKE) -f CMakeFiles/CCEncoder.dir/build.make CMakeFiles/CCEncoder.dir/CCEncoder.cpp.o.provides.build
.PHONY : CMakeFiles/CCEncoder.dir/CCEncoder.cpp.o.provides

CMakeFiles/CCEncoder.dir/CCEncoder.cpp.o.provides.build: CMakeFiles/CCEncoder.dir/CCEncoder.cpp.o


CMakeFiles/CCEncoder.dir/CCEncoderDocs.cpp.o: CMakeFiles/CCEncoder.dir/flags.make
CMakeFiles/CCEncoder.dir/CCEncoderDocs.cpp.o: CCEncoderDocs.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xongile/Lab-Project/CustomBlocks/CCEncoder/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/CCEncoder.dir/CCEncoderDocs.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/CCEncoder.dir/CCEncoderDocs.cpp.o -c /home/xongile/Lab-Project/CustomBlocks/CCEncoder/CCEncoderDocs.cpp

CMakeFiles/CCEncoder.dir/CCEncoderDocs.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/CCEncoder.dir/CCEncoderDocs.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xongile/Lab-Project/CustomBlocks/CCEncoder/CCEncoderDocs.cpp > CMakeFiles/CCEncoder.dir/CCEncoderDocs.cpp.i

CMakeFiles/CCEncoder.dir/CCEncoderDocs.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/CCEncoder.dir/CCEncoderDocs.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xongile/Lab-Project/CustomBlocks/CCEncoder/CCEncoderDocs.cpp -o CMakeFiles/CCEncoder.dir/CCEncoderDocs.cpp.s

CMakeFiles/CCEncoder.dir/CCEncoderDocs.cpp.o.requires:

.PHONY : CMakeFiles/CCEncoder.dir/CCEncoderDocs.cpp.o.requires

CMakeFiles/CCEncoder.dir/CCEncoderDocs.cpp.o.provides: CMakeFiles/CCEncoder.dir/CCEncoderDocs.cpp.o.requires
	$(MAKE) -f CMakeFiles/CCEncoder.dir/build.make CMakeFiles/CCEncoder.dir/CCEncoderDocs.cpp.o.provides.build
.PHONY : CMakeFiles/CCEncoder.dir/CCEncoderDocs.cpp.o.provides

CMakeFiles/CCEncoder.dir/CCEncoderDocs.cpp.o.provides.build: CMakeFiles/CCEncoder.dir/CCEncoderDocs.cpp.o


# Object files for target CCEncoder
CCEncoder_OBJECTS = \
"CMakeFiles/CCEncoder.dir/CCEncoder.cpp.o" \
"CMakeFiles/CCEncoder.dir/CCEncoderDocs.cpp.o"

# External object files for target CCEncoder
CCEncoder_EXTERNAL_OBJECTS =

libCCEncoder.so: CMakeFiles/CCEncoder.dir/CCEncoder.cpp.o
libCCEncoder.so: CMakeFiles/CCEncoder.dir/CCEncoderDocs.cpp.o
libCCEncoder.so: CMakeFiles/CCEncoder.dir/build.make
libCCEncoder.so: /usr/lib/x86_64-linux-gnu/libPothos.so
libCCEncoder.so: /usr/lib/libPocoUtil.so.50
libCCEncoder.so: /usr/lib/libPocoXML.so.50
libCCEncoder.so: /usr/lib/libPocoNet.so.50
libCCEncoder.so: /usr/lib/x86_64-linux-gnu/libexpat.so
libCCEncoder.so: /usr/lib/libPocoJSON.so.50
libCCEncoder.so: /usr/lib/libPocoFoundation.so.50
libCCEncoder.so: /usr/lib/x86_64-linux-gnu/libpcre.so
libCCEncoder.so: /usr/lib/x86_64-linux-gnu/libz.so
libCCEncoder.so: CMakeFiles/CCEncoder.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/xongile/Lab-Project/CustomBlocks/CCEncoder/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX shared module libCCEncoder.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/CCEncoder.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/CCEncoder.dir/build: libCCEncoder.so

.PHONY : CMakeFiles/CCEncoder.dir/build

CMakeFiles/CCEncoder.dir/requires: CMakeFiles/CCEncoder.dir/CCEncoder.cpp.o.requires
CMakeFiles/CCEncoder.dir/requires: CMakeFiles/CCEncoder.dir/CCEncoderDocs.cpp.o.requires

.PHONY : CMakeFiles/CCEncoder.dir/requires

CMakeFiles/CCEncoder.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/CCEncoder.dir/cmake_clean.cmake
.PHONY : CMakeFiles/CCEncoder.dir/clean

CMakeFiles/CCEncoder.dir/depend: CCEncoderDocs.cpp
	cd /home/xongile/Lab-Project/CustomBlocks/CCEncoder && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/xongile/Lab-Project/CustomBlocks/CCEncoder /home/xongile/Lab-Project/CustomBlocks/CCEncoder /home/xongile/Lab-Project/CustomBlocks/CCEncoder /home/xongile/Lab-Project/CustomBlocks/CCEncoder /home/xongile/Lab-Project/CustomBlocks/CCEncoder/CMakeFiles/CCEncoder.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/CCEncoder.dir/depend

