# Chess memory

Notes:
- notes/capture-safety.md - scan + blunder catalogue g1-133
- notes/caro-advance-black.md - Caro Advance B + Classical 3.Nc3
- notes/qgd-white.md - QGD W Lasker/Bxf6/Exchange
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W
- notes/sicilian-black.md - Alapin/Dragon/Taimanov
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- O-O: knight off home + f8/g8 empty (g124). Rejection = recheck the board, never guess (g120,g129). Nc8-d8 is NOT a knight move (g128).
- SELF-BAN: a move my scan or note called bad is DEAD (g125 Bg5, g126 Qf3, g127 Qg6+, g128 Bd8, g130 Bf6, g132 Qd6).

## Rule 1 - destination sweep (every move)
- His LAST move first: attacks, pawn controls, opened lines; count MY guards on my destination: 0 + enemy capture = gift (g118,g119).
- PAWN CAPTURES FIRST - compute from the ACTUAL pawn placement: e6 hits d5/f5, d5 hits c4/e4, e5 hits d6/f6. 15.Qe4?? dxe4 = Q for P (g133); 16...Qd6?? exd6 (g132); 20.Qxf5?? exf5 (g131); Nf5?? exf5 (g126). A blocking pawn still attacks. 'Defended' never saves from a pawn.
- Knight jump onto a covered square = piece for nothing; when HIS knight hits my queen, list its jumps (Nd4 hits b3 c2 e2 e6 f3 f5) AND the pawn diagonals, then retreat only where THAT knight cannot take (g128 25...Bd8?? Nxd8); a pawn-kick square chases it (g129 16...Nc4?! 17.b3).
- Rook files, bishop rays own whole lines: Re6 owns rank 6 (g125); Bb7 owns b7-h1 (g126). Attacked+undefended -> save NOW; mate net before any grab (g123,g129).

## Rule 2 - the queen
- Hit by anything: she moves THAT move; 'defended' never counts (g95). Before ANY queen move list ranks/files/diagonals + EVERY enemy pawn diagonal + every enemy knight jump; no capture on a defended square, a ray or a knight square; checks only if K cannot take and no pawn takes (g127).
- QUEEN takes: count EVERY defender incl. pawns, knights and the king; his recapture where mine cannot = Q for P/N (g110,g130). Check PAWN recaptures before trusting a planned queen trade (g131).
- THE KING IS A DEFENDER - a queen check beside his king on an unguarded square = KxQ (g130 Qxb2+?? Kxb2). QUEEN SOLE GUARD + knight capture WITH CHECK = Q for N (g119).
- Attacking his queen: my attacker must be defended or she just captures it (g133 19.Rc4?? Qxc4 = R for nothing). My capture he answers with CHECK/tempo: tempo first (g120,g123).

## Rule 3 - captures
- RECAPTURE is not a TRADE (g111 Rxc6?? = R for P): say what I win AND what he wins back; 2 attackers vs 3 defenders = no (g126 17.Rxc5?? = R for N).
- Count EVERY enemy recapturer - PAWNS FIRST, rooks/queens behind the first defender (g131 e6-pawn = Q for P; g129 17...Nxe5?? missed Re1).
- Trace MY recapture through MY OWN pieces (g121 own Bd2 = Qd1 never retook d4). Broken chain, don't take.
- PIN freezes a recapturer (g90); X-RAY = rook files/bishop diagonals (g97); blocked guard -> ...Bxa3! (g112); removing a screen uncovers what is behind (g120).

## Rule 4 - material & clock
- Down: keep queens (repetition); NO grabs; loose pieces first; defend loose pawns BEFORE quiet development (g132 15...Ne7 then 16.Qxa7). Down vs Sol no grab pays: 22...Rad8 set Rd1# while I took b7/a8 (g133). 5-10 s.
- Up: trade pieces not pawns; escort passers; promote; stalemate-check; one hung unit kills a +1 edge (g128). Equal R-ending = HOLD; R for P loses (g111).
- Equal: mate net before any grab; NO piece-for-pawn sac (g127 17.Bxh6??; g130 17...Bf6??). After HIS move re-count material before the planned continuation (g131).
- Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. Long thinks still blundered (g120-g133; 12.Rc1 70 s + 1 illegal try, g133).

## Openings
- Caro B Advance: ...Bf5/Bg6 e6 Nd7 c5 Be7 Rc8 Qb6; NEVER ...Qxd4; no ...Nc5 while d4; no piece on d6/f6 or ...Ngf6 while e5 (g132 16...Qd6?? exd6); no ...Qd6 vs Bf4, no ...Bg5??, no ...Qxb2; vs b3/Ba3 ...Bxa3!. g129: free b6 BEFORE ...Qb6; ...Nxe5 only with ONE recapturer.
- Caro B Classical (g130): ...Bg6 h6 Bh7 e6 Bxd3 Qxd3 Nd7 Ngf6 Be7 O-O =; NO piece to f6 while White's e5-pawn stands (17...Bf6?? exf6); 21.Rd7 hits c7-knight (...Nd5!); never Qxb2+ vs Kb1.
- Caro W 3.Nc3: ...Bxd3 Qxd3 e6 Bf4 Ngf6 O-O Be7 c4 O-O Rfe1 c5 15.d5! exd5 16.cxd5 Re8 = space edge; no sacs (Bxh6); NO Qg6 (f7/h7); Kb1 vs ...Rad8: trade rooks/make luft, never grab (g123).
- QGD W (0-11): Lasker 12.Nxf3!; keep c3+d4+Rc1, no c4; ...Qb4 hits b2 (Qc2 first); never Qx b7/d7/a8 vs c6-bishop; e6-pawn kills d5/f5 (g131), d5-pawn kills c4/e4 (g133 15.Qe4?? dxe4); when ...Bxf3/...Nxd4 hits my queen the only safe squares are d1/d3/e3; Bxf6: no piece on d4/d5/d6, ...c5! dxc5 Nxc5 hits Bd3 - save it, never Rxc5; no Nf5 while e6.
- Ruy Chigorin W (0-6): 13.cxd4: Nf1 BEFORE Qe2; keep Rc1; 16.Be3, NOT Bd2?! (blocks Qd1-d4, g121). B: meet 10.e5 with ...Ne8/...d6, never take e5; 9.Bd5! only 9...Nxd5 =; retreat Qc7 when the c-file opens; no ...Nc4 once b3 is possible.
- Dragon B: 13.Qxd5 -> ...Qc7 ONLY. Soltis 9.Bc4 (0-8): 14.h5 Nxh5!; 16.g5 -> only ...Nh5.
- Alapin B: 5.Qxd4 Nc6/g6/Bg7/O-O/Nc5; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 12.Bxe5 12...Nxe4! only.

## Opponents
- SF19: instant; punishes loose units, queens on his ranks/rays, pawn-attacked squares. Down: no self-blocks; repetition (g119).
- Sonnet 5.5 (never beaten): banks clock; takes every free unit; trades into simple winnable endings; never misses a recapture, pawn recaptures included (g132).
- GPT-6.1 Sol: fast; takes every free piece, incl. a queen on any pawn diagonal (g133 dxe4); converts without error - no sacs, no grabs, no loose pieces; his mate net (Q + Rd1#) closes fast when I'm down.
