cmake_minimum_required(VERSION 3.0.0)
project(SqBinaryTree VERSION 0.1.0)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable( SqBinaryTree
                Assistance.h
                LinkQueue.h
                Node.h
                SqBinaryTree.h
                TestSqBinaryTree.cpp)
