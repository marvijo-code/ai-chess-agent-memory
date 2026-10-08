# Four Knights as Black - 4.Bb5 Bb4 (g3, g4, g11, g14 - all lost 0-1)
1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 Nd4 8.Nxd4 exd4 9.b3 Be7 10.Re1

## Move 10: RETREAT the b4 bishop (g11 killer)
- This line is fine: eval ~+0.1-0.5 through 10.c3.
- 10.c3 attacks Bb4 -> retreat Ba5 / Be7 / d6, then ...d6 hits the e5-knight.
- 10...Bxc3?? 11.dxc3 (or bxc3) = BISHOP FOR A PAWN, +0.1 -> +7.4, game lost. c3 is defended by b2+d2 pawns.
- Same family as 8...Bxd2?? (g4): never take a defended pawn with a bishop in the opening.

## Double-trade line (g14): 6.Nd5 Nxd5 7.exd5 Nd4 8.Nxd4 exd4 9.b3 Be7 10.Re1
- White keeps a pawn on d5 (from e4xd5), Black a pawn on d4 (from e5xd4); no knights remain. Eval equal through 10.Re1 (+0.1).
- 10...c6! is the standard challenge to d5, best before White plays Qf3; 10...d6 also fine. 10...Re8?! is a mistake: 11.Qf3! (queen covers d5 via f3-e4-d5) plus Bd3/Bb2 battery.
- After 11.Qf3 do NOT open with ...c6/...cxd5: 12.Bd3 cxd5? 13.Bb2! (bishop attacks d4 and g7; Bd3 blocks White's d-file recaptures) 13...Bc5 14.Rxe8+ Qxe8 15.Qxd5 wins the d5 pawn (my queen left d8, nothing defends d5), 15...Qe7 16.Bxd4! Bxd4 17.Qxd4 wins d4 too. Better: ...d6/...Bd6/...Bf6/...g6/...h6, keep d4 covered, keep the c-file closed.
- ...c6 boxes my c8-bishop: ...Bf5/...Bg4 are illegal while the d7-pawn sits there; free it with ...d6 first (g14 13...Bf5 illegal try, 1:33 spent).

## Legality (g11 9...Nf6: 3 tries, 2 illegal; g14: 2 illegal)
- Illegal Nxd2: a d5-knight reaches c7, e7, b6, f6, b4, f4, c3, e3 - not d2.
- Illegal Be6/Bf5/Bb7: own pawns on d7/b7 block the c8-bishop's paths.
- Invalid attempts waste clock and tries - check geometry and path before submitting.

## Working setup and plans
- 8...Nxd5 (main) or ...d6/...c6 hitting e5; g3: 10...Bc5 11.d4 Bb6 12.Bd3 d6 was solid.
- g11 continued reasonably: 11...d6 12.Nf3 Be6 13.Bb5 a6 14.Be2 Re8 15.Bg5 h6 16.Bh4 Qd7 17.Bxf6 gxf6 18.Ne1 Rad8 19.Nf3 d5 20.b4 c5.
- Keep f7 covered; never a piece on a square a White knight attacks; keep every piece defended when nothing forces.

## Late blunders (g11, g14 - repeat patterns)
- g11 25...Bf5?? Nd4xf5: Nd4 attacks b3 c2 e2 f3 f5 b5 c6 e6. After 24...Bd3 25.Bf1 declined the trade, play Bxf1 or retreat to a safe square - not f5.
- g11 26...Qxb4?? cxb4 = Q for P: b4 is defended by the c3-pawn. Never grab a pawn any pawn defends.
- g14 17...Qe1+?? Rxe1 = QUEEN FOR NOTHING: I offered a queen trade with check, but the a1-rook recaptures along the cleared b1/c1/d1; then 19.Re8# (my Ra8 blocked by my own Bc8, f8/h8 uncovered). Never move/check the queen onto a square a rook (or king) attacks - a check does not make it safe.

## b6-bishop trap (g3)
- 13.Nc4! hits Bb6 (no free square); answer 13...b5! attacking the c4-knight; 14.Nxb6 axb6 = B for N, equal.
- Do NOT play ...Bg4 then ...Bxd4?? cxd4.

## Other blunders (do not repeat)
- g4: 10...Nf4?? Qxf4; 12...Qxe5?? Qxe5; 13...Re8?? Qxe8#. g3: 15...Ne4?? Bxe4; 19...Qxe4?? Rxe4.
- Down material: play fast, defend loose pieces, no tilt captures.
