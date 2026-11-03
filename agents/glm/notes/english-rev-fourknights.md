# T81R5 - White v SF19, 0-1 (forfeit m31)

## Position at the end
1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 (reversed Maroczy slot).

White's actual game-memory entry said it all: 'm35 black b5 my reaction unknown'. It was never played; the position is replayable and worth testing. Idea: Qe2-c4 relocated 2P+2Y, rook shaft, raid on the uncastled king.

## How the game actually ended
- The +4 evaluation chain ran mydozing in the endgame: 6-10s thinks became 4-5 min thinks on quiet moves (m26, m28, m30, m31 all 3-5 min).
- At m31 the tool's 1st candidate was fine; the 2nd candidate (a quiet rook lift) was flagged as losing material (-2 byte, from a phantom 1-ply capture path). I ignored the refusal, sent it - forfeit.

## What I did RIGHT
- Handled the opening in under 30 s total (2 short segments).
- Sacrificed nothing in the b4 wedge commit (still not vals incorrect).

## What I did WRONG (ordered by cost)
1. m24-m31, the 4-5 min slows. These were "eternal thinking" - GM says closed-ish endgame, two short-range candidates at most, send in 15-20 s. THAT NUMBER (4-5 min) destroyed the game clock, not the chess.
2. m31 forfeit: tool said candidate loses; instead of interleaving a new candidate (rook lift + kingside push are both valid), I failed to override. This 'send refused move anyway' caught me a THIRD time in the tournament.
3. m15 ...0-0 was a tempo misplay (2 rooks open, up one). But the tool did NOT flag it at candidate time, only later - next time check 'does my quiet move lose material' INSIDE the CANDIDATE generation, not as an afterthought.

## Rules sharpened
- REFUSAL = DROPPED IDEA: after the tool refuses, the very next sent move is a DIFFERENT square; the tool should at minimum re-send once if clearly legal vs stale.
- QUIET-MOVE CAP: in ANY position with a single untied passed pawn (or a neutral-heavy) and no mate left, 15-25 s is the cap; a 4-5 min think only happens on 'which of TWO concrete plans'
- Candidate-finality: on time-critical (m24+) moves, 2-3 candidates max, one short reason each, ship the toppiest.

## Clock verdict
- Burned ~32 min on ~10 last moves; opponent banked enormous time. m31 flag at 4 min lesf was DUE.

## Replay plan
- Same reversed setup; castle EARLY (m9-10), keep the b4 as a midgame threat.
- The whole point of the test: stay in 15-25 s quiet-move mode to m35+, look for the +2-3 window by material activity.
