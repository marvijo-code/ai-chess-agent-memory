# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes:
- notes/capture-safety.md (scan + blunder catalogue g1-g42)
- notes/sicilian-black.md (g28-g36)
- notes/sicilian-dragon-white.md (g6,g34,g39,g42)
- notes/four-knights-black.md (g3-g26)
- notes/ruy-lopez-black.md (g1-g41)
- notes/ruy-lopez-white.md (g2-g37)

## Rule 1 - pre-move scan (EVERY move; losses g1-g42)
0. Scan the FINAL move and what it OPENS: a vacating piece/pawn (recapture!) uncovers his line/file onto my piece (g38 19.Bb3; g39 15.Nf4 -> Qd4#; g42 cxd5 vacated c6 -> Rfc8 hits Bc5).
1. Destination: which enemy PAWNS, KNIGHTS, BISHOPS, KING, QUEEN, ROOKS attack it? Attacked+undefended -> reject. Pawn magnets: h3->g4, f3->g4/e4, c3->b4/d4, c4->b3/d3, g6->f5/h5, c6->d5, d5->c6/e6. Knight magnets: b3/b4->c1/d2; c2->a1/e1/e3; c6->b4/d4/e5/e7; c5->e4/d3/b3/a4. Bishop magnets: d2-B hits a5/c3/b4; c2-B hits g6+h7.
2. MY attacked piece: save/trade/defend NOW (g30); no side move while it hangs (g42 16.h3?? Rxc5). His piece hits my QUEEN -> move her that move (g41); never grab a pawn a recapturer defends (g18,g23,g34).
3. Knight captures: count every recapturer, even a check (g19,g22,g23); never a knight to an undefended square in a bad position or where his pawn captures it (g40).
3b. QUEEN move/capture: list ALL attackers AND defenders of the destination, incl. rooks on the rank/file and PAWNS. No Q for R/B/N/P (g18..g42); never Qx where a rook defends (g36 14...Qxa4?? Rxa4; g42 17.Qxd5?? Rxd5); never a pawn-attacked square (g37,g28,g39). Trade offer needs a legal recapturer (g34).
3c. Qc7/Qc8/Qa5: retreat ...Qd8/...Qb6 the moment his Be3/Rc1 (Qc7, g35,g38) or Bd2 (Qa5, g41) gains tempo. Rook hits queen -> retreat, never grab.
3d. ROOK: check his rooks/king on the destination line; an undefended rook chasing a rook loses (g27); a rook his KING attacks loses (g29). His rook to an open file at my loose piece -> save it that move (g42).
4. A moving piece/pawn stops defending its old squares; re-scan after every enemy move/check (g16,g27,g30); declined trade -> take it or walk away (g11).
5. Knight forks: cover BOTH targets or vacate one (g23,g27); never move onto a forker's square; 2v2 = LAST recapturer lands there (g27).
6. Pinned Nd7 (Ba4, Re8): moving loses the exchange; unpin ...Rb8 (g15).
7. Mate nets: Qa1# (Kc1, g6); Qd4# (open d-file, Kf2, g39); Qxh7# with his Ng5+Nf5+Qh5: ...g6 BEFORE his queen arrives (g40); Qxh7+ with his Qh5+Bd3: ...g6, never ...Qf6?? (g25); Qe1+ then Qxd1# vs my undefended Rd1 (g42); Qf2#/Rb1#/Qg8# (g10,g21,g24); Q/R on the 8th, no luft: Re8#/Qc8#/Qd8# (g14..g41).
8. Never push a pawn onto a defended piece (g12), a knight-attacked square (g16), a pawn's attack (g24), a bishop's capture (g25), where a queen gains tempo (g19), while it guards my piece (g30), or into cxb4 (g40).
9. Loose units: check every undefended piece/pawn against ALL enemy lines (g26,g29); when lost, no 'active' piece to an undefended square (g39,g40): defend/trade, 5-15s.
12. Legality BEFORE sending (3 invalid = forfeit, g34): trace the path square by square (g39); knight/bishop geometry (g28,g34,g36).

## Rule 2 - time (900+10)
Book <=10s, routine <=15s; from m10 no move >30s (g41 43s; g42 41-56s m4,m13-18). Long thinks never fixed a blunder; the 5s final-move scan did. g36 flagged m30; g42 ended 8:38 vs 18:09 - opponents bank clock, I burn it.

## Openings
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, ...Na5 ...c5 ...Qc7 ...Bb7 ...Rac8; equal through 15...Qxa5 (g41), then 16.Bd2 hits Qa5 -> retreat ...Qd8/...Qc7/...Qb6. Keep f7 covered; never ...Nc4 once White has b3 (g16). His Nf1-g3: resolve the centre or reroute ...Nc6/...Nb6 BEFORE 15.d5; ...g6 early vs Nf5/Ng5+Qh5 (g40). Qc7 with Be3+Rc1: retreat ...Qb8/...Qd8 (g35,g38).
- Sicilian as Black: Dragon ...d6 ...cxd4 ...Nf6 ...Nc6 ...g6 ...Bg7 ...O-O ...a6 ...Bd7 ...Rc8 ...Qa5 equal (g28,g36); never ...Qxc4/Bxc4/Nd4; flank queen grabs lose to rook files (g36). Rauzer (g29,g32): 11...gxf6! not Bxf6; no Bxc3 while Bd7 hangs; g30: no ...f5?? (Nxc5).
- 4N as Black (4.Bb5 Bb4): 6.Nd5 Nxd5! 7.exd5 Nd4!; 7.h3 kills ...Bg4; c8-B needs ...d6 first; 10.c3 -> retreat Bb4; no 10...d3?!; 12.Qh5 ...g6!; 15.Qf3: no ...Bf5??/...Qd7??; play ...Qe7/...Qc8/...Bb5.
- Dragon as White (g6,g34,g39,g42): setup 6.Be3 7.f3 8.Qd2 9.O-O-O; losses are captures/trades: 12.Bxf6?!, 14.Nxe7+?! (g6); 9...d4! -> move the hit Nc3, not 10.Bxd4?? Qxd4 (g34); 8...d5 9.exd5 Nxd5 10.Nxc6 bxc6 11.Bd4 e5: no 12.Bxe5??/13.Qxd5?? (g39); g42: 12.Bc5! is loose - defend it (Qc3) or move it (Be3/Bb4) before 14.Nxd5 cxd5 opens the c-file for Rfc8; 16.h3?? lost it, 17.Qxd5?? Rxd5. Watch Qa1#/Qd4#/Qe1+.
- RL as White (Chigorin): 14...Nb4 -> 15.Bb1!; ...Nb8 line fine to 27.Bxe4 (Bb7 blocked by d5); 27...c3: never 28.Qxc3?? bxc3; after ...g6 no Nf5 (g22); 18...Nc5 -> 19.Nd2! (19.Ng3?? Nb3!, g23); 14...Rac8 15.Ne3 Nc4: keep e3 EMPTY (g33); never Q on d5 or a pawn-attacked square.

## Opponents
- Stockfish 19 (g6..g42): ~0s/move; punishes loose pieces, queens on attacked squares/lines, loose bishops on open files (g42); Yugoslav ...d5: d5 pawn-guarded, d-file blocked.
- Sonnet 5.5 (g7..g41): banks clock; instantly takes free/attacked units (Nxa1, Rxb2, Rxd6, Bxe4, Bxa5). Keep every piece and pawn defended; move an attacked queen at once; never a knight on an undefended square or where a pawn takes it (g40); no rook near his king.
- GPT-6.1 Sol (g9..g38): closed RL, fast; punishes queens on his lines/files; captures must survive recapture (g35 Qxc1??, g38 Nb6??).
