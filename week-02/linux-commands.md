# Class 2 — Linux commands for log files

Data files used:
- `module-01/data/orders_oct2026.csv`
- `module-01/data/app_2026-10.log`

## Getting started
- `cd ~/de-bootcamp/ostad-de-bootcamp-main` — go to the course folder
- `pwd` — check where I am

## Counting lines
- `wc -l module-01/data/orders_oct2026.csv` — lines in the orders file
- `wc -l module-01/data/app_2026-10.log` — lines in the log file

## Counting by log level
- `grep -c "| WARN" module-01/data/app_2026-10.log` — total WARN
- `grep -c "| DEBUG" module-01/data/app_2026-10.log` — total DEBUG
- Note: `"| WARN |"` returns 0 because the level column is 5 characters wide,
  so WARN has an extra space after it. Computers count spaces too.

## Counting each level at once
- `cut -d'|' -f3 module-01/data/app_2026-10.log | sort | uniq -c`
  — split by `|`, take the 3rd column (level), count each one

## Combining two greps with a pipe
- `grep "^2026-10-10" module-01/data/app_2026-10.log | grep -c "| ERROR |"`
  — ERRORs on 10 October only

## Which date had the most WARN (the 5-step chain)
    grep "| WARN" module-01/data/app_2026-10.log | cut -c1-10 | sort | uniq -c | sort -rn | head -1
1. `grep` — keep only WARN lines
2. `cut -c1-10` — keep only the date part
3. `sort` — put same dates next to each other
4. `uniq -c` — count each date
5. `sort -rn | head -1` — biggest count on top, show only that
- Use `sort -n` instead of `sort -rn` to get the date with the fewest.

## Searching a CSV file
- `grep -c "bKash" module-01/data/orders_oct2026.csv` — orders paid with bKash

## Writing answers to a file
- `echo "text" > file.txt` — create a new file (overwrites)
- `echo "text" >> file.txt` — add to the end of a file
