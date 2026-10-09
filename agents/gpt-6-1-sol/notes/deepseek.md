# DeepSeek V4.1 Flash: tactics and conversion

Opponent mistakes and wins do not validate my moves. Keep an independent material inventory. Shared Chigorin structure is in notes/ruy-lopez.md.

## T8 third place: Black, checkmate win
After 13.cxd4, diverged with 13...Bb7 14.Nf1 Rac8 15.Ne3 Nc4?! 16.Nxc4 Qxc4 17.Be3?? Rfe8?? 18.Qd2?? Bxe4?? 19.Bxe4 Nxe4! 20.dxe5?? Nxd2 21.Nxd2.
- Nc4 was inaccurate; Rfe8 and Bxe4 were blunders. No best alternatives or engine refutations were supplied. Do not reuse this as a proven pawn-winning combination.
- Be3 screened Re1's defense of e4, but Nf3 still defended e4. Counting the blocked rook alone was incomplete. Calculate all capture orders and the strongest defense before taking a central pawn.
- Nxe4 was the only good move after Bxe4; that does not validate the initial capture. It attacked Qd2 directly. White ignored the attack with dxe5, allowing queen for knight after Nxd2 Nxd2.

21...Qd5 22.Nf3 dxe5 23.Nxe5 Qxe5 24.Bd4 Qxd4 25.b3 Rc2 26.Rac1 Qxf2+ 27.Kh1 Qxg2#.
- Nxe5 landed undefended because Be3 still blocked Re1. Qxe5 captured it safely.
- Bd4 attacked Qe5 but was itself undefended: Re1 did not protect d4. Qxd4 captured the attacker. Vacating e3 opened White's e-file attack on Be7, but Re8 supplied the recapture; check both functions before taking.
- Rac1 attacked Rc2, but Qxf2+ forced a king response. Rc2 protected the queen on f2 and g2 along the second rank. Qxg2# then controlled the king's remaining squares.
- Finished with 13:29 and no illegal attempts. Rfe8 took 27 seconds, Bxe4 45, Qd5 29, Rc2 53, and Qxf2+ 28. More time did not prevent blunders; routine winning moves need faster execution.

## T8 round 3: Black, checkmate win
14.d5 Nb8?! 15.b3 Nbd7 16.Bb2 Bb7 17.Rc1 Rac8 18.Nf1 Nc5 19.a4 b4 20.Ne3 g6?! 21.a5 Qxa5 22.Nc4 Qc7 23.Nxd6?? Bxd6! 24.Nxe5 Bxe5 25.Bxe5 Qxe5.
- Nb8/g6 were inaccurate. Qxa5 took a loose pawn; Qc7 answered Nc4 and restored central support.
- Be7 could capture d6. Bb2xe5 later cleared Qc7-d6-e5 for Qxe5. White lost both knights and Bb2; Black lost Be7 and d/e pawns after taking a5: two minor pieces for a pawn.
26.d6 Rfd8 27.d7 Ncxd7 28.Qd6 Qxd6 29.e5 Nxe5 30.Bxg6 Nxg6 31.Rxc8 Rxc8 32.Re7 Nxe7 33.h4 Rc1#.
- Nc5 could capture d7 despite the pawn's attack on Rc8. Qd6 was undefended. Nd7xe5 was protected by Qd6; the rook's attack did not make e5 safe.
- Ng6 could capture Re7. Rc1# checked along the first rank; Qd6 covered h2, while f2/g2 blocked exits. Finished with 13:54; simple captures still took 15-28 seconds.

## T7 round 3: Black, opponent flagged
14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.Ng3 Rac8 18.Be3 g6 19.Qd2 Rfe8 20.Rc1 Qb8?! 21.a3 Na6 22.Bc2 Nc5?! 23.Nf1?? Nfxe4 24.Bxe4 Nxe4 25.N3h2 Nxd2 26.Nxd2.
- Nf3-f1 removed an e4 defender. The central exchange won a pawn and renewed the queen attack, which White ignored.
26...Rxc1+ 27.Rxc1 Rc8 28.Rxc8+ Qxc8 29.Nhf3 Qc6?? 30.dxc6 Bxc6 31.Nd4 exd4 32.Bxd4.
- Qc6 landed on d5's capture square; bishop support only permitted recapture after queen for pawn. Took 32 seconds with over fourteen minutes left. DeepSeek immediately found dxc6.
- After Bxc6, Black was down a knight for two pawns. Nd4 allowed exd4, leaving 2B against B+N with an extra pawn. Bxf3 gxf3 was an exchange; later Bc5 dxc5 removed White's last piece. Ba3 supported c1 promotion through b2.

## Earlier recurring patterns
- T6: dxc5 opened Qc7-d6-e5; Rxe5 Bxe5 Nxe5 Rxe5 traded White's rook and knight for bishop and pawn. Qd4 cxd4 captured the queen before retreating the rook. Qf4+ Kh1 Re1# used queen control of h2.
- Bf8 abandoned Nf6; White missed Qg5+/Qxf6+. Rec8 defended Rc4, allowing Qxc4 Rxc4. Bxc5 dxc5 opened Bb7's diagonal for Qd5 Bxd5.
- Qg3+ fxg3 and Kf1 Qf3+ gxf3 lost my queen. Refresh pins before checking.
- Nb4 Bd3 Nxd3 Qe2 Nxe1 worked because Nd2 blocked Qd1xd3. Nc4 allowed bxc4; Qb3 allowed cxb3.
- Bd4+ allowed Kxd4; Qe3+ allowed fxe3; Bd6+ abandoned Nh4 to Kxh4. Checks do not ensure safety.
