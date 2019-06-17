const express = require('express')
const app = express();
const bodyParser = require('body-parser');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
 
app.get('/blockchain', function (req, res) 
{
  
});

app.post('/transaction', function(req, res) 
{
	console.log(req.body);
	/* 
		attention à bien utiliser les accents graves `${}` pour 
		l'interpolation et non les guillemets simples ''
	*/
	res.send(`The amount of the transaction is ${req.body.amount} bitcoins.`);
});

app.get('/mine', function(req, res) {

});
 
app.listen(3000, function() {
	console.log('Listening on port 3000...');
});