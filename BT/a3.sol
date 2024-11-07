// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract StudentContract {
    struct Student {
        uint256 id;
        string name;
        uint256 age;
        string branch;
    }

    Student[] public studArray;

    mapping(address => uint256) studentIds;

    event studentAdded(uint256 id, string name, uint256 age, string branch);

    event Log(string msg);

    function addStudent(string memory _name, uint256 _age, string memory _branch) public {
        uint256 _id = studArray.length + 1;
        studArray.push(Student(_id, _name, _age, _branch));
        studentIds[msg.sender] = _id;
        emit studentAdded(_id, _name, _age, _branch);
    }

    function getStudentByID(uint256 id) public view returns (string memory, uint256, string memory) {
        require(id >= 1 && id <= studArray.length, "Student does not exist!");
        Student memory st = studArray[id - 1];
        return (st.name, st.age, st.branch);
    }

    fallback() external payable { 
        emit Log("fallback executed");
    }

    receive() external payable { 
        emit Log("receive executed");
    }
}