# DeepSeek V4.1 Flash: Dragon tactics

Wins, sparse marks and opponent explanations do not validate moves. Track material, defenders, pawn squares and blockers independently. Chigorin: notes/ruy-lopez.md.

## Shared opening
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3 O-O 8.Qd2 Nc6 9.Bc4 Bd7 10.O-O-O Rc8 11.Bb3 Ne5 12.h4 Nc4 13.Bxc4! Rxc4!.
- Nc4 attacks Qd2/Bb3; remove it before continuing the attack. Rxc4 was the only good reply.

## T17 round 3: g4 before h5, mate win
14.g4 Rc8?! 15.h5 Nxh5?! 16.gxh5 Qa5 17.Kb1 Qb4 18.Bh6 Qb6 19.hxg6 hxg6 20.Bxg7 Kxg7 21.Qh6+ Kg8 22.Qh7#.
- Keeping the pawn on g4 made Nxh5 capturable by gxh5. Black had copied the knight capture from a different pawn order. White gained a knight for a pawn without sacrificing a rook. No best defense to g4/h5 or forced win before Black's errors was supplied.
- Qa5/Qb4 sought counterplay against Nc3, Nd4 and queenside pawns. Kb1 left the c-file and guarded a2/b2. Qd2 defended both knights; Bh6 removed Be3's additional guard of Nd4. Queen attacks need a defender count, not automatic retreats.
- hxg6 removed Black's original g-pawn; h7xg6 moved the remaining h-pawn OFF the h-file. Trace the entire file: Rh1 now supported Qh6 and Qh7.
- Bxg7 exchanged the defensive bishop. After Kxg7, Qh6+ Kg8 Qh7# worked, but Kg8 was not forced. At mate Rh1 prevented Kxh7, Qh7 covered h8/g8/g7, and Rf8/f7 occupied exits.
- No invalid attempts; finished with 13:53. Opening moves mostly 3-7 seconds; Bh6/hxg6/Bxg7 took 47/39/52. Calculate captures and king replies within a deadline.

## T16 semifinal: h5 first, protected knight block
14.h5 Nxh5 15.g4 Nf6 16.Bh6 Bxh6? 17.Qxh6! Qe8 18.g5? Nh5! 19.Rxh5 gxh5 20.Nd5?! Qd8? 21.Rh1 h4 22.Rxh4 Rxd4 23.Qxh7#.
- g5 cannot capture Nh5; g6 protects that square. Rxh5 traded rook for knight, and the win did not establish compensation. Bh6 was not proven best against stronger defense; no verified replacements for g5/Nd5 supplied.
- Qh6 alone did not protect Qxh7 against Kxh7. Rd1-h1 supplied support; Rxh4 removed the file blocker. Black's h4 pawn attacked g3, not g5.
- Rh1 abandoned Nd4: Rd1 had guarded it through empty d2/d3 after Qxh6. Rxd4 won the knight but ignored mate. Rh4 protected h7 through empty h5/h6.

## Qh2 branches: actual pawn location matters
T16 round 1: 14.h5 Nxh5 15.g4 Nf6 16.Qh2?! Rc8?? 17.g5?? Nxe4?? 18.Qxh7#.
- g5 again allowed protected Nh5. Nxe4 abandoned h7; mate before answering the knight attack. No verified best replacement for Qh2 supplied.

T13 semifinal: same through 15...Nf6, then 16.Qh2 Nh5?? 17.gxh5 gxh5 18.Qxh5 Bxd4 19.Qxh7#.
- With g4 still present, gxh5 removes the knight. Nf6 guards h7; Nh5 only blocks the file. Captures clear it and Rh1 supports mate. Trace Qd2-h2 through e2/f2/g2.

T13 round 3: 16.g5?! Ne8?! 17.Qh2 Rxd4?? 18.Qxh7#.
- Ne8 abandoned h7 and opened Bg7 toward Nd4. Always test Nh5 before claiming g5 forces the defender away.

## T12: ...gxh5 branch
14.h5 gxh5?! 15.Bh6?? Bxh6?? 16.Qxh6! Nxe4?? 17.Rxh5 Rxd4 18.Qxh7#.
- Bh6 abandoned Nd4: Rxd4 Qxd4 Bxh6+ gives Black both minors for rook. Black chose the bishop exchange instead; Qxh6 was the only good recapture.
- Nxe4 abandoned h5/h7; Rxh5 cleared the file and supplied support. Black's claimed Nc3xd4 Rxd1+ was false: the recapture removes its attacking rook.

## Other recurring geometry
- Ng3 ignored Qxc2 Qxc2 Rxc2 with c3-c6 empty, losing Bc2. Nc6 later screened that file.
- Rc1/Qc7 can have Bc2 and Nc5/Nc4 as screens. Removing both permits Rxc7. Rac8 Rxc8 Rxc8 Rxc8 traded one White rook for both Black rooks.
- ...e4 forked Qd3/Nf3 but Qxe4 removed it safely. Rc8 protected Qh8#; Qc3 protected Rh8#.
- Qg3+ fxg3 and Kf1 Qf3+ gxf3 lost queens: refresh pins after king moves.
- Nb4 Bd3 Nxd3 worked only with Nd2 blocking Qd1xd3. Nc4 allowed bxc4; Qb3 allowed cxb3.
