let nem = require("nem-sdk").default;

let endpoint = nem.model.objects.create("endpoint")(nem.model.nodes.defaultTestnet, nem.model.nodes.defaultPort);

let common = nem.model.objects.create("common")("password", "7a431b6f6047ce1b44fb1c779f5dec3f97817ed644340dfe379b798103f507fb");

let transferTransaction = nem.model.objects.create("transferTransaction")("TD3JLYCEXEYZYVI4SJCARYI3BN2QVSTYB4TCUV56", 1, "Sent mosaic");

var mosaicDefinitions = nem.model.objects.get("mosaicDefinitionMetaDataPair");

var mosaicAttachment = nem.model.objects.create("mosaicAttachment")("emacsfreeman", "emacscoin", 10000);

transferTransaction.mosaics.push(mosaicAttachment);
nem.com.requests.namespace.mosaicDefinitions(endpoint, mosaicAttachment.mosaicId.namespaceId).then(function(res){
  var definition = nem.utils.helpers.searchMosaicDefinitionArray(res.data, ["emacscoin"]);
  var fullName = nem.utils.format.mosaicIdToName(mosaicAttachment.mosaicId);
  mosaicDefinitions[fullName] = {};
  mosaicDefinitions[fullName].mosaicDefinition = definition[fullName];

  var preparedTransaction = nem.model.transactions.prepare("mosaicTransferTransaction")(common, transferTransaction, mosaicDefinitions, nem.model.network.data.testnet.id);
  preparedTransaction.fee = 1000000;

  nem.model.transactions.send(common, preparedTransaction, endpoint).then(function(res){
    console.log(res);
  }, function(err){
    console.log(err);
  });

  console.log(definition);
}, function(err){});
