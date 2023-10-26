cmake_minimum_required(VERSION 3.22)
project(seq_stack)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(seq_stack
        Assistance.h
        SeqStack.h
        TestSeqStack.cpp)
