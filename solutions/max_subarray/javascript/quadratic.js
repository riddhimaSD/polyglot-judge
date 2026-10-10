const lines = require("fs").readFileSync(0, "utf8").split("\n");

function solve(line) {
  const a = line.trim().split(/\s+/).map(Number).slice(1);
  let best = a[0];
  for (let i = 0; i < a.length; i++) {
    let s = 0;
    for (let j = i; j < a.length; j++) { s += a[j]; best = Math.max(best, s); }
  }
  return best;
}

const t = parseInt(lines[0], 10);
const out = [];
for (let i = 1; i <= t; i++) out.push(String(solve(lines[i])));
console.log(out.join("\n"));
