'use strict';

const
    express = require('express'),
    http = require('http'),
    fib = require('./fib');

let app = express();

app.get('/:number', (req, res) => {

    setTimeout(() => {
        let newFib = fib.incrementFib(Number.parseInt(req.params.number));
        console.log(`New Fibonacci number -> ${newFib}`);

        http.get(`http://python_server/${newFib}`);

        res.status(200);
        res.send();
    }, 500);
})

app.listen(80, '0.0.0.0', () => { console.log('Listening...'); });

module.exports = { incrementFib };