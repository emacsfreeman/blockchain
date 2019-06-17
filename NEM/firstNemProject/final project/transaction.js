// SDK : https://github.com/QuantumMechanics/NEM-sdk#11---installation

let nem = require("nem-sdk").default;

let endpoint = nem.model.objects.create("endpoint")(nem.model.nodes.defaultTestnet, nem.model.nodes.defaultPort);

let common = nem.model.objects.create("common")("password", "privateKey");

let transferTransaction = nem.model.objects.create("transferTransaction")("TDTM7NAX3EZ2KD3O22SBRMLFREYWHPTW2GXTSL5W", 10, "Hello World");

let preperedTransaction = nem.model.transactions.prepare("transferTransaction")(common, transferTransaction, nem.model.network.data.testnet.id);

nem.model.transactions.send(common, preparedTransaction, endpoint).then(function(res){
  console.log(res);
}, function(err){
  console.log(err);
});
