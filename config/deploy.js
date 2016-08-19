var http = require('http');
var moment = require('moment')
var createHandler = require('github-webhook-handler');
var handler = createHandler({ path: '/deployer', secret: '3MEY#F964H2Mz3sj5Fg&Z*q2**gzMnd^' });
// 上面的 secret 保持和 GitHub 后台设置的一致

function run_cmd(cmd, args, callback) {
  var spawn = require('child_process').spawn;
  var child = spawn(cmd, args);
  var resp = "";

  child.stdout.on('data', function(buffer) { resp += buffer.toString(); });
  child.stdout.on('end', function() { callback (resp) });
};

http.createServer(function (req, res) {
  handler(req, res, function (err) {
    res.statusCode = 404;
    res.end('no such location');
  });
}).listen(7777);

handler.on('error', function (err) {
  console.error('Error:', err.message);
});

handler.on('push', function (event) {
  console.log(moment(new Date()).format('YYYY-MM-DD HH:mm:ss') + ' --- Received a push event for %s to %s',
    event.payload.repository.name,
    event.payload.ref);
  if( event.payload.repository.name === 'golem' && event.payload.ref === 'refs/heads/staging' ) {
    run_cmd('sh', ['./golemDeploy.sh'], function(text){ console.log(text) });
  } else if( event.payload.repository.name === 'giant' && event.payload.ref === 'refs/heads/staging' ) {
           run_cmd('sh', ['./giantDeploy.sh'], function(text){ console.log(text) });
  }
});

