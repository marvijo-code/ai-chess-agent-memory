# Ruy Lopez: attack liquidation, screens and conversion

## T24 semifinal 2 game 1: White vs Sonnet, time win
Closed Chigorin: c3/h3/d4/Nbd2-f1-g3, ...a5 d5 Nb8-d7, a4 bxa4 Rxa4 Bb7 Be3 Nb6 Ra1 c4 Nf5. Qd2?!/g4-g5/h4-h5/g6?! hxg6 hxg6 fxg6 N5h4?! Bxh4 Nxh4!.
- The closed center allowed kingside space, but the storm did not establish a forced attack. White lost both g/h pawns for Black's h-pawn. ...fxg6 attacked Nf5; retreating and exchanging on h4 did not recover the pawn.
- Qe2-g4-h3, Kg2/Rh1/Nf3 opened the h-file. ...Bc8 attacked Qh3 through d7-e6-f5-g4. Qh8+! Kf7 Ng5+ Ke8 forced the king out, but forced checks did not establish a winning continuation.
38.Ne6?? Bxe6! 39.dxe6! Rxe6! 40.Ba4+ Kf7! 41.f3 Re7 42.Rad1 Rae8? 43.Bxe8+! Rxe8.
- Ne6 forked Qc7/Nf8 but ignored Bc8-d7-e6. The d5 pawn DID protect Ne6; nevertheless Bxe6 dxe6 Rxe6 traded N+P for B, losing another pawn. My calculation considered only ...Rxe6. List every capturer before valuing a fork or protected sacrifice.
- Do not call the resulting e6 pawn a lasting asset without calculating its immediate capture. After the sequence Black had two knights against the bishop pair and two extra pawns.
- ...Rae8 placed a rook on Ba4-b5-c6-d7-e8. Bxe8+ recovered an exchange through an opponent error, not a forced result of Ne6. Before f4, White had 2R+B against R+2N, two pawns down; there was no whole extra rook.
45.f4?! Nxf4+ 46.Bxf4! exf4! 47.Qxf4?! Rxe4 48.Qxd6?! Qxd6?? 49.Rxd6!.
- f4 exchanged the remaining bishop for a knight and cost a pawn. Qxf4 abandoned e4; Rxe4 was defended by Nf6, so Qxe4 was not a legal material recovery. Qxd6 recovered a different pawn. The marked queen exchange was Black's error; do not infer that forcing it was sound.
49...Re2+ 50.Kf3 Rxb2! 51.Rd4 Rb3 52.Rxc4 Nd5 53.Rc1 Kf6 54.Ke4! Ke6? 55.Kd4? Kd6 56.Ra4 Rb5! 57.Rh1 Ke6?? 58.Rh7?? Kf6?! 59.Kc4?!, Black flagged.
- Final material: White 2R+c3 against R+N+a5/g6/g7. This was a time win, not demonstrated endgame conversion.
- Rxc4 defended c3 along the c-file; Rc1 added another defender. Rc6+ was not automatically protected by Rc1 because OWN c3 blocked that file.
- With Kd4/c3 facing Rb5/Nd5, c4 attacks BOTH pieces. Scan this pawn fork after ...Ke6 before pursuing g7 with Rh7. No engine-best replacement or forced winning continuation was supplied.
- No invalid White attempts; 7:21 remained after Kc4. Sonnet repeatedly spent 45-63 seconds on bishop shuffles and quiet defenses, reaching under a minute. My own 29-53-second critical/quiet moves still missed Bxe6 and the pawn fork. Preserve speed while checking concrete replies.

## T24 round 3: White vs Sonnet, mate win
Berlin d3/Bc5: c3/h3/Re1/Bc2/d4, ...exd4 cxd4! Bb4 Nc3 Bxc3 bxc3! Re8 Bf4 Qe7 e5 dxe5 dxe5 Nh5 Bh2 Rad8 Qd3?! f5? exf6 e.p. Nxf6 Rxe7 Rxe7.
- e5 cleared Bc2-h7. En passant removed e5/f5 and opened Re1-e7 against Qe7. Qd3's battery was not a proven advantage.
- Nd4 Nxd4 cxd4, then d5 Bxd5 lost P: Nf6 barred Qxd5. Passed pawns still need destination checks.
- Bf5 Bxf5 Qxf5/Rxd8+ Rxd8 reduced counterplay. Bxc7 freed h2 with tempo. ...Rd5 skewered Be5/Qf5; Qe6+ defended B. Bxf6 Rd1+ Kh2 gxf6 Qxf6 reached Q vs R.
- Qg4 lost f2's guard; Kf4?! lost g2's. Kf5-e6-e7-f6-f7 activated K. Qxg7# worked because Kf7 guarded g7 against Kh7.

## Stockfish and earlier geometry
- Qb1 Bxf3 gxf3 weakened shelter; doubled g-rooks lacked a proven threat. ...g5 supported Nf4: h4 threatened hxg5, h5 abandoned it.
- Qd4 c6 Qxc4 cxd5 forked Qc4/Be4. Saving B lost Q; scan pawn breaks before grabs.
- Bh5/Qe2 retained Nf3 as the SAME bishop-ray screen: Ne5?? Bxe2. Ne5 screened Re6-e1: Nxf7?? Re1# before the fork paid.
- Sonnet's ...dxe5 once ignored Bb1/Qe4-h7 mate; do not assume repetition. ...a5 supplies Na6: d5/Nb4/Bb1/a3 does not trap N.
- Qe2 Rfc8 Bc2?? Qxc2 Qxc2 Rxc2 loses B. ...Nxg3 fxg3 can abandon Be3 to Rxe3.
- Qd2 guards d5 only with d3/d4 clear; Bd2 screens Qd1-d5. Rb1+?? Bxb1 follows Bd3-c2-b1.
