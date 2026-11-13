# rebuild6 Track 2 — external-book variant ("ext")

## What it is
The opening-book engine (rebuild2 A base + 120-entry house opening book),
repacked to fit the 4,096-byte limit by moving the book OUT of main.py
into a sibling file `book.txt` (JSON, 1,101 bytes) loaded at import time.
Repo total: packed main.py 4,083 + book.txt 1,101 = 5,184 < 8,192.

Files:
- `ext/main.py` — source (7,826 bytes), written in-session (3 chunks)
- `ext/book.txt` — 120 entries, keys = str((zh>>41)&0x7ff), values = index
  into g()-order legal list. Same book data as `book.json`.
- `ext/packed/main.py` — packed (4,083 bytes, FITS 4,096)
- `ext/packed/book.txt` — copy of book.txt next to the packed file
  (the packed file loads it via `__file__[:-7]+'book.txt'`)

## Changes vs rebuild2 base (measured, exp7)
- `BK=json.load(open(__file__[:-7]+'book.txt'))` at import; `fm` parsed
  from the FEN (fullmove number); book lookup in r() only when fm==5.
- Golfs (behaviour-neutral): CD dict-comprehension, W/M as 10**6/10**5,
  KP as dict + .get(), E() enumerate.
- Behaviour change 1: repetition-avoidance block in r() DROPPED
  (saves 60 packed bytes; isolated Elo cost unknown — the trials below
  measure the net effect).
- Behaviour change 2: `sys.exit` env guard dropped (error-path only).
- `sys.path[0]` NOT used: under `python3 -P -s` it is
  '/usr/lib/python312.zip', not the script dir. `__file__` works both
  as a script and when imported by trial_driver.

## Bugs found while building this variant
1. JSON keys are strings: `BK.get((zh>>41)&2047)` (int key) NEVER hits.
   Fixed to `BK.get(str((zh>>41)&2047))`. (Without the fix the first
   verification ran 120 full 60k-node searches instead of book hits —
   that slowness is how it was caught.)
2. `opening/pack.py` dropped one closing paren: it produced
   `...b85decode(b'...'))` (2 parens) instead of `...')))` (3).
   Both `opening/packed/main.py` (4,637) and the first ext pack were
   SyntaxErrors. Fixed pack.py (added the missing `)`); re-packed ext
   to 4,083 bytes. NOTE: this means the opening track's 1,464/1,326
   scores came from the SOURCE main.py (run_trial2.sh passed
   `bot=main.py`), never from the packed file — and the packed file
   was never valid Python.

## Verification (source AND packed, before trials)
- perft 1/2/3: 20 / 400 / 8,902 (source and packed)
- determinism: startpos d2d4 twice (source 3.0s/2.9s; packed d2d4=d2d4)
- book hits via r(): 120/120 (source and packed)
- packed size: 4,083 bytes (fits, 13 slack)

## Trials (packed file, grade-local)
- trial-1: Elo 1,326 (2W/3D/3L, working=1, spare_plies 156), wall 923s,
  worst move 3,734 ms. IDENTICAL score and W/D/L to plain-book trial-1
  (1,326, 2W/3D/3L) — the repetition-block drop cost nothing here.
  3 games ended by threefold repetition.
- trial-0: Elo 1,464 (4W/1D/3L, working=1, spare_plies 378), wall 1,331s,
  512 moves, worst move 3,100 ms. IDENTICAL score and W/D/L to
  plain-book trial-0 (1,464, 4W/1D/3L, spare 378, 512 moves).
  The golfing (external book + dropped repetition block) cost ZERO Elo:
  both trials reproduce the plain book's scores exactly.
- Worst moves: trial-0 3,100 ms, trial-1 3,734 ms (target ≤ ~3 s local;
  ~6–7.5 s at 2x server slowdown, still under the 10 s limit).
  (Plain-book trial-0's 7,535 ms worst was likely CPU contention
  during that run; ext ran on a quiet machine.)

## Warm variant — DROPPED (decided 13:20 UTC)
- trial-1-warm finished: Elo 1,396 (3W/2D/3L, working=1).
- Warm final: trial-0 1,326 / trial-1 1,396, mean ~1,361.
- Plain book final: trial-0 1,464 / trial-1 1,326, mean ~1,395.
- Reason: plain book beats warm on mean and on trial-0; TT-warming
  does not pay. Warm is not a candidate.
