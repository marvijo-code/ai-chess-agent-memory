# DeepSeek V4.1 Flash: tactics and conversion

Wins and opponent explanations do not validate moves. Track material, defenders, pawn locations and blockers independently. Chigorin structure: notes/ruy-lopez.md.

## Shared Dragon opening, T12/T13 White mate wins
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3 O-O 8.Qd2 Nc6 9.Bc4 Bd7 10.O-O-O Rc8 11.Bb3 Ne5 12.h4 Nc4 13.Bxc4! Rxc4! 14.h5.
- Nc4 attacked Qd2/Bb3. Bxc4 removed it; Rxc4 was Black's only good reply.

## T13 semifinal 2 game 1: Qh2 before g5
14...Nxh5 15.g4 Nf6 16.Qh2 Nh5?? 17.gxh5 gxh5 18.Qxh5 Bxd4 19.Qxh7#.
- My h-pawn had disappeared, but g4 remained. Qh2 aligned queen and Rh1 against h7 while Nf6 still defended h7.
- DeepSeek reused its planned ...Nh5 response to g5. Here g4 could capture h5 immediately. After g5, that capture would be unavailable. Recheck the actual pawn square before importing an earlier defensive resource.
- Nh5 blocked the h-file but did not defend h7. gxh5 removed the knight; ...gxh5 replaced it with a pawn; Qxh5 removed that pawn, threatening Qxh7# with Rh1 support.
- ...Bxd4 took Nd4 through g7-f6-e5-d4 but ignored mate. Choose mate before recapturing material. Do not infer that Qxh5 forces mate against every defense: Black still needed a concrete defensive reply.
- Qd2-h2 passed through empty e2/f2/g2. At Qxh7#, Rh1 protected the queen through empty h2-h6; Qh7 covered h8, while Rf8/Bg7 and Black's pawns enclosed Kg8.
- Qh2 was not marked inaccurate, but no engine-best replacement for the earlier g5 line was supplied. Record this as a successful move order, not certified optimal preparation.
- No invalid attempts; finished with 16:03 before the final increment. Qh2 took 30 seconds, gxh5 17, Qxh5 11, mate 3. Familiar development gained clock.

## T13 round 3: g5 before Qh2
14...Nxh5 15.g4 Nf6 16.g5?! Ne8?! 17.Qh2 Rxd4?? 18.Qxh7#.
- g6 defended Nh5 after the first capture; immediate Rxh5 would allow ...gxh5.
- g5 was marked inaccurate; no best replacement supplied. Nf6 guarded h7; ...Ne8 removed that defense and opened Bg7's diagonal toward Nd4.
- ...Rxd4 ignored Qxh7#. Finished with 15:28; g5 took 34 seconds, Qh2 25. Calculation time did not establish soundness.

## T12 round 3: ...gxh5 branch
14...gxh5?! 15.Bh6?? Bxh6?? 16.Qxh6! Nxe4?? 17.Rxh5 Rxd4 18.Qxh7#.
- Bh6 abandoned Be3's defense of Nd4. ...Rxd4 Qxd4 Bxh6+ gives Black both minors for a rook; the bishop reaches Kc1 through g5/f4/e3/d2 after Qd2 leaves.
- Black chose the bishop exchange. Qxh6 was the only good recapture; ...Nxe4 abandoned h5/h7 and did not attack Qh6. Rxh5 cleared the file and supported mate.
- Black's claimed Nc3xd4 Rxd1+ was false: the recapture removes its attacking rook. No invalid attempts; Rxh5 took 53 seconds despite a verified forcing win.

## Chigorin: recurring c-file errors
- T11/T9: Ng3 ignored ...Qxc2 Qxc2 Rxc2 with c3-c6 empty, losing Bc2. ...Nc6 later screened the file; d5 drove it away and Bd3 saved the bishop.
- Rc1/Qc7 may have Bc2 and Nc5/Nc4 as screens. Removing both permits Rxc7. Attacking a knight need not force its retreat.
- T11: b4 Nb3 Bxb3 and ...Nc5 bxc5 dxc5 lost both Black knights. Qd1 defended d6 through d2-d5; ...Qxd6 Qxd6 lost the queen. Forfeit tested no conversion.
- T10 Black: Nf3 Qxc2 Qxc2 Rxc2 won Bc2; Nd2 never screened the file. ...Nc4 Bc3 f6 Nd2 Nxd2 Bxd2 Rxd2 won another bishop with Rc2 support.

## Other patterns
- ...Rac8 Rxc8 Rxc8 Rxc8 traded one White rook for both Black rooks. ...e4 forked Qd3/Nf3, but Qxe4 removed it safely.
- Rc8 protected Qh8#; Qc3 protected Rh8#. ...g6 can occupy a king escape.
- Bxc5 dxc5 opened Bb7 for Qd5 Bxd5. Bf8 abandoned Nf6; Rec8 defended Rc4.
- Qg3+ fxg3 and Kf1 Qf3+ gxf3 lost queens: refresh pins after king moves.
- Nb4 Bd3 Nxd3 worked only with Nd2 blocking Qd1xd3. Nc4 allowed bxc4; Qb3 allowed cxb3.
- Bd4+ Kxd4, Qe3+ fxe3 and Bd6+ Kxh4 illustrate captures of checking pieces or abandoned guards.
