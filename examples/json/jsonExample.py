from PyJS import *
from PyJS.modules import fs

file = fs.createReadStream("file.json")

data = JSON.parse(file)

console.log(JSON.stringify(data))