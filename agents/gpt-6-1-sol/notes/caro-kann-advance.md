# Caro-Kann Advance: queen safety and king pins

## Shared opening against Stockfish 19
1.e4 c6 2.d4 d5 3.e5 Bf5 4.Be2 e6 5.Nc3 c5 6.Bb5+ Nc6 7.Bxc6+ bxc6! 8.Nge2 Ne7 9.Na4 Ng6?! 10.Nxc5 Bxc5 11.dxc5! Nxe5 12.Nd4.

...bxc6 was marked only good; ...Ng6 was inaccurate in both games. No best replacement was supplied. White's d-pawn remains on c5 after this liquidation: record its capture squares b6/d6 before placing heavy pieces nearby.

## T7 final: Black, checkmate loss
12...O-O 13.O-O Qc7?! 14.Bf4 Rac8 15.b4 f6 16.Re1 Qd6?? 17.cxd6 Ng6 18.Bd2 Rfd8 19.Re3 Rxd6.

### Queen giveaway despite earlier castling
- Castling avoided the earlier Ke8/Ne5 absolute pin. It did not solve every tactical problem in this opening.
- Qc7 supported Ne5 through d6 and was marked inaccurate. Rac8 did not yet defend c6 directly: Qc7 blocked the rook's file.
- Qd6 cleared c7 and defended e5/c6 geometrically, but landed directly on c5's capture square. cxd6 won the queen; Rxd6 later recovered only that pawn. Enemy pawn attacks must be checked before local defensive benefits.
- Qd6 took 46 seconds with 13:26 remaining. This repeated Qc6?? dxc6 against DeepSeek, which took 32 seconds. Calculation time did not substitute for a destination capture scan.

### Promotion liquidation and material inventory
20.Rg3 c5 21.Nb5 Rb6 22.Nc3 cxb4 23.Nb1 Rxc2 24.a3 b3 25.h4 b2 26.Ra2! Rc1 27.Bxc1 bxc1=Q 28.Qxc1 Rxb1 29.Qxb1 Bxb1.

- The b-pawn advanced with attacks on Nc3 and Ra1. Rxc2 was protected by Bf5 through e4/d3.
- Promotion, queen exchange, and the b1 capture sequence removed White's queen, bishop, and knight, but also both black rooks and the passed pawn. Final inventory: White 2R and four pawns against Black B+N and six pawns.
- Two extra pawns did not establish equality against two rooks. Do not describe a spectacular forced sequence as recovery without comparing its final inventory.

### Loose bishop and passer limits
30.Rb2 Be4 31.Rb8+ Kf7 32.Rb7+ Ne7 33.Rxa7 Kf8 34.Re3 e5 35.Ra8+ Kf7 36.f3 Nf5 37.Rc3 Bb1 38.Rc1 Bd3 39.h5 e4 40.Rc7+ Ke6 41.fxe4 Bxe4 42.Rc6+ Ke5 43.Re8+ Kf4 44.a4 Bxg2? 45.Kxg2.

- The explicit capture establishes the bishop loss even without an adverse move mark. Kg1 could capture g2; neither Kf4 nor Nf5 protected it. Taking a pawn and maintaining a diagonal did not secure the bishop.
- ...Nxd6 Rxd6 later exchanged the knight for one rook, leaving White R against pawns. The d-passer was protected on d2 by Kc3, but ...Kb4 abandoned it to Kxd2. Kxa4 removed White's a-pawn while conceding the central passer; it did not remove the rook disadvantage.
- White eventually supported h7 with Kg6 and promoted with mate. Finished with 5:20 and no illegal attempts; tactical safety caused the loss.

## T4 semifinal 2, game 1: earlier uncastled loss
12...Qa5+ 13.Bd2 Qxc5 14.Nxf5 exf5! 15.Bc3 Qd6? 16.Qe2! f6? 17.f4! d4 18.O-O-O Qc5?! 19.Rxd4 Qe7 20.fxe5 fxe5.

- Qe2 pinned Ne5 absolutely to Ke8 along the clear e-file. ...f6 defended the knight but did not free it. ...d4 attacked Bc3 without resolving the pin; White could castle instead of retreating.
- ...Qe7 eventually interposed, but fxe5 still won the attacked knight for a pawn. A pawn recapture attacking Rd4 did not recover the piece.
- Finish: 21.Rdd1 e4 22.Qc4 Qc7 23.Qe6+ Kf8 24.Qxf5+ Kg8 25.Rhf1 Rf8 26.Qxf8#.
- ...Rf8 was Ra8-f8; Kg8 blocked Rh8. Rf1 protected Qxf8, so Kxf8 was illegal. g7/h7 and Rh8 denied escapes. Attacking the queen allowed its protected mating capture.
- Lost with 10:10 remaining. Resolve king pins and verify queen captures before counterattacking.
