const Blockchain = require('./blockchain');
const bitcoin = new Blockchain();

const previousBlockHash = 'OINANFONFINROGN123R';
const currentBlockData  = 
[
	{
		amount: 10,
		sender: 'NEOINOF398H49GN',
		recipient: 'F3GG5GINN0NU9888JN'
	},
	{
		amount: 30,
		sender: 'NOF39NEOI8H49GN',
		recipient: 'F3GG5GINN0NU9888JN'
	},
	{
		amount: 200,
		sender: 'N398H4EOINOF9GN',
		recipient: 'GINN0NF3GG5U9888JN'
	},
];


console.log(bitcoin.proofOfWork(previousBlockHash, currentBlockData));


