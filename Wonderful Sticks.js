function solve(input) {
    const lines = input.trim().split('\n');
    let t = parseInt(lines[0]);
    let lineIndex = 1;

    for (let _ = 0; _ < t; _++) {
        let n = parseInt(lines[lineIndex++]);
        let s = lines[lineIndex++].trim();

        let count_L = (s.match(/</g) || []).length;
        let count_R = (s.match(/>/g) || []).length;

        let small = [];
        for (let i = 1; i <= count_L; i++) small.push(i);

        let large = [];
        for (let i = n - count_R + 1; i <= n; i++) large.push(i);

        let full_set = new Set();
        for (let i = 1; i <= n; i++) full_set.add(i);
        let mid_vals = new Set(full_set);
        small.forEach(val => mid_vals.delete(val));
        large.forEach(val => mid_vals.delete(val));

        let mid = [...mid_vals][0];

        let demands = [...s].map(ch => (ch === '<' ? 'S' : 'L'));

        let ans = new Array(n);
        ans[0] = mid;
        let pos = 1;

        let i = 0;
        while (i < demands.length) {
            let tag = demands[i];
            let j = i + 1;
            while (j < demands.length && demands[j] === tag) j++;
            let length = j - i;

            if (tag === 'S') {
                let block = small.slice(-length).sort((a, b) => b - a);
                small.length -= length;
                for (let x of block) ans[pos++] = x;
            } else {
                let block = large.slice(0, length).sort((a, b) => a - b);
                large = large.slice(length);
                for (let x of block) ans[pos++] = x;
            }
            i = j;
        }

        console.log(ans.join(' '));
    }
}

// Read from stdin
const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8');
solve(input);
