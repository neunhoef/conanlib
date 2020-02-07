project(conanlib CXX)

cmake_minimum_required(VERSION 3.5)
set(CMAKE_CXX_STANDARD 17)

add_library(conanlib conanlib.cpp)
target_include_directories(conanlib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

