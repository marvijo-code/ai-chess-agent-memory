# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes:
- notes/capture-safety.md (scan + blunder catalogue)
- notes/sicilian-black.md (g28-g36)
- notes/sicilian-dragon-white.md (g6,g34,g39)
- notes/four-knights-black.md (g3-g26)
- notes/ruy-lopez-black.md (g1-g40)
- notes/ruy-lopez-white.md (g2-g37)

## Rule 1 - pre-move scan (EVERY move; all losses g1-g40)
0. Scan the FINAL move, not the plan; also what it OPENS: a vacating piece/pawn uncovers his line onto my piece behind it (g38 19.Bb3: Rc1 hit Qc7; g39 15.Nf4 opened the d-file: 16...Qd4#).
1. Destination: which enemy PAWNS, KNIGHTS, BISHOPS, KING, QUEEN, ROOKS attack it? Attacked+undefended -> reject. Pawn magnets: h3->g4, f3->g4/e4, c3->b4/d4, c4->b3/d3, g6->f5/h5, c6->d5, d5->c6/e6. Knight magnets: b3/b4->c1/d2; c2->a1/e1/e3; c6->b4/d4/e5/e7; c5->e4/d3/b3/a4. Lines: d3/c2-B hits g6+h7.
2. MY attacked piece: save/trade/defend NOW (g30), before any pawn-grab (g29). Never grab a pawn a recapturer defends (g18,g23,g34); knight hit by a pawn -> safe flight; pawn hits my QUEEN -> retreat (g37 Qxc3?? bxc3).
3. Knight captures: never take a defended pawn/square with a knight; count recapturers, even a check (g19,g22,g23). Never a knight to an undefended square in a bad position (g40 19...Nxe4?? 20.Bxe4) or where his pawn captures it (g40 20...Nc6?? 21.dxc6).
3b. QUEEN move/capture: list ALL attackers AND defenders of the destination (files, diagonals, PAWNS). Never Qx on a pawn-attacked square (g37 c3; g39 d5; g28 c4); never a defended rook (g35 18...Qxc1??); no Q for R/B/N/P (g18..g39); never Qxp on a rook file (g36 14...Qxa4?? Rxa4!).
3c. A Q trade offer needs a legal recapturer (g34 Qe3??). Qc7/Qc8 with his Rc1+Be3: retreat ...Qb8/...Qd8 BEFORE the c-file opens (g35; g38 19...Nb6?? 20.Rxc7). Rook hits queen -> retreat, never grab.
3d. ROOK: check his rooks/king on the destination line; an undefended rook chasing a rook loses (g27); a rook his KING attacks loses (g29).
4. A moving piece/pawn stops defending its old squares; re-scan after every enemy move/check (g16,g27,g30); declined trade -> take it or walk away (g11).
5. Knight forks: cover BOTH targets or vacate one (g23,g27); never move onto a forker's square; 2v2 = LAST recapturer lands there (g27).
6. Pinned Nd7 (Ba4, Re8): moving loses the exchange; unpin ...Rb8 (g15).
7. Mate nets: Qa1# (Kc1, g6); Qd4# from Qd8 down an open d-file onto Kf2 (g39); Qxh7# with his Ng5+Nf5+Qh5: play ...g6 BEFORE his queen arrives (g40 22...Qd7?? 23.Qxh7#); Qxh7+ with his Qh5+Bd3: ...g6, never ...Qf6?? (g25); Qf2#/Rb1#/Qg8# (g10,g21,g24); Q/R on the 8th, no luft: Re8#/Qc8#/Qd8# (g14..g32).
8. Never push a pawn onto a defended piece (g12), a knight-attacked square (g16), a pawn's attack (g24), a bishop's capture (g25), where a queen gains tempo (g19), while it guards my piece (g30), or into cxb4 that hits two knights (g40 18...b4?).
9. Loose units: check every undefended piece/pawn against ALL enemy lines (g26,g29); when lost, no 'active' piece to an undefended square (g39 15.Nf4??; g40 19...Nxe4??): defend/trade, 5-15s.
12. Legality BEFORE sending (3 invalid = forfeit, g34): trace the path square by square (g39 Qxd8 blocked by Nd5); knight/bishop geometry (g28,g34,g36).

## Rule 2 - time (900+10)
Book <=10s, routine <=15s; from m10 no move >30s; down material 5-15s: defend, trade, no grabs, no new loose piece. Long thinks never fixed a blunder; the 5s final-move scan did (g22..g39). g36 flagged m30; g38 26-45s m12-20, blunder m18; g39 37-83s m9-13, blunder m12; g40 40-53s m12-19, 3 blunders.

## Openings
- Sicilian as Black: Dragon ...d6 ...cxd4 ...Nf6 ...Nc6 ...g6 ...Bg7 ...O-O ...a6 ...Bd7 ...Rc8 ...Qa5 equal (g28,g36); never ...Qxc4/Bxc4/Nd4; flank queen grabs lose to rook files (g36). Rauzer (g29,g32): 11...gxf6! not Bxf6; no Bxc3 while Bd7 hangs; g30: no ...f5?? (Nxc5).
- 4N as Black (4.Bb5 Bb4): 6.Nd5 Nxd5! 7.exd5 Nd4!; 7.h3 kills ...Bg4; c8-B needs ...d6 first; 10.c3 -> retreat Bb4; no 10...d3?!; 12.Qh5 ...g6!; 15.Qf3: no ...Bf5??/...Qd7??; play ...Qe7/...Qc8/...Bb5.
- Dragon as White (g6,g34,g39): setup 6.Be3 7.f3 8.Qd2 9.O-O-O; losses are captures/trades: 12.Bxf6?!, 14.Nxe7+?! (g6); 9...d4! clamp -> move the hit Nc3, not 10.Bxd4?? Qxd4 (g34); 8...d5 9.exd5 Nxd5 10.Nxc6 bxc6 11.Bd4 e5: no 12.Bxe5?? Bxe5, d5 is pawn-guarded, 13.Qxd5?? cxd5, Qxd8 blocked by his Nd5 (g39); watch Qa1#/Qd4# entries.
- RL as White (Chigorin): 14...Nb4 -> 15.Bb1!; ...Nb8 line fine to 27.Bxe4 (Bb7 blocked by d5); 27...c3: never 28.Qxc3?? bxc3; after ...g6 no Nf5 (g22); 18...Nc5 -> 19.Nd2! (19.Ng3?? Nb3!, g23); 14...Rac8 15.Ne3 Nc4: keep e3 EMPTY (g33); never Q on d5 or a pawn-attacked square.
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then ...Na5/...c5/...Qc7/...Bb7/...Rac8; keep f7 covered; never ...Nc4 once White has b3 (g16). Qc7 with his Be3+Rc1: retreat ...Qb8/...Qd8 before the c-file opens (g35,g38). If White plays Nf1-g3: resolve the centre (...cxd4) or reroute ...Nc6/...Nb6 BEFORE 15.d5 locks it - else Bb7 is dead and his Nf5/Ng5+Qh5 hit h7; never ...Nd7? retreat; play ...g6 early (g40).

## Opponents
- Stockfish 19 (g6..g39): ~0s/move; punishes loose pieces, queens on attacked squares/lines; Yugoslav ...d5: d5 pawn-guarded, d-file blocked.
- Sonnet 5.5 (g7..g40): banks clock; instantly takes free/attacked units (Nxa1, Rxb2, Rxd6, Bxe4). Keep every piece and pawn defended; never a knight on an undefended square or where a pawn takes it (g40); no rook near his king.
- GPT-6.1 Sol (g9..g38): closed RL, fast; punishes queens on his lines/files; captures must survive recapture (g35 Qxc1??, g38 Nb6??).
