# DeepSeek V4.1 Flash: concrete tactics

Wins, sparse marks and opponent explanations do not validate moves. Track material, defenders, pawn squares and blockers independently. More Chigorin history: notes/ruy-lopez.md.

## T21 round 3: White Dragon, mate win
Opening: e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 g6 Be3 Bg7 f3 O-O Qd2 Nc6 Bc4 Bd7 O-O-O Rc8 Bb3 Ne5 h4 h5 Bg5 Nc4 Bxc4 Rxc4! Kb1? Qa5?? Nb3! Rfc8?? Nxa5.
- Kb1 was marked a mistake; no verified replacement supplied. Do not make it automatic after ...Rxc4. Nb3 moved Nd4 away from the rook's attack and attacked Qa5. Black ignored the queen attack to double rooks; Nxa5 collected it. No forced queen win before ...Rfc8 established.
- ...Rxc3 Qxc3 Rxc3 bxc3 removed both rooks. Across moves 17-19, White lost Q+Nc3 and Black lost Q+2R, leaving White 2R+N+B against 2B+N. This was a queen-for-rooks liquidation, not an ordinary queen trade.
- Rxd6 Kf8 Bxf6 Bxf6 Rxd7 removed Nf6, the defender of Bd7, before taking that bishop. Rxb7 Bxc3 Nc6 saved Na5 from the bishop's new c3-b4-a5 attack. Opponent commentary incorrectly called it an attack on an a1 rook.
- Rd1/Rdd7/Rxf7+ coordinated rooks, but Rh7 and Rbg7+ consumed 53/52 seconds. Rbg7+ Bxg7 Rxg7+ Kxg7 traded BOTH rooks for B, leaving N+5P vs 4P. The win does not validate reducing such a large advantage. Explicitly include the king's final recapture; preserve a rook unless a concrete finish justifies liquidation.
- Nxa7/Nb5 and a4-a5-a6-a7-a8=Q+ won the race while Black's king captured f3/e4. The outside passer mattered more than defending remote pawns. gxh3 removed Black's advanced h-pawn.
- Against the e-passer: Nd6, Qg4+ protected by h3, Qd4+ protected by Kc3, Nc4, Qe3+ protected by Nc4, then Qxe2. Use protected checks to separate king and passer; remove promotion threats before the mating approach.
- Final: Qa7 Kd8 Kd4 g4 Nd6. Qa7 bars the seventh rank; Nd6 controls c8/e8, so Kd8 has no legal move. Capturing the last pawn would stalemate. Preserve pawn tempi: ...gxh3 Ke5 h2 Ke6 h1=Q Qd7#. Ke6 protects d7; the promoted queen cannot answer mate.
- No invalid White attempts; Black made two. Finished 12:00. Use shorter routine conversion moves; ample time did not prevent the excessive rook liquidation.

## Earlier Chigorin games as Black
- T19: Qb6 behind Be3/d4 allowed dxe5 to uncover an attack on Q AND hit Nf6. Qxc8 Rxc8 Rxc8+ Bxc8 left Black Q against R; White miscounted the exchange. Refresh attacks after bxc4/Nxc4 and other captures.
- ...Nf4 attacked Re2 AND cleared Qc4-d3-e2. Bxf4 Qxe2 took R before recovering B; Ng3 Qe1+ Nf1 exf4 used check before recapture. A queen attack does not force passive retreat.
- ...e2 bxa4 e1=Q# used Qe5's guard of e1/h2. Check promotions before remote pawn grabs.
- T18: ...Nxe3 forked Qd1/Bc2 and cleared Qc7/Rc8. Queen exchanges left an extra bishop. Undefended Re2/Re1 fell to successive rook captures. Re1+ Kh2 Be5# exploited Rc2's absolute pin of g2; g3 was illegal.

## Dragon pawn order and h-file
- Shared branch: ...Ne5 h4 Nc4 Bxc4 Rxc4. Remove the fork on Qd2/Bb3 before continuing the attack.
- g4 BEFORE h5 permits gxh5 after ...Nxh5. h5 FIRST Nxh5 g4 Nf6 Bh6 Bxh6 Qxh6 Qe8 g5 Nh5 leaves g6 guarding Nh5; Rxh5 gxh5 trades R for N without proven compensation.
- hxg6 hxg6 clears Rh1's file. Bxg7 Kxg7 Qh6+ Kg8 Qh7# worked after errors; Kg8 was not forced. Qh6 alone does not protect Qxh7: Rh1 supplies support and Rxh4 clears the blocker.
- Rh1 abandons Rd1's guard of Nd4. Bh6 can also abandon Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for R. DeepSeek missed this; do not reuse the tactic as sound.
- Nf6 guards h7. ...Nxe4 can abandon the mating square; test mate immediately, but do not assume DeepSeek will repeat earlier defensive errors.
