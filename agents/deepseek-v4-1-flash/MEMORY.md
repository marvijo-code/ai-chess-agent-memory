# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes:
- notes/capture-safety.md (scan + blunder catalogue g1-g24)
- notes/sicilian-dragon-white.md (g6)
- notes/four-knights-black.md (g3,g4,g11,g14,g17,g20,g24)
- notes/ruy-lopez-black.md (g1,g7,g8,g12,g15,g16,g19)
- notes/ruy-lopez-white.md (g2,g5,g9,g10,g13,g18,g21,g22,g23)

## Rule 1 - pre-move scan (EVERY move; all losses g1-g24)
0. Scan the FINAL chosen move, not the plan or a 'standard' line (g21 15.Bd3?? after noting Nb4's squares; g24 spent 47s on 10...Bg4?? - a square the h3-pawn attacks).
1. Destination: which enemy PAWNS, KNIGHTS, KING attack it? Attacked+undefended -> reject. Pawn magnets: h3->g4 (g24 10...Bg4?? 11.hxg4 = B for P), f3->g4/e4, e5->d6/f6, d5->c6/e6, c3->b4/d4, b3->a4/c4, b5->a4/c4, c4->b3/d3, g6->f5/h5. Knight magnets: b4->a2/c2/d3/d5; b3->a1/c1/d2/d4/a5/c5 (g23 20.Bd2?? Nxa1); d4->b3/c2/e2/f3/f5/b5/c6/e6; e4->d2/f2/c3/g3/c5/f6; c6->a5/a7/b4/b8/d4/d8/e5/e7 (NOT d7); b8->a6/c6/d7 only if no enemy Q/B (g20 11...Nd7??).
2. Knight captures: never take a defended pawn/square with a knight - count recapturers (g19 18...Nd7?! dxc6; g22 26.Nxd6?? Qxd6; g23 38.Nxe5?? dxe5).
3. Queen/rook moves: list ALL attackers incl. rooks on the target's file (g22 31.Qxc4?? Rc8xc4); Q for B/N/P is a loss even if 'defended' (g18 23.Qd5?? Bxd5); d5 is a queen trap (g12,g17,g18,g19); name the squares a queen leaves (g17 12...Qd6?? left d4).
4. A moving piece stops defending: fix the squares it leaves; re-scan after checks/forced moves and after every enemy move (g16 26...Nxe4?? Re1 re-covered e4).
5. Knight forks: cover BOTH attacked units or vacate one (g23 19...Nb3 forked Ra1+Bc1, both loose - save the rook); never move onto a forker's square (20.Bd2?? Nxa1).
6. Pinned knight behind Ba4-Nd7-Re8: moving it loses the exchange (g15 17...Nb6? 18.Bxe8); unpin ...Rb8.
7. Mate nets: Qa1# (king c1, d2 blocked, g6); Qxf7# (king f8, g12); Qf2# (g10); Qxg2# (g13); Re8#/Qc8# (king g8/h8, open 8th rank, g14,g16,g19,g20); Rb1# (g21); Qg8# (king c8 + Rf7, g24).
8. Never push an undefended pawn onto a defended piece (g12 19...h6?? Bxh6), a knight-attacked square (g16 21...f5?? Nxf5), onto any enemy pawn's attack (g24), or where the queen takes with tempo (g19 24...b3?? Qxb3+).
9. Loose pieces: my undefended units + enemy Q/R/N lines; king-only defense fails vs a queen (g12 25...Nh7??).
10. Attacked piece with no profitable trade: retreat to a square no pawn/knight attacks, no line covers; declined trade -> take it or walk away (g11 25...Bf5?? Nxf5).
11. Enemy pawn attacks a knight -> move it or defend it (g19 18...Nd7?! dxc6).
12. No rook grab of a pawn a rook/queen recaptures (g18 25.Rxe5 Rxe5); no bishop grab of a twice-defended pawn (g23 21.Bxa5?? Rxa5 = B for P); down material, no pawn grabs at all.
13. Legality: path clear (own pieces block! g23 Be3 blocked by Nd2), knight geometry; illegal tries waste clock.
14. Mate threat > material: with a mate net on my king defend first, never grab a pawn (g12,g17).

## Rule 2 - time (900+10)
Book <=10s, routine <=15s, max 3 thinks of 30-45s; after 25s play the safest candidate now. Long thinks never prevented a blunder; the 5s scan did (g22 40-60s/move, flagged; g23 43-68s, 2 blunders; g24 47s on 10...Bg4??). HARD: from move 10, no move >30s unless a forced tactic/mate; check the clock every move; when down material play 5-15s (g24 wasted 30-56s/move 11-34 while a piece down).

## Openings
- 4N as Black (4.Bb5 Bb4): if White plays 7.h3, ...Bg4 is dead - play ...Bd7/...Ne7 (g24 10...Bg4?? 11.hxg4 Nxg4 = B for P). 6.Nd5 -> TAKE 6...Nxd5! (7.exd5 Nd4!); 6...Be7?! lets 7.c3 and 9.Nxe5! (g20). 10.c3 attacks Bb4 -> retreat (10...Bxc3?? dxc3, g11). 12...Qd6?? left d4 -> 13.Qxd4! (g17). 10...c6! beats ...Re8.
- RL as White (Chigorin): 11.d4/13.cxd4/14.d5 fine. 14...Nb4 -> 15.Bb1! (b4-knight attacks a2/c2/d3/d5). 14...Nb8: 15.Nf1 Nbd7 16.Be3 Bb7 17.Qd2 Nc5 18.Ng3 Rfe8 19.Nf5 Bf8 20.Bxc5 Qxc5 equal; after ...g6 do not tour Nf5 (g22 23.Nef5?? gxf5). 15...a5 16.a3 Na6 17.Qe2 Bd7 18.Nf1 Nc5: 19.Nd2! (covers e4 AND b3); 19.Ng3?? let 19...Nb3! fork a1/c1 and lost a rook (g23). Keep queen off c-file after ...Qb6 and off d5; keep the dark bishop.
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then ...Na5/...c5/...Qc7/...Nc6/...Bb7/...Rac8; keep f7 covered. Never ...Nc4 once White has b3 (g16). Breyer: 16.Bxa4 pins Nd7 to Re8 -> no ...c5?!, unpin ...Rb8 (g15). Chigorin g19: 16...a5?! 17...b4?! weakened the queenside; 18.d5! hit Nc6.
- Sicilian Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O; watch ...Qxa2/...Qa1#.

## Opponents
- Stockfish 19 (ladder, g6,g17,g20,g24): ~0s/move; punishes every deviation and loose piece (g24: a piece onto a pawn-attacked square = lost, no counterplay). Known-solid lines only; scan every destination; retreat attacked pieces.
- Sonnet 5.5 (g7,g8,g12,g15,g16,g19,g23): banks clock (16:25 vs 1:09, g23); takes free/attacked units at once (Nxa1, Rxa5, dxe5). Keep every piece on unattacked squares.
- GPT-6.1 Sol (g9,g10,g13,g18,g21,g22): solid closed RL; takes exposed units at once; punishes queens on his lines; banks clock. Any capture I make must survive his recapture.

## Principles
- Scan mate nets and ALL attackers of every queen/rook/knight destination; queen/knight safety before material; a knight taking a defended pawn is a blunder (g19,g22,g23).
- 'Standard' development is not a scan: verify each destination against enemy pawns (g24 h3xg4 = B for P).
- Attacked piece with no profitable trade: retreat to a square no pawn/knight attacks and no line covers.
- The 5s scan on the final move beats any long think; routine <=15s, no move >30s from move 10.
- After a blunder: defend loose pieces, trade down, play fast (5-15s); king safety first; no pawn grabs while down material (g23).
