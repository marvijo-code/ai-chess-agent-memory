# MEMORY (clocks 900+10)

## Record
- T34 R3 W v DeepSeek, Rauzer Sicilian: L m26. 13.g5?? (after 12...Bxf6 the bishop hit d4, my Nd4's ONLY guard was Qd2): 13...Bxd4! 14.Qxd4 Nxd4 = Q for B. Later 24...Qxf4+ 25.Kb1? Qxd2 (rook unguarded) 26...Qe1#. 5 illegal attempts cost 17-40 s each.
- T34 R1 B v Sol, Open Sicilian (Scheveningen): L m24. Marks: 14...b5?, 15...Qb6?; killer 21...Qd3?? (queen beside the c2-pawn, 22.cxd3).

## Key lessons (check before EVERY move)
- RECAPTURE FIRST: after his capture, name MY recapturer before anything else - and what that recapturer leaves unguarded (14.Qxd4 'restored balance' but sat where Nxd4 wins it). 15...Qb6?? (T34 R1) left b5 AND c6 loose; 15...axb5 was there.
- ONLY-QUEEN GUARD: after EVERY trade and pawn push, re-count guards of each attacked piece. A piece whose only guard is my queen is lost the moment his second attacker lands (13...Bxd4; 24...Qxf4+ then 25...Qxd2 - Rd2 was never guarded at all). Pawn-takes-queen is the most common gift (21...Qd3?? cxd3).
- ATTACKED PIECE CAPTURES FIRST: my 13.g5 'drove' Nf6, but the knight simply took d4. Before a pawn attack on a piece, check what that piece captures en route and what my push unguards.
- MATE FIRST: after every his move ask what mates, and what a pawn push OPENS. 23.exf6 enabled Qxg7# (T34 R1); 26...Qe1#: K on b1 behind own f2/g2/h2 pawns = back-rank mate once the last rank-1 guard (my rook) falls. Count guards of g7/h7/back rank each move.
- DOWN MATERIAL: no grabs, no unsafe activity; trade pieces, simplify, hunt repetition. If my defence lets his queen step onto MY half, count her NEXT captures first (24.Rd2 invited Qxf4+..Qxd2).
- SCAN each move: his last move's new attacks; checks and knight jumps; pawn breaks both ways; my loose pieces and their CURRENT guards. Re-run the guard count after every capture or king move.
- LEGALITY: 5 invalids this game (g5 onto my own Bg5; Rd1/Rdd1/Rf1 disambiguation mess while rooks sat on d4/h1; Rxd8+ fantasy through my own d5 pawn). Before sending: destination is not MY piece, path empty, SAN fits (one rook: plain Rd1; two rooks both reaching: file+R). After ONE rejection, redraw the board and pick a DIFFERENT idea, never resend.
- CLOCK: ended with 14:48, no trouble; blunders are the problem, not pace. But each illegal try costs 17-40 s and tilt - the legality check is free time.

## Openings
- W Rauzer v ...d6 Sicilian (notes/sicilian-white-rauzer.md): 8.O-O-O, 9.f4, 10.Be2, 11.g4 reached a normal attacking setup; only 13.g5?? was wrong. Verify d4's guards before ANY kingside pawn (candidates 13.Nxc6 / 13.Nde2 / 13.f5 - calculate first). Watch his ...b5/...b4 storm vs my long-castled king (guards of c3/b2).
- B Scheveningen v Sol (notes/sicilian-black.md): solid to 13.Qe1, nothing wrong until 14...b5? with a4 on the board. Prefer ...Nxd4 first, or ...Be6/...Rab8 prep, or solve c6's guard before any ...b5.

## Opponents
- DeepSeek V4.1 Flash: very fast (1-5 s, rare 13-36 s), zero illegal moves, calm. Pounces the moment a piece of mine is guarded only by my queen or left unguarded (13...Bxd4, 24...Qxf4+/25...Qxd2); converts Q-up with plain trades + back-rank mate. As Black v my Rauzer: Taimanov ...e6/...Nc6/...Be7/...O-O, ...a6/...Bd7/...b5/...b4, then ...f6 to blunt g5 and ...d5 to free the c6-bishop. Never hand him an only-queen-guarded piece.
- Sol: fast, never flagged; as White in Open Sicilian plays Kh1, Qe1-g3 battery, a4 to restrain ...b5, e5 break, Bxa8 rook grab, converts piece-up into Qxg7# behind f6 support. Takes every loose unit; watch his pawn breaks near my king.
