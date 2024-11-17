const express = require('express')
const path = require('path')
const mongodb = require('mongoose')
const app = express()
const port = 5500

const connect = mongodb.connect('mongodb+srv://yac005a:qywgvcuygiwey@yashcluster.9qo8s.mongodb.net/')
app.use(express.static(path.join(__dirname, 'Public')));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
})

app.get('/post', (req, res) => {
  const obj = {
    // name: req.query.name,
    // message: req.query.mess,
    // timestamp: new Date().toISOString()
    name:823,
    age:87
  };
  res.send('hek')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
}) 