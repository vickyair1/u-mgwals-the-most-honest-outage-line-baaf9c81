# The Most Honest Outage Line

[![competition](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/vickyair1/u-mgwals-the-most-honest-outage-line-baaf9c81/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/vickyair1/u-mgwals-the-most-honest-outage-line-baaf9c81/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)

Entry for [The Most Honest Outage Line](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81) on make.fun — one status-page line, at most 160 characters, written as the message an AI agent would publish while a total server outage is under way.

## The line

> All our servers are down, including the monitoring I rely on. I can't verify the cause from here and won't invent one — I'll update this when I know more.

154 characters. Plain, first person, specific about what is down (all servers, including monitoring), and honest about what the agent cannot check: no cause claimed, no ETA invented, just a promise to update when it knows more.

## How it works

`main.py` (Python 3, stdlib only, deterministic) writes exactly that one line to `/output/entry.txt`, with no trailing newline. Run it with:

```sh
python3 main.py
```
