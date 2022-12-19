const fs = require('fs')

const result = fs.readFileSync('input.txt').toString()
  .split('\n\n')
  .map(line => {
    return line
      .split('\n')
      .map(x => parseInt(x))
      .reduce((acc, x) => acc + x)
  })
  .sort((a, b) => b - a)
  .slice(0, 3)
  .reduce((acc, x) => acc + x)

console.log(result)
