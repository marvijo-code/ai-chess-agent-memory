# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries on ONE move forfeit. T47R1, T48R1, T49R1, T49 Final, T50R2 (one try on 8.Be3), T50R3 (one try on 51...Bf8). Before sending list the piece's CURRENT square, destination and path; before CASTLING check king and rook unmoved and the two squares empty. After ONE rejection redraw and pick a DIFFERENT move, never resend.
- ANY OF MY PIECES ON HIS PAWN'S CAPTURE SQUARE IS LOST - CHECKS INCLUDED. T50R3 44...Ra4+?? bxa4! (the b3-pawn's capture square); T49R4 21.Qd3?? cxd3; T49R2 10.Qxg4?? Bxg4. Before every queen/rook/bishop landing write every enemy pawn's two capture squares FROM THE BOARD; a pawn 'defender' does not make the square safe.
- HIS PIECE GUARDED ONLY BY HIS QUEEN IS FREE IF MY OTHER PIECE COVERS THE RECAPTURE SQUARE. T50R3 18...Nxd5! won a bishop: his Bd5 looked defended by Qd1, but my Be6 covered d5, so Qxd5?? Bxd5 lost his queen. Name each defender AND who covers the square after my capture.
- A CAPTURE THAT LEAVES HIM A PIECE AHEAD IS A SAC. T50R2 11.Nxd5?? (Nf6 recaptured and stayed). After every capture chain write 'W pieces / B pieces' from the board; never NxP on a defended square without a named recapture.
- A WARNING I WRITE IS AN ORDER FOR THE NEXT MOVE. T49R1 wrote 'watch Nf6+' then played ...Nb4??; T50R3 wrote 'keep my rook safe' and played ...Ra4+??. Re-read the last comment before choosing.
- THE PIECE I MOVE MAY BE g7's ONLY GUARD (T49R1, T50R1). An uncastled king never guards g7; ...h6 is luft only for a Kg8. With his queen near g3 ask 'what guards g7 after this?' - or castle.
- COUNT EVERY DEFENDER BEFORE ANY CAPTURE, FULL DIAGONALS BOTH WAYS (T49R2 Bc8 guarded g4; T49R3 18.Qxd8+?? Bf6). A check is not a forcing win; up material there is no queen grab.
- A PAWN-ATTACKED PIECE MUST MOVE; defending it does not save it (T49R3 12.exf6!). Mirror: when HIS pawn attacks my piece, move it now; when MY pawn attacks his, take.
- A LANDING SQUARE IS A CAPTURE SQUARE: 16.Nd6?? Bxd6; 12...Nd5?! into Nc3. List every enemy capturer of the arrival square first.
- Qg3 + his bishop reaching e5/f6 = Qxg7# (T48 Final 13...dxe5??). Put a PIECE on g7 or decline the central break.
- CHECKED? List block/capture squares and which of my pieces sit on the checker's line.
- QUEEN TRADE = RECAPTURE CHAIN ON MY CENTRAL KNIGHT (T48R1 11.Qd2?? ...Nxd4/...Bxd4). Block with a guarded piece or keep queens.
- DOWN A QUEEN OR PIECE v SF: no rescue; guard every unit, 5-10 s moves. The mirror converts cleanly too (T50R2 11...Nxd5, 30...Re1#).
- A QUICK MOVE STILL GETS THE SCAN (T48 Final 5-20 s/move lost to a skipped g7 audit; T50R3 1:34 on ...Ra4+). Speed is fine only when the per-move list is written.

## Endings, king safety, conversion
- KING ON h1 + HIS QUEEN ON g3 = HIS ROOK ON e1 IS MATE (T50R2 30...Re1#). After my king goes to h1, name the rank-1 squares his rooks reach and keep a rook/pawn on e1/e2.
- UP MATERIAL IN R+B vs R: STOP THE PASSER BEFORE RACING. T50R3 (B+3P v R+2P) I pushed ...f5/...f4/...f3 and his a-pawn queened first; the rook or bishop had to hold a6/a7 and my king had to come. Racing pawns is the last plan, not the first.
- A ROOK NEEDS A SAFE SQUARE, NOT A CHECK. T50R3 ...Ra4+ was picked only because it 'forced his king off c4'; the destination sweep was skipped. Every rook/queen move: his pawn capture squares, then sliders, then the purpose.
- TWO ROOKS (or R+R+N) v QUEEN: draw by blockade, not raids (T49R3: rook on the f-file, rook on d1 covering e1, knight c3 shielding b2/a2). T49R4 2R+N v Q+pawns: one rook on d1 vs the passed pawn, the other active.

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. My losses are scan misses, not the clock. T50R3: I finished with ~27 min and the opponent ~8 min; the blunder came from a 1:34 'forcing' check, not from pressure. Never a time problem - bad moves are.

## Opening: English reversed QGD as BLACK (T50R3)
- 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies), then ...Bf5/...Nbd7/...Re8/...Qb6 - solid, level to move 11. His plan d4/Bf4/Re1/Nd2-f1 is slow; ...Qb6 wins the IQP d4 when HIS Nd2 blocks Qd1 (T50R3 12...Qxd4!).
- With the extra pawn, ...c5 (T50R3 m14) was a mistake: it took the c6 guard off d5, so after 'Nxd5 Nxd5 Bxd5' he regained the pawn. Keep ...c6 or ...Ne4 support before the break.
- Winning pattern (T50R3): his piece guarded only by his queen + my other piece covering the trade square = ...Nxd5!/...Bxd5!. Then trade queens into R+B v R and stop his passers.

## Opening: Open Sicilian Taimanov (both colours)
- 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O then f4/Qd2/Rad1 (White) or ...Qc7/...b5/...Bb7/...Rfc8 (Black).
- T49R3 WHITE plan that worked: 9.Qd2 b5 10.f4 Bb7 11.e5 Qc7 12.exf6! (8 plies), then ...Bxf6 13.Nxc6 dxc6 14.Rad1 - a piece up by move 13. BAN premature f4-f5.
- T50R2 WHITE, the ...d5 answer: 9.Qd2 d5 10.exd5 exd5, then d5 is guarded by Nf6 AND Qd8 - trade the f6-knight FIRST; never 11.Nxd5??.
- T49R4 (v GLM): 12.Nxc6! worked because after ...Nxe4?? the in-between 13.Nxe7+ Qxe7 kept c6, then 14.Nxe4 won a piece. A check or a bigger capture beats resolving a queen attack.
- As BLACK v his 9.f4/10.Qd2: ...Nxd4 then ...b5/...Bb7/...Rfc8; ...Qc7 covers c6 and eyes e5. Do NOT jump ...Nd5 into his Nc3.

## Opening: Open Sicilian Dragon (me White)
- 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 Ng4 (16 plies): that Ng4 is GUARDED by Bc8 through d7-e6-f5. Answer with h3 or 9.Nxc6 bxc6 10.Bg5; NEVER Qxg4.
- T48R1 Dragon ...d5: 8.exd5 Nxd5 9.Nxd5 Qxd5! 10.Bf3 Qa5+ - do NOT block with Qd2??; use a guarded block (Bd2/c3).

## Opening: Taimanov as BLACK v Stockfish
- 1.e4 c5 2.Nf3 Nc6 3.Nc3 e6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.e5 Nd5 8.Qf3 Nxc3 (16 plies). Standard continuation ...Be7/...O-O/...Qc7/...Bf4/...d6 is level to move 12, but ...Nxc3 hands him c3+d4+e5 - take it only for a concrete reason.
- T49R1 (8...Qc7 9.Qg3 h6 10.Ne4): king on e8, Bf8 the ONLY g7 guard; 10...Be7? lost a rook to 11.Qxg7. ...O-O or keep Bf8 home; ...h6 is luft only for Kg8.
- T49 Final: 11...O-O? allowed 12.Bxc6! winning the a8 rook - after ...bxc6 nothing recaptures on c6. Play ...Qc7 FIRST.
- T50R1 same line: after 12.Qxh8 down a rook, ...Nb4?? lost to 13.Nf6+ 14.Qxf8#. Down material, audit every enemy knight landing for check + fork + mate.

## Opponents
- Stockfish 19 (depth 4): instant, no second chances. Punishes any piece I call 'undefended' (hidden defender Bc8-g4), pounces on any capture that opens a bishop to g7, plays Bxc6! on an unguarded c6, and converts a queen up without gifts.
- DeepSeek V4.1 Flash (mirror, T49R1 and T50R2): solid Taimanov as Black, 1:04-8:23 thinks, converts a piece-up position without gifts (T50R2 ...Nxd5 ...Nxd4 ...Be6 ...Qd7, then 30...Re1#). My losses to it were my own blunders - win on the checklist.
- GLM 5.3 Flash: as White now plays the English reversed QGD (1.c4/2.Nc3/3.g3 v my ...Nf6/...e6/...d5), 1-5 s early and 2-3 min in the middlegame, banks a huge clock, 3 invalid tries in T50R3, takes any piece left on a pawn capture square (bxa4), and mated me with Q+R. Play 10-15 s sound moves, guard every unit, never put a rook or queen where a pawn takes it.

## Record
- T47R1 White v GLM: 1-0 forfeit; one piece up after 19.Nxe4.
- T48R1 White v SF19: 0-1 mate. 11.Qd2?? lost a bishop in the queen trade; 2 illegal king tries.
- T48 Final Black v SF19: 0-1 (Qxg7# m15). 13...dxe5??; level to move 12.
- T49R1 Black v mirror: win by forfeit m13; 1 illegal (O-O with Ng8 home).
- T49R2 White v SF19: 0-1 m28. 10.Qxg4?? Bxg4 won my queen.
- T49R3 White v GLM: draw 3-fold. +piece after 12.exf6!; 18.Qxd8+?? Bxd8; then held 2R v Q.
- T49R4 White v GLM: 1-0 on time. +piece after 12.Nxc6 13.Nxe7+ 14.Nxe4; 21.Qd3?? cxd3; GLM flagged at 0:46.
- T49 Final Black v SF19: 0-1. 11...O-O? 12.Bxc6! won the a8 rook; ...Qc7 guards c6.
- T50R1 Black v SF19: 0-1 m14. 10...Be7? left g7 unguarded (Ke8), 11.Qxg7 Bf8 12.Qxh8; 12...Nb4?? 13.Nf6+ 14.Qxf8#.
- T50R2 White v mirror: 0-1 m30. 11.Nxd5?? knight for a pawn; 16.Qh6?? gxh6; 30...Re1#.
- T50R3 Black v GLM (English reversed QGD): 0-1 m56 (Rd8#). 12...Qxd4!, 18...Nxd5!, 20...Nxf4, ...Bxh4, ...Bxb3 built +piece; 44...Ra4+?? bxa4 gave a rook back and his a-pawn queened. 1 illegal try.

Note files:
- notes/stockfish-dragon-queen-trade.md - SF19 Dragon ...d5, the Qd2?? queen trade and king-move legality.
- notes/taimanov-black-g7-battery.md - SF19 as White in the Taimanov, the dxe5/Bxe5/Qxg7 mate and the g7 audit.
- notes/black-taimanov-guards.md - T49 Final and T50R1: the c6 guard and the g7 guard with an uncastled king.
- notes/white-dragon-yugoslav.md - T49R2: the Ng4/Bc8 trap and correct ...Ng4 answers.
- notes/white-taimanov-qd2-f4.md - T49R3/T50R2: the Qd2/f4/e5/exf6 plan, the Nxd5?? and Qh6?? losses.
- notes/white-taimanov-glm-t49r4.md - T49R4: the Nxe7+ intermezzo, Qd3?? cxd3, GLM's clock.
- notes/black-english-reversed-qgd-t50r3.md - T50R3: ...Qb6 v his slow build, ...c5?? losing the d5 guard, ...Nxd5!, the Ra4+?? rook loss and the passer race.
