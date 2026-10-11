# Ruy Lopez: central recaptures, screens and king safety

## T26 round 2: White vs Stockfish 19, mate loss
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O b5 6.Bb3! Bc5 7.d3 d6 8.c3 h6 9.Re1 O-O 10.d4 Bb6 11.h3 Bb7 12.Nbd2?! exd4! 13.cxd4 Nxd4! 14.Nxd4 Bxd4! 15.Nf3 Bb6 16.e5 dxe5! 17.Nxe5.
- Nbd2 blocked Qd1-d2-d3-d4. After exd4 cxd4, only Nf3 defended d4 against Nc6 and Bb6 (b6-c5-d4). Nxd4 Nxd4 Bxd4 left no recapturer: Nd2 cannot capture d4 and blocks the queen. Audit the full central liquidation before routine development. No verified best replacement for Nbd2 supplied.
- Nf3 attacked Bd4 but merely chased it. e5 dxe5 Nxe5 exchanged White's e-pawn for Black's d-pawn; it did not recover the earlier deficit. White had lost c/d/e pawns, Black d/e: still one pawn down.
17...c5 18.Bf4 c4 19.Bc2 Qd5 20.Nf3 Rad8 21.Qe2 Qc6 22.Ne5?? Qxg2#.
- Qd5 threatened Qxg2# with Bb7 support. Nf3 interposed on d5-e4-f3-g2. Qc6 retained the same route through d5/e4/f3; moving the queen did not remove the threat.
- Ne5 attacked Qc6 but abandoned the sole screen. Qxg2 was checkmate, protected by Bb7 through c6-d5-e4-f3-g2 AFTER the queen vacated c6. Trace the attacker's departure square too: the queen capture uncovered its own bishop support.
- Qe2 defended Nf3 but did not replace its defensive duty; f2 blocked Qe2-g2. Before moving a king screen, calculate checks and mating captures on the resulting board before counting a queen tempo.
- No invalid attempts; finished 14:41. Ne5 took 22 seconds; Qe2 35 and Nf3 30. Ample time did not prevent the missed mate. Only Nbd2 received an adverse mark; the unmarked Ne5 still allowed mate in one.

## T25 round 2: White vs Sonnet, Chigorin mate win
12.Nbd2 cxd4 13.cxd4 Nc6 14.Nf1 a5 15.d5 Nb4 16.Bb1 a4 17.a3 Na6 18.Ng3 Nc5 19.Be3 Bd7 20.Bd3 Rac8 21.Qd2?! Rfe8 22.Rad1 h6 23.Nh2 Bf8 24.f4? exf4 25.Bxf4 Be7 26.Nf5?! Bxf5 27.exf5 Nxd5 28.Bxb5 Red8?? 29.Qxd5.
- Nf1 cleared d2 and restored Qd1-d4. Qd2 permitted ...Nb3's fork of Q/Ra1; Rad1 removed the rook target. Qd2/f4/Nf5 were marked adverse; no verified improvements supplied.
- Bxf5 exf5 opened Re1-e7, but Qc7 still guarded Be7. After Red8, own d6 blocked Rd8-d5, so Qxd5 won N and defended Bf4.
- Nc6 forked Rd8/Be7; ...Rf8 Nxe7 Qxe7 Rxe7 won B+Q for N. Neither enemy rook could recapture e7. Later ...Rfe8 Rxe8+ Rxe8 Bxe8 removed both enemy rooks for one; Bb5-e8 was clear after the knight moved.
- Bf8 protected g7 for Qxg7#. Finished 11:43; shorten quiet conversion after checking guards and exchanges. Opponent gifts do not validate earlier errors.

## T25 round 1: White vs Stockfish 19, mate loss
...Bc5/O-O/d5: exd5 Nxd5 Nxe5 Bxf2+ Kxf2! Nxe5 12.d4?? Qh4+ Kg1 Ng4 h3 Nf2 Qe2 Nxh3+ gxh3 Qg3+ Kh1 Bb7 Rg1 Nxc3+ Qg2 Qxh3#.
- d4 attacked N but ignored checks against Kf2. Rxe5 also needs ...Qf6+, forking K/R; no verified replacement supplied.
- Nxh3+ gxh3 cleared g2. Nd5 screened Bb7-Kh1; Nxc3+ uncovered check AND attacked Qe2. Rg1's queen attack did not gain time.
- Qg2 interposed but became absolutely pinned; Qxh3 was illegal. Finished 13:55: checking-reply failure, not clock shortage.

## Earlier lessons
- Chigorin: g6 hxg6 hxg6 fxg6 lost P; N5h4 Bxh4 and Ne6 Bxe6 dxe6 Rxe6 lost material without verified compensation. Own c3 can block Rc1-Rc6; c4 can fork Rb5/Nd5.
- d3/Bc5: e5 clears Bc2-h7. ...f5 exf6 e.p. Nxf6 Rxe7 won Q for R. d5 Bxd5 lost P because Nf6 blocked Qxd5; ...Rd5 skewered Be5/Qf5.
- Qd4 c6 Qxc4 cxd5 forks Qc4/Be4. Bh5/Qe2 share Nf3: Ne5 Bxe2. Ne5 screens Re6-e1: Nxf7 Re1#.
- Own d4 blocks Qd1-d5: Rxd5 Qxd5. Qe2 Rfc8 Bc2 Qxc2 Qxc2 Rxc2 loses B. ...Nxg3 fxg3 can abandon Be3 to Rxe3.
