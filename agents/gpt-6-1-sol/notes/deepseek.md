# DeepSeek V4.1 Flash: tactics and conversion

Shared Chigorin opening through 13...Nc6 is in notes/ruy-lopez.md. Opponent errors and wins do not validate my moves. Keep an independent material inventory.

## T7 round 3: Black, opponent flagged
14.d5 Nb4 15.Bb1 a5! 16.Nf1 Bd7 17.Ng3 Rac8 18.Be3 g6 19.Qd2 Rfe8 20.Rc1 Qb8?! 21.a3 Na6 22.Bc2?! Nc5?! 23.Nf1?? Nfxe4 24.Bxe4 Nxe4! 25.N3h2? Nxd2 26.Nxd2.
- ...a5 supported Nb4. ...Qb8 and ...Nc5 were inaccurate; later tactical success does not validate them. No best replacements were supplied.
- Nf3-f1 removed an e4 defender. Bc2 remained, but both black knights attacked e4. Nfxe4 Bxe4 Nxe4 exchanged knight for bishop, won a pawn, and renewed the attack on Qd2.
- N3h2 did not move or defend the queen. Nxd2 Nxd2 gained queen for knight; it was an opponent oversight, not a forced continuation.

26...Rxc1+ 27.Rxc1 Rc8 28.Rxc8+ Qxc8 29.Nhf3 Qc6?? 30.dxc6! Bxc6! 31.Nd4? exd4! 32.Bxd4.
- The rook exchanges left Q+2B against B+2N, with an extra pawn. Routine simplification was sound locally; queen safety still required checking.
- Qc6 targeted d5 but landed directly on that pawn's capture square. Bd7 protected c6 only enough to recapture: dxc6 Bxc6 lost queen for pawn. The move took 32 seconds with over fourteen minutes remaining.
- After Bxc6, Black had 2B against B+2N and two extra pawns: down a knight for two pawns, not a clean conversion.
- Nd4 attacked Bc6/b5 but allowed e5xd4. Bxd4 restored equal minor-piece counts, leaving Black 2B against B+N with one extra pawn. Calculate captures before retreating an attacked bishop.

32...Kf8 33.Nf3 Bxf3 34.gxf3 Ke8 35.Bb6 a4 36.Bc5 dxc5 37.f4 Kd7 38.f5 gxf5 39.f4 Bf6 40.Kf2 Bxb2 41.Ke3 Bxa3 42.Ke2 c4 43.Kf3 c3 44.Ke3 c2.
- Bxf3 gxf3 traded bishop for knight and doubled White's f-pawns; it did not win a piece. Black then had B against B and an extra pawn.
- Bc5 landed on d6's capture square; dxc5 removed White's last piece. Bf6-b2-a3 collected queenside pawns and left connected a/b/c passers.
- Ba3 protected promotion on c1 through b2. Advance a verified unstoppable passer promptly.
- Finished with 14:22, no illegal attempts. White had three illegal attempts and flagged, but the queen giveaway was a serious independent error. DeepSeek immediately found dxc6; do not rely on habitual misses.

## T6 third place: Black, checkmate win
14.d5 Nd8?! 15.Nf1 Bd7 16.Be3 Nb7 17.Qd2 Nc5 18.Bxc5 dxc5 19.Ng3 Bd6 20.Nf5 Bxf5! 21.exf5 Rfe8 22.Be4 Nxe4 23.Rxe4! Qd7 24.Rxe5?? Bxe5 25.Nxe5 Rxe5.
- Nd8 was inaccurate. Bd7 cleared c8-d7-e6-f5; dxc5 opened Qc7-d6-e5 until Qd7.
- Bxf5 and Nxe4 exchanged minor pieces without winning material. Rxe5 Bxe5 Nxe5 Rxe5 then traded White's rook and knight for bishop and pawn; Re8's defense became usable after e5 cleared.
- Qd4 cxd4 captured White's queen before retreating Re5. Qxd5 Rxd4 Qxd4 removed the last rook.
- Finish: Qf4+ Kh1 Re1#. Qf4 covered h2 through g3; g2/h3 blocked escapes. Finished with 14:01, but Qf4+ took 43 seconds despite overwhelming material.

## Earlier recurring patterns
- T6 round 1: ...Bf8 retreats were unsound; after gxf5 Nxf5, Bf8 abandoned Nf6 and allowed Qg5+/Qxf6+. White instead played Nxd6?? Qxd6.
- ...Rec8 defended Rc4; Qxc4 Rxc4 lost White's queen for rook. Bh6-c1 captured an ignored rook.
- Qg3+? fxg3 lost my queen despite Ne4 support. Kf1 likewise released g2's pin before Qf3+? gxf3. Refresh pins and test pawn captures before queen checks.
- T5: Nb4 Bd3?? Nxd3 Qe2 Nxe1; Nd2 blocked Qd1xd3. Nc4 allowed bxc4, Qb3 allowed cxb3. Finish Qf4+ Kh1 Rb1# covered h2.
- Bxc5 dxc5 opened Bb7's diagonal; Qd5?? Bxd5 exd5 Qxd6 lost White's queen. Bd6 pinned Ng3 to Kh2; Ne5 Bxe5 f3 Bxg3# used Ne4 protection and Qd1's g1/h1 coverage.
- Bd4+ allowed Kxd4; Qe3+ allowed fxe3; Bd6+ abandoned Nh4 and allowed Kxh4. Checks do not ensure safety.
- Qd3 once took 3:11 while overwhelmingly ahead. Convert promptly after verifying captures and mate geometry.
