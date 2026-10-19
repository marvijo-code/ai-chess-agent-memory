# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries on ONE move forfeit. T50 3rd had 3 invalid tries (moves 20/30/32), each recovered by a DIFFERENT legal move. Before sending list the piece's CURRENT square, destination and path; before CASTLING check king and rook unmoved and the two squares empty. After ONE rejection redraw a different move, never resend.
- ANY OF MY PIECES ON HIS PAWN'S CAPTURE SQUARE IS LOST - CHECKS INCLUDED. T50R3 44...Ra4+?? bxa4!; T49R4 21.Qd3?? cxd3; T49R2 10.Qxg4?? Bxg4. List every enemy pawn's two capture squares FROM THE BOARD before landing; a pawn 'defender' does not make the square safe.
- A CAPTURE THAT UNSCREENS A LINE RE-ARMS THE PIECE BEHIND IT. T50R4 14...Bxe5?? 15.Bxe5 Qxe5+ 16.Qxe5! In any 2+ capture chain redraw after EACH capture and name HIS last capturer and the line it now uses.
- HIS PIECE GUARDED ONLY BY HIS QUEEN IS FREE IF MY OTHER PIECE COVERS THE RECAPTURE SQUARE (T50R3 18...Nxd5! won a bishop). Name each defender AND who covers the square after my capture.
- A CAPTURE THAT LEAVES HIM A PIECE AHEAD IS A SAC (T50R2 11.Nxd5??). Write 'W pieces / B pieces' after every chain; never NxP on a defended square without a named recapture.
- A WARNING I WRITE IS AN ORDER FOR THE NEXT MOVE (T49R1, T50R3). Re-read the last comment before choosing.
- THE PIECE I MOVE MAY BE g7's ONLY GUARD (T49R1, T50R1): an uncastled king never guards g7; ...h6 is luft only for Kg8. With his queen near g3 ask 'what guards g7 after this?' - or castle.
- COUNT EVERY DEFENDER BEFORE ANY CAPTURE, FULL DIAGONALS BOTH WAYS (T49R2 Bc8 guarded g4; T49R3 18.Qxd8+?? Bf6). A check is not a forcing win; up material there is no queen grab.
- A PAWN-ATTACKED PIECE MUST MOVE; defending it does not save it (T49R3 12.exf6!). Mirror: when HIS pawn attacks my piece, move it now; when MY pawn attacks his, take.
- A LANDING SQUARE IS A CAPTURE SQUARE: 16.Nd6?? Bxd6; 12...Nd5?! into Nc3. List every enemy capturer of the arrival square first.
- Qg3 + his bishop reaching e5/f6 = Qxg7# (T48 Final 13...dxe5??). Put a PIECE on g7 or decline the central break; T50R4: never capture on e5 while his Qg3-Bf4 battery screens it.
- CHECKED? List block/capture squares and which of my pieces sit on the checker's line.
- QUEEN TRADE = RECAPTURE CHAIN ON MY CENTRAL KNIGHT (T48R1 11.Qd2?? ...Nxd4/...Bxd4). Block with a guarded piece or keep queens.
- DOWN A QUEEN OR PIECE v SF: no rescue; guard every unit, 5-10 s moves.
- A QUICK MOVE STILL GETS THE SCAN. Speed is fine only when the per-move list is written.

## Endings, king safety, conversion
- KING ON h1 + HIS QUEEN ON g3 = HIS ROOK ON e1 IS MATE (T50R2 30...Re1#). After Kh1 name the rank-1 squares his rooks reach; keep a piece on e1/e2.
- Q+R v BARE K (T50 3rd): Qc6+ Kb8 Qb6+ Ka8/c8 Rd8# - rook protected by the queen on b6. Queen checks drive the king to the edge, then the rook check on the 8th; name his flights and check stalemate each move.
- UP A ROOK, 2R v R (T50 3rd): take the first clean rook trade (26.Rxe6 dxe6), then collect the loose pawns with the last rook (a6/d4/b4/h7/e6). A bare king standing on my passer's square (33...Ke4!) cannot be pushed - drive it off with a rook check (43.Rd8+) before promoting.
- UP MATERIAL IN R+B vs R: STOP THE PASSER BEFORE RACING (T50R3). Racing pawns is the last plan, not the first.
- A ROOK NEEDS A SAFE SQUARE, NOT A CHECK (T50R3 ...Ra4+ chosen only to drive his king off c4). Every rook/queen move: his pawn capture squares, then sliders, then the purpose.
- TWO ROOKS (or R+R+N) v QUEEN: draw by blockade, not raids (T49R3: rook on the f-file, rook on d1, knight c3). T49R4 2R+N v Q+pawns: one rook on the passed pawn, the other active.
- DOWN A QUEEN v SF: hold the blockade, keep every unit guarded, trade nothing into his queen's files, wait for his error (T50R4 held 28 moves to move 43).

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. My losses are scan misses, not the clock: T50 3rd had ~44 min left vs his ~20 and still spent 3:27 on Bf3 and 3 invalid tries. Never a time problem - bad moves are.

## Opening: English reversed QGD as BLACK
- 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies), then ...Bf5/...Nbd7/...Re8/...Qb6.
- ...Qb6 wins the IQP d4 when HIS Nd2 blocks Qd1 (T50R3 12...Qxd4!). With the extra pawn, ...c5 took the c6 guard off d5 and lost it back - keep ...c6 or ...Ne4 support first.

## Opening: Open Sicilian Taimanov (both colours)
- 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies; 6...Nf6 7.O-O Be7 transposes). Then f4/Qd2/Rad1 (White) or ...Qc7/...b5/...Bb7/...Rfc8 (Black).
- WHITE WIN v GLM (T50 3rd): 9.Qd2 b5 10.f4 Bb7 11.e5 Nxd4 12.Bxd4 Nd5 13.Nxd5 Bxd5 14.Bf3 (11 plies) - the e5 clamp. Trade the d5-bishop into doubled d-pawns, Qe3 behind e5, and if he plays ...f6 then exf6 Bxf6 Be5! offers the bishop; after ...Qc4 sidestep, Bxf6 gxf6 Qd3 forces the queen trade into 2R v R.
- 12.exf6! takes a knight with a PAWN whatever recaptures (T49R3, +piece by move 13). BAN premature f4-f5.
- T50R2 9...d5 10.exd5 exd5: trade the f6-knight FIRST; never 11.Nxd5??.
- T49R4 12.Nxc6! after ...Nxe4?? 13.Nxe7+ Qxe7 14.Nxe4 - an in-between check beats resolving a queen attack.
- As BLACK v his 9.f4/10.Qd2: ...Nxd4 then ...b5/...Bb7/...Rfc8; ...Qc7 covers c6 and eyes e5. Do NOT jump ...Nd5 into his Nc3.

## Opening: Open Sicilian Dragon (me White)
- 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 Ng4 (16 plies): that Ng4 is GUARDED by Bc8 through d7-e6-f5. Answer with h3 or 9.Nxc6 bxc6 10.Bg5; NEVER Qxg4.
- T48R1 Dragon ...d5: 8.exd5 Nxd5 9.Nxd5 Qxd5! 10.Bf3 Qa5+ - do NOT block with Qd2??; use a guarded block (Bd2/c3).

## Opening: Taimanov as BLACK v Stockfish
- 1.e4 c5 2.Nf3 Nc6 3.Nc3 e6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.e5 Nd5 8.Qf3 Nxc3 (16 plies). The standard ...Be7/...O-O/...Qc7/...Bf4/...d6 is level to move 12, but ...Nxc3 hands him c3+d4+e5 - take it only for a concrete reason.
- T50R4 main branch: 9.bxc3 Qc7 10.Qg3 g6 11.h4 Bg7 12.Bf4 O-O 13.h5 (7 plies). Level to move 13 (-0.4ish); with queens on do NOT open the centre (13...c5?!) and NEVER take on e5: 14...Bxe5?? let 15.Bxe5 Qxe5+ 16.Qxe5 (his Qg3 re-guarded e5 through the f4 square his own bishop vacated). Plan ...Bb7/...f6/...Rfc8 and wait; take e5 only when his Bf4 is gone or his queen has left g3.
- T49R1 (8...Qc7 9.Qg3 h6 10.Ne4): king on e8, Bf8 the ONLY g7 guard; 10...Be7? lost a rook to 11.Qxg7. ...O-O or keep Bf8 home; ...h6 is luft only for Kg8.
- T49 Final: 11...O-O? allowed 12.Bxc6! winning the a8 rook - after ...bxc6 nothing recaptures on c6. Play ...Qc7 FIRST.
- T50R1: after 12.Qxh8 down a rook, ...Nb4?? lost to 13.Nf6+ 14.Qxf8#. Down material, audit every enemy knight landing for check + fork + mate.

## Opponents
- Stockfish 19 (depth 4): instant, no second chances. Punishes any piece I call 'undefended' (hidden defender Bc8-g4), pounces on any capture that opens a bishop to g7, plays Bxc6! on an unguarded c6, builds a slow h4/h5/Bf4/Qg3 clamp and converts a queen up without gifts.
- DeepSeek V4.1 Flash (mirror): solid Taimanov as Black, 1-8 min thinks, converts a piece-up position without gifts (...Nxd5 ...Nxd4 ...Be6 ...Qd7, then 30...Re1#). My losses to it were my own blunders - win on the checklist.
- GLM 5.3 Flash: as White the English reversed QGD (1-5 s early, 2-3 min middlegame, banks clock, punishes a rook on a pawn capture square, 3 illegal tries in T50R3). As BLACK now the Taimanov (...a6/...b5/...Bb7/...Be7/...O-O, 3-6 min thinks): allowed my 11.e5 clamp, played ...Nd5/...Bxd5 into doubled d-pawns, then defended R v 2R by standing its king on my passer's square (33...Ke4!) but left a6/d4/b4/h7 loose and lost them. 1 invalid try here. Plan: f4/e5 clamp, trade into 2R v R, take the loose pawns, put nothing on its pawn's capture square.

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
- T50R3 Black v GLM (English reversed QGD): 0-1 m56 (Rd8#). 12...Qxd4!, 18...Nxd5! built +piece; 44...Ra4+?? bxa4 gave a rook back and his a-pawn queened. 1 illegal try.
- T50R4 Black v SF19 (Taimanov): 0-1 m43. 14...Bxe5?? queen for a pawn; down Q from move 15, held 28 more moves, 0 illegal, 45 min left.
- T50 3rd White v GLM (Taimanov): 1-0 mate m51. 11.e5 clamp, traded to his doubled d-pawns, queen trade on d3; 23.fxe5 won a rook, then ate a6/d4/b4/h7, promoted, 51.Rd8#. 3 invalid tries, ~44 min left.

Note files:
- notes/stockfish-dragon-queen-trade.md - SF19 Dragon ...d5, the Qd2?? queen trade and king-move legality.
- notes/taimanov-black-g7-battery.md - SF19 as White in the Taimanov, the dxe5/Bxe5/Qxg7 mate and the g7 audit.
- notes/black-taimanov-guards.md - T49 Final and T50R1: the c6 guard and the g7 guard with an uncastled king.
- notes/black-taimanov-e5-screen.md - T50R4: the e5 capture that unscreened his Qg3, and the 9...Qc7/10.Qg3 branch.
- notes/white-dragon-yugoslav.md - T49R2: the Ng4/Bc8 trap and correct ...Ng4 answers.
- notes/white-taimanov-qd2-f4.md - T49R3/T50R2/T50 3rd: the Qd2/f4/e5 clamp win, Nxd5??, Qh6??, 2R v R conversion.
- notes/white-taimanov-glm-t49r4.md - T49R4: the Nxe7+ intermezzo, Qd3?? cxd3, GLM's clock.
- notes/black-english-reversed-qgd-t50r3.md - T50R3: ...Qb6 v his slow build, ...c5?? losing the d5 guard, ...Nxd5!, the Ra4+?? rook loss and the passer race.
