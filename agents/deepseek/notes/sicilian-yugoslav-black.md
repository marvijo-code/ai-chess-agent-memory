# Yugoslav Dragon as Black - 9.O-O-O (g75,g79,g80,g81) + 9.Bc4 9...Nxd4 (g79)

## g81 vs Stockfish19 (0-1, m29) - 17...dxe5?? took the last screen; queen lost
9.O-O-O Nxd4 10.Bxd4 Be6 11.h4 Qa5 12.h5 Nxh5 13.Bxg7 Kxg7? 14.g4 Nf6 15.Qh6+ Kg8 16.Kb1 Qd8 17.e5 dxe5?? 18.Rxd8 (queen gone) Rfxd8 19.Kc1 Rac8 20.Bb5 Rxc3 21.bxc3 ... 28.Rd8+ Ne8 29.Rxe8#.
- 17...dxe5?? his Rd1 faced my Qd8 on the d-file with only the d6-pawn between (d7/e7 empty): pushing the last blocker lost the queen (g79 screen rule in the centre). Meet 17.e5 (hits Nf6) with 17...Nfd7; keep d6.
- 13...Nxg7! (knight takes from h5), not Kxg7?: recapturing with the king walks into g4/Qh6; knight recapture keeps g8 safe and guards h5. Grabbing h5 here (12...Nxh5 ?!) opened lines vs SF - not worth it.
- From m18 down Q for R: defense only, keep every unit guarded, expect mate; no tricks vs SF.

## g80 vs Stockfish19 (0-1, m39) - 12...Qxd5? recapture choice; 21...Rd2+?? rook blunder
9.O-O-O d5 10.exd5 Nxd5 11.Nxc6 bxc6 12.Nxd5 Qxd5? 13.Qxd5! cxd5 14.Rxd5 Bf5 ... 21.Kc2 Rd2+?? 22.Bxd2.
- 12.Nxd5: recapture with the PAWN 12...cxd5! (d5 stays defended by Qd8; 13.Qxd5?? Qxd5). 12...Qxd5? 13.Qxd5 cxd5 14.Rxd5 left the pawn undefended - a pawn down (+2.8). Two recaptures: take with the pawn when the queen is the square's only remaining defender.
- 21...Rd2+??: undefended rook onto a square attacked by Be3 (e3-d2) AND Kc2 -> 22.Bxd2. A check does not make it safe (also g68 Ra6??, g78 Re2??). After 17...gxf5 (R+B each, pawn down) = lost vs SF: defend only, play fast.

## g79 vs Sonnet (0-1, Qg7# m29) - rank-6 queen screen
9.Bc4 Nxd4 10.Bxd4 Be6 11.Bxe6 fxe6 12.O-O-O Qc7 13.Kb1 e5 14.Be3 Rf7 15.Bh6 Bxh6 16.Qxh6 Qd7 17.h4 Raf8 18.g4 Qe6?! 19.g5 Nd7?? 20.h5 gxh5?? 21.Qxe6.
- 11...fxe6!, Qc7, e5, Rf7, Bxh6, Qd7, Raf8 were all fine. 18...Qe6?! put my queen on rank 6 with his Qh6 and screens f6-knight + g6-pawn; 19.g5 hit the knight, 19...Nd7 removed a screen, 20.h5 hit g6, 20...gxh5?? (67 s) removed the last -> 21.Qxe6 (nothing recaptures).
- RULE: count the blockers between my Q and his Q/R on a rank/file; with one left, move the QUEEN off the line first (18...Qd8/Qc8), then touch the blocker.

## g75/g71 - condensed
- g75 vs SF (1/2): 13.Qxd5 -> 13...Qc7! only (noted, then played 13...Qxd5? after 44 s). 18...Rb5?! 19.Rxb5 Bxb5 20.Bxb5: count ALL his attackers of the exchange square. 3x repetition = half point.
- g71: 13...Qc7! (13...Be6? 14.Qxd8!); 14...Qb6? 15.Qxb6 axb6 +2.4; when he attacks my rook, save the rook first.

## Rules
- Queens on one rank/file: count screens; never move the last one - move the queen off the line first (g79; g81 17...dxe5??).
- 13.Qxd5 -> 13...Qc7!; two recaptures -> the pawn, when the queen is the square's only remaining defender (g75, g80). Keep queens when a pawn down.
- Count ALL his attackers before any exchange/rook swing; no rook onto his bishop diagonal (g68 Ra6??) or his rook's file/rank undefended (g78 Re2??); a check changes nothing (g80).
- Routine <=15 s (book <=10); long thinks produced every blunder (g79 67 s, g80/g81 41-47 s); when lost 1-5 s; repetition = half point.
