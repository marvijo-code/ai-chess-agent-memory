# Caro-Kann Advance: forcing moves, destinations and pins

## T19 final: Black vs Stockfish 19, checkmate win
1.e4 c6 2.d4 d5 3.e5 Bf5 4.a3 e6 5.h4 h5 6.Bd3 Bxd3 7.Qxd3 Nd7 8.c3 Ne7 9.Nd2 Nf5 10.Ndf3 c5 11.Ne2 Be7 12.Bg5 O-O 13.O-O-O cxd4 14.Bxe7 Qxe7! 15.Nexd4 Nxd4 16.Qxd4 Rac8 17.Qe3 f6 18.Rhe1 fxe5 19.Nxe5! Nxe5! 20.Qxe5! Rxf2.
- Develop Bf5 outside the chain, restrain h4 with ...h5, and use ...Ne7-f5/c5 against d4. This setup worked here; no forced opening advantage established.
- ...cxd4/Nxd4 opened the c-file and left c3 pinned to Kc1 by Rc8. ...f6/fxe5 and the knight exchange opened the f-file for Rxf2. Coordinate invasion squares on both files.

21.Qxd5?? Rxc3+ 22.Kb1 Rxb2+ 23.Kxb2 Qxa3+ 24.Kb1 exd5.
- Qxd5 left e6 screening Qe7 from Re1. Immediate ...exd5 would expose Qe7. The checking sequence relocated Qe7 to a3 before the pawn captured White's queen. Before recapturing, test checks that remove the exposure with tempo.
- Against 22.bxc3, ...Qxa3+ forces Kb1, then ...Qb2# is protected by Rf2. Rf2 also controls c2/d2, excluding those king escapes. Calculate acceptance AND refusal of a rook sacrifice.
- In the actual line, ...Rxb2+ cleared b2; ...Qxa3+ removed a3. Rc3 protected Qa3 and controlled the c-file, forcing Kb1. Only then ...exd5 completed the payoff: Black Q+R against White's two rooks.

25.Re8+ Kh7 26.Re3 Rxe3 27.Rd2 Rb3+ 28.Kc2 Qb2+ 29.Kd1 Qb1+ 30.Ke2 Rb2 31.Rxb2 Qxb2+ 32.Kf1 Kg6 33.g3 Kf5 34.Kg1 Kg4 35.Kh1 Kxg3 36.Kg1 Qg2#.
- Qa3 protected Rxe3 through b3/c3/d3. Rb3+/Qb2+/Qb1+ drove the king into a pin: Rb2 attacked Rd2 with Ke2 behind it; Qb1 protected b2. The rook exchange left queen versus two pawns.
- Bring the king to support the mating square: Kg6-f5-g4xg3 protected Qg2#. Check escapes and stalemate throughout conversion.
- Stockfish searched depth 5 and blundered Qxd5; opponent strength is no substitute for calculating legal replies. Sparse marks do not prove every unmarked move best.
- No invalid attempts; finished with 9:34. Rxf2/Rxc3+/Rxb2+ took 54/54/51 seconds. Several routine conversion moves took 26-35 seconds. Budget forced continuations more tightly.

## T12 final: Black vs Stockfish, mate loss
Advance 4.Be2 e6 5.Nc3 c5 6.Bb5+ Nc6 7.Bxc6+ bxc6 8.Nge2 cxd4 9.Nxd4 Bc5 10.Nxf5 exf5 11.O-O Ne7 12.Na4 Bb6 13.Re1 O-O 14.Qf3 Qd7 15.h4 c5 16.Nxb6 axb6 17.h5 Nc6 18.Qg3 g6? 19.hxg6 fxg6 20.e6 Qg7 21.Qd6 Nd4 22.e7 Rfe8.
- ...g6 displaced f7's pawn and removed its control of e6. White's e6/e7 advances attacked Qd7/Rf8. Calculate exchanges and central breakthroughs before calling a shelter push safe.
- 23.Bg5 Nxc2 24.Re6 Nxa1 25.Qxd5? Rad8?? 26.exd8=N Qc7 27.Rxe8+ Kg7 28.Rg8#. The rook fork did not stop promotion. Rad8 put a rook on e7's capture-promotion square; its queen attack supplied no tempo.
- Re6's departure opened Qd5-e6-f7-g8, protecting mate; Nd8 controlled f7. Test checks before trying to recover the promoted piece. Had 11:36 after Rad8: safety failure, not clock shortage.

## Earlier destination and pin failures
- T9: after Kh1, Bc5 no longer pinned Nd4. f5 exf5 Nxf5 Qxe5 Bd3 Rae8 Qg4 Qe7?? Nxe7+ Rxe7 lost Q for N. A rook recapture does not make a knight-attacked queen square safe.
- Later ...Ne4+ Ke3 f4+ abandoned f5's protection of Ne4, allowing Kxe4; f6 did not defend e4.
- ...Nc6/Ng6 line: Nxc5 Bxc5 dxc5 Nxe5 Nd4; c5 attacks b6/d6. ...Qd6?? cxd6 loses Q. Qe2 can absolutely pin Ne5 to Ke8; ...f6 support or ...d4 attacking a bishop does not release that pin.
