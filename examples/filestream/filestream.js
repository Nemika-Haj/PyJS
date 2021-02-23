const fs = require('fs');

var writeStream = fs.createWriteStream('hello.txt');

writeStream.write("Whatchu lookin' at!");

var readStream = fs.createReadStream('hello.txt');

readStream.on("data", function(data) {
    var chunk = data.toString();
    console.log(chunk);
}); 