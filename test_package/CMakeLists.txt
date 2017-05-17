PROJECT(MyHello)
cmake_minimum_required(VERSION 3.0)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

CONAN_BASIC_SETUP()

ADD_EXECUTABLE(main main.cpp)
TARGET_LINK_LIBRARIES(main ${CONAN_LIBS})
