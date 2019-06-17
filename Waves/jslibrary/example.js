import { SeedAdapter, SIGN_TYPE } from '@waves/signature-adapter';
import { Money, Asset } from '@waves/data-entities';

const asset = new Asset({
   ticker: 'WAVES',
   id: 'WAVES',
   name: 'Waves',
   precision: 8,
   description: '',
   height: 0,
   timestamp: new Date('2016-04-11T21:00:00.000Z'),
   sender: '',
   quantity: 10000000000000000,
   reissuable: false
});

const transferTransactionData = {
   recipient: 'some address or alias',
   amount: Money.fromTokens(1, asset),
   attachment: 'Some attachment text less 140 bytes',
   fee: Money.fromTokens(0.001, asset)
};

const adapter = new SeedAdapter('some seed phrase with 15 or more chars');
const signable = adapter.makeSignable({
   type: SIGN_TYPE.TRANSFER,
   data: transferTransactionData
});

signable.getDataForApi().then(data => fetch('node-url', {
   method: 'POST',
   body: JSON.stringify(data)
}));
