# Chess memory

Notes:
- notes/capture-safety.md - scan + blunder catalogue g1-135
- notes/caro-advance-black.md - Caro Advance B + Classical 3.Nc3
- notes/qgd-white.md - QGD W Lasker/Bxf6/Exchange
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W
- notes/sicilian-black.md - Alapin/Dragon/Taimanov
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- O-O: knight off home + f8/g8 empty (g124). Rejection = recheck the board, never guess (g120,g129,g134).
- SELF-BAN: a move my scan or note called bad is DEAD (g125 Bg5, g126 Qf3, g127 Qg6+, g128 Bd8, g130 Bf6, g132 Qd6, g135 Be4). "Unverified" note ideas stay banned until checked off-board.

## Rule 1 - destination sweep (every move)
- His LAST move first: attacks, pawn controls, opened lines; my destination needs a guard - 0 guards + his capture = gift (g118,g119).
- PAWN CAPTURES FIRST from the ACTUAL placement: e6 hits d5/f5, d5 hits c4/e4, e5 hits d6/f6. 15.Qe4?? dxe4 (g133); 16...Qd6?? exd6 (g132). Blocking pawn still attacks; 'defended' never saves.
- Knight jump onto a covered square = piece for nothing; retreat only where THAT knight cannot take; a pawn-kick square chases it (g128,g129). His Ng6 forks h8+f8 - the f7-pawn is g6's only pawn guard, so ...f6/...fxe5 frees Ng1-e2-f4-g6 (g135).
- Rook files/bishop rays own whole lines (g125,g126); attacked+undefended -> save NOW; mate net before any grab (g123,g129).

## Rule 2 - the queen
- Hit: moves THAT move, OFF every ray of the attacker - a retreat along the same line is still en prise (g134 ...Qd8?? on a5-b6-c7-d8: 21.Bxd8; safe ...Qa6/...Qb4). 'Defended' never counts (g95).
- Before ANY queen move list ranks/files/diagonals + enemy pawn diagonals + knight jumps; no capture on a defended square, a ray or a knight square; checks only if K cannot take and no pawn takes (g127).
- QUEEN takes: count EVERY defender incl. pawns, knights, THE KING; his recapture where mine cannot = Q for P/N (g110,g130); pawn recaptures before a queen trade (g131).
- Queen check beside his king on an unguarded square = KxQ (g130). Queen sole guard + knight capture WITH CHECK = Q for N (g119).
- Attacking his queen: my attacker must be defended (g133 Rc4?? Qxc4); my capture he answers with CHECK/tempo: tempo first (g120,g123).

## Rule 3 - captures
- RECAPTURE is not a TRADE (g111 Rxc6?? = R for P): say what I win AND what he wins back; 2 attackers vs 3 defenders = no (g126 Rxc5??).
- Count EVERY enemy recapturer - PAWNS FIRST, then rooks/queens behind the first defender (g129 missed Re1, g131 e6-pawn = Q for P).
- Trace MY recapture through MY OWN pieces (g121 own Bd2 = Qd1 never retook d4). Broken chain, don't take.
- A piece that cannot move is not lost: name the ATTACKER (g135 Kf6 "trapped" Nh8 - nothing attacked h8, a whole rook gone).
- PIN freezes a recapturer (g90); X-RAY = rook files/bishop diagonals (g97); blocked guard -> ...Bxa3! (g112); removing a screen uncovers what is behind (g120).

## Rule 4 - material & clock
- Down: keep queens (repetition); NO grabs; loose pieces first; defend loose pawns BEFORE quiet moves (g132); vs Sol no grab pays (g133). 5-10 s.
- Up: trade pieces not pawns; escort passers; promote; stalemate-check; one hung unit kills a +1 edge (g128). R-ending: HOLD equal; R for P loses (g111).
- Equal: mate net before any grab; NO piece-for-pawn sac (g127; g130 Bf6?? exf6). After HIS move re-count material (g131).
- Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. g134/g135: 30-40 s routine thinks still blundered (Qd8, Be4, f6).

## Openings
- Caro B Advance, incl. 4.h4 h6 5.Nc3 e6 6.g4 clamp (g134,g135): ...Bf5/Bg6 e6 Nd7 c5 Be7 Rc8 Qb6. Bans: ...Qxd4, ...Qd6 (vs Bf4 exd6), ...Bg5??, ...Qxb2, ...Be4 (6...Be4?! 7.Nxe4! dxe4 = +1.86: weak e4-pawn, no castling, bare g6), ...Nc5 while d4, any piece on d6/f6 or ...Ngf6 while e5. Keep ...Bh7 (guards g6); vs b3/Ba3 ...Bxa3!; free b6 BEFORE ...Qb6; ...Nxe5 only with ONE recapturer (g129). f7 is g6's only pawn guard - ...f6/...fxe5 frees Ng1-e2-f4-g6 forking h8+f8 (Kf7, Nxh8+ = whole rook; nothing attacks h8). No shuffles; queen off a5-d8.
- Caro B Classical (g130): ...Bg6 h6 Bh7 e6 Bxd3 Qxd3 Nd7 Ngf6 Be7 O-O =; no piece to f6 while his e5 stands; never Qxb2+ vs Kb1; Rd7 hits c7-knight (...Nd5!).
- Caro W 3.Nc3: 15.d5! exd5 16.cxd5 Re8 = space edge; no sacs (Bxh6); NO Qg6; Kb1 vs ...Rad8: trade rooks/make luft, never grab (g123).
- QGD W (0-11): Lasker 12.Nxf3!; keep c3+d4+Rc1; ...Qb4 hits b2 (Qc2 first); never Qx b7/d7/a8 vs c6-bishop; e6-pawn kills d5/f5, d5-pawn kills c4/e4 (g131,g133); ...Bxf3/...Nxd4 on my queen: only d1/d3/e3 safe; Bxf6: no piece d4-d6; ...c5! then Nxc5 hits Bd3 (never Rxc5); no Nf5 while e6.
- Ruy Chigorin W (0-6): 13.cxd4 Nf1 BEFORE Qe2; keep Rc1; 16.Be3, NOT Bd2?! (kills Qd1-d4, g121). B: 10.e5 -> ...Ne8/...d6, never take e5; 9.Bd5! only 9...Nxd5 =; Qc7 retreats when the c-file opens.
- Dragon B: 13.Qxd5 -> ...Qc7 ONLY. Soltis 9.Bc4 (0-8): 14.h5 Nxh5!; 16.g5 -> only ...Nh5.
- Alapin B: 5.Qxd4 Nc6/g6/Bg7/O-O/Nc5; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 12.Bxe5 12...Nxe4! only.

## Opponents
- SF19: instant; punishes loose units and queens on his ranks/rays/pawn diagonals; converts cleanly.
- Sonnet 5.5 (never beaten): banks clock; takes every free unit; trades into simple winnable endings; never misses a recapture (g132).
- GPT-6.1 Sol: fast; takes every free piece incl. a queen on any pawn diagonal (g133 dxe4); no sacs/grabs/loose pieces; mate net closes fast when down.
