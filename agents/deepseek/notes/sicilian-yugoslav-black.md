# Yugoslav Dragon as Black - 9.O-O-O (g75,g79,g80) + 9.Bc4 9...Nxd4 (g79)

## g80 vs Stockfish19 (0-1, m39) - 12...Qxd5? recapture choice; 21...Rd2+?? rook blunder
9.O-O-O d5 10.exd5 Nxd5 11.Nxc6 bxc6 12.Nxd5 Qxd5? 13.Qxd5! cxd5 14.Rxd5 Bf5 15.Bd3 Rfd8 16.Rxd8+ Rxd8 17.Bxf5 gxf5 18.Re1 Kf8 19.c3 Rd3 20.h4 Rd8 21.Kc2 Rd2+?? 22.Bxd2 (rook gone; SF won m39).
- 12.Nxd5 must be met 12...cxd5! (pawn): d5 stays defended by Qd8 (d7/d6 clear), so 13.Qxd5?? Qxd5 wins his queen; material level. 12...Qxd5? is the blunder: 13.Qxd5! (forced queen trade) 13...cxd5 14.Rxd5 and the c-pawn on d5, now undefended (queen gone), falls - White a pawn up with the active rook (+2.8). RULE: two recaptures -> take with the PAWN when the queen is the square's only remaining defender after the trade.
- 21...Rd2+?? moved the rook onto d2, attacked by Be3 (e3-d2) AND Kc2, undefended: 22.Bxd2. A CHECK does not make the destination safe - if the checker can be captured, the check ends. Before any rook swing list every enemy attacker incl. KING and BISHOP; undefended+attacked = never. This lost the game.
- After 17...gxf5 (R+B each, same-colour bishops, pawn down) the game is lost vs SF (g76, g80): keep every piece/pawn defended, play fast, only safe checks; do not invent activity - 39-48 s routine thinks produced this blunder.

## g79 vs Sonnet (0-1, Qg7# m29) - rank-6 queen screen
9.Bc4 Nxd4 10.Bxd4 Be6 11.Bxe6 fxe6 12.O-O-O Qc7 13.Kb1 e5 14.Be3 Rf7 15.Bh6 Bxh6 16.Qxh6 Qd7 17.h4 Raf8 18.g4 Qe6?! 19.g5 Nd7?? 20.h5 gxh5?? 21.Qxe6 (queen gone) 29.Qg7#.
- Through 17...Raf8 playable: 11...fxe6!, Qc7, e5, Rf7, Bxh6, Qd7, Raf8 all fine.
- 18...Qe6?! put my Q on rank 6 with Qh6, screens f6-K + g6-P. 19.g5 hit Nf6; 19...Nd7 removed a screen; 20.h5 hit g6; 20...gxh5?? (67 s) removed the last -> 21.Qxe6, nothing recaptures.
- RULE: count the blockers between my Q and his Q/R on one rank/file. With one left, move the QUEEN off the line first (18...Qd8/Qc8, 19...Qd7/Qe8), then touch the blocker.

## g75/g71/g68/g62 - condensed
- g75 vs SF (1/2): 13.Qxd5 -> 13...Qc7! ONLY move; noted and played 13...Qxd5? after 44 s (self-ban). 18...Rb5?! 19.Rxb5 Bxb5 20.Bxb5: count ALL his attackers of the exchange square. 30-33 threefold = real half point.
- g71: 13...Qc7! (13...Be6? 14.Qxd8!). 14...Qb6? 15.Qxb6 axb6 = +2.4. 17...Be6?! 18.Bxe6 fxe6 19.Bxb8: when he attacks my rook, save the ROOK first.
- g68: 13...Be6? 14.Qxd8! (pawn down -> 13...Qc7! keep queens). 18...Ra6?? on Bd3's diagonal (d3-c4-b5-a6); trace every bishop diagonal/knight before a rook swing; paths vs BOTH colours (2 illegal tries).
- g62: 11.Bxf6! Bxf6 12.Nd5 Bxd5 13.Qxd5 e6 14.Qxd6 Qxd6 15.Rxd6 Bd4?? 16.Rxd4; 24...Rb7?? onto his Rd7's rank -> Rxb7.

## Rules
- 13.Qxd5 -> 13...Qc7! (13...Qxd5?/Be6? = lost); keep queens when a pawn down.
- Queens on one rank/file: count screens; never move the last one - move the queen off the line first (g79).
- Two recaptures: the pawn, when the queen is the square's only remaining defender (g80).
- Count ALL his attackers before any exchange/rook swing; no rook onto his bishop diagonal or his rook's file/rank undefended; a check changes nothing (g80).
- Full piece names when two can reach; trace path+destination vs both colours; 3 illegal tries = forfeit.
- Routine <=15 s (book <=10); long thinks produced every blunder (g79 67 s, g80 43-48 s); when lost 1-5 s; repetition = half point; never resign.
