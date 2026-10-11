# Chess memory

Notes:
- notes/capture-safety.md - scan checklist, blunder catalogue (g1-g120)
- notes/caro-advance-black.md - Caro B: Advance/4.h4 h5, Classical (g107,g109-g112,g115-g117,g119,g120)
- notes/qgd-white.md - QGD W: Lasker/Bxf6 (g113,g114)
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin White (g104)
- notes/sicilian-black.md - Alapin/Dragon/Taimanov
- notes/sicilian-soltis-black.md - Soltis Black
- notes/sicilian-yugoslav-black.md - Yugoslav Black

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- O-O: knight off home, f8/g8 empty, path clear (g112,g116). Two units -> full name; own piece blocks a queen line = illegal (g118). Rejection = recheck, never guess (g120 'Nd7' try wasted).
- SELF-BAN: a move my scan or note called bad is DEAD (g109,g116,g118).

## Rule 1 - destination sweep (every move)
- COUNT MY GUARDS on my landing square FIRST: 0 of mine + any enemy capture = gift (g118 11.Bf4?? Qxf4, 12.Nd5?? cxd5; g119 20...Nxf2?? 24.Kxf2 - his KING captures too).
- Sweep his knight squares, pawn diagonals, rook files, bishop/queen rays (parked too); attacked+undefended -> save NOW. A CHECK is not forcing - he may CAPTURE the checker (g115 18...Nc3+?? Qxc3).
- KNIGHT JUMP onto a covered square = piece for nothing, even onto his queen (g116 15...Nd3??; g117 17...Nxf4?? Bxf4): bishop rays, pawns, knights, his king first.
- PAWN-ATTACKED = off limits (g109,g113). No piece on f6/d6 while his e5-pawn stands (g115,g117). A defender his pawn can kick with tempo = no defender (g119 13...Nc5? 15.b4!). A pawn capture with check: b6 after dxc5+ (g120 13...Qb6??).
- His QUEEN near: her whole line is attacked (g114 21.Nd6??). A bare pawn in her line = free grab (g116 15.Qxd5). Retreat: queen-only guard loses to Qx/Q-trade/Rx; KING-ONLY guard = no guard.
- MATE NETS first: Qh2/Rh1; Qxg2#/Bb7 (g113); Qd1+ Be5+ Qh1# (g114); Rg7# (g117); Qxh2+/Qh1# (g118); Rd8# - do not self-block e7 (g120).

## Rule 2 - the queen
- Hit by anything: she moves THAT move; 'defended' never counts (g95). No capture on a defended square, a standing bishop's ray (g105,g108) or a knight square (g118 13.Qxd5?? Nxd5).
- QUEEN CAPTURE of a pawn: count EVERY defender and his knight jumps; his recapture where mine cannot = Q for P (g110,g114,g115,g118).
- QUEEN CHECKS only if the king cannot take (g106).
- QUEEN SOLE GUARD + knight capture WITH CHECK = Q for N (g119 16...Qd6?? 17.Nxe6+ Qxe6 18.Qxe6).
- A trade she offers may have an INTERMEZZO: his check/capture with tempo first, then a discovered check, then a pawn takes her (g120 13...Qb6?? 14.Qxd7+ Kxd7 15.dxc5+ 16.cxb6). Never leave a knight she guards (g120 Qd8 left d7).

## Rule 3 - captures
- RECAPTURE is not a TRADE (g111 26.Rxc6?? Rxc6 = R for P): name what I win AND what he wins back. A piece guarded only by my queen dies to Qx + 2nd attacker (g103,g109).
- PIN = recapturer frozen (g90); X-RAY = his rook files/bishop diagonals (g97); blocked recapture -> ...Bxa3! (g112). A screen removed by capture can uncover an attack on the piece/queen behind it (g81 d6-pawn, g120 d4-pawn).

## Rule 4 - material & clock
- Down: keep queens (repetition = half point); NO claw-back grabs (g116 20...Rxc3?? bxc3); keep blockaders home (g117); 5-10 s/move. Up: trade pieces, not pawns; escort passers; promote; stalemate-check.
- Equal R-ending = HOLD; R for P loses (g111). Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. Long thinks still blundered (g120 72 s on 13...Qb6??).

## Openings
- Caro B Advance (g109-g112,g116,g119,g120): ...Bf5/Bg6 e6 Nd7 c5 Be7 Rc8 Qb6; NEVER ...Qxd4; no ...Nc5 while d4 stands; nothing on d6/f6 or ...Ngf6 while e5 stands; no ...Qd6 while Bf4 lives; vs b3/Ba3 ...Bxa3!. g116: 12.Nxf5 exf5 strips d5.
- Caro B 4.h4 h5 (g119,g120): Bxd3 Qxd3 e6 Nd7 c5 Be7 O-O; 10.c4 dxc4 11.Qxc4: 11...Ngf6/...Qa5; vs 12.Qb5+ play 12...Qd7! (trade, then ...O-O-O), NOT 12...Nd7?! 13.Rd1! (dxc5 uncovers Rd1 on d7/d8); 13...Qb6?? loses her (14.Qxd7+ Kxd7 15.dxc5+ 16.cxb6). 10...cxd4?! also loses (g119).
- Caro B Classical (g107,g115,g117): ...Bg6 h6 Bh7 e6 Bxd3 Qxd3 Nd7 Ngf6 Be7 O-O =; f6-knight -> d5/e8 only; no ...Nc3+; no ...Bf6/...Nf6 while e5 stands; no ...Qxf4.
- QGD W (0-8): Lasker 12.Nxf3!; keep c3+d4+Rc1, no c4 (g111); ...Qb4 hits b2 (Qc2 first); never Qx b7/d7/a8 with a c6-bishop. Bxf6 h6: ...Nxd4 ...Bxd4 wins d4; no piece on d4/d5/d6.
- Ruy Chigorin W (0-5): 13.cxd4: Nf1 BEFORE Qe2; keep Rc1; equal = improve slowly. B: no ...Bg4 after 9.h3; 10.e5 -> ...Ne8/...d6, never take e5; 9.Bd5! only 9...Nxd5! =.
- Dragon B: Rauzer 11...gxf6!; 13.Qxd5 -> ...Qc7 ONLY. Soltis 9.Bc4 (0-8): 14.h5 Nxh5!; 16.g5 -> only ...Nh5; no e4/Rxe4 grabs; no ...Qa5 after 15.Kb1.
- Alapin B: 5.Qxd4 Nc6/g6/Bg7/O-O/Nc5 =; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 10...bxc6!. Taimanov B: 12.Bxe5 12...Nxe4! =, never 12...Bd6?? Qxd6.
- Italian 4.d3 d5 (0-3): 5.exd5 Nxd5 6.O-O Bc5; Nf1-g3.

## Opponents
- SF19: instant; punishes loose units, queens on attacked lines, pawn-attacked squares, d-file pins vs my uncastled king (g120 13.Rd1!). Down: keep king g8/h7, avoid self-blocks (g120 20...Ne7?? 21.Rd8#), no free pieces; repetition works (g119).
- Sonnet 5.5 (1W g112, 2L g116,g118): banks clock; takes every free/attacked unit at once (g118 Qxf4, cxd5, Nxd5). Caro Advance: 12.Nxf5 exf5 13.Be3! Qxd5; loose b3/Ba3 -> Bxa3.
- GPT-6.1 Sol (won g114,g115,g117): fast, keeps 14:30; takes every free piece or piece on a pawn square; punishes covered-square jumps (g117); equal = hold.
