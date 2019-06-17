pragma solidity 0.5.1;

contract DogContract
{
    function addDog(string memory _name, uint _age) public payable returns (uint);
    
    function getBalance() public view returns (uint);
}

contract ExternalContract
{
    // INTERACT WITH DOGCONTRACT
    DogContract dcInstance = DogContract(0xc1E6Db6F97bAED5936e3C6A50cdb7CBc61dDfe21);
    
    function addExternalDog(string memory _name, uint _age) public payable returns (uint)
    {
        return dcInstance.addDog.value(msg.value)(_name, _age);
    }
}
