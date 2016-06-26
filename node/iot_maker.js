re('https');
const AWS = require('aws-sdk');

exports.handler = (event, context, callback) => {
    console.log('Received event:', event.clickType, event.serialNumber, event.batteryVoltage);
    console.log('Done processing response.');

//setup REST call to IFTTT   
var iftttMakerSecretKey = 'dD37h2LH22FMQNR83Ur-Fl';


jsonObject = JSON.stringify({ "value1" : "Matt", "value2" : "Sahn", "value3" : "" });

// prepare the header for passing some JSON options
var postheaders = {
    'Content-Type' : 'application/json',
    'Content-Length' : Buffer.byteLength(jsonObject, 'utf8')
};

var options = {
  host: 'maker.ifttt.com',
  port: 80,
  path: '/trigger/' + event.clickType.toLowerCase() + '/with/key/' + iftttMakerSecretKey,
  method: 'POST',
  headers: postheaders
};

console.log('Sending POST.');

https.request(options, function(res) {
  console.log('STATUS: ' + res.statusCode);
  console.log('HEADERS: ' + JSON.stringify(res.headers));
  res.setEncoding('utf8');
  res.on('data', function (chunk) {
    console.log('BODY: ' + chunk);
  });
}).end();


};

console.log('Exit.')
