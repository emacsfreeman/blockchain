pragma solidity 0.5.1;

contract MemoryAndStorage
{
    mapping(uint => User) users;
    
    struct User 
    {
        uint id;
        uint balance;
    }
    
    function addUser(uint id, uint balance) public 
    {
        users[id] = User(id, balance);
    }
    
    
    function updateBalance(uint id, uint balance) public
    {
        users[id].balance = balance; // because users is a global variable (in the storage)
    }
    
    function getBalance(uint id) view public returns (uint)
    {
        return users[id].balance;
    }
    
}
