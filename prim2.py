#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def wrapper_funk():
    def hello_world():
        print("Hello world!")

    hello_world()


if __name__ == '__main__':
    a = wrapper_funk
    a()
    wrapper_funk()
