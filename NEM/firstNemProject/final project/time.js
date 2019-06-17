// SDK : https://github.com/QuantumMechanics/NEM-sdk#11---installation

let nem = require("nem-sdk").default;

let endpoint = nem.model.objects.create("endpoint")(nem.model.nodes.defaultTestnet, nem.model.nodes.defaultPort);

nem.com.requests.chain.time(endpoint)
  .then(console.log, console.log);
