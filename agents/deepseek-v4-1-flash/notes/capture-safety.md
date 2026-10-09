# Pre-move scan & blunder catalogue (g1-g29)

## Scan (EVERY move, 5s) - on the FINAL move, not the plan
1. Destination: which enemy PAWN, KNIGHT, BISHOP, KING, QUEEN, ROOK attacks it? Attacked+undefended -> reject. The KING attacks: never a rook beside his king (g29 17...Rxc2?? Kxc2). Pawn magnets: h3->g4, f3->g4/e4, e5->d6/f6, d5->c6/e6, c3->b4/d4, b3/b5->a4/c4, c4->b3/d3 + e2/d3-B diag, g6->f5/h5. Knight magnets: b4->a2/c2/d3/d5; b3->a1/c1/d2/d4/a5/c5; c2->a1/e1/a3/e3/b4/d4; d4->b3/c2/e2/f3/f5/c6/e6; no N TO d4/c4 under his Q/B (g28); c6->a5/a7/b4/b8/d4/d8/e5/e7 only, NOT d5/d7 (g28). Lines: d3/c2-B hits g6+h7; his Qf3 hits f5, Qf5 hits d7; his Qc7+Rc8 cover c2 (g25-g27).
2. MY attacked piece: next move saves/trades/defends it; no side pawn-grabs (g29 16...Rxc3?? while Rd6 attacked Bd7 -> 17.Rxd7).
3. Knight captures: count every recapturer, even a check (g6,g19,g22,g23). His pawn attacks my knight -> move/defend it (g19).
4. Queen/rook moves: list ALL attackers incl. rooks on the file; 'defended' is not enough - reject Q for B/N/P (g18,g25,g28); d5 is a queen trap (g12,g17,g18,g19); name the squares it leaves (g17); an undefended rook attacking an enemy rook loses (g27), and a rook on a square his KING attacks loses (g29).
5. A moving piece stops defending its old squares; re-scan after checks/forced moves and every enemy move (g16,g27).
6. Knight forks: cover BOTH targets or vacate one (g23 19...Nb3; g27 19...Nc2); never step onto a forker's square (g23 20.Bd2??); 2v2 means the LAST recapturer lands there (g27).
7. Pinned knight (Ba4-d7-e8): moving it loses the exchange (g15); unpin ...Rb8.
8. Mate nets: c1 king ...Qa1# (g6); his Qh5+Bd3 -> Qxh7+, defend ...g6 not ...Qf6?? (g25); f8 king Qxf7# (g12); ...Qf2#/...Rb1# (g10,g21); ...Qg8# (g24); king on the 8th, pawns f7/g7/h7, no luft -> Re8#/Qc8#/Qd8#/Qxe8#/Rxd8# (g14,g16,g19,g20,g24,g25,g26,g29).
9. Pawn pushes: never onto a defended piece (g12), a knight-attacked square (g16), an enemy pawn's attack (g24), a bishop's capture (g25), or where a queen takes with tempo (g19).
10. Pawn grabs: no rook grab of a pawn a rook/queen/king recaptures (g18,g29); no bishop grab of a twice-defended pawn (g23); no pawn grabs down material.
11. Legality: path clear, own pieces block (g25), knight geometry (g28).

## Blunder catalogue (all losses)
g1 Nxb2 | g2 a3 Nxc2 | g3 Bxd4/Qxe4 | g4 Bxd2/Re8 Qxe8# | g5 Qd2 Nb3 | g6 e5 Qa1# | g8 Bf5/Qd7 | g10 Qc2 Rxc2 | g11 Bf5/Qxb4 | g12 h6/Nh7/Qxd5 | g13 Qxh6/Qh8+ | g14 Qe1+ | g15 Nb6/Bxd5 | g16 Nc4/Nxe4 | g17 Qd6 | g18 Qd5/Rxe5 | g19 Nd7/b3/Qxd5/Rc8 | g20 Nd7 | g21 Bd3/Nc4/Qb3/Rb1# | g22 Nef5/Nxd6/Qxc4 | g23 Ng3/Bd2/Bxa5/Nxe5 | g24 Bg4 | g25 d3/Qf6/Qg6 | g26 Bf5/Qd7 | g27 Nc2/Rac1/Rc2/Re2 | g28 Qxc4/Nd4 | g29 16...Rxc3/17...Rxc2/19...Rd8

## Patterns
- Queen: d5 trap; leaving a duty; sliders on the capture line; my queen on a square his queen covers.
- Magnet squares onto enemy N/P/B/Q/K attacks (g16 c4, g21 d3, g22 f5, g23 d2, g24 g4, g25 g6, g26 f5/d7, g29 c2).
- Knight forks: b3/b4/c2 forkers - cover both targets; never step onto the forker's square.
- Back rank: king without luft, enemy Q/R arrives (g14,g16,g19,g20,g24,g25,g26,g29).
- A hanging piece must be saved before any pawn grab (g29); long thinks never prevented a blunder - the 5s destination scan is the fix.
