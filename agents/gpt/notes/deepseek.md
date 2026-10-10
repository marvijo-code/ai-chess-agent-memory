# DeepSeek V4.1 Flash: tactics and conversion

Wins, sparse marks and opponent explanations do not validate moves. Track material, defenders, pawn squares and blockers independently. Chigorin details: notes/ruy-lopez.md.

## Shared Dragon opening
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3 O-O 8.Qd2 Nc6 9.Bc4 Bd7 10.O-O-O Rc8 11.Bb3 Ne5 12.h4 Nc4 13.Bxc4! Rxc4! 14.h5 Nxh5 15.g4! Nf6.
- Nc4 attacks Qd2/Bb3; remove it before continuing the attack. Rxc4 was Black's only good reply.

## T16 semifinal 1 game 1: h-file mate after protected block
16.Bh6 Bxh6? 17.Qxh6! Qe8 18.g5? Nh5! 19.Rxh5 gxh5 20.Nd5?! Qd8? 21.Rh1 h4 22.Rxh4 Rxd4 23.Qxh7#.
- Bh6 avoided the previously marked Qh2 line, but this game establishes no best continuation against stronger defense. Bxh6 was marked a mistake; Qxh6 was the only good recapture.
- g5 repeated the blocking-retreat error: g6 protects h5 and g5 cannot capture Nh5. Nh5 was Black's only good reply. Rxh5 gxh5 traded rook for knight; the win does not establish compensation. Nd5 was also inaccurate. No verified replacements or forced win before ...Qd8 supplied.
- After Rxh5, Qh6 alone did not protect Qxh7 against Kxh7. Rd1-h1 supplied the missing rook support. ...h4 moved the blocker down the same file; Rxh4 removed it. A black pawn on h4 attacks g3, NOT g5, despite Black's explanation.
- Rh1 removed Nd4's remaining defender: Rd1 had guarded it through empty d2/d3 after Qxh6. ...Rxd4 took that knight but ignored Qxh7#. Rh4 then protected h7 through empty h5/h6; Qh7 covered h8, while Rf8 and f7/g7 enclosed Kg8.
- No invalid attempts; finished with 13:39. Rh1 took 64 seconds, Rxh4 39, mate 3. Calculate the rook transfer and defense to mate promptly; ample clock did not prevent g5's error.

## Qh2 branches: pawn location changes the defense
T16 round 1: 16.Qh2?! Rc8?? 17.g5?? Nxe4?? 18.Qxh7#.
- Qh2 was inaccurate; no verified replacement supplied. g5 restored protected ...Nh5 and missed the opportunity after ...Rc8. ...Nxe4 abandoned h7; mate before responding to the knight's attack.

T13 semifinal: 16.Qh2 Nh5?? 17.gxh5 gxh5 18.Qxh5 Bxd4 19.Qxh7#.
- With g4 still present, gxh5 removes the knight. Nf6 guards h7; Nh5 only blocks the file. The captures clear that blocker and Rh1 supports mate.
- Trace Qd2-h2 through e2/f2/g2 and Rh1-h7 through h2-h6. This successful branch does not certify Qh2 against better defenses.

T13 round 3: 16.g5?! Ne8?! 17.Qh2 Rxd4?? 18.Qxh7#.
- ...Ne8 abandoned h7 and opened Bg7 toward Nd4; taking the knight did not meet mate. Always test ...Nh5 before claiming g5 forces the defender away.

## T12 round 3: ...gxh5 branch
14...gxh5?! 15.Bh6?? Bxh6?? 16.Qxh6! Nxe4?? 17.Rxh5 Rxd4 18.Qxh7#.
- Bh6 removed Be3's guard of Nd4: ...Rxd4 Qxd4 Bxh6+ gives Black both minors for rook. After Qd2 leaves, Bh6-e3-c1 runs through g5/f4/e3/d2.
- Black chose the bishop exchange; Qxh6 was the only good recapture. ...Nxe4 abandoned h5/h7. Rxh5 cleared the file and supplied mate support.
- Black's claimed Nc3xd4 Rxd1+ was false: the recapture removes its attacking rook. Rxh5 took 53 seconds despite a concrete forcing win.

## Other recurring errors
- Ng3 ignored ...Qxc2 Qxc2 Rxc2 with c3-c6 empty, losing Bc2. Later ...Nc6 screened the file; d5 drove it away and Bd3 saved the bishop.
- Rc1/Qc7 may have Bc2 and Nc5/Nc4 as screens; removing both permits Rxc7. ...Rac8 Rxc8 Rxc8 Rxc8 traded one White rook for both Black rooks.
- ...e4 forked Qd3/Nf3, but Qxe4 removed it safely. Rc8 protected Qh8#; Qc3 protected Rh8#.
- Qg3+ fxg3 and Kf1 Qf3+ gxf3 lost queens: refresh pins after king moves.
- Nb4 Bd3 Nxd3 worked only with Nd2 blocking Qd1xd3. Nc4 allowed bxc4; Qb3 allowed cxb3.
