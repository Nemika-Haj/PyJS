var string = "Ohayou gozaimasu!"

console.log(string.search("gozaimasu!"))
console.log(string.length)
console.log(string.slice(4))
console.log(string.substring(3, 8))
console.log(string.toUpperCase())
console.log(string.toLowerCase())
console.log(string.concat(" Hey", " there! What'chu doin?"))

trimMe = "    A      "
console.log(trimMe.trim())
console.log(string.padStart(5, 0))
console.log(string.padEnd(3, "E"))
console.log(string.charCodeAt(4))