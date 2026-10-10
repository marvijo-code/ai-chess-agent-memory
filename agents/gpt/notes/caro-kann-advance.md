# Caro-Kann: defensive coverage, captures and conversion

## T20 final: Black vs Stockfish 19, mate loss
Advance: e4 c6 d4 d5 e5 Bf5 h4 h5 Bd3 Bxd3 Qxd3 e6 Nf3 Nd7 c3 Ne7 Na3 Nf5 Nc2 c5 Ne3 Nxe3 Bxe3 Be7 g3 O-O Kf1 cxd4 cxd4 Rc8 Kg2 f6 Rac1 fxe5 Nxe5 Nxe5 dxe5! Rxc1 Rxc1! Qd7.
- No opening refutation or verified best replacement supplied. The opening and central exchanges did not justify later tactical errors.
- Bxa7 Ra8 Bb6 Rxa2 Rc7 Qe8! Bd4 b5 Rb7 b4?! f4? Qf7?? Rb8+ Bf8 Qc2?! Qxf4?! gxf4.
- Qe8 guarded Be7 and b8 through empty d8/c8. Qf7 preserved e6's guard but abandoned b8. Before moving the queen, list defensive squares LOST and test enemy rook checks, not just the new queen's targets.
- Rb8+ forced the played Bf8 interposition. Qf7 defended Bf8, but Rb8-f8-g8 absolutely pinned it. A defended interposer can still leave the position tied down.
- Qxf4 directly lost Q for P: White's pawn was on g3 and could capture f4. Calling f4 undefended ignored an ordinary pawn diagonal. The mild supplied mark does not override gxf4 on the board. White's f4/Qc2 errors supplied no verified saving line for Black.
- Kf7 released the pin, then Rb7+ Be7 Rxe7+ Kxe7 left White Q+B against R, with pawns. This liquidation did not repair the queen loss.
- Later Rb5 was unsupported. Qe2+ Kc3 Qxb5 used e2-d3-c4-b5; Kc3 guards b4, not b5. King proximity does not establish rook protection.
- No invalid attempts; finished 10:29. Qxf4 took 71 seconds with 12:43 before the move. This was a capture-scan failure, not clock shortage. Keep critical thinks bounded and reserve time for the final-board pawn scan.

## T20 semifinal 2 Armageddon: Black vs Sonnet, mate win
Classical: dxe4 Nxe4 Bf5 Ng3 Bg6 h4 h6 h5 Bh7 Bd3 Bxd3 Qxd3 e6 Bf4 Nd7 O-O-O Ngf6 Nf3 Be7 Ne5 Nxe5 Bxe5 O-O Ne4 Nxe4 Qxe4 Qd5 Qxd5 cxd5.
- h6 supplies h7 and controls g5. Exchanges reduced attacking material; cxd5 opened the c-file. No opening advantage established.
- Rh3 Rac8 Rg3 f6! Bf4 Kf7 removed Be5's attack and g7's absolute pin. Rfd8/Bd6/Bxd6/Rxd6 reached an equal-material two-rook ending.
- f5/Kf6/a6/Rf7/Ke7 had adverse marks without verified replacements/refutations. Rg6 and Re3 doubled attacks on e6; Rc6 added a second guard beside Ke7.
- Rxh6?? gxh6! won R for P. Unpinned g7 controls h6. The eventual win does not validate earlier defense.
- Answer pawn attacks on Rc6 before collecting h5: b5 axb5 axb5 Rc4; g3 Rxh5. Later Rxb6+ took the passer; Kc6 supported Rb6.
- With White Ka4/Rf3, c3 blocked the rook's route to a3. Rh1 threatened Ra1#; c4 cleared the route: Ra1+ Ra3 Rxa3+ Kxa3 dxc4. A forced interposition enabled safe liquidation.
- c3/c2/c1=Q followed; Qb2# used Rb6's support. Finished 5:40 from 7:30 plus increment; some routine conversion moves still took 26-33 seconds.

## T20 round 2: Black vs DeepSeek, Classical, mate win
- Same setup with Nf3 before h5, then Bd3 Bxd3 Qxd3 e6 O-O Ngf6 c4 Be7. Bg5?? hxg5! Nxg5 loses B for P.
- Nxh5 Nxh5 Rxh5? retained extra B but was marked; no verified replacement supplied. Nxh5 cleared Be7-f6-g5. Qh3? Rxh3 gxh3 Bxg5 exchanged R for Q and removed White's last minor.
- Bf6/Bxd4+/Qf6/O-O-O supplied Rd8's guard of Bd4. Against Kg3/Re4: Nc5 f5 Nxe4+ Kf3 Qxf5+ Kg2 Qf2+ Kh1 Ng3#. Bd4 guards f2; Qf2 guards g3 and covers g1/g2/h2.

## T19 final: Advance, forcing clearance
- Bf5/Nd7/Ne7-f5/c5/Be7/O-O; cxd4/Nxd4/Rac8 pressured Kc1, f6/fxe5 opened f-file.
- Qxe5 Rxf2 Qxd5??: e6 screened Qe7 from Re1. Rxc3+ Kb1 Rxb2+ Kxb2 Qxa3+ Kb1 exd5 relocated Q with check before recapturing. bxc3 permits Qxa3+ Kb1 Qb2#, supported by Rf2.

## Earlier recurring failures
- Re6's departure opens Qd5-e6-f7-g8. Rad8?? exd8=N: a rook fork does not stop capture-promotion.
- Kh1 can release Nd4's pin: Qe7?? Nxe7+ Rxe7 loses Q for N.
- Ne4+ Ke3 f4+ abandons f5's guard of Ne4: Kxe4. f6 does not defend e4.
- c5 controls d6: Qd6?? cxd6. Qe2 can absolutely pin Ne5 to Ke8; pawn support or attacking a bishop does not release that pin.
