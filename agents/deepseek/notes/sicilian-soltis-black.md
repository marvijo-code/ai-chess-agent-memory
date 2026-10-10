# Sicilian Dragon - Soltis 9.Bc4 as Black (g49,g53,g54,g66,g69,g74 vs Sol; g55)

## Line
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3 O-O 8.Qd2 Nc6 9.Bc4 Bd7 10.O-O-O Rc8 11.Bb3 Ne5 12.h4 Nc4 13.Bxc4 Rxc4 =; 14.h5 Nxh5! (never ...gxh5, g49); 15.g4 Nf6 (only move).
Record vs Sol in this line: 0-6 (g74 = 6th loss). Every loss = guard/pin/loot blunder, not the opening; if it appears again, weigh 9...d5 / other paths.

## g74 vs Sol (0-1, Qh7# m22) - Nxh5 blunder with g4 already on
12.h4 Nc4 13.Bxc4 Rxc4 14.g4!? Rc8 15.h5 Nxh5?? 16.gxh5 (N for P) Qa5 17.Kb1 Qb4 18.Bh6 Qb6 19.hxg6 hxg6 20.Bxg7 Kxg7 21.Qh6+ Kg8 22.Qh7#.
- Move-order trap: 14.h5 Nxh5 works only while his g-pawn is home (then 15.g4 kicks the knight to f6). He played 14.g4 FIRST, so 15...Nxh5?? = 16.gxh5, knight for a pawn. My own ply-30 note said it; I played it anyway (self-ban violation). With g4 on: keep Nf6 (h7's guard); meet h5 with ...Qa5 counterplay or ...gxh5 (then gxh5 leaves his pawn on h5, blocking Rh1 - no Qh7 net).
- 14...Rc8?! (SF) drifts; 13...Rxc4! was right; then ...Qa5/...h5 ideas, not a passive rook pull.
- 18.Bh6 without recapture was correct, but 19.hxg6 opened the h-file. 19...fxg6 keeps f7 as a king escape; 19...hxg6? 20.Bxg7 Kxg7 21.Qh6+ Kg8 22.Qh7# (Rh1 protects Qh7; my own Rf8 blocks f8, f7/g7/h8 covered).
- Clock: 36-46 s thinks on moves 12-22 produced 14...Rc8?!/15...Nxh5??; the 5 s recapture scan (does his g4-pawn take h5?) catches it.

## Older games - condensed
- g69: 16.Bh6 Bxh6? terrible (17.Qxh6 Qe8 18.g5 Nh5 19.Rxh5! gxh5 ... Re8 next); 20...Qd8? 21.Rh1 h4 22.Rxh4!; 22...Rxd4?? R for N = 23.Qxh7#. Never recapture Bh6; get ...Re8 luft early; no loot with mate on.
- g66: 16.Qh2 (h-file open; Nf6 = h7's only guard) 16...Rc8?? 17.g5 Nxe4?? 18.Qxh7#. 16.Qh2: the only knight square is h5, and only once g4 has left.
- g54/g53: 16.Qh2 with g4 on: NO ...Nh5 (17.gxh5!); 16.g5 -> only ...Nh5 (Ne8?? 17.Qh2 Rxd4?? 18.Qxh7#). 18...Bxd4?? greedy with mate on.
- g49: 14...gxh5?! opened the h-file (14...Nxh5!); 15.Bh6 do NOT trade (15...Bxh6?? 16.Qxh6); 16...Nxe4?? 17.Rxh5! Qxh7#.
- g55: 19...gxf5?? moved g6, h5-knight's sole guard -> 20.Rxh5; 27...Rd2?? Kxd2; flagged.

## Rules
- Before any knight move: is f6/h5 my only h7 guard? is the h-file open? does his g-pawn attack h5? g4 ON: ...Nxh5 loses to gxh5 (piece for pawn). g4 GONE: ...Nh5 only after g5, and g6 must stay.
- Never trade Bh6: ...Qe8/...Qa5 + luft (...Re8). Keep g6 while a knight sits on h5.
- No material grabs (Rxd4, Bxd4, Nxe4) while Qxh7# is pending.
- Routine <=15 s; long thinks produced every blunder in this line.
