cmake_minimum_required(VERSION 3.24)
project(assemble)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(assemble
        assemble.cpp
        Assistance.h
        SeqList.h)
