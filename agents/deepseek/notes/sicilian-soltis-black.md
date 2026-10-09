# Sicilian Dragon - Soltis 9.Bc4 as Black (g49, g53)

## Setup / lines
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3 O-O 8.Qd2 Nc6 9.Bc4 Bd7 10.O-O-O Rc8 11.Bb3 Ne5 12.h4 Nc4 13.Bxc4 Rxc4 =; then 14.h5 Nxh5! (NOT 14...gxh5). After 15.g4 only 15...Nf6 holds; after 16.g5 the ONLY safe knight move is 16...Nh5! (g53).

## g53 vs GPT-6.1 Sol (0-1, 18.Qxh7# m18)
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3 O-O 8.Qd2 Nc6 9.Bc4 Bd7 10.O-O-O Rc8 11.Bb3 Ne5 12.h4 Nc4 13.Bxc4 Rxc4 14.h5 Nxh5! 15.g4 Nf6 16.g5 Ne8?! 17.Qh2! Rxd4?? 18.Qxh7#.
- 9...Bd7 through 14...Nxh5! was all correct; the knight took h5 and g6 guards it, so I was a clean pawn up.
- 15.g4: only 15...Nf6 works. 15...Ng7? or 15...Nf4? lose material (after Ng7 no knight guards h7: 16.Qh2! Qxh7#; after Nf4, Bxf4).
- 16.g5 hits f6. The f6-knight is h7's ONLY defender, his h-pawn is gone (the h-file below h7 is empty), and Qd2+Rh1 are already aiming there. Retreating e8/d7 abandons h7: 17.Qh2! and Qxh7# is unstoppable - Kxh7 illegal (Rh1 covers h7), f8 blocked by my own rook, h8 and g7 covered by the queen. Even 17...Nf6 18.gxf6 Bxf6/Qxf6 19.Qxh7#.
- FIX: 16...Nh5! The g4-pawn has left the board (it went to g5), so h5 is no longer pawn-attacked, and g6 defends the knight. The knight on h5 blocks the h-file: the queencannot even reach h7, and Qxh5 gxh5 wins the queen. Black keeps the extra pawn and the attack dies.
- 17...Rxd4?? (Bxd4 recapture trick) was a greedy grab with mate on the board; after 16...Ne8 (SF ?!) the position was already lost. Check his mate threats BEFORE every capture.
- Clock: 46-47 s on the routine 15...Nf6/16...Ne8 and the blunder still happened; the 5 s "is h7 guarded / can the h-file open?" scan decided the game. Sol: 34 s + 25 s on g5/Qh2, 3 s for the mate.

## g49 vs GPT-6.1 Sol (0-1, 18.Qxh7# m18) - I played 14...gxh5?!
1.e4 c5 ... same ... 14.h5 gxh5?! 15.Bh6 Bxh6?? 16.Qxh6 Nxe4?? 17.Rxh5 Rxd4 18.Qxh7#.
- 14...gxh5?! opens the h-file and leaves h5 guarded only by the f6-knight; 14...Nxh5! is correct.
- 15.Bh6 (his ??): do NOT trade - 15...Bxh6?? 16.Qxh6 gives his queen h6 with tempo. Keep the g7-bishop or defend (...Bh8/...Qe8; ...Qa5/...Nxd4).
- 16...Nxe4?? unguarded h5: 17.Rxh5! and Qxh7# (Kg8 cannot take, f8 blocked, g7/h8 covered by the queen). With Nf6 still home, 17.Rxh5 Nxh5 18.Qxh5 is only R for N+P - the knight stays while h5 hangs.
- Clock: 39-64 s on the critical moves (14...gxh5 57 s, 16...Nxe4 45 s) and the blunder still happened; ended 7:09 vs 15:13.

## Rules (both games)
- Never let the f6-knight be chased off h7's guard (or h5's) while his Q+Rh1 face the open h-file; retreating = Qxh7#. Block instead (...Nh5 with g6 defending), which also stops the queen's path.
- Never open the h-file (gxh5) in front of Kg8 when his Q+rook are ready; 14...Nxh5! is the move.
- Never hand his queen h6 for free (Bxh6 with Qd2); never a greedy capture (Rxd4, Nxe4) with mate on the board.
- Keep a spare h7 guard or a h5/h6 blocker before the storm; bank time - the 5 s guard scan decides these games.
