pragma solidity ^0.4.0;

///////////
// BAD WAY
/////////

// RE-ENTRANCY
contract Fund
{
    // Mapping of ether shares of the contract
    mapping(address => uint) shares;
    // Withdraw your share 
    function withdraw() public 
    {
        if (msg.sender.send(shares[msg.sender]))
            shares[msg.sender] = 0;
    }
}

/*
    DEVELOPMENT PATTERN
    CHECK-EFFECTS-INTERACTIONS
*/

////////////
// GOOD WAY
///////////
contract Fund
{
    // Mapping of ether shares of the contract
    mapping(address => uint) shares;
    // Withdraw your share 
    function withdraw() public 
    {
        var share = shares[msg.sender];
        shares[msg.sender] = 0;
        msg.sender.transfer(share);
    }
}


// BAD PRACTICES

// LOOPS WITHOUT FIXED NUMBER OF ITERATIONS 


// NEVER USE TX.ORIGIN FOR AUTHENTIFICATION - USE MSG.SENDER 
// PEOPLE COULD PROXY TRANSACTIONS AND ACT AS you



// FAIL SAFE MODE 

// READ THIS https://solidity.readthedocs.io/en/v0.4.0/security-considerations.html#pitfalls
