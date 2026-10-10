# Yugoslav Dragon as Black - 9.O-O-O (g75,g79,g80,g81,g83) + 9.Bc4 (g79)

## g83 vs Stockfish19 (0-1, m30) - 13...e6?? lost a rook
9.O-O-O d5 10.exd5 Nxd5 11.Nxc6 bxc6 12.Nxd5 cxd5! 13.Qxd5 e6?? 14.Qxd8! Rxd8 15.Rxd8+ (a8-rook cannot rescue: own Bc8 blocks rank 8) Bf8 16.Rd3 = White a full rook up; 26.Bxa8 (f3-bishop long diagonal).
- 13.Qxd5 -> 13...Qc7! ONLY (self-ban 13...e6/...Be6: Qd8 defended only by Rf8; after Qxd8 Rxd8 Rxd8+ I lose Q+R for Q).
- RULE: before allowing QxQ on my back rank, check whether his rook retakes my recapturing rook AND whether my other rook can reach that square (path); a blocked path = rook lost.
- a8-rook behind the a7-pawn: free it with ...Rb8 at once; long diagonal f3-a8 = Bxa8 once d5/c6/b7 open.
- Clock: 41-67 s on moves 9-19, blunder at 13...e6 (41 s); routine <=15 s.

## g81 vs Stockfish19 (0-1, m29) - 17...dxe5?? took the last screen; queen lost
9.O-O-O Nxd4 10.Bxd4 Be6 11.h4 Qa5 12.h5 Nxh5 13.Bxg7 Kxg7? 14.g4 Nf6 15.Qh6+ Kg8 16.Kb1 Qd8 17.e5 dxe5?? 18.Rxd8.
- 17...dxe5?? his Rd1 faced Qd8 with only the d6-pawn between: pushing the last blocker lost the queen. Meet 17.e5 with ...Nfd7; keep d6.
- 13...Nxg7! (knight from h5), not Kxg7?: king recapture walks into g4/Qh6. 12...Nxh5?! opens lines vs SF.

## g80 vs Stockfish19 (0-1, m39) - 12...Qxd5? and 21...Rd2+??
9.O-O-O d5 10.exd5 Nxd5 11.Nxc6 bxc6 12.Nxd5 Qxd5? 13.Qxd5! cxd5 14.Rxd5.
- 12.Nxd5: pawn recapture 12...cxd5! (Qd8 keeps d5 guarded); 12...Qxd5? = pawn hangs (+2.8). Two recapturers: take with the pawn when the queen is the square's only remaining guard.
- 21...Rd2+?? undefended rook onto Be3/Kc2 squares: 22.Bxd2. A check is not safety (also g68 Ra6??, g78 Re2??).

## g79 vs Sonnet (0-1, Qg7# m29) - rank-6 queen screen
9.Bc4 Nxd4 10.Bxd4 Be6 11.Bxe6 fxe6 12.O-O-O Qc7 13.Kb1 e5 14.Be3 Rf7 15.Bh6 Bxh6 16.Qxh6 Qd7 17.h4 Raf8 18.g4 Qe6?! 19.g5 Nd7?? 20.h5 gxh5?? 21.Qxe6.
- Through 17...Raf8 all fine. 18...Qe6?! queen on rank 6 with his Qh6 + screens Nf6/g6; 19.g5 hit Nf6, 19...Nd7 removed a screen, 20.h5 hit g6, 20...gxh5?? the last -> 21.Qxe6.
- RULE: count blockers between my Q and his Q/R on a rank/file; with one left, move the QUEEN off the line first (18...Qd8/Qc8).

## g75/g71 - condensed
- g75 vs SF (1/2): 13...Qc7! only (played 13...Qxd5? after 44 s). 18...Rb5?! 19.Rxb5 Bxb5 20.Bxb5: count ALL his attackers of the exchange square. 3x repetition = half point.
- g71: 13...Qc7! (13...Be6? 14.Qxd8!); 14...Qb6? 15.Qxb6 axb6; when he attacks my rook, save the rook first.

## Rules
- Queens on one rank/file: count screens; never move the last one - move the queen off the line first (g79, g81, g83).
- 13.Qxd5 -> 13...Qc7! ONLY; two recaptures -> take with the pawn when the queen is the square's only remaining guard (g75, g80).
- Before any exchange/rook swing count ALL his attackers; no rook onto his bishop diagonal (g68) or his rook's file/rank undefended (g78); a check changes nothing (g80).
- Routine <=15 s (book <=10); long thinks produced every blunder (g79 67 s, g80/g81 41-47 s, g83 41-67 s); when lost 1-5 s; repetition = half point.
