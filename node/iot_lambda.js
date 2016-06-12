// Node.js code that runs in an AWS Lambda function (Oregon)
// Triggers my HomeAssistant as events

var http = require('http');
const AWS = require('aws-sdk');

exports.handler = (event, context, callback) => {
    console.log('Received event:', event.clickType, event.serialNumber, event.batteryVoltage);
    console.log('Done processing response.');

//setup REST call to my raspberry Pi via static DNS    
var options = {
  host: 'mattsahn.duckdns.org',
  port: 8123,
  path: '/api/events/dash_button_pressed_' + event.clickType,
  method: 'POST'
};

http.request(options, function(res) {
  console.log('STATUS: ' + res.statusCode);
  console.log('HEADERS: ' + JSON.stringify(res.headers));
  res.setEncoding('utf8');
  res.on('data', function (chunk) {
    console.log('BODY: ' + chunk);
  });
}).end();


};

console.log('Exit.')
