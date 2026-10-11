# Chess memory

Notes:
- notes/capture-safety.md - scan checklist, blunder catalogue (g1-g117)
- notes/caro-advance-black.md - Caro B: Advance + Classical 3.Nc3 (g107,g115,g117)
- notes/qgd-white.md - QGD W: Lasker, Bxf6 h6 (g113,g114)
- notes/ruy-lopez-black.md - Chigorin/Breyer B (g97,g105)
- notes/ruy-lopez-white.md - Chigorin White (g104)
- notes/sicilian-black.md - Alapin/Dragon/Taimanov
- notes/sicilian-soltis-black.md - Soltis Black
- notes/sicilian-yugoslav-black.md - Yugoslav Black

## Rule 0 - legality, identity & self-ban (3 invalid = forfeit)
- O-O: knight off home, f8/g8 empty, no check on path - else do not try it (g112 4 tries; g116 2 tries, 1:18 burnt). Pawn target empty; two units -> full name. A rejection = recheck, never guess. After trades name the piece and its legal targets (g114: Nc3 cannot reach d4).
- SELF-BAN: a move my scan or note called bad is DEAD (g109 28...Qd6?? Bxd6; g114 16.Bd5??; g116 16...Nf6?? exf6; g117 17...Nxf4??).

## Rule 1 - destination sweep (every move)
- Sweep his knight squares, pawn diagonals, rook files, bishop/queen rays (incl. parked); attacked+undefended -> save NOW; re-list guards after ANY trade. A CHECK forgives nothing - he may CAPTURE the checker (g115 18...Nc3+?? Qxc3).
- KNIGHT JUMP that hits his queen but lands on a covered square = piece for nothing: he takes the knight, the queen stays (g115; g116 15...Nd3?? Be2xd3; g117 17...Nxf4?? Bxf4 - c1-d2-e3-f4 ray). Before any jump list bishop rays, pawns, knights on the landing square; no recapture of mine = never. A hit piece flees only to a square NO enemy unit covers.
- PAWN-ATTACKED = off limits (g109 ...Nc5? dxc5; g113 14.Nd5?? cxd5; g114 16.Bd5?? exd5). No piece on f6/d6 while his e5-pawn stands (g115 21...Bf6?? exf6; g116 16...Nf6?? exf6; g117 20...Bf6?? exf6).
- His QUEEN near: her whole file/rank is attacked (g114 21.Nd6?? Qxd6). A bare pawn in her line = free grab with tempo (g116 15.Qxd5). RETREAT: queen-only guard loses to Qx/Q-trade/Rx (g107); KING-ONLY guard = no guard (g110).
- MATE NETS first: Qh2/Rh1; Qxg2#/Bb7 (g113); Qd1+ Be5+/Bxf4+ Qh1# (g114); Rg7# with Bf6 guarding g7 (g117).

## Rule 2 - the queen
- Hit by anything: she moves THAT move; 'defended' never counts (g95). No capture on a defended square; no trade without MY surviving recapturer; never on a standing bishop's ray (g105,g108,g109) or back on the ray that chased her (g102).
- QUEEN CAPTURE of a pawn: count EVERY defender; his recapture where mine cannot = Q for P (g110,g114,g115). QUEEN CHECKS only if the king CANNOT take (g106).

## Rule 3 - captures
- RECAPTURE is not a TRADE (g111 26.Rxc6?? Rxc6 = R for P): name what I win AND what he wins back. A piece guarded only by my queen dies to Qx + 2nd attacker (g103,g107,g109).
- PIN = recapturer frozen (g90); X-RAY = his rook files/bishop diagonals (g97); blocked recapture -> ...Bxa3! (g112).

## Rule 4 - material & clock
- Down: keep queens (repetition = half point); NO claw-back grabs - R taking a pawn his pawn guards = R for P (g116 20...Rxc3?? bxc3); refuse N-for-P (g116 16...Nf6?? exf6); keep blockaders home (g117 17...Nxf4??); 5-10 s/move.
- UP: trade pieces not pawns; escort passers; promote, mate, stalemate-check; 5-10 s. ROOK ENDING: equal = HOLD; R for P loses (g111).
- Time: book <=10 s, routine <=15 s, hard cap 20 s; <3 min <=5 s, <1 min 1-2 s. EQUAL = HOLD. g114-g117: 33-49 s on moves 10-22 every game and still blundered; ended 6:00-9:40 vs 13-15 min. Over 20 s = play the safe candidate.

## Openings
- Caro B Advance (g109,g110,g112,g116): ...Bf5/Bg6 e6 Nd7 c5 cxd4 Be7 Rc8 Qb6; NEVER ...Qxd4; no ...Nc5 while d4 stands; nothing on d6/f6 or ...Ngf6 while e5 stands; no ...Qd6 while Bf4 lives; vs b3/Ba3 ...Bxa3!. g116: 12.Nxf5 exf5 strips d5 -> 15.Qxd5 (pre-defend d5; keep ...Bg6).
- Caro B Classical (g107,g115,g117): ...Bg6 h6 Bh7 e6 Bxd3 Qxd3 Nd7 Ngf6 Be7 O-O =; f6-knight -> d5/e8, NEVER d7; no ...Nc3+; no ...Bf6/...Nf6 while his e5 stands; no ...Qxf4. g117: 17...Nxf4?? Bxf4 (keep the d5 blockader; slow ...Rac8/...Rfd8/...Qb6); 19.Qd7! Qxd7 20.Rxd7 hits e7.
- QGD W (0-8): Lasker 12.Nxf3!; keep c3+d4+Rc1, no c4 (g111); ...Qb4 hits b2 (Qc2 first); never Qx b7/d7/a8 with a c6-bishop. Bxf6 h6 (g113,g114): ...Nxd4 ...Bxd4 wins d4; 16.Bd5?? exd5; 21.Nd6?? Qxd6; 23.Qxd4?? Qxd4; no piece on d5(e6)/d6(Qd7).
- Ruy Chigorin W (0-5): 13.cxd4: Nf1 BEFORE Qe2; keep Rc1; equal = improve slowly. Chigorin B: no ...Bg4 after 9.h3; 10.e5 -> ...Ne8/...d6, never take e5; 9.Bd5! only 9...Nxd5! =.
- Dragon B: Rauzer 11...gxf6!; 13.Qxd5 -> ...Qc7 ONLY. Soltis 9.Bc4 (0-8): 14.h5 Nxh5!; 16.g5 -> only ...Nh5; no e4/Rxe4 grabs; no ...Qa5 after 15.Kb1.
- Alapin B: 5.Qxd4 Nc6/g6/Bg7/O-O/Nc5 =; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 10...bxc6!. Taimanov B: 12.Bxe5 12...Nxe4! =, never 12...Bd6?? Qxd6.
- Italian 4.d3 d5 (0-3): 5.exd5 Nxd5 6.O-O Bc5; Nf1-g3.

## Opponents
- SF19: instant; punishes loose units, queens on attacked lines, pawn-attacked squares (g110,g113); down: repetition.
- Sonnet 5.5 (1W g112, 1L g116): banks clock; takes every free/attacked unit. Vs my Caro Advance: 12.Nxf5 exf5 13.Be3! Qxd5 - never let d5 go bare; loose b3/Ba3 -> Bxa3; shields passers, promotes.
- GPT-6.1 Sol (won g114,g115,g117): fast, keeps 14:30; takes every free piece or piece on a pawn square; punishes any covered-square jump at once (g117 17...Nxf4??); equal = hold.
