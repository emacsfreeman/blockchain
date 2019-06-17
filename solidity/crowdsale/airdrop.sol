pragma solidity ^0.4.16;


interface FilipCoin {
    function transferForm(address from, address to, uint tokens);
}

contract Airdrop {
    
    FilipCoin public token;
    address tokenHolder;
    uint amountToTransfer;
    
    function Airdrop(address addressOfToken, address addresOfHolder, uint fixedAmount)
    {
        token = FilipCoin(addressOfToken);
        tokenHolder = addresOfHolder;
        amountToTransfer = fixedAmount;
    }
    
    function drop() public {
        token.transferForm(tokenHolder, msg.sender, amountToTransfer);
    }
}
