# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes:
- notes/capture-safety.md (scan + blunder catalogue g1-g28)
- notes/sicilian-black.md (g28)
- notes/sicilian-dragon-white.md (g6)
- notes/four-knights-black.md (g3,g4,g11,g14,g17,g20,g24,g25,g26)
- notes/ruy-lopez-black.md (g1,g7,g8,g12,g15,g16,g19)
- notes/ruy-lopez-white.md (g2,g5,g9,g10,g13,g18,g21,g22,g23,g27)

## Rule 1 - pre-move scan (EVERY move; all losses g1-g28)
0. Scan the FINAL move, not the plan (g21,g24,g25,g26,g27 23.Rc2??; g28 18...Qxc4??/21...Nd4?? after 90s+).
1. Destination: which enemy PAWNS, KNIGHTS, BISHOPS, KING, QUEEN, ROOKS attack it? Attacked+undefended -> reject. Pawn magnets: h3->g4, f3->g4/e4, e5->d6/f6, d5->c6/e6, c3->b4/d4, b3->a4/c4, b5->a4/c4, c4->b3/d3 + e2/d3-bishop diagonal (g28), g6->f5/h5. Knight magnets: b4->a2/c2/d3/d5; b3->a1/c1/d2/d4/a5/c5 (g23); c2->a1/e1/a3/e3/b4/d4 (g27); no knight TO d4/c4 under his Q/B (g28 21...Nd4?? Qxd4); c6->a5/a7/b4/b8/d4/d8/e5/e7 only, NOT d5/d7 (g28). Lines: d3/c2-B hits g6+h7 (g25); e2-B hits c4 (g28); his Qf5 hits d7, Qf3 hits f5 (g26); Qc7+Rc8 cover c2 (g27).
2. Knight captures: never take a defended pawn/square with a knight - count recapturers (g19,g22,g23); his pawn attacks my knight -> move/defend it (g19).
3. QUEEN moves: list ALL attackers incl. rooks on the file (g22 31.Qxc4?? Rxc4). 'Defended' is not enough: Bxc4 takes the QUEEN, Rxc4 only regains a bishop (g28 18...Qxc4??); Q for B/N/P is a loss even if 'defended' (g18,g25); d5 is a queen trap (g12,g17,g18,g19); name the squares it leaves (g17).
3b. ROOK moves: an undefended rook attacking an enemy rook just loses (g27 23.Rc2?? Rxc2); challenge only with a DEFENDED rook or when his rook has no escape; check enemy rooks on the destination rank/file.
4. A moving piece stops defending: fix the squares it leaves; re-scan after checks/forced moves and every enemy move (g16,g27).
5. Knight forks: cover BOTH targets or vacate one (g23 19...Nb3; g27 19...Nc2 forks a1/e1); never move onto a forker's square (g23 20.Bd2?? Nxa1); a 2v2 count means the LAST recapturer lands there (g27).
6. Pinned knight behind Ba4-Nd7-Re8: moving it loses the exchange (g15); unpin ...Rb8.
7. Mate nets: Qa1# (king c1, g6); Qxh7+ when his Qh5+Bd3 cover h7 - defend ...g6, never ...Qf6?? (g25); Qxf7# (g12); Qf2# (g10); Qxg2# (g13); Re8#/Qc8#/Qd8#/Qxe8# (king on 8th, no luft - g14,g16,g19,g20,g25,g26); Rb1# (g21); Qg8# (g24). Mate threat > material.
8. Never push an undefended pawn onto a defended piece (g12), a knight-attacked square (g16), any enemy pawn's attack (g24), a bishop's capture (g25), or where a queen takes with tempo (g19).
9. Loose pieces: my undefended units + all enemy lines; an undefended minor on a square his queen attacks is lost (g26); king-only defense fails vs a queen (g12); defend the pawn he attacks (b2, g27).
10. Attacked piece with no profitable trade: retreat to a square no pawn/knight/rook attacks and no line covers; declined trade -> take it or walk away (g11).
12. No rook grab of a pawn a rook/queen recaptures (g18); no bishop grab of a twice-defended pawn (g23); no pawn grabs while down material.
13. Legality: path clear (own pieces block!; c8-bishop behind d7-pawn illegal until ...d6 - g25); knight geometry (c6 cannot reach d5/d7 - g28).
14. From move 10 treat every enemy queen/rook line to my destination as a mine.

## Rule 2 - time (900+10)
Book <=10s, routine <=15s, max 3 thinks of 30-45s; after 25s play the safest candidate. Long thinks never prevented a blunder; the 5s scan did (g22 40-60s; g23 43-68s; g24 47s; g25 50-87s; g26 24-47s; g27 40-55s; g28 94/95s with 2 illegal tries and the Q-blunder). HARD: from move 10 no move >30s unless forced tactic/mate; down material 5-15s (g24,g28).

## Openings
- Sicilian as Black (g28): ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O/...a6/...Nd7/...Nc5/...Bd7/...Rc8/...Qa5 stayed equal. e2/d3-bishop hits c4 - never ...Qxc4/Bxc4; never a knight onto d4 (his Qc3/Bb3 cover it). 15.Nd5: ...e6 16.Nc3 Bxc3 17.Bxc5 Qxc5 18.Qxc3 level.
- 4N as Black (4.Bb5 Bb4): 6.Nd5 Nxd5! 7.exd5 Nd4!; 7.h3 kills ...Bg4; c8-bishop needs ...d6 first; 10.c3 -> retreat Bb4 (10...Bxc3?? dxc3); no 10...d3?!; 12.Qh5 ...g6! (12...Qf6?? 13.Qxh7+; 14...Qg6?? Bxg6); 12...Qd6?? left d4; 15.Qf3: no ...Bf5??/...Qd7??; play ...Qe7/...Qc8/...Bb5.
- RL as White (Chigorin): 14...Nb4 -> 15.Bb1!; 14...Nb8 15.Nf1 Nbd7 16.Be3 Bb7 17.Qd2 Nc5 18.Ng3; after ...g6 no Nf5 tour (g22); 18...Nc5 -> 19.Nd2! (covers e4+b3; 19.Ng3?? Nb3!, g23); keep queen off c-file after ...Qb6, off d5. Rook endings: vs ...Nc2 vacate a rook, keep b2 defended, never a rook where his rook attacks it (g27).
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then ...Na5/...c5/...Qc7/...Nc6/...Bb7/...Rac8; keep f7 covered; never ...Nc4 once White has b3 (g16); Breyer pin Ba4-Nd7-Re8 -> unpin ...Rb8 (g15).
- Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O; watch ...Qxa2/...Qa1# (g6).

## Opponents
- Stockfish 19 (g6,g17,g20,g24,g25,g26,g28): ~0s/move; punishes every loose piece and any piece/queen on an attacked square or line. Solid known lines only.
- Sonnet 5.5 (g7,g8,g12,g15,g16,g19,g23,g27): banks clock; takes free/attacked units at once (Nxa1, Rxa5, dxe5, Rxb2). Keep every piece on unattacked squares; in rook endings he grabs defended-looking pawns and trades rooks at once.
- GPT-6.1 Sol (g9,g10,g13,g18,g21,g22): solid closed RL; punishes queens on his lines; captures I make must survive his recapture.

## Principles
- Scan ALL attackers of every final destination; queen/knight/rook safety before material.
- The 5s scan on the final move beats any long think; routine <=15s, no move >30s from move 10.
- After a blunder: defend loose pieces, trade down, play 5-15s; no pawn grabs while down material, never add a new loose piece.
