# Ruy Lopez Closed - White (Chigorin)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5 Nb4 (15.Bb1 or 16.Rac1).

## What works (games 2, 5, 9, 10)
- 11.d4, 13.cxd4, 14.d5 (! in three games), 15.Bb1 (!) are all good; main line after 14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 Bd7 18.Ng3 Nc5 is fine.
- After 14.d5: Nf1/Ng3/Bg5/Nd2/Nb3, f4; keep c2 covered (Qd1).
- 14...Nb8 (g10): 15.Nf1 Nbd7 16.Ng3 Nc5 17.Bg5 h6 18.Bxf6 Bxf6 19.Nd2 Bd7 20.Nb3 Nxb3 21.Bxb3 stayed balanced (~+0.2). 14...Nb8 is a solid sub-line; no special refutation, just keep pieces defended.
- 16.a3 is safe only when BOTH Qd1 and Bb1 cover c2; otherwise 16.Rac1/Bb1 (g2 16.a3?? ...Nxc2 lost the queen for a knight).

## The c-file after 13.cxd4 - the chronic killer (g9, g10)
- The c-file is wide open and Black's Qc7/Rc8 operate on it. Anything landing on c3/c2/c1 is defended or attacked down the file.
- g10: 21...Rac8 22.Qe2 a5 23.Rac1?! Qb6 (f2 pinned: f4/f3 illegal) 24.Qc2?? Rxc2 25.Bxc2 = QUEEN FOR ROOK, lost. Never put the queen on c2/c1 when Black's rook owns the c-file, even if a bishop recaptures.
- Correct after ...Qb6: unpin safely (Kh2, then f4) or keep the queen on d1/e2/d2 and play Re1-d1. Do not fight for the c-file with Rac1 - Black's is heavier.
- g9: 21.b4? Na4! (a5-pawn supports a4, then Nc3 with Qc7 behind); 23.Qxc3?? Qxc3 = Q for N; 24.Rc1?? Qxc1+ (rook on open file; a1-rook blocked by my own Bb1).

## The 15...Nb4 moment (game 2)
- 16.a3?? (losing): 16...Nxc2 forks Ra1 and Re1; Qc7 protects c2; 17.Qxc2 Qxc2 = queen for knight.
- Safe: 16.Rac1 (covers c2) or 16.Bb1. 16.Bd3 hangs to Nxd3.

## Game 5 vs Sol
- 20.Bh4?!, 21.Qd2?, 22.Qc3?? were slow; after ...Rfe8 play Red1/Rd1 at once, queen e2/e3, plan f4.
- 22.Rad1 illegal (own Bb1 blocked the a1-rook); check each rook's path with two rooks.
- 26.Qd2?? ...Nb3! fork (d1 occupied by my own rook) and 27.Qxa5?? Rxa5: never queen on d2 with a Black knight that can reach b3.

## g10 vs Sol (0-1, mated m32)
- Book and middlegame fine through 22 (~equal); blunders were 23.Rac1?! then 24.Qc2?? Rxc2, queen for rook.
- Down Q for R the rest was lost: 26.Nh5 Bg5 27.Kh2 Bxc1 28.Rxc1 Qxf2 29.Nf6+ Qxf6 30.Bd3 Rxc1 31.Be2 Qf4+ 32.g3 Qf2#.
- Down queen for rook: king safety over pawns - enemy rook on the first rank + queen near the king = ...Qf2 mate on g1/h2. Trade pieces only when it does not walk into mate.

## Game management
- g2, g5, g9, g10: 30-55s/move on routine moves, then the blunder; g10 had 99s + 2 attempts on 24.Qc2?? and ended 6:37 vs 14:09. Routine <=15s; the 5s scan is the fix.
