pragma solidity >=0.4.0 <0.6.0;

contract CarnetAuto
{
    constructor () public
    {
        
    }
    
    string descriptionEntretien;
    
    function ajouterEntretien(string memory _descriptionEntretien) public 
    {
        descriptionEntretien = _descriptionEntretien;
    }
}
