from PyJS import *
from PyJS.modules import fs

writeStream = fs.createWriteStream("hello.txt")
writeStream.write("Whatchu lookin' at!")

readStream = fs.createReadStream("hello.txt")

console.log(readStream.chunk())