const Blockchain = require('./blockchain');
const bitcoin = new Blockchain();

const bc1 = {
"chain": [
{
"index": 1,
"timestamp": 1558964495235,
"transactions": [],
"nonce": 100,
"hash": "0",
"previousBlockHash": "0"
},
{
"index": 2,
"timestamp": 1558964513685,
"transactions": [],
"nonce": 18140,
"hash": "0000b9135b054d1131392c9eb9d03b0111d4b516824a03c35639e12858912100",
"previousBlockHash": "0"
},
{
"index": 3,
"timestamp": 1558964697902,
"transactions": [
{
"amount": 12.5,
"sender": "00",
"recipient": "25106d30808511e9b5a2c7709f6f40fc",
"transactionId": "3016b130808511e9b5a2c7709f6f40fc"
},
{
"amount": 70,
"sender": "4TPOZRG04",
"recipient": "7EZROI19",
"transactionId": "4c58e250808511e9b5a2c7709f6f40fc"
},
{
"amount": 90,
"sender": "4TPOZRG04",
"recipient": "7EZROI19",
"transactionId": "7120ee20808511e9b5a2c7709f6f40fc"
},
{
"amount": 30,
"sender": "4TPOZRG04",
"recipient": "7EZROI19",
"transactionId": "857edbc0808511e9b5a2c7709f6f40fc"
}
],
"nonce": 3301,
"hash": "0000726b70f4e0e1d886a0e63d04484349cbfb8fed34af5fe678d2d310f74d35",
"previousBlockHash": "0000b9135b054d1131392c9eb9d03b0111d4b516824a03c35639e12858912100"
},
{
"index": 4,
"timestamp": 1558964824773,
"transactions": [
{
"amount": 12.5,
"sender": "00",
"recipient": "25106d30808511e9b5a2c7709f6f40fc",
"transactionId": "9ddd4300808511e9b5a2c7709f6f40fc"
},
{
"amount": 40,
"sender": "4TPOZRG04",
"recipient": "7EZROI19",
"transactionId": "b6e22370808511e9b5a2c7709f6f40fc"
},
{
"amount": 50,
"sender": "4TPOZRG04",
"recipient": "7EZROI19",
"transactionId": "c93c03b0808511e9b5a2c7709f6f40fc"
},
{
"amount": 60,
"sender": "4TPOZRG04",
"recipient": "7EZROI19",
"transactionId": "cd43d050808511e9b5a2c7709f6f40fc"
},
{
"amount": 70,
"sender": "4TPOZRG04",
"recipient": "7EZROI19",
"transactionId": "d138d840808511e9b5a2c7709f6f40fc"
}
],
"nonce": 9540,
"hash": "00009175232215bf60b35ba62f8b973506b23db49b49326ba7e6a69344ab87af",
"previousBlockHash": "0000726b70f4e0e1d886a0e63d04484349cbfb8fed34af5fe678d2d310f74d35"
}
],
"pendingTransactions": [
{
"amount": 12.5,
"sender": "00",
"recipient": "25106d30808511e9b5a2c7709f6f40fc",
"transactionId": "e97c3d70808511e9b5a2c7709f6f40fc"
}
],
"currentNodeUrl": "http://localhost:3001",
"networkNodes": []
};

console.log('VALID: ', bitcoin.chainIsValid(bc1.chain));

