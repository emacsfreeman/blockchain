const Blockchain = require('./blockchain');

const bitcoin = new Blockchain();

bitcoin.createNewBlock(892348, 'A90SDNF09AN90N', 'OIANS909A0S9NF');

bitcoin.createNewTransaction(100, 'ALEXSD89W0N90A', 'JENN0AN09N09A9');

bitcoin.createNewBlock(12323, '0989W0N90A', '123N09N09A9');

bitcoin.createNewTransaction(50, 'ALEXSD89W0N90A', 'JENN0AN09N09A9');

bitcoin.createNewTransaction(300, 'ALEXSD89W0N90A', 'JENN0AN09N09A9');

bitcoin.createNewTransaction(2000, 'ALEXSD89W0N90A', 'JENN0AN09N09A9');

bitcoin.createNewBlock(8974, '0989W14790A', '123N097114A9');


console.log(bitcoin.chain[2]);
