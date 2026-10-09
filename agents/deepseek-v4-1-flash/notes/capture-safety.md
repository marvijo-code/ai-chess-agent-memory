# Pre-move scan & blunder catalogue (g1-g43)

## Scan (EVERY move, 5 s) - on the FINAL position
1. Destination: which enemy PAWN, KNIGHT, BISHOP, rook (rank/file), QUEEN, KING attacks it? Attacked+undefended -> reject. Piece moves vacate squares; pawn pushes stop guarding old squares (g30).
2. Open lines: my capture can open a file/diagonal and orphan my unit. g43: 18.axb4 opened the a-file (his a6-knight still blocked it); 19...Nxb4 vacated a6 and won a pawn; my Ra1 was UNDEFENDED (Bb1 blocked Qd1/Re1) -> 20...Rxa1. Fix the rook that move: 20.Rxa8! (then 21.Bxb4 wins his loose knight); never a side move (19.Ba3) or greedy grab (20.Bxb4??) first.
3. My attacked piece: save/trade/defend NOW before any other move (g30,g42,g43).
4. Queen: never on a square his PAWN/slider/rook attacks (g37 28.Qxc3?? bxc3; g43 22.Qa4?? Rxa4 - the a-file rook and b5-pawn both covered a4, no defender). Every queen capture/trade: count ALL recapturers incl. rooks on the destination rank/file and PAWNS (g36 14...Qxa4?? Rxa4; g42 17.Qxd5?? Rxd5). No Q for R/B/N/P (g18,g35-g43).
5. Knight: never an undefended square down material (g40 19...Nxe4??) or one a pawn takes (g40 20...Nc6??); knight captures count recapturers incl. checks (g6,g22).
6. Rook: undefended rook facing his rook loses (g27 23.Rc2??; g43); his rook to an open file at my loose piece = emergency (g42 16.h3??, 16...Rxc5).
7. Forks: cover both targets or vacate one; never step onto a forker's square; 2v2 -> last recapturer (g23,g27).
8. Pinned Nd7 (Ba4, Re8): move loses the exchange; unpin ...Rb8 (g15).
9. Mate nets: Qa1# (g6); Qd4# open d-file/Kf2 (g39); Qxh7# with Ng5/Nf5+Qh5 -> ...g6 BEFORE Qh5 (g40); back-rank Q/R on the 8th no luft (g14..g41); Qe1+/Qxd1# vs loose Rd1 (g42).
10. Pawn pushes: never onto a defended piece (g12), knight-attacked square (g16), a pawn's attack (g24), a bishop's capture (g25), where a queen gains tempo (g19), while it guards my piece (g30), into cxb4 (g40).
11. Pawn grabs/captures: never a pawn a recapturer defends; B-for-P loses (g6,g34,g39,g42; g43 21.Bxd6? Bxd6, 28.Bxb5 Bxb5); never down material or while a piece hangs (g18,g23,g29).
12. Legality BEFORE sending (3 invalid = forfeit, g34): trace the path square by square (g39 Qxd8 blocked); knight/bishop geometry (g28,g34,g36); g43 Qg4 illegal (Nf3 blocks d1-g4).
13. Lost position: no 'active' piece to an undefended square (g39,g40); defend/trade; 5-15 s; long thinks still burned clock and games (g36,g42,g43).

## Blunder catalogue (losses g1-g43)
g1 Nxb2, g2 Nxc2, g3 Bxd4/Qxe4, g4 Bxd2/Re8, g5 Nb3, g6 Qa1#, g8 Bf5/Qd7, g10 Qc2 Rxc2, g11 Bf5/Qxb4, g12 Qxd5, g13 Qh6/Qh8+, g14 Qe1+, g15 Nb6/Bxd5, g16 Nc4/Nxe4, g17 Qd6, g18 Qd5/Rxe5, g19 Nd7/Qxd5/Rc8#, g20 Nd7, g21 Rb1#, g22 Nef5/Qxc4, g23 Nb3/Bxa5, g24 Bg4, g25 Qf6/Qg6, g26 Bf5/Qd7, g27 Rc2/Re2, g28 Qxc4/Nd4, g29 Rd8, g30 Bxe6/f4, g31 Re7/Qd6, g32 Bxc3/Rxd3, g33 Be3/Qd2/Bd4, g34 Bxd4/Qe3+3 illegal, g35 Qxc1??, g36 Qxa4??, g37 Qxc3??, g38 Nc4/Nb6->Rxc7, g39 Bxe5/Qxd5/Nf4->Qd4#, g40 Nxe4/Nc6/Qd7->Qxh7#, g41 Rfd8->Bxa5, g42 Nxd5/h3/Qxd5??, g43 20.Bxb4?? Rxa1, 22.Qa4?? Rxa4.

## Patterns
- Queen on a square his queen/slider/rook/PAWN covers (g10..g43); d5 (c6-pawn g39, Rc5 g42) and a4 (b5-pawn/Ra1 g43) are traps.
- Knight to an undefended or pawn-attacked square, esp. down material (g24,g40).
- Tempo hits (rook/pawn/Be3 at my queen): retreat, never grab (g35,g37,g38,g41); rook at my loose piece: save it (g42,g43).
- My pawn capture opening a file next to my undefended rook (g43): Bb1 blocked two defenders of a1.
- No luft + enemy Q/R on the 8th -> back-rank mate (g14..g32); Qxh7# with Ng5 (g40); Qe1+/Qxd1# (g42).
- Down material: no 'active' piece to an undefended square (g39,g40); B-for-P grabs (g43) and pawn pushes that guard a piece (g30) lose.
- Illegal tries (g25,g28,g30,g33,g34,g36,g38,g39,g43): forfeit at 3; trace path/geometry before sending.
