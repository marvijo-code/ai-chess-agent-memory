# Caro-Kann: screens, defensive coverage and conversion

## T21 round 2: Black vs Stockfish 19, mate loss
1.e4 c6 2.d4 d5 3.e5 Bf5 4.h4 h5 5.Bd3 Bxd3 6.Qxd3 e6 7.Nf3 Ne7 8.Bg5! Nf5?? 9.Bxd8 Kxd8.
- Bg5 created g5-f6-e7-d8 against Qd8, with Ne7 the sole screen. Nf5 was legal but lost Q for B; attacking d4/h4 did not resolve the relative pin. The planned Ne7-f5 route must be conditional on the latest board. Resolve the ray by preserving/replacing its screen, moving Q safely or removing B; no engine-best replacement supplied.
- Only Nf5 was marked. It took six seconds with over 15 minutes left: an automatic opening plan skipped the new bishop attack. Later pawn gains did not establish compensation.
- Finish: ...Rbc8 Rd2 Nc4 Rd7+ Kb8 Qxa7#. Rd7 protected a7 and controlled b7/c7; Qa7 controlled a8/b8/b7, while Rc8 occupied c8. Before retreating behind active rooks, test protected queen entries and seventh-rank coverage.
- No invalid attempts; finished 10:04. Late Rb8/Kb5 took 53/54 seconds despite the decisive material deficit.

## T20 final: Black vs Stockfish 19, mate loss
Advance through ...Nd7/Ne7-f5/Nxe3/Be7/O-O, then ...cxd4/Rc8/f6/fxe5. Nxe5 Nxe5 dxe5 Rxc1 Rxc1 Qd7.
- Bxa7 Ra8 Bb6 Rxa2 Rc7 Qe8 Bd4 b5 Rb7 b4 f4 Qf7?? Rb8+ Bf8 Qc2 Qxf4?? gxf4.
- Qe8 guarded Be7 AND b8 through d8/c8. Qf7 abandoned b8. List defensive squares lost before moving Q; test rook checks before pursuing targets.
- Bf8 interposed but was absolutely pinned by Rb8 to Kg8. Queen support did not release that pin.
- Qxf4 lost Q for P to the pawn on g3. Its mild supplied mark does not override the direct capture. White's errors supplied no verified saving line.
- Kf7 released the pin; Rb7+ Be7 Rxe7+ Kxe7 left White Q+B against R, with pawns. Later Qe2+ Kc3 Qxb5 captured unsupported Rb5: Kc3 guards b4, not b5.
- No opening refutation supplied. Finished 10:29; Qxf4 took 71 seconds with 12:43 left. Reserve the final scan for pawn captures and back-rank checks.

## T20 semifinal 2 Armageddon: Black vs Sonnet, mate win
Classical: dxe4 Nxe4 Bf5 Ng3 Bg6 h4 h6 h5 Bh7 Bd3 Bxd3 Qxd3 e6; ...Nd7/Ngf6/Be7/O-O, then Qd5 Qxd5 cxd5.
- h6 supplies h7 and controls g5. Rac8/f6 drove Be5 off g7; Kf7 removed g7's pin. Rfd8/Bd6/Bxd6/Rxd6 reached equal-material two-rook play.
- Rg6/Re3 doubled attacks on e6; Rc6 added a second guard beside Ke7. Earlier adverse marks had no verified replacements. Rxh6?? gxh6 won R for P; victory does not validate earlier defense.
- Answer attacks on Rc6 before collecting h5: b5 axb5 axb5 Rc4; g3 Rxh5. Rxb6+ removed the passer, supported by Kc6.
- With White Ka4/Rf3, c3 blocked Ra3. Rh1 threatened Ra1#; c4 cleared the route: Ra1+ Ra3 Rxa3+ Kxa3 dxc4. Forced interposition enabled liquidation, then c3/c2/c1=Q and Qb2# supported by Rb6.
- Finished 5:40; routine conversion moves still took 26-33 seconds.

## T20 round 2: Black vs DeepSeek, Classical, mate win
- Same setup with Nf3 before h5, then Bd3 Bxd3 Qxd3 e6 O-O Ngf6 c4 Be7. Bg5?? hxg5 Nxg5 loses B for P.
- Nxh5 Nxh5 Rxh5 retained extra B but was marked; no verified replacement. Nxh5 cleared Be7-f6-g5. Qh3? Rxh3 gxh3 Bxg5 exchanged R for Q and removed White's last minor.
- Bf6/Bxd4+/Qf6/O-O-O supplied Rd8's guard of Bd4. Against Kg3/Re4: Nc5 f5 Nxe4+ Kf3 Qxf5+ Kg2 Qf2+ Kh1 Ng3#. Bd4 guards f2; Qf2 guards g3 and covers g1/g2/h2.

## T19 final: Advance, forcing clearance
- Bf5/Nd7/Ne7-f5/c5/Be7/O-O; cxd4/Nxd4/Rac8 pressured Kc1, f6/fxe5 opened f-file.
- Qxe5 Rxf2 Qxd5??: e6 screened Qe7 from Re1. Rxc3+ Kb1 Rxb2+ Kxb2 Qxa3+ Kb1 exd5 moved Q with check before recapturing. bxc3 permits Qxa3+ Kb1 Qb2#, supported by Rf2.

## Earlier recurring failures
- Re6's departure opens Qd5-e6-f7-g8. Rad8?? exd8=N: a rook fork does not stop capture-promotion.
- Kh1 releases Nd4's pin: Qe7?? Nxe7+ Rxe7 loses Q for N.
- Ne4+ Ke3 f4+ abandons f5's guard of Ne4: Kxe4. f6 does not defend e4.
- c5 controls d6: Qd6?? cxd6. Qe2 can pin Ne5 to Ke8; pawn support or attacking B does not release it.
