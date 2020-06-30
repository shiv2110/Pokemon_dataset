const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const path = require('path');
const urlencodedParser = bodyParser.urlencoded({extended : false});
app.set('view engine', 'ejs');

app.use('/assets', express.static('assets'));

app.listen(3000, () =>{
    console.log('Now listenng to port 3000');
});

app.get('/name', (req, res) =>{
    res.render('index', {qs : req.query});
    
});

app.post('/name', urlencodedParser, (req, res) =>{
    console.log(req.body);
    //res.render('index', {qs : req.query});
    const spawn = require('child_process').spawn;
    const process = spawn('python', ['./test2.py', req.body.type1, req.body.hp, req.body.attack, req.body.defense, req.body.spatk, req.body.spdef, req.body.speed, req.body.generation]);
    process.stdout.on('data', (data) =>{
        
            res.send(data.toString());
        
        
    });

});

