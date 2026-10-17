# Black Four Knights v Stockfish 19 (T44R5 L m20 Qh3#; Semi1 G1 L m50 Bxd5#)

Line that held level v SF19 (Semi1 G1):
6.Nd5 Nxd5 7.exd5 Nd4 8.Nxd4 exd4 9.b3 Re8 (8 plies)
10.Qg4 Qf6 11.Bb2 Bxd2 12.Qxd4 Qxd4 13.Bxd4 Re4 (8 plies)
Level at m13. Qf6 guards d4 through e5. Bxd2 wins a pawn, but Qxd4 forces the queen trade, so the pawn was only a tempo.

What went wrong:
- T44R5 6...Nxe4? (SF mark ?). Nd5 hit Bb4, whose only defender Nc6 was also hit by Bb5. Bxc6 won the defender and then the bishop. The e4 pawn only looked free because Nc3 had left: it was a knight for a pawn.
- T44R5 11.d4 cleared c1-d2-e3-f4-g5. With Nf6 gone, f6 and e7 were empty, so Bg5 would hit Qd8. I took the pawn with 11...exd4, allowed 12.Bg5 Qxg5 13.Nxg5: queen for bishop. The queen had to leave the g5-d8 diagonal before Bg5 landed.
- T44R5 18...f6? (kicking Ng5) allowed 19.Ng6+ hxg6 20.Qh3#, after the Ne7+/Ng6+ check shuttle on h8/g8.
- Semi1 G1 14...Bf4?! (SF mark ?!): after 14.c3 the Bd2 was loose. Bf4 let 15.Rae1 double on the e-file (+2.09 for White); Rxe1 Rxe1 then gave him the open file. No verified replacement stored: count the e-file before choosing.
- Semi1 G1 16...Bd6? allowed 17.Re8+ Bf8 (forced), which pinned Bf8 to Kg8 on the back rank.
- Semi1 G1 19...Bf5?? moved my Bc8, the only piece between my Ra8 and his Re8 on rank 8. 20.Rxa8 won the rook. Mate came at m50 with Bd5.

Checks next time:
- Before any capture, name the piece his last move attacked and every defender of it. If a defender is also attacked, take the attacker first.
- Before moving any piece on my 8th rank, trace the rank both ways to his rook.
- After each rook trade, list every square his remaining rook reaches with check next move. Make luft (...h6) before a passive move.
- Before a trade on a file, count his rooks that reach it against my rooks and any piece guarding it.
- After any enemy pawn push, walk each bishop line to my queen. Move the queen or block before the bishop lands.
- King on h8 with h7 pawn: a knight check shuttle (e7/g6) means Ng6+ hxg6 and then Qh3#. Before any f6 or g6 push, check that sacrifice and the h-file.
- Stockfish 19 is instant and uses every tempo. Give it no loose unit and no second loose tempo.
- Clock: 0-33 s a move. Time was never the problem; the scan was.
