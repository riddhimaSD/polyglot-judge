const lines = require("fs").readFileSync(0, "utf8").split("\n");

function solve(line) {
  const s = line.trim();
  const last = new Map();
  let left = 0, best = 0;
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    if (last.has(c) && last.get(c) >= left) left = i;
    last.set(c, i);
    best = Math.max(best, i - left + 1);
  }
  return best;
}

const t = parseInt(lines[0], 10);
const out = [];
for (let i = 1; i <= t; i++) out.push(String(solve(lines[i])));
console.log(out.join("\n"));
