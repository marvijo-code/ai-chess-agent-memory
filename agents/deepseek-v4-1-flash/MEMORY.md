# Chess memory

Notes (read at start):
- notes/capture-safety.md - pre-move scan + blunder catalogue g1-g44
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Chigorin as White
- notes/sicilian-black.md - Dragon/Rauzer as Black
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/four-knights-black.md - 4.Bb5 Bb4 as Black

## Rule 1 - pre-move scan (5 s, FINAL position)
1. Destination: which enemy PAWN, knight, bishop, rook (rank/file), queen, king attacks it? Attacked+undefended -> reject. Pawn moves vacate guards.
2. My attacked piece: save/trade/defend NOW before any other move.
3. Queen: never on a square his pawn/slider/rook attacks. Count ALL recapturers incl. rooks on destination rank/file and PAWNS.
4. Knight: never undefended or on a pawn/bishop-attacked square, esp. down material. g44 21...Nb3?? Bxb3; 22...Nc5?? bxc5.
5. Rook: undefended rook facing his rook loses; rook to an open file at my loose piece = emergency.
6. Pawn pushes/captures: never onto a defended piece, a pawn's attack, where a queen gains tempo, while it guards my piece; never down material.
7. Legality BEFORE sending (3 illegal = forfeit): trace path square by square; geometry. g44 22...axb3 illegal (a6-pawn), 22...Rxc1 blocked by own c5-pawn/Qc7.
8. Lost position: defend/trade; no 'active' piece to an undefended square; 5-15 s.
9. Time: routine <=15 s; from m10 no move >25 s. g44 spent 47-63 s many moves and 2:10 on 22...Nc5, clock 2:58 vs 13:38, then timeout/forfeit. Long thinks never fixed anything.

## Openings
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, ...Na5 ...c5 ...Qc7 ...Bb7 ...Rac8. After 9.h3 no ...Bg4. g44: 15...Nc6?? allowed 16.d5; in Chigorin after White Nf1-g3, prefer ...Nc4! (hits e3/d2) or ...Rfe8/...Qb8; don't put a knight on c6 where d5 kicks it. Resolve centre BEFORE his d5. 19...Nfd7?/20...Bf6? let 21.b4 kick Nc5; retreat to a safe defended square, not b3.
- RL as White (Chigorin): 14...Nb4 -> 15.Bb1!; 14...Nb8: 15.Nf1 Nbd7 16.Be3; 14...Rac8 15.Ne3 Nc4: keep e3 EMPTY (g33). 17.b4 axb4 18.axb4 OPENS a-FILE: fix Ra1 (trade Rxa8) before anything; after 19...Nxb4 20.Rxa8! NOT 20.Bxb4?? Rxa1 (g43). No Q on pawn/rook-attacked squares; never Bx a defended pawn down material.
- Sicilian as Black: Dragon ...d6 ...cxd4 ...Nf6 ...Nc6 ...g6 ...Bg7 ...O-O ...a6 ...Bd7 ...Rc8 ...Qa5 (g28,g36). Rauzer: 11...gxf6! not Bxf6; never leave Bd7 as d6's only shield; no ...Qxa4/...Qxc4 vs rook files; no ...f5/...f4 pushes that guard a knight (g30).
- 4N as Black (4.Bb5 Bb4): 6.Nd5 Nxd5! 7.exd5 Nd4!; nothing on f5 while his Qf3 (g26); no ...Bg4 after h3; play ...Qe7/...Qc8/...Bb5.
- Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O; all four losses were trades/grabs: no B-for-P (12.Bxf6?!, 12.Bxe5??, 10.Bxd4??); keep Bc5 defended while Rfc8/Ra8 can come (g42); after ...d5 count pawn/rook recapturers on d5 (g39,g42); after O-O-O no queen on a1-net squares (g6).

## Opponents
- Stockfish 19 (g6..g43): ~0 s/move; punishes loose units, queens on attacked squares/lines, loose bishops on open files (g42), back-rank.
- Sonnet 5.5 (g7..g43): banks clock; takes EVERY free/attacked unit instantly (Nxa1, Rxb2, Rxd6, Bxe4, Bxa5; g43 Nxb4, Rxa1, Rxa4, Rxc4, Qxc1, Qxe1+, Qxe4, Qxd5). Keep every piece and pawn defended; move an attacked queen at once; a loose rook facing his rook on an open file is lost.
- GPT-6.1 Sol (g9..g44): closed RL, fast, solid; punishes queens on his lines/files; takes undefended/pawn-attacked knights (g44 22.Bxb3, 23.bxc5). Captures must survive recapture; keep every piece defended and off his bishop/pawn attack squares.
