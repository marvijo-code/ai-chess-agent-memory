# Black Closed Ruy / Chigorin (DeepSeek 8 W 1 D; Sol W T9SF2G1,T5R1,T6SF2G1; L T7R1,G3,T14R3,T14SF2G1; D G4,T15R3)

## Main line
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 then 14.d5 Nb4 15.Bb1 a5 (a3 Na6, ...Nc5) / 14.Nb3 / 14.Nf1 Bd7 / 14.Bb3 Bd7.

## T15R3 vs Sol: DRAW by repetition THREE PAWNS UP (ply 105, 900+10; clock 7:32 v 9:57)
14.Nf1 Bd7 15.Be3 Rac8 16.d5 Nb4 17.Bb1 a5 18.a3 Nc2! 19.Bxc2 Qxc2 20.Qxc2 Rxc2 21.Rab1 a4 22.Ng3 Rfc8 23.Rec1 Rxc1+ 24.Rxc1 Rxc1+ 25.Bxc1 h6 26.Kf1 Kf8 ... 32...Bg5 33.Bxg5 Nxg5 34.b3 axb3 35.Nxb3 Ke7 36.Nd2 Nh7 37.a4? bxa4 38.Kc4 Nf6 39.Kb4 Ng4 40.f3? Ne3 41.Ndf1 Nxg2 42.Nf5+ Bxf5 43.exf5 Nf4 44.Ne3? Nxh5 45.Kxa4 g6 46.Kb5 Nf4 47.Kc6 Nd3 48.Nc4 Nb4+ 49.Kc7 Nxd5+ 50.Kc6 Nb4+ 51.Kc7 Nd5+ 52.Kc6 Nb4+ 53.Kc7 threefold.
- 18...Nc2 is the equalizer: queens and rooks come off, B+N each. Then 25-36 was a safe waiting game (Nh7, Bf6, Bg5 trade) with every piece defended; Sol self-destructed (37.a4, 40.f3, 44.Ne3 = three pawns).
- THE MISS: after 49...Nxd5+ I had N+5P (d6,e5,f7,g6,h6) v N+2P (f5,f3). 50.Kc6 hit Nd5, Nxd6 threatened, and I chose checks that repeat. Even losing d6 leaves +2 with a passed e-pawn. I never wrote an ending plan (notes only said 'keep Ke7 guarding d6') and used 1 min per check move.
- Better (unverified): ...gxf5 / ...Ke6 hitting f5 / ...e4 break; answer K+N on d6 with activity, not passive checks. Knight trade into K+P with 4P v 2P wins. At 45-48 (10 min left) write the pawn plan.
- Vary BEFORE the 2nd repetition; the third arrival ends the game.

## T14R5.2 vs DeepSeek: WON (mate 30)
14.d5 Nb4 15.Bb1 a5! 16.Nb3 a4 17.Nbd2 Bd7 18.Nxe5?? dxe5! 19.d6 Bxd6 20.Nf3 Rac8 21.Qxa4?? bxa4 ... Qxg1#. ...a5/...a4 kicks Nb3, Rac8 behind Qc7. List Qxa4/Ba3/Qg4 before taking a 'free' piece.

## T14SF2G1 vs Sol: LOST (mate 45): Q for R+B at move 25
14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 Nc5 18.Ng3 Bd7 19.Ba2 a4 20.Be3 Rfc8 21.Rc1 h6 22.Nd2 Rab8 23.b4 axb3 e.p. 24.Nxb3 Nxb3 25.Bxb3 Qxc1?? 26.Bxc1 Rxc1 27.Qxc1 (-6).
- c-file: Rc1 / Nc5 (front) / Qc7 / Rc8. 24...Nxb3 uncovered Rc1 on Qc7; Be3 + Qd1 both guard c1. Fix: at 21-23 queen off the c-file (...Qb6/...Qd8); after 25.Bxb3 play ...Qd8/...Qb6. Qxc1 only if c1 has ONE defender.

## T14R3 vs Sol: LOST (mate 52)
...17.Nf1 Nc5 18.Ng3 Bd7 19.Be3 Rac8 20.Nf5 Bxf5 21.exf5 Rfe8 22.Ba2 h6 23.Rc1 Kh8?? 24.Qe2 Bd8?? 25.Qxb5. 20...Bxf5 removed the ONLY guard of b5. Fix: 20...Bf8 or ...Qb7/...b4. List knight forks before putting two pieces on c7/a7/d6.

## DeepSeek wins/draw
T14R1: 14.Bb3 Bd7 15.dxe5 dxe5 16.Nc4? bxc4! ... Qh2#. T13R1 DRAW (B+B+N vs pawns): 15 shuffle moves; walk K, push h-pawn, never allow 2nd repetition.
T12R5.2: 14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.a3 Na6 18.Be3 Nc5 19.Bxc5 Qxc5: keep Ra8 guarding a5. T12R2: 18.a3 Na6! (Nc6?? dxc6). T11R2: 16.a3 Na6 17.b4 axb4 18.axb4 Bd7! (not Nxb4: Rxa8). T6R2: 19.Ng3?? Nb3! forks.

## Sol wins/losses
T9SF2G1 WON: 14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 ... trade outpost knight, ...Bf6 vs g5, queen off c-file, ...Nh7. T7R1 LOST after winning a piece: 19...Qc4?? 20.Rxc4 (list queen escape squares). G3: pawn up, thrown away by 42...Qe6??. G4: 28.f4 exf4?? opened e5/b1-h7.

## Endgame
Q vs b-pawn is lost. No Rxh3 when gxh3. Stalemate check every ply.
