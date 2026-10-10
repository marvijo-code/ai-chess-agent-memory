# Caro-Kann: clearance, defensive coverage and conversion

## T22 round 1: Black vs Sonnet, mate win
Classical: dxe4 Nxe4 Bf5 Ng3 Bg6 h4 h6 h5 Bh7! Bd3 Bxd3 Qxd3! e6; Bf4 Nd7 O-O-O Ngf6 Nf3 Be7 Ne5 Nxe5 Bxe5 O-O Kb1 c5 Bxf6 Bxf6! dxc5 Qc7 b4 a5 a3?? axb4 axb4 Ra1#.
- h6 supplies h7; Bh7 and Bxf6 were marked the only good moves. Do not confuse this successful setup with a forced opening advantage.
- Bxf6 preserved the pawn structure and placed the bishop on f6-e5-d4-c3-b2-a1. White's dxc5 removed d4's screen; b4 removed b2's screen. The bishop then protected a1 and controlled b2 before the a-file opened.
- Qc7 pressured c5. ...a5 undermined its b4 defender while threatening to open Ra8's file toward Kb1. Sonnet spent 58/61 seconds on b4/a3 to retain the extra pawn but overlooked the mating geometry.
- After ...axb4, axb4 removed White's last a-file blocker. Ra1# was protected by Bf6; Kxa1 was illegal, b2 was bishop-controlled, a2/c1 rook-controlled, and c2 occupied by White's pawn. An adjacent rook check permits no interposition. Rd1 could not capture a1 through its own king on b1.
- Scan the board AFTER the intended pawn recapture. Supporting a pawn chain can clear a bishop diagonal and a rook file simultaneously. No engine-best replacement for a3 supplied; do not claim a forced win before the error.
- No invalid attempts; finished 15:23. Book mostly 3-6 seconds, central decisions 12-13, Qc7/a5/axb4 26/27/23, mate four. Spend time on concrete replies and keep routine development short.

## T21 round 2: Black vs Stockfish, mate loss
h4 h5 Bd3 Bxd3 Qxd3 e6 Nf3 Ne7 Bg5! Nf5?? Bxd8 Kxd8.
- Bg5 created g5-f6-e7-d8 against Qd8. Ne7 was the sole screen; Nf5 lost Q for B. Preserve/replace the screen, move Q safely or remove B before following Ne7-f5. No verified best replacement supplied.
- Nf5 took six seconds with over 15 minutes left: an automatic plan skipped the latest attack. Only this move was marked; later pawn gains did not establish compensation.
- Finish: Rbc8 Rd2 Nc4 Rd7+ Kb8 Qxa7#. Rd7 protected a7 and controlled b7/c7; Qa7 covered a8/b8/b7, Rc8 occupied c8. Test protected queen entries before retreating behind active rooks.

## T20 final: Black vs Stockfish, mate loss
Advance development, cxd4/Rc8/f6/fxe5; Nxe5 Nxe5 dxe5 Rxc1 Rxc1 Qd7. Later Qe8 Bd4 b5 Rb7 b4 f4 Qf7?? Rb8+ Bf8 Qc2 Qxf4?? gxf4.
- Qe8 guarded Be7 AND b8 via d8/c8. Qf7 abandoned b8; Bf8 was absolutely pinned to Kg8. List defensive coverage lost before moving Q.
- Qxf4 lost Q to g3's pawn despite a mild mark and 71 seconds thinking. Reserve the final scan for pawn captures and back-rank checks.
- Kf7 released the pin; Rb7+ Be7 Rxe7+ Kxe7 left Q+B against R. Later Kc3 did not protect Rb5: kings on c3 guard b4, not b5.

## T20 Armageddon: Black vs Sonnet, mate win
Classical setup; Qd5 Qxd5 cxd5, Rac8/f6 displaced Be5, Kf7 released g7's pin. Rfd8/Bd6/Bxd6/Rxd6 reached equal two-rook play.
- Rc6 added a second guard of e6 beside Ke7 against Rg6/Re3. Rxh6?? gxh6 won R for P; victory does not validate earlier defense.
- Answer attacks on Rc6 before taking h5. With Ka4/Rf3, c3 blocked Ra3. Rh1 threatened Ra1#; c4 cleared Ra3: Ra1+ Ra3 Rxa3+ Kxa3 dxc4, then c3/c2/c1=Q and Rb6-supported Qb2#.

## Other reusable tactics
- Classical vs DeepSeek: Bg5?? hxg5; Nxh5 Nxh5 Rxh5 clears Be7-f6-g5. Qh3? Rxh3 gxh3 Bxg5 wins Q and removes the last minor. Bd4 guards f2; Qf2 guards g3 for Ng3#.
- Advance: e6 screens Qe7 from Re1. Rxc3+ Kb1 Rxb2+ Kxb2 Qxa3+ Kb1 exd5 moves Q with check before recapturing; bxc3 permits Qxa3+ Kb1 Qb2# with Rf2 support.
- Re6's departure opens Qd5-e6-f7-g8. Rad8?? exd8=N ignores capture-promotion. Kh1 releases Nd4's pin: Qe7?? Nxe7+.
- Ne4+ Ke3 f4+ abandons Ne4's f5 guard: Kxe4. c5 controls d6: Qd6?? cxd6. Pawn support or attacking B does not release a knight pinned to its king.
