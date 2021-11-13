'use strict';

const
    express = require('express'),
    http = require('http');
let app = express();
let fibNumber = 0;


app.get('/:number', (req, res) => {

    setTimeout(() => {
        fibNumber += Number.parseInt(req.params.number);
        console.log(`New Fibonacci number -> ${fibNumber}`);

        http.get(`http://python_server/${fibNumber}`);

        res.status(200);
        res.send();
    }, 500);
})

app.listen(80, '0.0.0.0', () => { console.log('Listening...'); });