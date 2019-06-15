var Telnet = require('telnet-client')
var connection = new Telnet()
 
var params = {
  host: '000.000.000.000',
  port: 5000,
  //shellPrompt: '/ # ',
  shellPrompt: 'rtkrcv> ',
  shellPrompt: '',
  timeout: 1500,
  // removeEcho: 4
  negotiationMandatory: false,
  ors: '\r\n', // mandatory for your 'send' to work
  waitfor: '\n' // mandatory for your 'send' to work (set those either here or in your exec_params!)
}


var dict = {};

connection.on('data', function(response){
  response = response.toString();  
  var lines = response.split('\n');
  console.log('lines:'+lines.length);
  for (var i=0; i< lines.length; i++){
    line = lines[i];
    var cols = line.split(':');
    if (cols.length >= 2){
      dict[cols[0].trim()] = cols[1].trim();        
    }      
  }   
  key = '# of satellites rover';
  if (key in dict){
    console.log('sats rover:'+dict[key]);
  } 
});

connection.on('connect', function() {
  connection.send('status 1',  {
    ors: '\r\n',
    waitfor: '\n'
  }, function(err, response) {
    if (err) return err;
  })
});
 
 
connection.on('timeout', function() {
  console.log('socket timeout!')
  connection.end()
})
 
connection.on('close', function() {
  console.log('connection closed')
})
 
connection.connect(params)
