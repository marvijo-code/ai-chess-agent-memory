# Caro-Kann: support chains, clearance and exchanges

## T22 final: Black vs Stockfish 19, mate loss
Advance: 4.h4 h5 5.Bd3 Bxd3 6.Qxd3 e6 7.Nf3 Nd7 8.c3 Ne7 9.Na3 Nf5 10.Nc2 Be7 11.g3 O-O 12.Ne3 Nxe3 13.Bxe3 c5 14.Kf1 cxd4 15.Bxd4 Rc8 16.Kg2 Nc5 17.Qe3 Ne4 18.Rad1 f6 19.Rhe1 fxe5 20.Bxe5! Bc5 21.Bd4 Bxd4 22.Rxd4 e5 23.Rdd1 Qf6?? 24.Rxd5!
- The opening remained near level through move 23; the loss does not refute the setup. ...Bc5 attacked Qe3, but Bd4 interposed and offered a bishop exchange: a queen attack need not force a queen move.
- ...e5 moved e6's pawn away from its defense of d5. Qd8 then supplied d5's sole guard through d7/d6; d5 in turn supported Ne4 against Qe3. Qf6 abandoned d5 while pursuing pressure on Nf3. Before a queen move, inspect the entire support chain it leaves behind.
- Rxd5 removed Ne4's pawn support and attacked e5 laterally. Reinforcing e5 alone did not preserve the center. No engine-best replacement for Qf6 supplied.
24...Nxc3 25.Rxe5 Qd6 26.bxc3 Qd7 27.Ng5 Qc6+ 28.Kg1 Rce8 29.Rxe8 Rxe8 30.Qxe8+ Qxe8 31.Rxe8#.
- Nxc3 attacked Rd5, but Rxe5 escaped while taking the other central pawn. Rc8 defended Nc3; nevertheless bxc3 won N for P. Qe3 guarded c3 through d3, so ...Rxc3 would permit Qxc3. Write the cheaper capture AND the purported recapture before calling a knight safe.
- Qc6 guarded e8 via d7, but that did not make ...Rce8 safe. White had Re5, Qe3 and Re1 lined up on the cleared e-file. The full exchange consumed both Black rooks and the queen, leaving White's rear rook to mate. Count every attacker in order, not just the first recapture.
- At mate Re8 covered f8/h8; Ng5 covered f7/h7, and Black's g7 pawn occupied g7. The advanced h-pawn did not provide an escape because h7 was knight-controlled.
- No invalid attempts; finished 12:17. Qf6 took 22 seconds with ample time. Nxc3/Qd6 took 47/53 seconds after the damage: spend calculation on concrete captures and final exchanges, not explanations of activity.

## T22 round 1: Black vs Sonnet, mate win
Classical: dxe4 Nxe4 Bf5 Ng3 Bg6 h4 h6 h5 Bh7! Bd3 Bxd3 Qxd3! e6; Bf4 Nd7 O-O-O Ngf6 Nf3 Be7 Ne5 Nxe5 Bxe5 O-O Kb1 c5 Bxf6 Bxf6! dxc5 Qc7 b4 a5 a3?? axb4 axb4 Ra1#.
- h6 supplied h7; Bh7/Bxf6 were only-good marks. Bxf6 preserved structure and created f6-e5-d4-c3-b2-a1. dxc5 removed d4's screen, b4 removed b2's: Bf6 protected a1 and controlled b2.
- ...a5 undermined b4 and opened Ra8 toward Kb1. After axb4, Ra1# was protected by Bf6; a2/c1 were rook-controlled and c2 occupied. Rd1 could not capture through Kb1. Scan AFTER the intended pawn recapture. No forced win before a3 established.

## T21 round 2: Black vs Stockfish, mate loss
h4 h5 Bd3 Bxd3 Qxd3 e6 Nf3 Ne7 Bg5! Nf5?? Bxd8 Kxd8.
- Bg5 created g5-f6-e7-d8 against Qd8. Ne7 was the sole screen; resolve this before following Ne7-f5. Six seconds with ample clock: automatic development skipped the latest attack.
- Rbc8 Rd2 Nc4 Rd7+ Kb8 Qxa7#: Rd7 protected a7 and controlled b7/c7; Rc8 occupied c8. Test protected queen entries.

## Earlier defensive geometry
- T20 Advance: Qe8 guarded Be7 AND b8. Qf7?? Rb8+ Bf8 absolutely pinned B to Kg8; Qxf4?? gxf4 lost Q to g3's pawn despite 71 seconds thinking. Kf7 later released the pin.
- T20 Sonnet: Rc6 plus Ke7 guarded e6. Rh1 threatened Ra1#; c4 cleared Ra3: Ra1+ Ra3 Rxa3+ Kxa3 dxc4, then promotion and Rb6-supported Qb2#.
- Classical: Nxh5 Nxh5 Rxh5 clears Be7-f6-g5. Qh3? Rxh3 gxh3 Bxg5 wins Q. Bd4 guards f2; Qf2 guards g3 for Ng3#.
- Advance: e6 screens Qe7 from Re1. Rxc3+ Kb1 Rxb2+ Kxb2 Qxa3+ Kb1 exd5 moves Q with check before recapturing; bxc3 permits Qxa3+ Kb1 Qb2# with Rf2 support.
- Re6's departure opens Qd5-e6-f7-g8. Rad8?? exd8=N ignores capture-promotion. Kh1 releases Nd4's pin: Qe7?? Nxe7+.
- Ne4+ Ke3 f4+ abandons Ne4's f5 guard: Kxe4. c5 controls d6: Qd6?? cxd6. Pawn support or attacking B does not release a knight pinned to its king.
