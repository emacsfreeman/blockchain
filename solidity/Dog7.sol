pragma solidity 0.5.1;

contract DogContract
{
    // storage most expensive
    // memory middle
    // stack less expensive
    
    struct Dog 
    {
        string name;
        uint age;
    }
    
    mapping(address => Dog) ownerToDog;
    
    modifier onlyNewOwners()
    {
        require(ownerToDog[msg.sender].age == 0);
        
        _; // _ is replaced by the body of addDog() function
    }
    
    function addDog(string memory _name, uint _age) public onlyNewOwners
    {
        Dog memory currentDog = Dog(_name, _age);
        ownerToDog[msg.sender] = currentDog;
    }
        
    
    function getDog(uint _id) public view onlyNewOwners returns (string memory)
    {
        address owner = msg.sender;
        return ownerToDog[owner].name;
    }
}
