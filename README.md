# makefun-tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/shun35960/makefun-tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/shun35960/makefun-tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in 3,589 bytes of Python (`main.py`, standard library only): iterative-deepening alpha-beta search with a fixed node budget (fully deterministic, no clock), quiescence over captures and promotions, a transposition table, killer and MVV-LVA move ordering, null-move and delta pruning, and a material + piece-square-table evaluation with a passed-pawn bonus. It plays the make.fun house gauntlet through the competition env over HTTP. Local practice result on the kit's trial 0: Elo 1279 (3 wins, 3 losses), above the 1,154 final-qualification floor.

## Run it

With a competition env running (see the tiny-chess-01 kit's `program/env/server.mjs`):

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8200 MAKEFUN_PROMPT_FILE=<practice-trial>/input/prompt.txt python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=3enr53qh&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
