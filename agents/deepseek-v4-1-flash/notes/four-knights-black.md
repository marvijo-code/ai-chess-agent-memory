# Four Knights as Black - 4.Bb5 Bb4 (g3, g4, g11, g14, g17 - all lost)
1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 Nd4 8.Nxd4 exd4 9.b3 (9.?) Be7 10.Re1.

## Move 10: RETREAT the b4 bishop (g11)
- 10.c3 attacks Bb4 -> Ba5/Be7/d6, then ...d6 hits the e5-knight.
- 10...Bxc3?? dxc3 = B for P (g11 +7.4). Same family as 8...Bxd2?? (g4): never take a defended pawn with a bishop in the opening.

## Double-trade line (g14, g17)
- 6.Nd5 Nxd5 7.exd5 Nd4 8.Nxd4 exd4: no knights; White pawn d5 vs my d4 pawn.
- 10...c6! (challenge d5) or ...d6; 10...Re8?! weak (g14 11.Qf3!/Bd3 plans; g17 11.Qg4!).
- g14: after 11.Qf3, do NOT open with ...c6/...cxd5: 12.Bd3 cxd5? 13.Bb2! ... 15.Qxd5 wins d5 then d4. Better ...d6/...Bd6/...Bf6/...g6, keep d4 covered, keep the c-file closed.
- ...c6 boxes the c8 bishop: ...Bf5/...Bg4 illegal while d7-pawn sits; free with ...d6 first (g14).

## g17 vs Stockfish 19 (0-1, mated m14)
9.b3 a6 10.Bd3 Re8 11.Qg4 Qf6 12.Bb2 Qd6?? 13.Qxd4! Qxd5?? 14.Qxg7#.
- 11...Qf6! was fine (engine -0.10 for White): the queen defends d4 via f6-e5-d4 and guards g7. Keep it there.
- 12...Qd6?? abandons d4 (d7-pawn blocks d6-d4) and lets White build Bb2+Qd4 on the b2-g7 diagonal. 13.Qxd4! wins the pawn and threatens Qxg7# (Bb2 defends g7; king g8 boxed by f7/h7; f8 empty after ...Re8).
- 13...Qxd5?? grabbed a pawn with mate on the board; defend the mate first (queen back to f6, or guard g7 with a piece). Never grab material while my king sits in a battery.
- 10...Re8 again inferior: 10...c6! challenges d5 and keeps the rook on f8 for the dark squares.
- Clock: 45/43/32/56/42/51/51/35s on moves 6-13 then blundered; 9:52 vs 17:09. Play the book fast; the 5s scan finds these.

## Legality (g11, g14, g16)
- d5-knight reaches c7 e7 b6 f6 b4 f4 c3 e3 - not d2.
- c8-bishop blocked by d7/b7 pawns (Be6/Bf5/Bb7 illegal before ...d6). Own pawn blocks f5 (g16 20...f5 with Nf6).
- Illegal tries waste clock. Check geometry/path before submitting.

## Working setup and plans
- 8...Nxd5 main; ...d6/...c6 hit e5; g3: 10...Bc5 11.d4 Bb6 12.Bd3 d6 solid.
- g11 went 11...d6 12.Nf3 Be6 ... 20.b4 c5 - reasonable.
- Keep f7 covered; never a piece on a square a White knight attacks; keep everything defended. With b3/Bb2 White aims at d4 and g7: keep d4 defended and e5/f6 occupied or g7 guarded.

## Late blunders (g11, g14, g17)
- g11 25...Bf5?? Nd4xf5 (Nd4 attacks b3 c2 e2 f3 f5 b5 c6 e6); after a declined trade, take it or retreat safely.
- g11 26...Qxb4?? cxb4 = Q for P (c3-pawn).
- g14 17...Qe1+?? Rxe1 = Q for nothing (a1-rook, cleared b1/c1/d1); then 19.Re8#.
- g17 12...Qd6?? / 13...Qxd5??: queen moves that abandon a defensive duty or ignore a mate.

## b6-bishop trap (g3)
- 13.Nc4! hits Bb6; answer 13...b5! 14.Nxb6 axb6 = B for N.

## Other blunders
- g4: 10...Nf4?? Qxf4; 12...Qxe5?? Qxe5; 13...Re8?? Qxe8#. g3: 15...Ne4?? Bxe4; 19...Qxe4?? Rxe4.
- Down material: fast, defend loose pieces, no tilt captures.
