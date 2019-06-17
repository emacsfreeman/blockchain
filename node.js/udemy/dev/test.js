const Blockchain = require('./blockchain');

const bitcoin = new Blockchain();

bitcoin.createNewBlock(892348, 'A90SDNF09AN90N', 'OIANS909A0S9NF');

bitcoin.createNewTransaction(100, 'ALEXSD89W0N90A', 'JENN0AN09N09A9');


console.log(bitcoin);