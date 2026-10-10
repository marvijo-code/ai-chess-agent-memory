# Sicilian Dragon - Soltis 9.Bc4 as Black (g49,g53,g54,g66 lost to Sol; g55 lost to Sonnet)

## Line
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3 O-O 8.Qd2 Nc6 9.Bc4 Bd7 10.O-O-O Rc8 11.Bb3 Ne5 12.h4 Nc4 13.Bxc4 Rxc4 =; 14.h5 Nxh5! (never ...gxh5, g49); 15.g4 Nf6 (only move).

## g66 vs Sol (0-1, Qxh7# m18) - Nf6 is PINNED to h7
14.h5 Nxh5 15.g4 Nf6 16.Qh2 Rc8?? 17.g5 Nxe4?? 18.Qxh7#.
- After 16.Qh2 the h-file is open (h3-h6 empty: his h-pawn died on h5) and his Qh2+Rh1 bear on h7. My Nf6 is h7's SOLE guard (Kg8 cannot take: Rh1 covers h7). So the knight is absolutely tied: any move OFF the h-file = Qxh7#. 17...Nxe4?? left h7 and was mated at once.
- The only safe knight square is h5, because it blocks the h-file: 17.g5 -> 17...Nh5! and Qxh5?? gxh5 wins his QUEEN (g6 defends h5), while gxh5 is impossible for his pawn (on g5 the pawn attacks f6/h6, not h5).
- ...Nh5 is safe ONLY once his g-pawn has left g4; with his pawn still on g4, gxh5! wins the knight and the mate follows on h5/h7 (g54 16...Nh5?? 17.gxh5!).
- 16...Rc8?? (38 s, Stockfish ??) was the first error; a queen/rook/pawn move that does not touch the pin was needed (...Qa5/...Qc7/...g5!? ideas). Never improvise in this razor-sharp line: at every move ask 'is Nf6 still the only guard of h7, and are h3-h6 empty?'
- Clock: 18-46 s on m8-17 and both bad moves came after 38-46 s. The 5 s pin-check would have caught 17...Nxe4.

## The ...Nh5 block - only when his g-pawn has left g4
- 16.g5: g4 vacated, h5 is NOT pawn-attacked -> 16...Nh5! is the only move: g6 defends h5, the knight blocks the h-file, Qxh5 gxh5 wins his queen. Retreating Ne8/Nd7 abandons h7: 17.Qh2! Qxh7# (g53).
- 16.Qh2: g4 STILL attacks h5 -> 16...Nh5?? loses: 17.gxh5! gxh5 18.Qxh5 and Qxh7# (g54). Instead ...Qa5 (hits a2/Nc3); if he then plays 17.g5, ...Nh5! is right.

## g55 vs Sonnet (0-1, flagged m53)
Same line to 16...Nh5! (only move); 17.Qd3 Rc8 18.Nf5 Bxf5! 19.exf5.
- 19...gxf5?? moved the g6-pawn, h5's ONLY guard: 20.Rxh5 won the knight for free - the game's turning point. After 19.exf5 keep g6 home: ...Qd7/...Qc7/...Nd7 first.
- 27...Rd2?? with White's Kc1: the rook stood on a square his KING attacks -> 28.Kxd2, a whole rook. Check the enemy king's 8 neighbour squares like any other attacker.
- Clock: 35-65 s on m14-27 (routine) yet still blundered, then 0:18 vs 11 min and flagged at m53. In lost positions play 1-3 s/move - the 10 s increment keeps you alive; only stalemate/repetition can rescue.

## g54 vs Sol (0-1, 19.Qxh7#)
13...Rxc4! 14.h5 Nxh5! 15.g4 Nf6 16.Qh2 Nh5?? 17.gxh5! gxh5 18.Qxh5 Bxd4?? 19.Qxh7#.
- Through 15...Nf6 correct (Rxc4! best, clean pawn up). 16...Nh5?? applied the g53 fix blindly; g4 took the knight, the h-file opened with tempo, mate followed.
- 18...Bxd4?? another greedy grab with mate on the board.
- Clock: 40/36/48/49/58 s on m14-18 - long thinks did not help. The 5 s scan - does his g-pawn attack h5? what guards h7? can the h-file open? - decides these games.

## g53 vs Sol (0-1, 18.Qxh7#)
14.h5 Nxh5! 15.g4 Nf6 16.g5 Ne8?! 17.Qh2! Rxd4?? 18.Qxh7#. 16.g5 = g4 gone -> only 16...Nh5!; Ne8/Nd7 lose h7 (Nf6 was its only guard).

## g49 vs Sol (0-1) - 14...gxh5?!
14...gxh5?! opened the h-file (14...Nxh5! was right); after 15.Bh6 do NOT trade (15...Bxh6?? 16.Qxh6 hits h7 with tempo); 16...Nxe4?? while h5 hung: 17.Rxh5! Qxh7#.

## Rules
- Block with ...Nh5 only from a square his g-pawn cannot capture (his pawn on g5, or h5 defended by g6); check the pawn first.
- Once his Q is on h2 with the h-file open, Nf6 cannot leave the h-file at all (mate); ...Nh5 (blocking) is the only knight move, and it needs his g-pawn off g4.
- The g6-pawn is the h5-knight's SOLE guard: never push or recapture with it while the knight sits on h5 (g55 19...gxf5??).
- Never move the f6/h5 knight off h7's guard while his Q+Rh1 face the open h-file.
- No greedy captures (Rxd4, Nxe4, Bxd4) with mate on the board.
- Keep a spare h7 guard or h5/h6 blocker before the storm; bank time - moves 14-17 come fast.
