pragma solidity 0.5.1;

contract RealEstate 
{
    address public seller;
    string public streetAddress;
    string title;
    uint256 public price;
    
    constructor() public 
    {
        // Who is the seller?
        seller = msg.sender;
        // What is the street address?
        streetAddress = "350 5th Ave, New York, NY 10118";
        // What is the title?
        title = "Juste un titre";
        // What is the price?
        price = 99000000000000000000;
        
    }
}
