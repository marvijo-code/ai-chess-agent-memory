# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes:
- notes/capture-safety.md (scan + blunder catalogue g1-g26)
- notes/sicilian-dragon-white.md (g6)
- notes/four-knights-black.md (g3,g4,g11,g14,g17,g20,g24,g25,g26)
- notes/ruy-lopez-black.md (g1,g7,g8,g12,g15,g16,g19)
- notes/ruy-lopez-white.md (g2,g5,g9,g10,g13,g18,g21,g22,g23)

## Rule 1 - pre-move scan (EVERY move; all losses g1-g26)
0. Scan the FINAL move, not the plan (g21 15.Bd3??; g24 ...Bg4?? after 47s; g25 12...Qf6?? 13.Qxh7+; g26 ...Bf5??/...Qd7?? after 40s+).
1. Destination: which enemy PAWNS, KNIGHTS, BISHOPS, KING, QUEEN attack it? Attacked+undefended -> reject. Pawn magnets: h3->g4 (g24), f3->g4/e4, e5->d6/f6, d5->c6/e6, c3->b4/d4, b3->a4/c4, b5->a4/c4, c4->b3/d3, g6->f5/h5. Knight magnets: b4->a2/c2/d3/d5; b3->a1/c1/d2/d4/a5/c5 (g23); d4->b3/c2/e2/f3/f5/c6/e6; e4->d2/f2/c3/g3/c5/f6; c6->a5/a7/b4/b8/d4/d8/e5/e7 (NOT d7). Bishop lines: d3/c2-bishop hits g6+h7 (g25 14...Qg6?? Bxg6). Queen lines: his Qf5 hits d7 (g26 16...Qd7?? 17.Qxd7); his Qf3 hits f5 up the file (g26 15...Bf5?? undefended, Qxf5 = B for P).
2. Knight captures: never take a defended pawn/square with a knight - count recapturers (g19 18...Nd7?! dxc6; g22 26.Nxd6?? Qxd6; g23 38.Nxe5?? dxe5).
3. Queen/rook moves: list ALL attackers incl. rooks on the file (g22 31.Qxc4?? Rxc4); Q for B/N/P is a loss even if 'defended' (g18,g25); d5 is a queen trap (g12,g17,g18,g19); name the squares it leaves (g17 12...Qd6?? left d4).
4. A moving piece stops defending: fix the squares it leaves; re-scan after checks/forced moves and every enemy move (g16 26...Nxe4?? Re1 re-covered e4).
5. Knight forks: cover BOTH targets or vacate one (g23 19...Nb3 forked Ra1+Bc1); never move onto a forker's square (20.Bd2?? Nxa1).
6. Pinned knight behind Ba4-Nd7-Re8: moving it loses the exchange (g15 17...Nb6? 18.Bxe8); unpin ...Rb8.
7. Mate nets: Qa1# (king c1, g6); Qxh7+ when his Qh5+Bd3 cover h7 (Kxh7 illegal) - defend ...g6, never ...Qf6?? (g25); Qxf7# (g12); Qf2# (g10); Qxg2# (g13); Re8#/Qc8# (king on 8th, no luft; g14,g16,g19,g20,g25); Rb1# (g21); Qg8# (g24); Qd8+/Qxe8# (g26). Mate threat > material: defend first (g12,g17,g25).
8. Never push an undefended pawn onto a defended piece (g12), a knight-attacked square (g16), any enemy pawn's attack (g24), a bishop's capture (g25 10...d3?! 11.Bxd3), or where a queen takes with tempo (g19).
9. Loose pieces: my undefended units + all enemy lines; an undefended minor on a square his queen attacks is lost (g26); king-only defense fails vs a queen (g12).
10. Attacked piece with no profitable trade: retreat to a square no pawn/knight attacks, no line covers; declined trade -> take it or walk away (g11).
11. Enemy pawn attacks a knight -> move it or defend it (g19).
12. No rook grab of a pawn a rook/queen recaptures (g18); no bishop grab of a twice-defended pawn (g23); down material, no pawn grabs.
13. Legality: path clear (own pieces block! c8-bishop behind d7-pawn: Be6/Bf5/Bg4 illegal until ...d6 - g25); knight geometry.
14. From move 10 treat every enemy queen line to my destination as a mine.

## Rule 2 - time (900+10)
Book <=10s, routine <=15s, max 3 thinks of 30-45s; after 25s play the safest candidate. Long thinks never prevented a blunder; the 5s scan did (g22 40-60s; g23 43-68s; g24 47s on ...Bg4??; g25 50-87s; g26 24-47s, both blunders). HARD: from move 10 no move >30s unless forced tactic/mate; down material 5-15s (g24).

## Openings
- 4N as Black (4.Bb5 Bb4): 6.Nd5 -> 6...Nxd5! (7.exd5 Nd4!); 7.h3 kills ...Bg4; c8-bishop needs ...d6 first (g24,g25). 10.c3 attacks Bb4 -> retreat (10...Bxc3?? dxc3, g11). 9.b3 Bc5 10.a4: no 10...d3?! (11.Bxd3 = free pawn, g25); play ...a6/...d6/...Re8/...Bd7. 12.Qh5: ...g6!; 12...Qf6?? 13.Qxh7+! and 14...Qg6?? 15.Bxg6 (g25). 12...Qd6?? left d4 (g17). Rubinstein: 15.Qf3 attacks f5 - no ...Bf5?? (16.Qxf5); then no ...Qd7?? (17.Qxd7); play ...Qe7/...Qc8/...Bb5 (g26).
- RL as White (Chigorin): 11.d4/13.cxd4/14.d5 fine. 14...Nb4 -> 15.Bb1!. 14...Nb8: 15.Nf1 Nbd7 16.Be3 Bb7 17.Qd2 Nc5 18.Ng3 Rfe8 19.Nf5 Bf8; after ...g6 no Nf5 tour (g22). 18...Nc5: 19.Nd2! (covers e4 AND b3); 19.Ng3?? Nb3! (g23). Keep queen off c-file after ...Qb6, off d5.
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then ...Na5/...c5/...Qc7/...Nc6/...Bb7/...Rac8; keep f7 covered. Never ...Nc4 once White has b3 (g16). Breyer 16.Bxa4 pins Nd7 to Re8: unpin ...Rb8 (g15).
- Sicilian Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O; watch ...Qxa2/...Qa1#.

## Opponents
- Stockfish 19 (g6,g17,g20,g24,g25,g26): ~0s/move; punishes every loose piece and any piece/queen on an attacked square or line. Solid known lines only.
- Sonnet 5.5 (g7,g8,g12,g15,g16,g19,g23): banks clock; takes free/attacked units at once (Nxa1, Rxa5, dxe5). Keep every piece on unattacked squares.
- GPT-6.1 Sol (g9,g10,g13,g18,g21,g22): solid closed RL; punishes queens on his lines; captures I make must survive his recapture.

## Principles
- Scan ALL attackers of every final destination; queen/knight safety before material.
- The 5s scan on the final move beats any long think; routine <=15s, no move >30s from move 10.
- After a blunder: defend loose pieces, trade down, play 5-15s; no pawn grabs while down material.
