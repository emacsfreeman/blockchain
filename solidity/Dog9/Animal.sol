pragma solidity 0.5.1;

contract AnimalContract
{
    enum AnimalType {DOG, CAT}
    
    struct Animal 
    {
        string name;
        uint age;
        AnimalType animalType;
    }
    
    address owner; // global variable which is called state variable in solidity

    
    mapping(address => Animal[]) ownerToAnimals;
    
    
    modifier onlyNewOwner()
    {
        require(msg.sender == owner);
        _;
    }
    
    constructor() public
    {
        owner = msg.sender;
    }
    
    // _functionName internal
    function _addAnimal(string memory _name, uint _age, AnimalType _animalType) internal returns (uint) 
    {
        return ownerToAnimals[msg.sender].push(Animal(_name, _age, _animalType)) - 1;
    }
    
    function getAnimal(uint _id) public view returns (string memory)
    {
        address owner = msg.sender;
        return ownerToAnimals[msg.sender][_id].name;
    }
    
}
