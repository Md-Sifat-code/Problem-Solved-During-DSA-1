function solve(input) {
    const lines = input.trim().split('\n');
    let t = parseInt(lines[0]);
    let index = 1;

    for (let _ = 0; _ < t; _++) {
        let [n, k] = lines[index++].split(' ').map(Number);
        let l = lines[index++].split(' ').map(Number);
        let r = lines[index++].split(' ').map(Number);

        let S = 0;
        let extras = new Array(n).fill(0);

        for (let i = 0; i < n; i++) {
            let li = l[i];
            let ri = r[i];
            if (li >= ri) {
                S += li;
                extras[i] = ri;
            } else {
                S += ri;
                extras[i] = li;
            }
        }

        extras.sort((a, b) => b - a); // Descending sort
        let overflow_needed = extras.slice(0, k - 1).reduce((acc, val) => acc + val, 0);
        let x_min = S + overflow_needed + 1;
        console.log(x_min);
    }
}

// Example input usage
const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8'); // Reads from stdin
solve(input);
