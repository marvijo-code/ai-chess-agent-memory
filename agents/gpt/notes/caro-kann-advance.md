# Caro-Kann: pawn controls, forcing clearance and mate

## T20 round 2: Black vs DeepSeek, Classical, mate win
1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.Nf3 Nd7 8.h5 Bh7! 9.Bd3 Bxd3 10.Qxd3 e6 11.O-O Ngf6 12.c4 Be7.
- ...h6 prepares the bishop's h7 retreat while retaining control of g5. Use ...Nd7/...Ngf6/...Be7 to develop. This game supplies a usable setup, not a forced opening advantage.
13.Bg5?? hxg5! 14.Nxg5 Nxh5 15.Nxh5 Rxh5? 16.Qh3? Rxh3 17.gxh3 Bxg5.
- Bg5 landed on h6's pawn-capture square. Nxg5 recovered a pawn, not the lost bishop. After the knight exchange on h5, Black still had an extra bishop; White's claims of balanced material were false.
- ...Nxh5 moved Nf6 off Be7-f6-g5. ...Rxh5 cleared h8 and attacked Ng5; h7/h6 were empty. Qh3 landed on that rook's clear file. After the rook-for-queen exchange, ...Bxg5 took White's last minor.
- ...Rxh5 was marked a mistake. The opponent's queen error does not validate it; no verified best replacement or refutation supplied. Do not memorize the capture sequence as forced or best.
18.f4 Bf6 19.Rfe1 Bxd4+ 20.Kg2 Qf6 21.Kg3 O-O-O 22.Re4 Nc5 23.f5 Nxe4+ 24.Kf3 Qxf5+ 25.Kg2 Qf2+ 26.Kh1 Ng3#.
- Retreat the attacked bishop, take d4 with check, then castle to connect king safety with Rd8's defense of Bd4. Nc5 attacked Re4 while the bishop stayed defended.
- Kf3 attacked Ne4, but ...Qxf5+ took a pawn with tempo and guarded e4. ...Qf2+ was protected by Bd4-e3-f2 and forced Kh1. ...Ng3# used Qf2's guard of g3 and control of g1/g2/h2; knight check cannot be blocked.
- No invalid attempts; finished with 14:18. Opening moves took 3-7 seconds, but ...Nxh5 took 49. DeepSeek spent 34-46 seconds on several material-losing moves; longer thought did not fix capture accounting.

## T19 final: Black vs depth-5 Stockfish, Advance, mate win
Bf5 outside chain; a3 e6 h4 h5 Bd3 Bxd3 Qxd3 Nd7 c3 Ne7 Nd2 Nf5 Ndf3 c5 Ne2 Be7 Bg5 O-O O-O-O cxd4 Bxe7 Qxe7 Nexd4 Nxd4 Qxd4 Rac8 Qe3 f6 Rhe1 fxe5 Nxe5 Nxe5 Qxe5 Rxf2.
- ...cxd4/Nxd4 opened c-file and pinned c3 to Kc1. ...f6/fxe5/knight exchange opened f-file. Coordinate invasion on both files.
21.Qxd5?? Rxc3+ 22.Kb1 Rxb2+ 23.Kxb2 Qxa3+ 24.Kb1 exd5.
- e6 screened Qe7 from Re1: immediate ...exd5 exposed my queen. Checks relocated it to a3 BEFORE the pawn recapture.
- 22.bxc3 permits Qxa3+ Kb1 Qb2#, supported by Rf2, which also excludes c2/d2. Calculate acceptance and refusal of sacrifices.
- Actual ...Rxb2+ cleared b2; ...Qxa3+ removed a3. Rc3 protected Qa3 and controlled c-file. Result: Q+R against two rooks.
- Qa3 supported Rxe3; Rb3+/Qb2+/Qb1+ drove king to e2. Rb2 pinned Rd2 with Qb1 guarding b2; Rxb2 Qxb2+ simplified. Kg6-f5-g4xg3 supported Qg2#.
- Shallow Stockfish blundered; do not assume infallibility. Finished 9:34; forcing moves took 51-54 seconds, routine conversion 26-35. Tighten budgets.

## Earlier promotion, destination and pin failures
- T12 Advance: ...g6 hxg6 fxg6 removed f7's control of e6. e6/e7 then attacked Qd7/Rf8. Calculate central breakthroughs before shelter pushes.
- Bg5 Nxc2 Re6 Nxa1 Qxd5? Rad8?? exd8=N Qc7 Rxe8+ Kg7 Rg8#. Forking a rook did not stop capture-promotion. Re6's departure opened Qd5-e6-f7-g8; Nd8 controlled f7. Ample clock, missed geometry.
- After Kh1, Bc5 no longer pinned Nd4. Qg4 Qe7?? Nxe7+ Rxe7 lost Q for N. A recapture does not make a knight-attacked queen square safe.
- Ne4+ Ke3 f4+ abandoned f5's guard of Ne4, allowing Kxe4; f6 did not defend e4.
- c5 attacks b6/d6: Qd6?? cxd6 loses Q. Qe2 can absolutely pin Ne5 to Ke8; ...f6 support or ...d4 attacking B does not release that pin.
