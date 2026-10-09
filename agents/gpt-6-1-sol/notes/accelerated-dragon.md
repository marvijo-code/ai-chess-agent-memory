# Accelerated Dragon: captures before attacking plans

## T10 semifinal 2 Armageddon: White vs Stockfish 19, mate loss
1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.f3 Bd7 9.Qd2 a6 10.O-O-O b5 11.Bb3 h5 12.h4 Na5 13.Kb1 Rc8.
- This game entered a Dragon structure with ...d6. Familiar development was quick, but the pawn attack needs concrete capture calculations. No best replacement for the marked inaccuracy was supplied.

### Pawn attack and recapture geometry
14.g4?! hxg4 15.h5 Nxb3 16.axb3 Rxh5 17.Rxh5 Nxh5 18.fxg4 Bxg4! 19.Rg1 Nf6.
- The rook exchange ended with Nf6xh5, not g6xh5. Black's g6 pawn remained. Reconstruct pieces after each recapture instead of assuming the intended attacking story occurred.
- fxg4 attacked Nh5, but Bd7 could capture g4 along d7-e6-f5-g4. Bxg4 also attacked Rd1 through empty f3/e2, making White respond to a counterthreat.
- White lost g/h/f pawns while Black lost only h: two pawns down after the liquidation. The knight attack did not force a retreat.

### Queen and rook destinations
20.Nd5 Nxd5 21.exd5 Qd7 22.Bh6 Be5 23.Nc6 Bf3 24.Qg5 Bf6 25.Qg3 Bxd5 26.Nb4 Be4 27.Qe3 Qe6 28.Rg4?? Qxg4.
- d5 supported Nc6. Bxd5 removed that support and opened Rc8's line to c6; Nb4 moved the exposed knight.
- Qe6 attacked g4 directly through f5. Rg4 added pressure on Be4 but put an undefended rook on that diagonal. Name every enemy capture of a proposed rook destination before claiming it forces a reply.
- Qg3's attack on Bf3 did not force retreat: Bxd5 captured a central pawn and attacked the knight indirectly.

### Track both e-pawns
After 34.Bd4 Qh1+ 35.Ka2 Qa8+ 36.Na3 Be5 37.Bxe5+ dxe5, White played 38.Qd6?? exd6.
- The pawn now on e5 came from d6. Black's original e7 pawn was still on e7 and captured the queen on d6. Targeting e5 overlooked a different pawn's immediate capture.
- Rg4 and Qd6 had no adverse viewer marks despite losing rook and queen outright. Sparse annotations do not replace board verification.
- White had 5:40 after Rg4, 3:11 after Qd6, and 3:58 at mate. Repeated 20-41-second choices missed direct captures; time shortage did not cause these losses. Armageddon win requirements do not justify sacrifices without calculated compensation.

## T10 semifinal 2 game 1: Black, repetition escape
1.e4 c5 2.Nf3 Nc6 3.Nc3 g6 4.d4 cxd4 5.Nxd4 Bg7 6.Be3 Nf6 7.Bc4 O-O 8.O-O Nxe4 9.Nxc6 bxc6 10.Nxe4 d5! 11.Bd3 dxe4! 12.Bxe4.
- The central fork recovered the knight. Both sides lost both knights and two pawns; material was equal. Calculate the complete liquidation.
- ...Qb6?! Qxb6 axb6 opened the a-file but exposed b6; no best replacement was supplied.
- ...Rb7 a5?? Bxe4 Rxe4 Rxb6 won a bishop because axb6 initially allowed Rxa1+ Re1 Rxe1#. This back-rank tactic depended on exact rook locations.
- After White relocated both rooks to d8/d4, 29...Kg7?? allowed axb6 Rxb6, losing a rook for a pawn. The a5 pawn attacked Rb6; the earlier mating sequence could not be assumed to persist.
- ...c5 Rf4! cxb4 Rdxf7+ Kg8 Rxf8+ captured Bf8. Rf4 protected f8 along the file, making Kxf8 illegal. A pawn attack on one rook did not stop the doubled-rook invasion.
- White later retained king and g/h pawns against a bare king but repeated. This depth-4 conversion failure was not a theoretical draw. Many routine moves consumed 25-50 seconds despite ample time.
