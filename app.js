var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var path = require('path');


var router = express.Router();


app.use(bodyParser.urlencoded({'extended':'true'}));
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname + '/client/')));
app.use(express.static(path.join(__dirname + '/bower_components')));

router.route('/')



app.use('/', router);


app.listen(8989);
console.log('app on 8989');
