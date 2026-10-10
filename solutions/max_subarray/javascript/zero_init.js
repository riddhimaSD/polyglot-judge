const lines = require("fs").readFileSync(0, "utf8").split("\n");

function solve(line) {
  const a = line.trim().split(/\s+/).map(Number).slice(1);
  let best = 0, cur = 0;
  for (const x of a) {
    cur = Math.max(0, cur + x);
    best = Math.max(best, cur);
  }
  return best;
}

const t = parseInt(lines[0], 10);
const out = [];
for (let i = 1; i <= t; i++) out.push(String(solve(lines[i])));
console.log(out.join("\n"));
