# Pre-move scan & blunder catalogue (g1-g42)

## Scan (EVERY move, 5s) - on the FINAL move
1. Destination: which enemy PAWN, KNIGHT, BISHOP, KING, QUEEN, ROOK attacks it? Attacked+undefended -> reject. Lines: d3/c2-B hits g6+h7; Qf3 hits f5; c6-PAWN covers d5; Rc5 covers d5 (g42).
2. What the move OPENS: a vacating piece/pawn uncovers his line/file onto my piece (g38 19.Bb3 uncovered c2->b3, Rc1 hit Qc7; g39 15.Nf4 opened the d-file, 16...Qd4#; g42 14.Nxd5 cxd5 vacated c6, Rfc8 hit Bc5).
3. MY attacked piece: save/trade/defend it NOW (g30,g42) before any side move or grab; g42 16.h3?? ignored Rxc5. A moving piece or PAWN stops defending its old squares (g30); re-scan after every enemy move/check.
4. Pawn hits my KNIGHT -> safe flight, never grab (g34). Never a knight to an undefended square in a bad position (g40 19...Nxe4?? 20.Bxe4) or where his pawn captures it (g40 20...Nc6?? 21.dxc6). Pawn hits my QUEEN -> retreat, not capture (g37 28.Qxc3?? bxc3). Knight captures: count every recapturer, even a check (g6,g19,g22,g23).
5. Queen move/capture: list ALL attackers AND defenders incl. rooks on the destination's rank/file and PAWNS (g37,g39; g42 17.Qxd5?? Rxd5). Never Qx a defended rook (g35); no Q for R/B/N/P (g18,g35-g42); never Qxp where a rook hits (g36 14...Qxa4?? Rxa4!). Trade offer needs a legal recapturer (g34).
6. Qc7/Qc8 with his Be3+Rc1: retreat ...Qb8/...Qd8 before the file opens (g35,g38). Rook hits my queen -> retreat, never grab (g35,g41).
7. Knight forks: cover BOTH targets or vacate one (g23,g27); never step onto a forker's square; 2v2 = LAST recapturer lands there (g27).
8. Pinned Nd7 (Ba4, Re8): moving loses the exchange; unpin ...Rb8 (g15).
9. Mate nets: Qa1# (g6); Qd4# down an open d-file onto Kf2 (g39); Qxh7# with his Ng5+Nf5+Qh5: ...g6 BEFORE his queen arrives (g40); Qxh7+ with Qh5+Bd3: ...g6, not ...Qf6?? (g25); Qf2#/Rb1#/Qg8# (g10,g21,g24); his Q/R on the 8th, no luft: Re8#/Qc8#/Qd8# (g14..g41); Qe1+/Qxd1# vs undefended Rd1 (g42).
10. Pawn pushes: never onto a defended piece (g12), a knight-attacked square (g16), an enemy pawn's attack (g24), a bishop's capture (g25), where a queen gains tempo (g19), while it guards my piece (g30), or into cxb4 (g40).
11. Pawn grabs: never a pawn a recapturer defends (g18,g23,g29,g34); never down material or while a piece hangs.
12. Legality BEFORE sending (3 invalid = forfeit, g34): trace the path square by square (g39 Qxd8 blocked by Nd5); knight/bishop geometry (g28,g34,g36).
13. A recapture I cannot make is no defense (g30 13...Bxe6); a rook/pawn coming to an open file at my loose piece is an emergency (g42).

## Blunder catalogue (losses g1-g42)
g1 Nxb2, g2 Nxc2, g3 Bxd4/Qxe4, g4 Bxd2/Re8, g5 Nb3, g6 Qa1#, g8 Bf5/Qd7, g10 Qc2 Rxc2, g11 Bf5/Qxb4, g12 Qxd5, g13 Qh6/Qh8+, g14 Qe1+, g15 Nb6/Bxd5, g16 Nc4/Nxe4, g17 Qd6, g18 Qd5/Rxe5, g19 Nd7/Qxd5/Rc8#, g20 Nd7, g21 Rb1#, g22 Nef5/Qxc4, g23 Nb3/Bxa5, g24 Bg4, g25 Qf6/Qg6, g26 Bf5/Qd7, g27 Rc2/Re2, g28 Qxc4/Nd4, g29 Rd8, g30 Bxe6/f4, g31 Re7/Qd6, g32 Bxc3/Rxd3, g33 Be3/Qd2/Bd4, g34 Bxd4/Qe3 + 3 illegal, g35 Qxc1??, g36 Qxa4??, g37 Qxc3??, g38 Nc4/Nb6->Rxc7, g39 Bxe5/Qxd5/Nf4->Qd4#, g40 Nxe4/Nc6/Qd7->Qxh7#, g41 Rfd8->Bxa5, g42 Nxd5/h3/Qxd5??

## Patterns
- Queen on a square his queen/slider/rook/PAWN covers (g10..g42); d5 the classic trap (c6-pawn g39, Rc5 g42).
- Knight to an undefended square or one a pawn captures, esp. down material (g40 e4/c6; g24 hxg4).
- Tempo hits (rook/pawn/Be3 at my queen): retreat, never grab (g35,g37,g38,g41); a rook to my loose bishop: save it (g42).
- No luft + enemy Q/R on the 8th -> back-rank mate (g14..g32); Qxh7# with his Ng5 (g40); Qe1+/Qxd1# (g42).
- Lost position: no 'active' piece to an undefended square (g39,g40); defend/trade 5-15s; never push a pawn that guards a piece (g30).
- Illegal tries (g25,g28,g30,g33,g34,g36,g38,g39) = forfeit risk at 3: trace path/geometry before sending.
