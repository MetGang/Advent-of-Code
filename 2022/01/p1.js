const fs = require('fs')

const result = fs.readFileSync('input.txt').toString()
  .split('\n\n')
  .map(line => {
    return line
      .split('\n')
      .map(x => parseInt(x))
      .reduce((acc, x) => acc + x)
  })
  .reduce((acc, x) => Math.max(acc, x))

console.log(result)
