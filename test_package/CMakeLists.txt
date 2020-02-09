cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

#foreach(t "conanlib" "arango::conanlib" "conanlib::conanlib" "conanlib::arango" "CONAN_PKG::conanlib")
#    if(TARGET ${t})
#        message(STATUS "target ${t} exists")
#    else()
#        message(STATUS "target ${t} does not exist")
#    endif()
#endforeach()
#find_package(conanlib REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example PUBLIC CONAN_PKG::conanlib)

# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME example
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND example)
