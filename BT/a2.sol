// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank {
    mapping(address => uint256) balances;

    event Deposit (address customer, uint256 value);

    event Withdraw(address customer, uint256 value);

    function deposit() external payable {
        require(msg.value > 0, "Cannot deposit negative ether!");
        balances[msg.sender] += msg.value;
        emit Deposit(msg.sender, msg.value);
    }

    function withdraw(uint256 amount) external {
        require(amount > 0, "Cannot withdraw negative ether!");
        require(balances[msg.sender] >= amount, "Insufficient Ether!");

        balances[msg.sender] -= amount;

        payable(msg.sender).transfer(amount);

        emit Withdraw(msg.sender, amount);
    }

    function showBalance() external view returns (uint256) {
        return balances[msg.sender];
    }
}