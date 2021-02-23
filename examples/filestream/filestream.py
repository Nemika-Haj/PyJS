from PyJS import *
from PyJS.modules import filestream as fs

writeStream = fs.createWriteStream("hello.txt")
writeStream.write("Whatchu lookin' at!")

readStream = fs.createReadStream("hello.txt")

console.log(readStream.chunk())