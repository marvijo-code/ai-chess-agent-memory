# Ruy Lopez Closed - White (Chigorin)

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 / 12...exd4 13.Nxd4 / 12...Nc6 13.d5 Nb4.

## g82 vs Sonnet (0-1, Qa3# m45) - 3 knight-geometry blunders after 17...exd4
13...Nc6 14.Bb1 a5 15.Qe2 Bd7 16.Nf1 Rac8 17.Ng3 exd4?? 18.Nxd4?? Nxd4! 19.Qd2 (Qxd4 illegal - e2-d4 is no queen line) Nc6 20.Nf5?? Bxf5 21.exf5 d5 22.Rxe7?? Nxe7 23.Qxd5?? Nexd5 24.Be4 Nxe4 25.Kf1 Qxc1+ 26.Rxc1 Rxc1+ 27.Ke2 Nec3+ 28.bxc3 Rxc3 29.Kd2 Rxh3 30.gxh3 Rd8 ... 45...Qa3#.
- After 13.cxd4 d4 has ONE defender (Nf3); Qe2 does NOT cover d4 - only Qd1/Qd2 do (file). 17...exd4 wins a pawn and 18.Nxd4?? Nxd4 (c6) loses a PIECE: no recapturer (c-pawn gone, Qe2 can't take). Keep Qd1 or Qd2 while ...Nc6/...exd4 hit d4: play Nf1 BEFORE Qe2.
- 20.Nf5?? was hit by Bd7 (d7-e6-f5) - check bishops, not just pawns. Down a piece: no N-for-B/R-for-B trades.
- 22.Rxe7??: c6-e7 recapture; 23.Qxd5??: e7 AND f6 both hit d5. Knight sweep every capture: count 2+1 squares.
- Clock: 43-61 s on moves 14-25, 3:32 vs 14:53 at the end.

## g78 vs Sol (0-1, Be5# m32) - ...Nc4/...Nxe3 after Bg5/Be3
13.cxd4! Bb7 14.Nf1 Rfe8 15.Ng3 Rac8 16.Bg5?? h6 17.Be3?? Nc4! 18.Nh5?? Nxe3! 19.fxe3 Qxc2! 20.Qxc2 Rxc2 21.Nxf6+ Bxf6 22.d5 Rxb2 23.Re2?? Rxe2 24.Re1 Rxe1+ 25.Kf2?? {Kxe1 legal} Rc1 ... 32.Kh2 Be5#.
- After 16...h6 do NOT come back to e3 (...Nc4 hits e3+b2); trade on f6 or Bd2/Bf4, then answer ...Nc4 at once.
- 19...Qxc2: Bc2 had one defender (Qd1) and his rook second-attacked; keep it doubly guarded or move Qd1 early. 23.Re2?? undefended rook onto his rook's rank. After any capture re-read the board (25.Kxe1 legal).

## g77 vs Sonnet (0-1, Qg2# m40) - 13.d5 c4
13.d5 Rac8 14.Nf1 c4 15.Ng3 Rfe8 16.Nh2 g6 17.f4 exf4 18.Bxf4 Nb7 19.Be3 Nc5 20.Bxc5?? Qxc5+ ... 28.Qh6+?? Kxh6 ... 39.g3 Bc6 40.gxf4?? Qg2#.
- 16...g6! takes f5 from both knights; with ...g6 on, Nf5+ is no sac (g6 recaptures). 20.Bxc5?? = B for N giving Qxc5+ with check.
- 28.Qh6+?? Kxh6: h6 undefended. 39...Bc6 aimed Qxg2# - 40.Bxc6 was the only block.

## g73 vs Sonnet (0-1, Qh1# m32) - pawn capture squares apply to any piece
23.Be5?? dxe5 24.Qd2?? Rxd2 25.Bd3 Rxd3.
- Keep the d4-bishop home. When his capture opens a file and his rook hits my queen, leave the FILE (Qe2/Qc2), never along it.

## Older - condensed
- g70: 23.Rxe5?? dxe5 ('not on' and sent); 24.Qd4?? exd4; 25.Bd3?? Nxd3. g67: 26.Rxe7?? marked bad and sent.
- g65: 21.Bxh6?? gxh6 22.Qxh6 Bxh6 = B+Q for 2P. g61: 24.Qa3?? Rxa3. g60: 21.Qxa4?? bxa4.
- g7/g8/g19: keep f7 covered; never a piece on a square a White knight attacks; no unit that must be saved ignored.

## Working
- 14...Nb4 -> 15.Bb1!; reroute d2-knight f1-e3-f5 only once d4 is safe (Qd2/Nf3) and ...g6 is off.
- No queen on d4 vs his e5-pawn; no queen on an open file facing his rook; count every recapturer; no undefended rook onto his rook's rank.
- Equal Chigorin: improve slowly; routine <=15 s; long thinks never prevented a blunder.
