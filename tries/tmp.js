"use strict";

//var http = require('http');
//var dns = require('dns');

//const spawn = require("child_process").spawn;
//console.log("1");
//const pythonProcess = spawn('python', ["./hello_world.py", "Hello world from nodejs to python and back!"]);
//console.log("2");
//
//pythonProcess.stdout.on('data', (data) => {
    //console.log(data)
//});

const express = require('express');
const app = express();

const sentences = [
	'You are stupid', 
	'You suck', 
	'Fat idiot', 
	'You are a bitch!',
	'Oshri is a traitor!',
	'Happy birthday!', 
	'You are the greatest', 
	'That is awesome',
	'Fuck you son of a bitch']

app.get('/', (req, res) => {
	
	const { spawn } = require('child_process');
	const pyProg = spawn('python', ['../classifier/sentiment_predict.py', sentences]);
	
	pyProg.stdout.on('data', function(data) {
		
		console.log(data.toString());
		res.write(data);
		res.end('end');
		
	});
	
});

app.listen(4000, () => console.log('Application listening on port 4000...'));