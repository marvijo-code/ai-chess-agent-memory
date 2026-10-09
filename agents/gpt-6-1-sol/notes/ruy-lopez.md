# Ruy Lopez: defenders, forks, and passers

## Shared Chigorin structure
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6.
Recount central defenders after reroutes and exchanges. Preserve Bc2 before a3 against ...Nb4 if ...Nxc2 forks rooks.

## T11 round 1: Black vs Sonnet, checkmate win
White chose 8.d3, then h3/Nbd2/Nf1/Ng3 without c3. Black developed ...Bb7/...Re8/...Bf8/...Na5.
- Bc2 was illegal while c2 remained occupied. White played c3 Nxb3 Qxb3: no doubled b-pawns. Name the actual recapture instead of assuming structural damage.
- ...d5 exd5 Bxd5 attacked Qb3. After Qd1 c5 Nxe5 Bd6 Nf3, White retained an extra pawn. No adverse early marks establish an optimal repertoire or adequate compensation.
- Rxe8+ Rxe8 Bg5 Bxg3 fxg3! Qxg3 Bh4 Qg6 Bxf6 Qxf6 exchanged both pairs of minor pieces except Black's bishop and White's knight, and recovered a pawn.
- Ne1?! c4?! dxc4 Bxc4 Qd7 Qe6 Qxe6 Bxe6 reached equal pawn counts, R+B against R+N. ...c4 was marked inaccurate; no best replacement was supplied.

### Missed king-rook fork
28.Nf3 Kf8 29.Kf2 Ke7 30.Nd4 Bc4 31.b3 Bd5 32.Rd1 Rd8? 33.h4? Kf6 34.g3 Ke5?? 35.Ke3?? h5?? 36.Rd2?? Rd6.
- With Ke5/Rd8/Bd5 against Nd4/Rd1, Nc6+ checks the king and attacks Rd8. ...Bxc6 removes the knight but vacates d5, allowing Rxd8: White wins the exchange. A nominal answer to a knight fork can uncover another capture.
- White missed Nc6+ on moves 35 and 36. ...Rd6 then removed the rook from d8 and protected it with Ke5. The escape does not validate ...Ke5 or ...h5.
- ...Rd8, ...Ke5 and ...h5 received adverse marks. No engine-best replacements were supplied.

### Two passers and promotion geometry
...f6/...g5/...gxh4 gxh4 left White's h4 pawn and Black's original h5 pawn. ...f5-f4+ drove Ke3 to f2; ...Ke4/...Rf6/...f3 brought the rook behind the passer.
- ...Kf4/...Kg4??/...Kxh4? collected White's h-pawn but contained marked errors. White's Rd2??/Ke3??/a3? failed to exploit them; do not infer that this king route was forced or sound.
- ...Kg3 Rf2 h4 a4 h3 a5 h2 Rf1 f2! opened Bd5-e4-f3-g2-h1. Rf1's rank coverage alone no longer stopped h-promotion because the bishop protected h1.
- Ne2+ Kg2 Nf4+ Kxf1 Nxd5 h1=Q Nxf6 Qh6+ Kf3 Qxf6+ converted both Black pieces into a queen while removing White's rook and knight. Calculate the full liquidation before preserving threatened pieces automatically.
- ...Ke1 cleared f1; ...f1=Q+ made a second queen. ...Kd2 blocked Qe2's second-rank control and allowed Kb2. Later ...Ke3+ vacated d2, uncovering Qe2's check; Qae1# finished with Qe2 protecting e1 and controlling the second rank.
- Finished with 4:23, no illegal attempts. Six moves after the second promotion reduced 6:24 to 4:23 despite increments. Routine mate choices took 26-45 seconds; simplify the search once a safe mating route is available.

## Earlier recurring failures
- T9 White: Bb1 saved the bishop before a3. Nxg5 hxg5 Bxg5 exchanged knight for bishop, not a piece gain. Bg5?? allowed fxg5: f6 was unpinned. Nf8 blockaded g6/h7 despite their proximity to promotion.
- Nc5 and Nd7 must be tracked separately. Bxd7 Nxd7 replaced one knight with the other on d7, preserving ...Nxf8. ...Rc8 added another f8 defender.
- Rc6 was protected by d5: ...Rxc6 dxc6 attacked Rb7/Nd7. This local tactic did not prove a win. ...b1=Q Rxb1 Rxb1 cost White a rook; Ra8 later allowed ...Rd8xa8.
- T8 Black: Rc1/Qc7 were screened by Bc2/Nc5. ...Na4 Bxa4 bxa4 Rxc7 removed both screens and lost queen for rook. ...Bf6 allowed gxf6; Bd4 prevented Kxf6 and supported the mating attack.
- Be3 Nxd4 Nxd4 exd4 Qxd4 Qxc2 opened the c-file while Qxd4 abandoned Bc2. ...Qc4 Rxc4 Rxc4 lost queen for rook.
- Qg3 threatened mate but abandoned Bd4 to Rxd4. ...Rg4 allowed Qh7#, protected by Rf7 through g7.
- Nxc5 dxc5 opened Bc8's diagonal; the OTHER bishop could capture Nf5. exf5 removed e4's support of d5.
- Bd3 cleared Rc1 against Qc7. Qa4 allowed bxa4; Nb3 allowed axb3. Nh4-f5/Bxf5/Ng3xf5, f3-f4 and Re3-g3 remove e4 defenders. Be7 can block Re8's defense of e5.
