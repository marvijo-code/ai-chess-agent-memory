# Black Four Knights v Stockfish 19 (T44R5, L m20, Qh3#)

Opening as played: 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O, then 6.Nd5 (SF's knight jump).

What went wrong:
- 6...Nxe4? (SF mark ?). Nd5 hit Bb4, and Bb4's only defender was Nc6, which Bb5 also hit. Bxc6 took the defender and the bishop was lost. The e4 pawn only looked free because Nc3 had left, so the grab was a knight for a pawn.
- Idea to check on the board (unverified here): 6...Nxd5 removes the attacker. Another player's note on the same structure gives ...Nxd5 exd5 e4 as the key reply.
- 11.d4 cleared c1-d2-e3-f4-g5. With Nf6 gone, f6 and e7 were empty, so Bg5 would hit Qd8. I took the pawn with 11...exd4 and allowed 12.Bg5 Qxg5 13.Nxg5: queen for bishop. The queen had to leave the g5-d8 diagonal before Bg5 landed. Check the Nd5 knight (it covers e7, c7, f6) before choosing the square.
- 13...c6 kicked Nd5 correctly. Then 14.Qf3 Rf8 15.Ne7+ Kh8 16.Ng6+ Kg8 17.Ne7+ Kh8 was a forced shuttle. 18...f6? (kicking Ng5) allowed 19.Ng6+ hxg6 20.Qh3#.

Checks next time:
- Before any capture, name the piece his last move attacked and every defender of it. If the defender is also attacked, take the attacker first.
- After any enemy pawn push, walk each bishop line to my queen. Move the queen or block before the bishop lands.
- King on h8 with h7 pawn: a knight check shuttle (e7/g6) means Ng6+ hxg6 and then Qh3#. Before any f6 or g6 push, check that sacrifice and the h-file.
- Stockfish 19 is instant and uses every tempo. Give it no loose unit and no second loose tempo.
- Clock: 0-26 s a move. Time was never the problem; the scan was.
