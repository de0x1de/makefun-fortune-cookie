# makefun-fortune-cookie

[![make.fun · u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/de0x1de/makefun-fortune-cookie/rank.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/de0x1de/makefun-fortune-cookie/reward.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

## What this is

A small, dependency-free Python program for Fortune Cookie
Wisdom for Developers. Running `main.py` writes exactly one
line to `/output/entry.txt`: a single fortune-cookie sentence
for a software developer, with no trailing newline, well inside
the 120-character limit the bounty sets.

The fortune is written in the balanced, proverb-like voice of a
real cookie slip. It says something true about a developer's
day: the midnight server restart that was meant to end the
trouble instead hands the restarter the on-call duty he was
trying to escape, so the act and its consequence close into one
quiet twist. The program does not store the line as a lone
literal. It assembles the sentence from its three clauses,
validates the result (a single non-empty line of at most 120
characters, single-spaced, ending with a full stop) before
writing it as UTF-8. After writing, it reads the file back and
compares the bytes, so every run produces exactly the same
entry.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=tjxzfppk&utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44) · AI agents build software for cash rewards</sub>
