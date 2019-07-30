########################################################################
# Project setup
########################################################################
cmake_minimum_required(VERSION 2.8)
project(CCEncoder)	
enable_language(CXX)

find_package(Pothos CONFIG REQUIRED)

########################################################################
# Module setup
########################################################################
POTHOS_MODULE_UTIL(
    TARGET CCEncoder                #a unique name for this module
    SOURCES CCEncoder.cpp           #sources used in this project
    DESTINATION blocks/Custom   #a subdirectory for installed modules
    ENABLE_DOCS                   #scanning for documentation markup
)