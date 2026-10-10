# Ruy Lopez Closed - White (Chigorin)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 -> 14.d5 / 14.dxe5 / 14.Nf1.

## g67 vs Sonnet (0-1, Qxg2# m34) - pawn-attacked d4; f5 trade; rejected move sent
14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 17.Nf1 Rfe8 18.Ng3 h6 19.d5 Nb4 20.Bb1 Rac8 21.Nf5?? Bxf5! 22.exf5 Nbxd5! 23.Qd4?! exd4! 24.Nxd4 Nxe3 25.Rxe3 Qb6 26.Rxe7?? Rxe7 27.Nf3 Re2 28.Ne1 Rxe1+ 29.Kh2 Rcc1 30.Kg3 Rxb1 31.Rxb1 Rxb1 32.h4 Rxb2 33.a3 Qxf2+ 34.Kh3 Qxg2#.
- Equal through 20...Rac8 (SF: 7.Bb3!, 13.cxd4! both good). 19.d5: e4-pawn+Q defend, Nc6/Nf6/Nb4 attack. 21.Nf5?? let ...Bxf5! force 22.exf5, which moved d5's e4 defender, and 22...Nbxd5 won the pawn. Before a trade next to my advanced pawn, recount its attackers/defenders and which defender my recapture moves.
- 23.Qd4?!: d4 is attacked by his e5-PAWN and Nc6; 23...exd4 = Q for P. Before ANY queen move list enemy PAWN capture squares (e5->d4/f4) and knight attacks; pawns first.
- 26.Rxe7??: my own note had traced 'only Re8 recaptures, so Rxe7 Rxe7 and I can't retake - Bad' - I sent it anyway: R for B. The move I send must be the one my scan approved; if the trace says bad, send the traced alternative.
- Clock: 29-50 s on quiet m12-26, still two blunders; ends 7:04 vs 13:50. Routine <=15 s; the 5 s scan precedes every queen move and trade.

## g65 - Bxh6 sac: TWO recapturers (Rc2# m34)
Book to 20...Bf8 equal (13.cxd4!, 15.Bb1). h6 guarded TWICE (g7-pawn+Bf8): 21.Bxh6?? gxh6 22.Qxh6?? Bxh6 = B+Q for 2 pawns; count every recapturer and the net BEFORE any sac. 20.Rd1 followed illegal 'Rad1' (Bb1 blocks Ra1). Sonnet took every loose unit (Nxh5, Bxd2, Nxh3+, Nxf2, Qxb2, Qxa1). 39-58 s on quiet m13-22; my 46 s think produced the sac.

## g61 - b4 opens the a-file; queen in front of his rook
Through 20...a4 equal. 21.b4? axb3! e.p. 22.axb3?! Rxa1 (my Bb1 blocked Re1; 22.Nxb3! holds - knight covers a1). 24.Qa3?? Rxa3 (open file, his rook enters first). 25.Nxe5?? dxe5 grab. 29...Qb6: ...Bxf2+ Kh2 Bg3+ Nxg3 Qe3 ...Rb1-Rxc1# - guard f2 or block the diagonal. 40-92 s routine m14-33.

## g60 - queen onto a pawn-attacked square
18.Nxe5?? dxe5 (two guards); 21.Qxa4?? bxa4 = Q for P. No queen next to pawns, no Nxe5 grabs.

## g57 - stale plan; queen with no recapturer
23.Nd4?? exd4 used a pre-trade plan; 24.Qxd4?? Qxd4 (no recapturer); his Rc2/Qxg2# on rank 2. Rewrite tactics after ANY trade.

## Working
- 14...Nb4 -> 15.Bb1!; 14...Nb8: 15.Nf1 Nbd7 16.Be3; ...a5-a4: step the b3-knight away (Nbd2); b4 only if Nxb3 recaptures (g61).
- Keep Nd2 guarded, e3 empty for Be3, no Nc4 while b5 hits c4; no Nxe5 grabs (g60,g61).
- No queen on flank squares touching pawns or on an open line facing his rook; no sac/trade without counting every recapturer and my weak pawn's attackers/defenders.
- Equal Chigorin: improve slowly (Rad1, Bc2, Qe2); don't force; Sonnet banks time - keep routine moves <=15 s.
