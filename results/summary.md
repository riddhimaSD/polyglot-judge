**16 correct solutions**: 16 pass every suite. **32 seeded bugs** across 4 problems × 4 languages.

| Test suite | Bugs it catches (alone) | Bugs it is the *first* to catch |
|---|---|---|
| examples | 0/32 (0%) | 0 |
| edge | 22/32 (69%) | 22 |
| random | 22/32 (69%) | 0 |
| stress | 18/32 (56%) | 10 |
| *(none: bug survives every suite)* | | 0 |

| Problem | Language | Bug | examples | edge | random | stress |
|---|---|---|---|---|---|---|
| max_subarray | python | Kadane initialised at 0: returns 0 when every element is negative | AC | WA | WA | AC |
| max_subarray | python | Correct but O(n^2): every subarray | AC | AC | AC | TLE |
| max_subarray | javascript | Kadane initialised at 0: returns 0 when every element is negative | AC | WA | WA | AC |
| max_subarray | javascript | Correct but O(n^2): every subarray | AC | AC | AC | TLE |
| max_subarray | java | Kadane initialised at 0: returns 0 when every element is negative | AC | WA | WA | AC |
| max_subarray | java | Kadane with int accumulators: overflows once sums exceed 2^31 | AC | AC | AC | WA |
| max_subarray | cpp | Kadane initialised at 0: returns 0 when every element is negative | AC | WA | WA | AC |
| max_subarray | cpp | Kadane with int accumulators: overflows once sums exceed 2^31 | AC | AC | AC | WA |
| lower_bound | python | Returns the LAST index of t when t repeats (upper bound - 1) | AC | WA | WA | AC |
| lower_bound | python | hi starts at n-1: answer n (t larger than every element) is unreachable | AC | WA | WA | WA |
| lower_bound | javascript | Returns the LAST index of t when t repeats (upper bound - 1) | AC | WA | WA | AC |
| lower_bound | javascript | hi starts at n-1: answer n (t larger than every element) is unreachable | AC | WA | WA | WA |
| lower_bound | java | Returns the LAST index of t when t repeats (upper bound - 1) | AC | WA | WA | AC |
| lower_bound | java | hi starts at n-1: answer n (t larger than every element) is unreachable | AC | WA | WA | WA |
| lower_bound | cpp | Returns the LAST index of t when t repeats (upper bound - 1) | AC | WA | WA | AC |
| lower_bound | cpp | hi starts at n-1: answer n (t larger than every element) is unreachable | AC | WA | WA | WA |
| inversions | python | Correct but O(n^2): checks every pair | AC | AC | AC | TLE |
| inversions | python | Merge uses < instead of <=, so equal elements are counted as inversions | AC | WA | WA | AC |
| inversions | javascript | Correct but O(n^2): checks every pair | AC | AC | AC | TLE |
| inversions | javascript | Merge uses < instead of <=, so equal elements are counted as inversions | AC | WA | WA | AC |
| inversions | java | Correct but O(n^2): checks every pair | AC | AC | AC | TLE |
| inversions | java | Merge sort with an int counter: overflows past 2^31 inversions | AC | AC | AC | WA |
| inversions | cpp | Correct but O(n^2): checks every pair | AC | AC | AC | TLE |
| inversions | cpp | Merge sort with an int counter: overflows past 2^31 inversions | AC | AC | AC | WA |
| unique_substring | python | Missing max(): left can jump BACKWARDS to an old occurrence ('abba') | AC | WA | WA | WA |
| unique_substring | python | On a repeat, restarts the window at i instead of after the old occurrence ('dvdf') | AC | WA | WA | AC |
| unique_substring | javascript | Missing max(): left can jump BACKWARDS to an old occurrence ('abba') | AC | WA | WA | WA |
| unique_substring | javascript | On a repeat, restarts the window at i instead of after the old occurrence ('dvdf') | AC | WA | WA | AC |
| unique_substring | java | Missing max(): left can jump BACKWARDS to an old occurrence ('abba') | AC | WA | WA | WA |
| unique_substring | java | On a repeat, restarts the window at i instead of after the old occurrence ('dvdf') | AC | WA | WA | AC |
| unique_substring | cpp | Missing max(): left can jump BACKWARDS to an old occurrence ('abba') | AC | WA | WA | WA |
| unique_substring | cpp | On a repeat, restarts the window at i instead of after the old occurrence ('dvdf') | AC | WA | WA | AC |
