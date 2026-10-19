# Sicilian as Black - Alapin/Dragon/Taimanov

## Taimanov B vs 6.Nxc6/8.e5 clamp (g158,g164,T38R6,T50R3 v SF19: all 0-1)
Book: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (15 plies). 8...Nd5! and 9...Bf8 vs 9.Qg4 are the only moves; ...Bf8 guards g7 with a PIECE.
- g158: 9...O-O?? 10.Bh6! Bb7?? 11.Qxg7#. g7's only guard was my king.
- g164: 9...d6? loses too: an e8-king does NOT guard g7 (only ADJACENT squares). 10.Qxg7 and 11.Qxh8+ Bf8.
- T38R6: 9...Nf6?? 10.exf6! - the e5-PAWN owns f6. 11...Rf8 was safe (Kxf8 reaches it); 12...Rg8?? 13.Qxg8+ - my KING on e8 is TWO squares from g8 = R for nothing.
- T50R3: 9...Bf8 10.O-O Qc7 11.Re1 g6?? (2:50). The push opened a1-h8: 12.h4 Nxc3 13.bxc3 h5 14.Qf4 Qa5 15.Qf6! won the h8-ROOK (g7 empty). Then 16...Qb6?? (3:23) 17.Bh6! Qb2 18.Qxf8# - f8 unguarded and Kxf8 illegal (Bh6). BANS after ...Bf8: ...g6, ...h5 unless it truly helps, any queen pawn-grab. Keep f8 AND g7 covered; plan ...c5/...Be6/...Qb6 and trade his d3-bishop or queens.
- Answer to 9.Qg4: COVER g7 with ...Bf8/...Kf8, or kick with ...h5 only if g7 is guarded. NEVER castle, ...d6 or ...Nf6 while e5 stands.

## Taimanov B, quiet 6.Be2 (g103,g150,g152,g156,T37R7)
Book: 6.Be2 e6 7.O-O Be7 8.Be3 O-O 9.f4 a6 10.Kh1 Bd7 11.a4 Qc7 12.Bf3 Nxd4 13.Bxd4 (15 plies), then ...Rfe8/...Rad8. His Qe1-g3 + Bd4 menaces Qxg7#; trade Bd4 or play ...f6/luft the moment Qg3 appears - never a passive rook shuffle.
- T37R7 v Astra (0-1, Qxh7# m31): 9...d5 10.e5 Nd7 11.Qe1 Nc5?? 12.Qg3 f6 13.exf6 Bxf6 14.Nxc6! moved his Nd4 SCREEN off the e3-c5 line and 15.Bxc5 won my loose c5-KNIGHT. Before ...Nc5 name its guard (only ...b6/...d6) and who screens his bishop's line; BAN ...Nc5 there.
- g156 v Sol: 15...Qb6?? lost my QUEEN to 16.Bxb6 - she stood on that bishop's d4-b6 diagonal. Walk every enemy bishop diagonal to its end before any queen move.
- g103: 12...Bd6?? guarded only by my queen - 13.Qxd6 Qxd6 14.Bxd6; 17...Bf5?? Rxf5; 36-38 s thinks.

## Taimanov B, g34 v GLM (1-0 m26)
6.Bg5 e6 7.Qd2 Be7 8.O-O-O O-O 9.f4 a6 10.Be2 Bd7 11.g4 b5 (15 plies) is safe while White has no a4. 13...Bxd4! 14.Qxd4?? Nxd4 = Q for B. Then ...Qc7/...f6/...gxf6/...d5/...Bc6. 24...Qxf4+ 25.Kb1?? dropped Kc1's guard of d2 -> ...Qxd2 ...Qe1#.

## Alapin 4.c3
- 5.Qxd4: ...Nc6/...g6/...Bg7/...O-O/...Nc5. No ...Nb4, no knight to d4 (12...Nd4?? 13.Rxd4), no ...b5 while Rd1 faces Qd8.
- g95: 6...Nf6?! allows 7.Nc3!; after 3...d5 the queen MOVES off d5 when hit - 7...e6?? 8.Nxd5 = Q for N.
- g91: 10...bxc6! not ...Bxc6?! (11.d5!); 14...Bxe6! not ...fxe6?! (16.exd6+); 19...Qxd6?? 20.Qxd6+ - d6-pawn was the last screen on the open d-file.

## Recurring
- QUEEN: hit -> she moves that move; 'defended' never counts; pawns e6 hits d5/f5, d5 c4/e4, f7 e6/g6; walk BOTH his bishop diagonals and his knight jumps to her landing square.
- MATE FIRST: Qg4/Bh6 and Qg3/Bd4 - count g7's guards BEFORE castling/shuffling; an e8-king guards nothing two ranks away.
- SCREEN: a knight screening his bishop can leave with tempo; the piece behind is then loose. A capture on the last screen of his queen/rook file = Q/R for P.
- RECAPTURE != TRADE: name my recapturer on the destination AND that it reaches it in ONE move.
- Time: book <=10 s, routine <=15 s; long thinks fixed nothing (T38R6 9...Nf6 37 s; T50R3 ...g6 2:50, ...Qb6 3:23).
