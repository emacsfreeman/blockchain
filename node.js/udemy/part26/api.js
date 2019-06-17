const express = require('express')
const app = express()
 
app.get('/', function (req, res) 
{
  res.send('<h1><a href="https://laurentgarnier.podia.com/comment-devenir-developpeur-blockchain" target="_blank">Becoming a Blockchain Developer</a> is Hard but Fun!</h1>')
})
 
app.listen(3000)
