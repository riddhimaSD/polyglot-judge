const lines = require("fs").readFileSync(0, "utf8").split("\n");

function solve(line) {
  const a = line.trim().split(/\s+/).map(Number).slice(1);
  const tmp = new Array(a.length);
  function sort(lo, hi) {
    if (hi - lo <= 1) return 0;
    const m = (lo + hi) >> 1;
    let c = sort(lo, m) + sort(m, hi), i = lo, j = m, k = lo;
    while (i < m && j < hi) {
      if (a[i] <= a[j]) tmp[k++] = a[i++];
      else { tmp[k++] = a[j++]; c += m - i; }
    }
    while (i < m) tmp[k++] = a[i++];
    while (j < hi) tmp[k++] = a[j++];
    for (let p = lo; p < hi; p++) a[p] = tmp[p];
    return c;
  }
  return sort(0, a.length);
}

const t = parseInt(lines[0], 10);
const out = [];
for (let i = 1; i <= t; i++) out.push(String(solve(lines[i])));
console.log(out.join("\n"));
