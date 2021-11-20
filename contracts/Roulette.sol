// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Roulette {
    mapping(int => mapping(int => int)) public board; 

    constructor() public {
        int i=0;
        for (int y = 0; y < 12; y++) {
            for (int x = 0; x < 3; x++) {
                board[y][x] = i;
                i++;
            }
        }
    }

    function getBoard(int x, int y) public returns (int) {
        return board[x][y];
    }
}
