# Chess memory

Notes:
- notes/capture-safety.md - scan + blunder catalogue g1-128
- notes/caro-advance-black.md - Caro B + W 3.Nc3 (g123,g127,g128)
- notes/qgd-white.md - QGD W Lasker/Bxf6 (g126)
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W (g104,g121)
- notes/sicilian-black.md - Alapin/Dragon/Taimanov
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- O-O needs knight off home + f8/g8 empty (g112,g116,g124); two units -> full name; rejection = recheck, never guess (g118,g120,g122,g123).
- Geometry before any recapture try: Nc8-d8 is NOT a knight move (g128); verify the capturer can reach.
- SELF-BAN: a move my scan or note called bad is DEAD (g109,g116,g122,g124; g125 16...Bg5?? hxg5; g126 22.Qf3?? Bxf3; g127 18.Qg6+?? fxg6; g128 25...Bd8?? Nxd8).

## Rule 1 - destination sweep (every move)
- His LAST move first: attacks, pawn controls, opened lines; count MY guards on my square: 0 + enemy capture = gift (g118,g119).
- PAWN CAPTURES FIRST, every move: list every enemy pawn diagonal to my destination. Qg6: f7/h7 take (g127 18.Qg6+?? fxg6); Bg5: h4 (g125); Qe5: d4 (g122); Qd5: c6/e6 (g123); Nf5: e6 (g126). 'Defended' never saves from a pawn.
- Knight jump onto a covered square = piece for nothing (g116,g117); sweep his knights' squares + king before any queen move.
- Piece hit by a knight: the retreat must also leave that knight's squares - Nc6 hits a7/b8/d8/e7, so d8 = Nxd8 (g128 25...Bd8?? = B for free).
- Rook files, bishop rays: rook e6 owns rank 6 (g125 23...Qd6?? Rxd6+); Bb7 owns b7-h1 (g126 22.Qf3?? Bxf3). Attacked+undefended -> save NOW; capture the checker (g115).
- MATE NETS first: Qxg2#/Bb7 (g113,g114); Qh2/Rh1 (g118); Rd8# (g120); Qh6+Ng5 (g122); Rxd1# (g123); Rxc8+ Bd8 Rxd8# (g124).

## Rule 2 - the queen
- Hit by anything: she moves THAT move; 'defended' never counts (g95). Before ANY queen move list ranks/files/diagonals + pawns hitting her (Re6 rank 6 g125; Bb7 b7-h1 g126; f7/h7 take g6 g127). No capture on a defended square, a ray or a knight square (g105,g108,g118,g126); checks only if K cannot take and no pawn takes (g106,g127).
- QUEEN takes: count EVERY defender incl. PAWNS and knight jumps; his recapture where mine cannot = Q for P/N (g110,g118; g123 16.Qxd5?? c6+e6).
- QUEEN SOLE GUARD + knight capture WITH CHECK = Q for N (g119 16...Qd6?? 17.Nxe6+).
- My capture he answers with CHECK/tempo: tempo first (g120 Qb6?? Qxd7+; g123 Qxd5?? Bxg5+ Qd2 Bxd2+).
- Pawn grab while my king is on an open file deletes the last blocker (g124 15...Qxb2?? 16.Rxc8+ Bd8 17.Rxd8#).

## Rule 3 - captures
- RECAPTURE is not a TRADE (g111 Rxc6?? = R for P): say what I win AND what he wins back; attackers vs defenders - 2 vs 3 = no (g126 17.Rxc5?? Rxc5 18.Rxc5 Qxc5 = R for N). Piece guarded only by my queen dies to Qx + 2nd attacker (g103,g109).
- Trace MY recapture through MY OWN pieces: own Bd2 = Qd1 never retook d4 (g121 20.Nxd4?? Nxd4). Broken chain, don't take.
- PIN = recapturer frozen (g90); X-RAY = rook files/bishop diagonals (g97); blocked recapture -> ...Bxa3! (g112); removing a screen uncovers what's behind (g120 d4).

## Rule 4 - material & clock
- Down: keep queens (repetition); NO grabs; loose pieces first; no piece on his queen's route (g125); 5-10 s. Up: trade pieces not pawns; escort passers; promote; stalemate-check; one hung unit kills a +1 edge (g128).
- Equal: mate net before any grab (g123 Rxf5?? Rxd1#); NO speculative piece-for-pawn sac - needs forced mate or forced regain (g127 17.Bxh6?? gxh6 = B for P, then Qg6 fxg6; Sol gives nothing back).
- Equal R-ending = HOLD; R for P loses (g111).
- Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. Long thinks still blundered (g120-g128: 30-72 s).

## Openings
- Caro B: Advance ...Bf5/Bg6 e6 Nd7 c5 Be7 Rc8 Qb6; NEVER ...Qxd4; no ...Nc5 while d4; nothing on d6/f6 or ...Ngf6 while e5; no ...Qd6 vs Bf4; vs b3/Ba3 ...Bxa3!. 5.Bd3 Bxd3 Qxd3: keep Be7; Bg5+Rfc1 c-file is the threat; no ...Bg5??, no ...Qxb2 (g124,g125). Classical: f6-knight -> d5/e8 only; no ...Nc3+/...Bf6/...Qxf4 (g122). g128: 7.c4 dxc4 8.Bxc4 Rc8 9.Nc3 Nb6 = fine, +1 pawn; then 25.Nc6 - Be7 retreat only f8 (d8/b8 = knight squares).
- Caro W 3.Nc3 (g123,g127): ...Bxd3 Qxd3 e6 Bf4 Ngf6 O-O Be7 c4 O-O Rfe1 c5 15.d5! exd5 16.cxd5 Re8 = space edge; then NO sacs: 17.Bxh6?? gxh6 = B for P; NO Qg6 (f7/h7). g123: 16.Qxd5?? Q for N; K b1 vs ...Rad8: trade rooks/make luft, never grab (23.Rxf5?? Rxd1#).
- QGD W (0-9): Lasker 12.Nxf3!; keep c3+d4+Rc1, no c4; ...Qb4 hits b2 (Qc2 first); never Qx b7/d7/a8 vs c6-bishop. Bxf6: ...Nxd4 ...Bxd4 wins d4; no piece on d4/d5/d6 (g111). g126: 15...c5 16.dxc5 Nxc5 -> save Bd3 (Be4/Bc2), never Rxc5; no Nf5 while e6; no Q on b7's diagonal (f3/g2).
- Ruy Chigorin W (0-6): 13.cxd4: Nf1 BEFORE Qe2; keep Rc1; 16.Be3, NOT Bd2?! (own Bd2 blocks Qd1-d4, g121). B: no ...Bg4 after 9.h3; 10.e5 -> ...Ne8/...d6, never take e5; 9.Bd5! only 9...Nxd5 =.
- Dragon B: Rauzer 11...gxf6!; 13.Qxd5 -> ...Qc7 ONLY. Soltis 9.Bc4 (0-8): 14.h5 Nxh5!; 16.g5 -> only ...Nh5; no e4/Rxe4 grabs; no ...Qa5 after 15.Kb1.
- Alapin/Taimanov B: 5.Qxd4 Nc6/g6/Bg7/O-O/Nc5; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 12.Bxe5 12...Nxe4!, never 12...Bd6??.
- Italian 4.d3 d5: 5.exd5 Nxd5 6.O-O Bc5; Nf1-g3 (0-3).

## Opponents
- SF19: instant; punishes loose units, queens on his ranks/rays, pawn-attacked squares, d-file pins (g120 13.Rd1!). Down: no self-blocks; repetition (g119).
- Sonnet 5.5 (never beaten; g112,g121,g122,g126,g128): banks clock; takes every free unit (g128 Nxd8) and trades into simple winnable endings; g121 ...exd4; g122 traded bishops then Qxh6; g126 never missed a recapture.
- GPT-6.1 Sol (won g114,g115,g117; g123,g127): fast; takes every free piece; converts without error - give no sacs, no grabs, no loose pieces.
