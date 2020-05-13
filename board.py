#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 12:41:26 2020

@author: NeilPatel
"""



def solve_Sudoku(b):
    #base case in which we find each element in the empty board and solve
    #if the board is solve return true else return find to finsih solving board
    find = empty_board(b)
    if not find:
        return True
    else:
        row, col = find
    
    #recursive algorithm to check if number is valid then add onto board 
    #recursively keep on trying until none of the numbers are valid
    #backtrack to see different values and try again to solve board.

    for i in range(1,10):
        if valid_number(b, i, (row, col)):
            b[row][col] = i

            if solve_Sudoku(b):
                return True

            b[row][col] = 0

    return False


def valid_number(b, num, pos):
     #we will first check the rows of the sudoku board and check if the number 
    #placed is valid or not by looping through each value to see of the number
    #is different than the number put in the empty square
    
    for i in range(len(b[0])):
        if b[pos[0]][i] == num and pos[1] != i:
            return False

    #we will first check the columns of the sudoku board and check if the number 
    #placed is valid or not by looping through each value to see of the number
    #is different than the number put in the empty square
    
    for i in range(len(b)):
        if b[i][pos[1]] == num and pos[0] != i:
            return False

    #use interger division to check each sub-board
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if b[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("--------------------------- ")

        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")


def empty_board(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j)  # row, col

    return None

