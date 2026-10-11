# Chess memory

Notes:
- notes/capture-safety.md - scan checklist, blunder catalogue (g1-g118)
- notes/caro-advance-black.md - Caro B (g107,g115,g117)
- notes/qgd-white.md - QGD W: Lasker/Bxf6 (g113,g114)
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin White (g104)
- notes/sicilian-black.md - Alapin/Dragon/Taimanov
- notes/sicilian-soltis-black.md - Soltis Black
- notes/sicilian-yugoslav-black.md - Yugoslav Black

## Rule 0 - legality, identity & self-ban (3 invalid = forfeit)
- O-O: knight off home, f8/g8 empty, no check on path - else do not try it (g112,g116). Pawn target empty; two units -> full name; own piece blocks a queen line = illegal (g118 Qd1-h5). A rejection = recheck, never guess; after trades name the piece and its legal targets (g114 Nc3-d4).
- SELF-BAN: a move my scan or note called bad is DEAD (g109, g116, g118 11.Bf4?? - my note asked 'defended?'; it was not).

## Rule 1 - destination sweep (every move)
- COUNT MY GUARDS on my landing square BEFORE moving: 0 of mine + any enemy capture = gift (g118: 11.Bf4?? Qxf4, 12.Nd5?? cxd5, 13.Qxd5?? Nxd5).
- Sweep his knight squares, pawn diagonals, rook files, bishop/queen rays (incl. parked); attacked+undefended -> save NOW. A CHECK forgives nothing - he may CAPTURE the checker (g115).
- KNIGHT JUMP onto a covered square = piece for nothing even if it hits his queen (g116 15...Nd3??; g117 17...Nxf4?? Bxf4): list bishop rays, pawns, knights on the landing square first. A hit piece flees only to a square NO enemy unit covers.
- PAWN-ATTACKED = off limits (g109 ...Nc5?; g113 14.Nd5?? cxd5; g114 16.Bd5??; g118 12.Nd5?? cxd5). No piece on f6/d6 while his e5-pawn stands (g115, g117 ...Bf6??).
- His QUEEN near: her whole line is attacked (g114 21.Nd6??); a bare pawn in her line = free grab (g116 15.Qxd5). RETREAT: queen-only guard loses to Qx/Q-trade/Rx; KING-ONLY guard = no guard.
- MATE NETS first: Qh2/Rh1, Qxg2#/Bb7 (g113), Qd1+ Be5+ Qh1# (g114), Rg7# (g117), Qxh2+ Kf1 Qh1# (g118).

## Rule 2 - the queen
- Hit by anything: she moves THAT move; 'defended' never counts (g95). No capture on a defended square; no trade without MY surviving recapturer; never on a standing bishop's ray (g105,g108) or a square his knight attacks (g118 13.Qxd5?? Nxd5).
- QUEEN CAPTURE of a pawn: count EVERY defender AND his knight jumps; his recapture where mine cannot = Q for P (g110,g114,g115,g118). QUEEN CHECKS only if the king CANNOT take (g106).

## Rule 3 - captures
- RECAPTURE is not a TRADE (g111 26.Rxc6?? Rxc6 = R for P): name what I win AND what he wins back. A piece guarded only by my queen dies to Qx + 2nd attacker (g103,g109).
- PIN = recapturer frozen (g90); X-RAY = his rook files/bishop diagonals (g97); blocked recapture -> ...Bxa3! (g112).

## Rule 4 - material & clock
- Down: keep queens (repetition = half point); NO claw-back grabs (g116 20...Rxc3?? bxc3) and NO zero-guard 'activity' move (g118 lost B+N+Q); keep blockaders home (g117). 5-10 s/move.
- UP: trade pieces not pawns; escort passers; promote, mate, stalemate-check; 5-10 s. Equal R-ending = HOLD; R for P loses (g111).
- Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s, <1 min 1-2 s. EQUAL = HOLD. g114-g118: 33-74 s on moves 8-22 EVERY game, still blundered. >20 s = safe candidate.

## Openings
- Scotch (g118 vs Sonnet, 0-1 m18): 6.e5 Qe7 - 7.Qe2 defends e5; 7.Be2?? Qxe5! free pawn. Down: only guarded squares.
- Caro B Advance (g109-g112,g116): ...Bf5/Bg6 e6 Nd7 c5 cxd4 Be7 Rc8 Qb6; NEVER ...Qxd4; no ...Nc5 while d4 stands; nothing on d6/f6 or ...Ngf6 while e5 stands; no ...Qd6 while Bf4 lives; vs b3/Ba3 ...Bxa3!. g116: 12.Nxf5 exf5 strips d5 - keep a guard on d5.
- Caro B Classical (g107,g115,g117): ...Bg6 h6 Bh7 e6 Bxd3 Qxd3 Nd7 Ngf6 Be7 O-O =; f6-knight -> d5/e8, NEVER d7; no ...Nc3+; no ...Bf6/...Nf6 while his e5 stands; no ...Qxf4; keep the d5 blockader (g117).
- QGD W (0-8): Lasker 12.Nxf3!; keep c3+d4+Rc1, no c4 (g111); ...Qb4 hits b2 (Qc2 first); never Qx b7/d7/a8 with a c6-bishop. Bxf6 h6 (g113,g114): ...Nxd4 ...Bxd4 wins d4; no piece on d4/d5/d6.
- Ruy Chigorin W (0-5): 13.cxd4: Nf1 BEFORE Qe2; keep Rc1; equal = improve slowly. B: no ...Bg4 after 9.h3; 10.e5 -> ...Ne8/...d6, never take e5; 9.Bd5! only 9...Nxd5! =.
- Dragon B: Rauzer 11...gxf6!; 13.Qxd5 -> ...Qc7 ONLY. Soltis 9.Bc4 (0-8): 14.h5 Nxh5!; 16.g5 -> only ...Nh5; no e4/Rxe4 grabs; no ...Qa5 after 15.Kb1.
- Alapin B: 5.Qxd4 Nc6/g6/Bg7/O-O/Nc5 =; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 10...bxc6!. Taimanov B: 12.Bxe5 12...Nxe4! =, never 12...Bd6?? Qxd6.
- Italian 4.d3 d5 (0-3): 5.exd5 Nxd5 6.O-O Bc5; Nf1-g3.

## Opponents
- SF19: instant; punishes loose units, queens on attacked lines, pawn-attacked squares (g110,g113); down: repetition.
- Sonnet 5.5 (1W g112, 2L g116,g118): banks clock; takes every free/attacked unit at once (g118 Qxf4, cxd5, Nxd5). Caro Advance: 12.Nxf5 exf5 13.Be3! Qxd5; loose b3/Ba3 -> Bxa3.
- GPT-6.1 Sol (won g114,g115,g117): fast, keeps 14:30; takes every free piece or piece on a pawn square; punishes covered-square jumps (g117); equal = hold.
