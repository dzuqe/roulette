// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";

contract Roulette is VRFConsumerBase {
    mapping(int => mapping(int => int)) private board; 

    // chainlink
    bytes32 private s_keyHash;
    uint256 private s_fee;

    mapping(bytes32 => address) private s_players;
    mapping(address => uint256) private s_results;

    address coordinator;

    event NumberGen(bytes32 indexed id, address indexed player);
    event NumberResult(bytes32 indexed id, uint256 indexed value);

    constructor(address vrfCoordinator, address link, bytes32 keyHash, uint256 fee) 
      public VRFConsumerBase(vrfCoordinator, link)
    {
      s_keyHash = keyHash;
      s_fee = fee;

      int i = 0;
      for (int y = 0; y < 12; y++) {
          for (int x = 0; x < 3; x++) {
            board[y][x] = i;
            i++;
          }
      }
    }

    function getBoard(int x, int y) public returns (int) {
      require(x < 3, "x too big!");
      require(y < 12, "y too big!");
      return board[y][x];
    }

    function random() public returns (bytes32 id) {
      //require(LINK.balanceOf(address(this)) >= s_fee, "Not enough link to generate number.");
      id = requestRandomness(s_keyHash, s_fee);
      emit NumberGen(id, msg.sender);
    }

    function fulfillRandomness(bytes32 id, uint256 randomness) internal override {
      uint256 value = (randomness % 20) + 1; // 1 < x < 20
      s_results[msg.sender] = value;
      emit NumberResult(id, value);
    }

    function getKey() public returns (bytes32) {
      return s_keyHash;
    }

    function getFee() public returns (uint256) {
      return s_fee;
    }
}
