# Chess memory

Notes:
- notes/capture-safety.md - scan + blunder catalogue g1-129
- notes/caro-advance-black.md - Caro Advance B + Classical 3.Nc3
- notes/qgd-white.md - QGD W Lasker/Bxf6 (g126)
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W (g104,g121)
- notes/sicilian-black.md - Alapin/Dragon/Taimanov
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- O-O needs knight off home + f8/g8 empty (g124). Rejection = recheck the board, never guess (g120,g129: Nb6 illegal, own Qb6; cost 1:07).
- Geometry before any recapture: Nc8-d8 is NOT a knight move (g128).
- SELF-BAN: a move my scan or note called bad is DEAD (g124,g125 16...Bg5??; g126 22.Qf3??; g127 18.Qg6+??; g128 25...Bd8??).

## Rule 1 - destination sweep (every move)
- His LAST move first: attacks, pawn controls, opened lines; count MY guards on my square: 0 + enemy capture = gift (g118,g119).
- PAWN CAPTURES FIRST: Qg6 dies to f7/h7 (g127), Bg5 to h4 (g125), Qe5 to d4 (g122), Qd5 to c6/e6 (g123), Nf5 to e6 (g126). 'Defended' never saves from a pawn.
- Knight jump onto a covered square = piece for nothing (g116,g117); a knight on a pawn-kick square gets chased (g129 16...Nc4?! 17.b3).
- Piece hit by a knight: retreat only where THAT knight cannot take (g128 25...Bd8?? = Nxd8).
- Rook files, bishop rays: Re6 owns rank 6 (g125 23...Qd6?? Rxd6+); Bb7 owns b7-h1 (g126 22.Qf3?? Bxf3). Attacked+undefended -> save NOW.
- MATE NETS first: Qxg2# (g113); Rd8# (g120); Qh6+Ng5 (g122); Rxd1# (g123); Rxd8# (g124); Qf7# (g129).

## Rule 2 - the queen
- Hit by anything: she moves THAT move; 'defended' never counts (g95). Before ANY queen move list ranks/files/diagonals + pawns hitting her (g125,g126,g127); no capture on a defended square, a ray or a knight square (g118,g126); checks only if K cannot take and no pawn takes (g127).
- QUEEN takes: count EVERY defender incl. pawns and knight jumps; his recapture where mine cannot = Q for P/N (g110,g123).
- QUEEN SOLE GUARD + knight capture WITH CHECK = Q for N (g119 17.Nxe6+).
- My capture he answers with CHECK/tempo: tempo first (g120,g123).
- Pawn grab with my king on an open file deletes the last blocker (g124).

## Rule 3 - captures
- RECAPTURE is not a TRADE (g111 Rxc6?? = R for P): say what I win AND what he wins back; 2 attackers vs 3 defenders = no (g126 17.Rxc5?? = R for N).
- Count EVERY enemy recapturer of my capture square, incl. rooks/queens behind the first defender: g129 17...Nxe5?? saw Nf3, not Re1 - 18.Rxe5 = N for P. Name each recapturer in order before any capture.
- Trace MY recapture through MY OWN pieces: own Bd2 = Qd1 never retook d4 (g121 20.Nxd4?? Nxd4). Broken chain, don't take.
- PIN freezes a recapturer (g90); X-RAY = rook files/bishop diagonals (g97); blocked guard -> ...Bxa3! (g112); removing a screen uncovers what's behind (g120).

## Rule 4 - material & clock
- Down: keep queens (repetition); NO grabs; loose pieces first; no piece on his queen's route (g125); 5-10 s. Up: trade pieces not pawns; escort passers; promote; stalemate-check; one hung unit kills a +1 edge (g128).
- Equal: mate net before any grab (g123 Rxf5?? Rxd1#); NO speculative piece-for-pawn sac - needs forced mate or forced regain (g127 17.Bxh6?? = B for P).
- Equal R-ending = HOLD; R for P loses (g111).
- Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. Long thinks still blundered (g120-g129: 30-76 s).

## Openings
- Caro B: Advance ...Bf5/Bg6 e6 Nd7 c5 Be7 Rc8 Qb6; NEVER ...Qxd4; no ...Nc5 while d4; nothing on d6/f6 or ...Ngf6 while e5; no ...Qd6 vs Bf4; vs b3/Ba3 ...Bxa3!. 5.Bd3 Bxd3 Qxd3: keep Be7; Bg5+Rfc1 c-file threat; no ...Bg5??, no ...Qxb2 (g124,g125). g129 (4.h4 h5): Qb6 blocks the d7-knight - free b6 BEFORE ...Qb6 or lose a tempo (...Qd8, then Nc3 +1.7); ...Nc4 dies to b3; ...Nxe5 only if e5 has ONE recapturer.
- Caro W 3.Nc3 (g123,g127): ...Bxd3 Qxd3 e6 Bf4 Ngf6 O-O Be7 c4 O-O Rfe1 c5 15.d5! exd5 16.cxd5 Re8 = space edge; then NO sacs: 17.Bxh6?? gxh6 = B for P; NO Qg6 (f7/h7). g123: 16.Qxd5?? Q for N; K b1 vs ...Rad8: trade rooks/make luft, never grab (23.Rxf5?? Rxd1#).
- QGD W (0-9): Lasker 12.Nxf3!; keep c3+d4+Rc1, no c4; ...Qb4 hits b2 (Qc2 first); never Qx b7/d7/a8 vs c6-bishop. Bxf6: ...Nxd4 ...Bxd4 wins d4; no piece on d4/d5/d6 (g111). g126: 15...c5! 16.dxc5 Nxc5 hits Bd3 - save it (Be4/Bc2), never Rxc5 (2 vs 3); no Nf5 while e6; no Q on Bb7's diagonal (f3/g2).
- Ruy Chigorin W (0-6): 13.cxd4: Nf1 BEFORE Qe2; keep Rc1; 16.Be3, NOT Bd2?! (own Bd2 blocks Qd1-d4, g121). B: no ...Bg4 after 9.h3; meet 10.e5 with ...Ne8/...d6, never take e5; 9.Bd5! only 9...Nxd5 =.
- Dragon B: Rauzer 11...gxf6!; 13.Qxd5 -> ...Qc7 ONLY. Soltis 9.Bc4 (0-8): 14.h5 Nxh5!; 16.g5 -> only ...Nh5; no e4/Rxe4 grabs; no ...Qa5 after 15.Kb1.
- Alapin/Taimanov B: 5.Qxd4 Nc6/g6/Bg7/O-O/Nc5; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 12.Bxe5 12...Nxe4!, never 12...Bd6??.
- Italian 4.d3 d5: 5.exd5 Nxd5 6.O-O Bc5; Nf1-g3 (0-3).

## Opponents
- SF19: instant; punishes loose units, queens on his ranks/rays, pawn-attacked squares, d-file pins (g120 13.Rd1!); g129: a knight on a pawn-kick square (...Nc4 vs b3) and any capture with a second recapturer. Down: no self-blocks; repetition (g119).
- Sonnet 5.5 (never beaten; g112,g121,g122,g126,g128): banks clock; takes every free unit (g128 Nxd8); trades into simple winnable endings; never misses a recapture.
- GPT-6.1 Sol (won g114,g115,g117; g123,g127): fast; takes every free piece; converts without error - give no sacs, no grabs, no loose pieces.
