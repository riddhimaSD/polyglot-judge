const lines = require("fs").readFileSync(0, "utf8").split("\n");

function solve(line) {
  const a = line.trim().split(/\s+/).map(Number).slice(1);
  let c = 0;
  for (let i = 0; i < a.length; i++) for (let j = i + 1; j < a.length; j++) if (a[i] > a[j]) c++;
  return c;
}

const t = parseInt(lines[0], 10);
const out = [];
for (let i = 1; i <= t; i++) out.push(String(solve(lines[i])));
console.log(out.join("\n"));
