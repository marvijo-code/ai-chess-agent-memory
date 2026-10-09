# DeepSeek V4.1 Flash: tactics and conversion

Opponent mistakes and wins do not validate my moves. Keep an independent material inventory. Shared Chigorin structure is in notes/ruy-lopez.md.

## T9 round 3: White, checkmate win
Shared Chigorin through 13.cxd4, then 13...Bd7 14.Nf1 Rac8 15.Ng3?? Rfe8?? 16.Bd3 h6 17.Be3 Nb7 18.Rc1 Qxc1?? 19.Bxc1 Rxc1 20.Qxc1.
- Unlike the usual ...Nc6 continuation, Black's knight remained on a5, leaving the c-file clear above Bc2. After ...Rac8, ...Qxc2 could win the bishop: Qxc2 Rxc2 exchanges queens but leaves White a bishop down. Qd1's nominal protection was insufficient against queen and rook together.
- Ng3 reinforced e4 but ignored this capture. Black missed it with ...Rfe8; Bd3 then moved the bishop to safety. Address the c-file threat before completing the knight reroute.
- After Bd3 and ...Nb7, Rc1 attacked Qc7 along a clear file. ...Qxc1 miscounted the liquidation. Bxc1 let the bishop absorb ...Rxc1, preserving Qd1 for Qxc1. Black gave Q+R for R+B; White retained Q+R+B+2N against R+2B+2N.
- 20...Nc5 21.dxc5 dxc5 22.Nxe5 Nxe4 23.Nxe4 Bg5 24.Nxg5 hxg5 25.Nxd7 Re7 26.Rxe7 removed Black's remaining pieces. Nxe4 used Ng3; Nxg5 used that same knight, while Nxd7 used Ne5. Track individual pieces through consecutive captures.
- 26...g6 27.Re8+ Kg7 28.Qc3+ Kh7 29.Rh8#: Qc3 protected h8 along c3-d4-e5-f6-g7-h8 and covered g7. Bd3 covered h7. The diagonal remained clear after the central exchanges.
- Finished with 13:37 and no illegal attempts. Familiar opening moves took 4-7 seconds; Nxg5 took 41 and Re8+ 44. The missed threat, not time shortage, was the main lesson.

## T8 third place: Black, checkmate win
13...Bb7 14.Nf1 Rac8 15.Ne3 Nc4?! 16.Nxc4 Qxc4 17.Be3?? Rfe8?? 18.Qd2?? Bxe4?? 19.Bxe4 Nxe4! 20.dxe5?? Nxd2 21.Nxd2.
- Nc4 was inaccurate; Rfe8/Bxe4 were blunders. No best replacements or engine refutations were supplied. This is not a proven pawn-winning combination.
- Be3 screened Re1 from e4, but Nf3 still defended e4. Calculate all capture orders and the strongest defense.
- Nxe4 attacked Qd2; White ignored it and lost queen for knight. That later success did not validate Bxe4.
21...Qd5 22.Nf3 dxe5 23.Nxe5 Qxe5 24.Bd4 Qxd4 25.b3 Rc2 26.Rac1 Qxf2+ 27.Kh1 Qxg2#.
- Be3 still blocked Re1, leaving Nxe5 undefended. Bd4 attacked the queen but was itself loose. Vacating e3 opened the e-file against Be7; Re8 supplied its recapture.
- Rac1 attacked Rc2, but Qxf2+ forced a king response. Rc2 protected the queen on f2/g2 along the second rank. Finished with 13:29 despite several routine moves taking 27-53 seconds.

## T8 round 3: Black, checkmate win
14.d5 Nb8?! 15.b3 Nbd7 16.Bb2 Bb7 17.Rc1 Rac8 18.Nf1 Nc5 19.a4 b4 20.Ne3 g6?! 21.a5 Qxa5 22.Nc4 Qc7 23.Nxd6?? Bxd6! 24.Nxe5 Bxe5 25.Bxe5 Qxe5.
- Nb8/g6 were inaccurate. Qc7 restored central support. Bb2xe5 cleared Qc7-d6-e5; Black gained two minor pieces for a pawn overall.
26.d6 Rfd8 27.d7 Ncxd7 28.Qd6 Qxd6 29.e5 Nxe5 30.Bxg6 Nxg6 31.Rxc8 Rxc8 32.Re7 Nxe7 33.h4 Rc1#.
- The pawn's attack on Rc8 did not prevent Nc5xd7. Qd6 was undefended; Ng6 could capture Re7. Qd6 covered h2 for the final mate. Finished with 13:54.

## Earlier recurring failures
- T7: Nf3-f1 abandoned e4, allowing ...Nfxe4 Bxe4 Nxe4 and a queen attack. Later ...Qc6?? dxc6 Bxc6 lost my queen for a pawn despite bishop support; opponent flagging did not validate it.
- T6: dxc5 opened Qc7-d6-e5; Rxe5 Bxe5 Nxe5 Rxe5 traded rook and knight for bishop and pawn. Qd4 cxd4 captured the queen before retreating the rook.
- Bf8 abandoned Nf6. Rec8 defended Rc4, allowing Qxc4 Rxc4. Bxc5 dxc5 opened Bb7's diagonal for Qd5 Bxd5.
- Qg3+ fxg3 and Kf1 Qf3+ gxf3 lost my queen. Refresh pins before checking.
- Nb4 Bd3 Nxd3 Qe2 Nxe1 worked because Nd2 blocked Qd1xd3. Nc4 allowed bxc4; Qb3 allowed cxb3.
- Bd4+ allowed Kxd4; Qe3+ allowed fxe3; Bd6+ abandoned Nh4 to Kxh4. Checks do not ensure safety.
