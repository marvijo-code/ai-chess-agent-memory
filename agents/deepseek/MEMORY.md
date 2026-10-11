# Chess memory

Notes:
- notes/capture-safety.md - scan + blunder catalogue g1-131
- notes/caro-advance-black.md - Caro Advance B + Classical 3.Nc3
- notes/qgd-white.md - QGD W Lasker/Bxf6
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W
- notes/sicilian-black.md - Alapin/Dragon/Taimanov
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- O-O needs knight off home + f8/g8 empty (g124). Rejection = recheck the board, never guess (g120,g129).
- Geometry before any recapture: Nc8-d8 is NOT a knight move (g128).
- SELF-BAN: a move my scan or note called bad is DEAD (g125 Bg5??; g126 Qf3??; g127 Qg6+??; g128 Bd8??; g130 Bf6??).

## Rule 1 - destination sweep (every move)
- His LAST move first: attacks, pawn controls, opened lines; count MY guards on my square: 0 + enemy capture = gift (g118,g119).
- PAWN CAPTURES FIRST: list every enemy pawn diagonal to my DESTINATION and my queen. e6 attacks d5/f5: 20.Qxf5?? exf5 = Q for P (g131); Nf5?? exf5 (g126). Bf6 dies to e5 (g130); Qg6 to f7/h7 (g127). 'Defended' never saves from a pawn.
- Knight jump onto a covered square = piece for nothing; hit by a knight, retreat only where THAT knight cannot take (g128 25...Bd8?? Nxd8); a pawn-kick square chases it (g129 16...Nc4?! 17.b3).
- Rook files, bishop rays own whole lines: Re6 owns rank 6 (g125); Bb7 owns b7-h1 (g126). Attacked+undefended -> save NOW; mate net before any grab (g123,g129).

## Rule 2 - the queen
- Hit by anything: she moves THAT move; 'defended' never counts (g95). Before ANY queen move list ranks/files/diagonals + pawns; no capture on a defended square, a ray or a knight square; checks only if K cannot take and no pawn takes (g127).
- QUEEN takes: count EVERY defender incl. pawns, knights and the king; his recapture where mine cannot = Q for P/N (g110,g130). Check PAWN recaptures before trusting a planned queen trade: g131 planned 'Qxf5 Qxf5' and ...exf5 took her.
- THE KING IS A DEFENDER: a queen check beside his king on an unguarded square = KxQ (g130 21...Qxb2+?? Kxb2).
- QUEEN SOLE GUARD + knight capture WITH CHECK = Q for N (g119). My capture he answers with CHECK/tempo: tempo first (g120,g123).

## Rule 3 - captures
- RECAPTURE is not a TRADE (g111 Rxc6?? = R for P): say what I win AND what he wins back; 2 attackers vs 3 defenders = no (g126 17.Rxc5?? = R for N).
- Count EVERY enemy recapturer - PAWNS FIRST, rooks/queens behind the first defender too (g131 missed the e6-pawn = Q for P; g129 17...Nxe5?? missed Re1 = N for P). Name them in order before any capture.
- Trace MY recapture through MY OWN pieces: own Bd2 = Qd1 never retook d4 (g121). Broken chain, don't take.
- PIN freezes a recapturer (g90); X-RAY = rook files/bishop diagonals (g97); blocked guard -> ...Bxa3! (g112); removing a screen uncovers what is behind (g120).

## Rule 4 - material & clock
- Down: keep queens (repetition); NO grabs; loose pieces first; no piece on his queen's route; 5-10 s. Up: trade pieces not pawns; escort passers; promote; stalemate-check; one hung unit kills a +1 edge (g128).
- Equal: mate net before any grab; NO piece-for-pawn sac (g127 17.Bxh6??; g130 17...Bf6??).
- After HIS move re-count material before playing the planned continuation: g131 played 21.Bxf5 'balanced' already down the queen (...exf5).
- Equal R-ending = HOLD; R for P loses (g111).
- Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. Long thinks still blundered (g120-g131: 30-76 s; g131 43-47 s routine).

## Openings
- Caro B Advance: ...Bf5/Bg6 e6 Nd7 c5 Be7 Rc8 Qb6; NEVER ...Qxd4; no ...Nc5 while d4; nothing on d6/f6 or ...Ngf6 while e5; no ...Qd6 vs Bf4, no ...Bg5??, no ...Qxb2; vs b3/Ba3 ...Bxa3!. g129: free b6 BEFORE ...Qb6; ...Nxe5 only with ONE recapturer.
- Caro B Classical (g130): ...Bg6 h6 Bh7 e6 Bxd3 Qxd3 Nd7 Ngf6 Be7 O-O =; NO piece to f6 while White's e5-pawn stands (17...Bf6?? exf6); 21.Rd7 hits c7-knight (...Nd5!); never Qxb2+ vs Kb1.
- Caro W 3.Nc3: ...Bxd3 Qxd3 e6 Bf4 Ngf6 O-O Be7 c4 O-O Rfe1 c5 15.d5! exd5 16.cxd5 Re8 = space edge; no sacs (Bxh6); NO Qg6 (f7/h7); Kb1 vs ...Rad8: trade rooks/make luft, never grab (g123).
- QGD W (0-10): Lasker 12.Nxf3!; keep c3+d4+Rc1, no c4; ...Qb4 hits b2 (Qc2 first); never Qx b7/d7/a8 vs c6-bishop; d5/f5 = e6-pawn squares, no piece there (g131 20.Qxf5?? exf5); Bxf6: no piece on d4/d5/d6, ...c5! dxc5 Nxc5 hits Bd3 - save it, never Rxc5; no Nf5 while e6; no Q on Bb7's diagonal.
- Ruy Chigorin W (0-6): 13.cxd4: Nf1 BEFORE Qe2; keep Rc1; 16.Be3, NOT Bd2?! (blocks Qd1-d4, g121). B: meet 10.e5 with ...Ne8/...d6, never take e5; 9.Bd5! only 9...Nxd5 =; retreat Qc7 when the c-file opens; no ...Nc4 once b3 is possible.
- Dragon B: 13.Qxd5 -> ...Qc7 ONLY. Soltis 9.Bc4 (0-8): 14.h5 Nxh5!; 16.g5 -> only ...Nh5.
- Alapin B: 5.Qxd4 Nc6/g6/Bg7/O-O/Nc5; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 12.Bxe5 12...Nxe4! only. Italian 4.d3 d5: Nf1-g3.

## Opponents
- SF19: instant; punishes loose units, queens on his ranks/rays, pawn-attacked squares, d-file pins. Down: no self-blocks; repetition (g119).
- Sonnet 5.5 (never beaten): banks clock (g131 15:34 vs my 9:33); takes every free unit; trades into simple winnable endings; never misses a recapture, pawn recaptures included (g131 ...exf5).
- GPT-6.1 Sol: fast; takes every free piece; converts without error - give no sacs, no grabs, no loose pieces.
