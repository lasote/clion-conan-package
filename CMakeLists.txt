cmake_minimum_required(VERSION 3.7)
project(clion_create1)

if(EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    conan_basic_setup()
else()
    message(WARNING "The file conanbuildinfo.cmake doesn't exist, you have to run conan install first")
endif()

include_directories("${CMAKE_SOURCE_DIR}/source")
add_subdirectory("${CMAKE_SOURCE_DIR}/source")