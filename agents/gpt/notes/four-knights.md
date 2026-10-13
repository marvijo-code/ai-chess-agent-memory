# Four Knights: rook control and king escape squares

## Castled opening vs Stockfish 19
5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6.
- Both sides lose both knights and e-pawns; material equal. Qd4/Bg4/Bd6 and queen exchanges repeatedly reached near equality. Distinguish Nd5 BEFORE castling; later tactical losses do not refute the opening.

## T38 round 1: Black vs SF19, c4# loss
- Qd4/Bg4/Bd6/Qxe3 and Rae8/c5/h6/a6/Be6/Rxe6/Rfe8 reached a balanced queenless position. The opening did not lose material. Equal material after the bishop trade did not make the double-rook ending safe.
- White activated Rf5, Kf2/Ke3 and Rg4. My king went to c6 while my pawns on a6/c5 restricted its exits. Evaluate the enemy rook ranks and pawn checks before seeking queenside targets.
- 32...Rh7?! was the only marked Black inaccuracy. It defended g7/h4 but ABANDONED Rh6's control of g6: Rg6+ could previously be met by Rxg6. A defensive retreat can admit a checking invasion. List the entry squares the rook currently denies before moving it. No engine-verified replacement supplied.
- After Rg6+, ...Kb5 attacked Ra4 but allowed c4#. The pawn checked b5 directly, so interposition was impossible. Ra4 covered b4/a5; Rg6 covered b6/c6; my a6/c5 pawns occupied a6/c5. Kxa4 was illegal because b3 guarded Ra4. Kxc4 was illegal because b3/d3 and Ra4 protected c4. Every adjacent square was covered or occupied.
- The warning was TWO active enemy rooks, nearby supporting pawns and my own pawns enclosing K. Enumerate enemy pawn checks and all eight exits BEFORE a king move that attacks material. The rook attack did not force White to save it.
- Zero invalid attempts; finished 12:26. Kf8 took 44 seconds, fxg5 38, Bxf4 41. Time pressure did not cause the loss. Rh7/Kb5 took 12/8; a short explicit flight map was needed, not a longer account of the plan.

## Earlier failures to retain
- T37 Be6?! Bxe6 required fxe6, leaving e6 weak. Rf6 ignored c3 chasing Bb4 and exposing b7. Qd6 did not guard b7/Ra8. Rb8 Qxb8+ lost R because c7 blocked Qd6-b8. Test Qxrook before claiming a queen tempo.
- Qxh4+ lost Q to g3xh4. White later offered Qf8+ to Rxf8, but still had 2R versus R. Count the actual board after a windfall.
- Supported Rg2/h2 threatened promotion, but rook checks drove K to rank 1; Rc2 sealed rank 2 and Rb1# finished. My threat did not stop their checks. Give K an escape route before joining the passer.
- T36 g6 supported f5 and screened Bc2-h7 but abandoned h6. Kingside exchanges gave White active sixth-rank rooks. Kg7 screened Rg8 from Kg1; Kf7+ uncovered check.
- Rdf8 allowed Bh6+ Kh8 Bxf8 Bxf8 Rxc6: the bishop recapture vacated d6 and exposed Bc6. Whole chain cost R+B for B. Audit the recapturer's departure.
- An a-passer forced Rxa1/Kxa1, but White's h-pawn outran Ka1. Later Q versus K repetition was an escape from a lost position, not a fortress.
- Ke5/Bc5 faced d4+, checking K and attacking B. Kd5 dxc5 Kxc5 lost B for P; e3 prevented Kxd4. Inspect checking pawn pushes before centralizing K.
- Bc3/Rd4 screened Bc3-e5 against Ke5. Rxg4+ vacated d4 and discovered bishop check; Rg8 could not recapture on g4. Rear-rook support does not prove legality.
- Re6/Re8 do not guard f5; Kf7 can screen Rf8-f5. Ke7 can block Re8-e6 while abandoning Re6's king guard. King moves change support AND screens.
- b8=Q+ can discover Ra7-d7, preventing Rxb8. Include en passant beside advanced pawns. Rf4 Bd2xf4 Bxf4 loses the exchange; Kxh6 abandons Bf6.
