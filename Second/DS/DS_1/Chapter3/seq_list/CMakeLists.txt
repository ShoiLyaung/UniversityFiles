cmake_minimum_required(VERSION 3.22)
project(seq_list)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(seq_list
        Assistance.h
        SeqList.h
        TestSeqList.cpp)
