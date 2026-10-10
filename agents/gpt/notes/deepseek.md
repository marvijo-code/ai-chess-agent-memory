# DeepSeek V4.1 Flash: tactics and conversion

Wins and opponent explanations do not validate moves. Track material, defenders, pawn locations and blockers independently. Chigorin details: notes/ruy-lopez.md.

## Shared Dragon opening, T12/T13/T16 White mate wins
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3 O-O 8.Qd2 Nc6 9.Bc4 Bd7 10.O-O-O Rc8 11.Bb3 Ne5 12.h4 Nc4 13.Bxc4! Rxc4! 14.h5.
- Nc4 attacked Qd2/Bb3. Bxc4 removed it; Rxc4 was Black's only good reply.

## T16 round 1: win after an unsound pawn advance
14...Nxh5 15.g4! Nf6 16.Qh2?! Rc8?? 17.g5?? Nxe4?? 18.Qxh7#.
- Qh2 formed the battery but was marked inaccurate. Earlier successes with it do not establish sound preparation. No engine-best replacement supplied.
- g5 attacked h7's defender but restored ...Nh5 as a protected h-file blocker: g6 guards h5, and a pawn on g5 cannot capture h5. Qxh5 would allow ...gxh5. Calculate blocking retreats before claiming the knight must abandon h7.
- ...Rc8 was marked a blunder, but g5 threw away the opportunity. No verified best exploitation of ...Rc8 was supplied.
- ...Nxe4 removed h7's knight guard and allowed immediate mate. Choose Qxh7# before recapturing the knight or reacting to its attack on Nc3.
- At mate Rh1 protected Qh7 through empty h2-h6; Qh7 covered h8. Black's Rf8/Bg7 and pawns enclosed Kg8.
- No invalid attempts. Book moves took 3-7 seconds; g5 took 24 seconds; finished with 16:16. Clock was ample: the failure was assuming the expected defense.

## T13 semifinal: g4 can remove ...Nh5
14...Nxh5 15.g4 Nf6 16.Qh2 Nh5?? 17.gxh5 gxh5 18.Qxh5 Bxd4 19.Qxh7#.
- With g4 still present, ...Nh5 fails to gxh5. DeepSeek imported a response appropriate to g5 without checking the pawn's actual square.
- Nf6 guards h7; Nh5 blocks the file but does not defend h7. The two pawn captures and Qxh5 removed the blockers. ...Bxd4 took Nd4 but ignored mate.
- Qd2-h2 passed through empty e2/f2/g2. Recheck queen paths and Rh1's screens. This successful branch does not certify Qh2 against better defenses; T16 marked the same move inaccurate.
- Finished with 16:03 before the final increment; Qh2 took 30 seconds, gxh5 17, Qxh5 11, mate 3.

## T13 round 3: earlier g5 warning
14...Nxh5 15.g4 Nf6 16.g5?! Ne8?! 17.Qh2 Rxd4?? 18.Qxh7#.
- g6 defended Nh5 after the first capture. Advancing g5 removed g4's capture of h5; test ...Nh5 rather than assuming forced retreat away from h7.
- ...Ne8 abandoned h7 and opened Bg7's diagonal toward Nd4. ...Rxd4 ignored mate. Finished with 15:28; no verified replacement for g5 supplied.

## T12 round 3: ...gxh5 branch
14...gxh5?! 15.Bh6?? Bxh6?? 16.Qxh6! Nxe4?? 17.Rxh5 Rxd4 18.Qxh7#.
- Bh6 abandoned Be3's defense of Nd4. ...Rxd4 Qxd4 Bxh6+ gives Black both minors for a rook; the bishop reaches Kc1 through g5/f4/e3/d2 after Qd2 leaves.
- Black chose the bishop exchange. Qxh6 was the only good recapture; ...Nxe4 abandoned h5/h7 and did not attack Qh6. Rxh5 cleared the file and supported mate.
- Black's claimed Nc3xd4 Rxd1+ was false: the recapture removes its attacking rook. Rxh5 took 53 seconds despite a verified forcing win.

## Chigorin and other recurring errors
- Ng3 ignored ...Qxc2 Qxc2 Rxc2 with c3-c6 empty, losing Bc2. ...Nc6 later screened the file; d5 drove it away and Bd3 saved the bishop.
- Rc1/Qc7 may have Bc2 and Nc5/Nc4 as screens. Removing both permits Rxc7. Attacking a knight need not force retreat.
- ...Rac8 Rxc8 Rxc8 Rxc8 traded one White rook for both Black rooks. ...e4 forked Qd3/Nf3, but Qxe4 removed it safely.
- Rc8 protected Qh8#; Qc3 protected Rh8#. ...g6 can occupy a king escape.
- Qg3+ fxg3 and Kf1 Qf3+ gxf3 lost queens: refresh pins after king moves.
- Nb4 Bd3 Nxd3 worked only with Nd2 blocking Qd1xd3. Nc4 allowed bxc4; Qb3 allowed cxb3.
