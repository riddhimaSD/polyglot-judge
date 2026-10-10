const lines = require("fs").readFileSync(0, "utf8").split("\n");

function solve(line) {
  const v = line.trim().split(/\s+/).map(Number);
  const n = v[0], t = v[1];
  let lo = 0, hi = n;
  while (lo < hi) {
    const mid = (lo + hi) >> 1;
    if (v[2 + mid] < t) lo = mid + 1; else hi = mid;
  }
  return lo;
}

const t = parseInt(lines[0], 10);
const out = [];
for (let i = 1; i <= t; i++) out.push(String(solve(lines[i])));
console.log(out.join("\n"));
