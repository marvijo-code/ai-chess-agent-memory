# DeepSeek V4.1 Flash: tactics and conversion

Shared Chigorin opening through 13...Nc6 is in notes/ruy-lopez.md. Opponent errors and wins do not validate my moves. Keep an independent material inventory.

## T8 round 3: Black, checkmate win
14.d5 Nb8?! 15.b3 Nbd7 16.Bb2 Bb7 17.Rc1 Rac8 18.Nf1 Nc5 19.a4?! b4 20.Ne3 g6?! 21.a5 Qxa5 22.Nc4 Qc7 23.Nxd6?? Bxd6! 24.Nxe5 Bxe5 25.Bxe5 Qxe5.
- Nb8 and g6 were inaccurate; no best replacements were supplied. The subsequent tactical win does not establish the opening plan's soundness.
- Qxa5 captured an undefended pawn; Nc4 attacked the queen, so Qc7 restored its central support.
- Be7 could capture d6 despite White's assumption otherwise. After Bxd6 Nxe5 Bxe5, Bb2xe5 removed that bishop and cleared Qc7-d6-e5 for Qxe5.
- White lost both knights and Bb2; Black lost Be7 and d/e pawns after previously taking a5. Final advantage: two minor pieces for a pawn, not merely a favorable bishop exchange.

26.d6 Rfd8 27.d7 Ncxd7 28.Qd6 Qxd6 29.e5 Nxe5 30.Bxg6 Nxg6 31.Rxc8 Rxc8 32.Re7 Nxe7 33.h4 Rc1#.
- Rfd8 blockaded the passer; Nc5 could capture it on d7 even though the pawn attacked Rc8. Check captures before retreating an attacked rook.
- Qd6 was an undefended queen, not a viable exchange offer. After Qxd6, Nd7xe5 was protected by Qd6; Re1's attack on e5 did not make that pawn safe.
- Ne5xg6 captured the bishop and then Ng6xe7 captured the invading rook. Enumerate knight destinations before treating seventh-rank activity as a threat.
- Rc1# checked along the first rank; Qd6 covered h2 via e5-f4-g3. White's f2/g2 pawns blocked exits. Finished with 13:54 and no illegal attempts. Several straightforward captures took 15-28 seconds; preserve verification but convert more promptly.

## T7 round 3: Black, opponent flagged
14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.Ng3 Rac8 18.Be3 g6 19.Qd2 Rfe8 20.Rc1 Qb8?! 21.a3 Na6 22.Bc2?! Nc5?! 23.Nf1?? Nfxe4 24.Bxe4 Nxe4 25.N3h2? Nxd2 26.Nxd2.
- a5 supported Nb4. Qb8/Nc5 were inaccurate; later success does not validate them.
- Nf3-f1 removed an e4 defender. Both black knights attacked e4; Nfxe4 Bxe4 Nxe4 won a pawn and renewed the attack on Qd2. N3h2 ignored that attack, allowing queen for knight.

26...Rxc1+ 27.Rxc1 Rc8 28.Rxc8+ Qxc8 29.Nhf3 Qc6?? 30.dxc6 Bxc6 31.Nd4? exd4 32.Bxd4.
- Rook exchanges left Q+2B against B+2N with an extra pawn. Qc6 then landed on d5's capture square; bishop support only enabled recapture after losing queen for pawn.
- Qc6 took 32 seconds with over fourteen minutes remaining. DeepSeek immediately found dxc6: do not rely on habitual misses.
- After Bxc6, Black was down a knight for two pawns. Nd4 allowed exd4; Bxd4 left 2B against B+N with one extra pawn. Calculate captures before retreating an attacked bishop.
- Bxf3 gxf3 exchanged bishop for knight, not a piece win. Bc5 later allowed dxc5, removing White's last piece. Bf6-b2-a3 collected pawns; Ba3 supported c1 promotion through b2. Advance verified unstoppable passers promptly. Finished with 14:22.

## T6 third place: central liquidation
Nd8 was inaccurate. After ...Bd7, ...dxc5 opened Qc7-d6-e5. Bxf5 and Nxe4 were exchanges; Rxe5?? Bxe5 Nxe5 Rxe5 traded White's rook and knight for bishop and pawn. Re8's defense became usable after e5 cleared.
- Qd4 cxd4 captured the queen before retreating Re5. Finish Qf4+ Kh1 Re1#: Qf4 covered h2; g2/h3 blocked exits. Qf4+ took 43 seconds despite overwhelming material.

## Earlier recurring patterns
- Bf8 abandoned Nf6 and allowed Qg5+/Qxf6+; White instead missed this. An opponent oversight does not repair my retreat.
- Rec8 defended Rc4; Qxc4 Rxc4 lost White's queen for rook. Bxc5 dxc5 opened Bb7's diagonal; Qd5 Bxd5 lost another queen.
- Qg3+? fxg3 and, after Kf1 released g2's pin, Qf3+? gxf3 lost my queen. Refresh pins and test pawn captures before queen checks.
- Nb4 Bd3?? Nxd3 Qe2 Nxe1: Nd2 blocked Qd1xd3. Nc4 allowed bxc4; Qb3 allowed cxb3.
- Bd4+ allowed Kxd4; Qe3+ allowed fxe3; Bd6+ abandoned Nh4 and allowed Kxh4. Checks do not ensure safety.
