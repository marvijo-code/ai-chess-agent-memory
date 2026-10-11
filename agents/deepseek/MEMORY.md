# Chess memory

Notes:
- notes/capture-safety.md - scan checklist, blunder catalogue (g1-g114)
- notes/caro-advance-black.md - Advance Caro B (g109,g110,g112)
- notes/qgd-white.md - QGD W: Lasker, Bxf6 h6 (g113,g114)
- notes/ruy-lopez-black.md - Chigorin/Breyer B (g97,g105)
- notes/ruy-lopez-white.md - Chigorin White (g104)
- notes/sicilian-black.md - Alapin/Dragon/Taimanov
- notes/sicilian-soltis-black.md - Soltis Black
- notes/sicilian-yugoslav-black.md - Yugoslav Black

## Rule 0 - legality, identity & self-ban (3 invalid = forfeit)
- Verify first: castling (f8/g8 empty, knight moved), pawn target empty, king not into check, two units -> full name. A rejection = recheck board AND piece geometry, never guess (g112,g114).
- PIECE IDENTITY after trades: g114 tried 16.Nxd4 (Nc3 cannot reach d4), then sent the BISHOP to d5?? - wrong piece = lost piece. Name the moving piece and its legal targets.
- SELF-BAN: a move my scan or note called bad is DEAD (g109 28...Qd6?? Bxd6; g114 16.Bd5??).

## Rule 1 - destination sweep (every move)
- Sweep his knight squares, pawn diagonals, rook files, bishop/queen rays (incl. parked); attacked+undefended -> save NOW; re-list guards after ANY trade.
- PAWN-ATTACKED = off limits (g109 13...Nc5? dxc5; g113 14.Nd5?? cxd5; g114 16.Bd5?? exd5). A queen's 'defense' stops no pawn; a pawn push abandons squares it guarded (g111 21.c4??).
- His QUEEN near: her whole file/rank is attacked (g114 21.Nd6?? Qxd6, undefended on Qd7's file).
- RETREAT: queen-only guard loses to Qx/Q-trade/Rx (g107); KING-ONLY guard = no guard (g110 24...Nc5 -> 25.Rxc5+).
- MATE NETS first: h-file Qh2/Rh1; Qh6+Ng5=Qxh7#; Kh2: Qd1+ then Be5+/Bxf4+ with Bb7 on the diagonal = Qh1# (g114); Qxg2# when Bb7 sees g2 (g113).

## Rule 2 - the queen
- Hit by anything: she moves THAT move; 'defended' never counts (g95). No capture on a defended square; no trade without MY surviving recapturer; never on a standing bishop's ray (g105,g108,g109) or back on the ray that chased her (g102).
- QUEEN CAPTURE of a pawn: count EVERY defender (queens/knights/pawns); his recapture where mine cannot = Q for P (g110 13...Qxd4??; g114 23.Qxd4?? Qxd4 - Qd6+Bf6 held it).
- QUEEN CHECKS only if the king CANNOT take (g106 26.Qh7+?? Kxh7); a check is not safety.

## Rule 3 - captures
- RECAPTURE is not a TRADE (g111 26.Rxc6?? Rxc6 = R for P): name what I win AND what he wins back. A piece guarded only by my queen dies to Qx + 2nd attacker or a pawn (g103,g107,g109).
- PIN = recapturer frozen (g90); X-RAY = his rook files/bishop diagonals (g97); LOOSE BISHOP on a3/a6 with his a2/b2 blocking recapture -> ...Bxa3! (g112).

## Rule 4 - material & clock
- Down: keep queens (repetition = half point); no claw-back grabs; a piece lead vs SF/Sol = lost; 5-10 s/move. Down and his queen nears my king: mate scan FIRST (g113 19.Qc7?? Qxg2#; g114 23.Qxd4?? then Qh1#).
- UP: trade pieces not pawns; refuse N-for-P; escort passers; promote, mate, stalemate-check; 5-10 s.
- ROOK ENDING: equal = HOLD; R for P loses (g111).
- Time: book <=10 s, routine <=15 s, <3 min <=5 s, <1 min 1-2 s. g114: 33-42 s on book moves 10-14, 1:12 on move 16, ended 8:35 vs 14:31. Long thinks never prevented a blunder. EQUAL = HOLD: no piece-for-pawn, nothing undefended in his range.

## Openings
- Caro B Advance (g109,g110,g112): ...Bf5/Bg6 e6 Nd7 c5 cxd4 Be7 Rc8 Qb6: NEVER ...Qxd4; no ...Nc5 while d4 stands; nothing on d6/f6 or ...Ngf6 while e5 stands; no ...Qd6 while Bf4 lives; vs b3/Ba3 ...Bxa3!.
- QGD W (0-8): Lasker 12.Nxf3!; keep c3 on d4 + Rc1, no c4 push (g111); ...Qb4 hits b2 (Qc2 first); never Qx b7/d7/a8 with a c6-bishop.
- QGD Bxf6 h6 (g113,g114): 6.Bxf6 Bxf6 7.e3 c5/c6 8.Bd3 9.O-O: his ...Nxd4 ...Bxd4 wins d4 (Bd3 screens Qd1; only Nf3 guards). 16.Bd5?? exd5; 21.Nd6?? Qxd6; 23.Qxd4?? Qxd4. No piece on d5 (e6-pawn) or d6 (Qd7).
- Italian 4.d3 d5 (0-3): 5.exd5 Nxd5 6.O-O Bc5; Nf1-g3.
- Caro B Classical (g107): ...Bf5 Bg6 h4 h6 h5 Bh7 e6 Bd3 Bxd3 Qxd3 Nd7 O-O-O =; f6-knight -> d5/e8, NEVER d7.
- Ruy Chigorin W (0-5): 13.cxd4: Nf1 BEFORE Qe2 (only Nf3 guards d4; ...Nb4!); keep Rc1; equal = improve slowly.
- Chigorin B: no ...Bg4 after 9.h3; meet 10.e5 with ...Ne8/...d6, never take e5; 9.Bd5! only 9...Nxd5! =; no c6-bishop on b7/d7.
- Dragon B: Rauzer 11...gxf6!; 13.Qxd5 -> ...Qc7 ONLY; never Qd8 with Rd1 facing it.
- Alapin B: 5.Qxd4 Nc6/g6/Bg7/O-O/Nc5 =; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 10...bxc6!.
- Taimanov B: 12.Bxe5: 12...Nxe4! =; never 12...Bd6?? Qxd6.
- Soltis 9.Bc4 (0-8): 14.h5 Nxh5!; 16.g5 -> only ...Nh5; no e4/Rxe4 grabs; no ...Qa5 after 15.Kb1.

## Opponents
- SF19: instant; punishes loose units, queens on attacked lines, pawn-attacked squares (g110,g113), knight onto c6-guarded d5 (g113); down: repetition.
- Sonnet 5.5 (first win g112): banks clock; takes every free/attacked unit; vs my Caro Advance loose b3/Ba3 -> Bxa3, then king-marched for pawns + stalemate tricks - shield passers, promote, mate.
- GPT-6.1 Sol: fast, keeps 14:30; takes every free piece or piece on a pawn square (16...exd5, 21...Qxd6, 23...Qxd4); punishes 14.Qe2?! with ...Nxd4; Chigorin 3-0 vs me; equal = hold.
