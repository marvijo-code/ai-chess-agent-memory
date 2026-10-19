# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries on ONE move forfeit. T50 3rd had 3 invalid tries (moves 20/30/32), each recovered by a DIFFERENT legal move. T51S2G1 1 invalid at 17...Qxe2, recovered. Before sending list the piece's CURRENT square, destination and path; before CASTLING check king and rook unmoved and the two squares empty. After ONE rejection redraw a different move, never resend.
- ANY OF MY PIECES ON HIS PAWN'S CAPTURE SQUARE IS LOST - CHECKS INCLUDED. T50R3 44...Ra4+?? bxa4!; T49R4 21.Qd3?? cxd3; T49R2 10.Qxg4?? Bxg4. List every enemy pawn's two capture squares FROM THE BOARD before landing; a pawn 'defender' does not make the square safe.
- A LANDING SQUARE IS A CAPTURE SQUARE, CHECKS TOO: 16.Nd6?? Bxd6; 12...Nd5?! into Nc3; T51R2 15.Nf6+?? exf6 - f6 is covered by his e7 AND g7 PAWNS, so a 'fork of king and rook' gave a knight for nothing. List every enemy capturer of the arrival square, pawns first, before any knight check.
- A CAPTURE THAT UNSCREENS A LINE RE-ARMS THE PIECE BEHIND IT. T50R4 14...Bxe5?? 15.Bxe5 Qxe5+ 16.Qxe5!; T51 Final 14...f6?? 15.exf6! opened Bf4-c7 to my Qc7, 16.Bxc7 won the queen (his PAWN left e5). In any 2+ capture chain redraw after EACH capture and name HIS last capturer and the line it now uses.
- HIS PIECE GUARDED ONLY BY HIS QUEEN IS FREE IF MY OTHER PIECE COVERS THE RECAPTURE SQUARE (T50R3 18...Nxd5! won a bishop). Name each defender AND who covers the square after my capture.
- A CAPTURE THAT LEAVES HIM A PIECE AHEAD IS A SAC (T50R2 11.Nxd5??). Write 'W pieces / B pieces' after every chain; never NxP on a defended square without a named recapture.
- A PAWN LOST IS GONE - NEVER 'BALANCE' WITH A QUEEN GRAB. T51R3 12...Qxc2?? his Qd1 guarded c2 and nothing of mine recaptured: queen for a pawn, mated 17 moves later. The mirror of it: his queen LEAVING the c2 guard makes c2 free (T51S2G1 16.Qxd4 16...Qxc2 won a pawn). Check where his queen stands NOW, not where it started.
- A WARNING I WRITE IS AN ORDER FOR THE NEXT MOVE (T49R1, T50R3). Re-read the last comment before choosing.
- THE PIECE I MOVE MAY BE g7's ONLY GUARD (T49R1, T50R1): an uncastled king never guards g7; ...h6 is luft only for Kg8. With his queen near g3 ask 'what guards g7 after this?' - or castle.
- COUNT EVERY DEFENDER BEFORE ANY CAPTURE, FULL DIAGONALS BOTH WAYS (T49R2 Bc8 guarded g4; T49R3 18.Qxd8+?? Bf6). A check is not a forcing win; up material there is no queen grab.
- A PAWN-ATTACKED PIECE MUST MOVE; defending it does not save it (T49R3 12.exf6!). Mirror: when HIS pawn attacks my piece, move it now; when MY pawn attacks his, take.
- Qg3 + his bishop reaching e5/f6 = Qxg7# (T48 Final 13...dxe5??). Put a PIECE on g7 or decline the central break; T50R4: never capture on e5 while his Qg3-Bf4 battery screens it.
- CHECKED? List block/capture squares and which of my pieces sit on the checker's line.
- QUEEN TRADE = RECAPTURE CHAIN ON MY CENTRAL KNIGHT (T48R1 11.Qd2?? ...Nxd4/...Bxd4). Block with a guarded piece or keep queens.
- A QUEEN IN FRONT OF HER KING ON AN OPEN FILE IS PINNED: a rook lift to that file wins her (T51R1 21.Rg3! pinned Qg6 to Kg8, 22.Rxg6+ hxg6 = Q for R). Every queen landing: is an enemy rook on that file? And never park my queen on my own king's file.
- DOWN A QUEEN OR PIECE v SF: no rescue; guard every unit, 5-10 s moves. T51R2: an initiative sac (Nf6+) only accelerated mate.
- A QUICK MOVE STILL GETS THE SCAN. Speed is fine only when the per-move list is written.

## Endings, king safety, conversion
- KING ON h1 + HIS QUEEN ON g3 = HIS ROOK ON e1 IS MATE (T50R2 30...Re1#). After Kh1 name the rank-1 squares his rooks reach; keep a piece on e1/e2. T51R2 same net: ...Rg3+/...Rg4+ drove Kh2-h1, then Qxd5+ 37.Rf3 Qxf3#.
- MY ...Bb7 + HIS Kg1 (g2 held only by his king, f2/h2 unable to block) = Qxg2# (T51S2G1 27...Qxg2#, Bb7 protected the queen). Look for it whenever his f2-rook leaves or his queen steps off g2's defence - a recurring Taimanov net.
- Bf6 + Qh6 v his Kg8: Qg7# when f8/d8/h7/h8 are covered or blocked by HIS OWN pieces (T51R1: his Rd7 blocked d7, his f7-pawn f8). Look for this net whenever a bishop reaches f6 with his f-pawn pinned/blocked.
- Q+R v BARE K (T50 3rd): Qc6+ Kb8 Qb6+ Ka8/c8 Rd8# - rook protected by the queen on b6. Queen checks drive the king to the edge, then the rook check on the 8th; name his flights and check stalemate each move.
- UP A ROOK, 2R v R (T50 3rd): take the first clean rook trade (26.Rxe6 dxe6), then collect the loose pawns with the last rook. A bare king standing on my passer's square (33...Ke4!) cannot be pushed - drive it off with a rook check (43.Rd8+) before promoting.
- UP MATERIAL IN R+B vs R: STOP THE PASSER BEFORE RACING (T50R3). Racing pawns is the last plan, not the first.
- A ROOK NEEDS A SAFE SQUARE, NOT A CHECK (T50R3 ...Ra4+). Every rook/queen move: his pawn capture squares, then sliders, then the purpose.
- TWO ROOKS (or R+R+N) v QUEEN: draw by blockade, not raids (T49R3: rook on the f-file, rook on d1, knight c3).
- DOWN A QUEEN v SF: hold the blockade, keep every unit guarded, trade nothing into his queen's files, wait for his error (T50R4 held 28 moves to move 43).

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. My losses are scan misses, not the clock: T50 3rd had ~44 min left vs his ~20 and still spent 3:27 on Bf3 and 3 invalid tries. T51S2G1 finished 52 min left vs his 30.

## Opening: English reversed QGD as BLACK
- 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies), then ...Bf5/...Nbd7/...Re8/...Qb6.
- ...Qb6 wins the IQP d4 when HIS Nd2 blocks Qd1 (T50R3 12...Qxd4!). With the extra pawn, ...c5 took the c6 guard off d5 and lost it back - keep ...c6 or ...Ne4 support first.

## Opening: Open Sicilian Taimanov (both colours)
- 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies; ...b5/...Bb7/...Qc7 first is the same setup). Then f4/Qd2/Rad1 (White) or ...Qc7/...b5/...Bb7/...Rfc8 (Black).
- AS BLACK v his 9.f4/10.Qd2 clamp: ...b5 is safe once ...a6 guards it (T51S2G1 11...b5 fine). After 12.e5 the f6-knight must NOT retreat to e8 - his knight then gets d7: Nxd7 wins a pawn and hits the f8-rook, then Nb6 hits a8-rook + c8-bishop (T51S2G1), and T51R3 11...Ne8? met Nc7 forking a8+e8. Play ...Nd5 (accept Nxd5 exd5, count guards) or ...Nh5. Counter: ...Qxc2 only once his queen has left d2's guard, and ...Bb7 sets up the Qxg2# net.
- AS BLACK, ...b5 NEEDS A GUARD BEFORE IT LANDS: ...a6 first (its pawn guards b5) or ...Bb7, else 12.Nxb5! wins it (T51R3). When his e5 kicks the f6-knight, do not park it on e8 while my a8-rook is home: Nc7/Nd7-b6 fork.
- WHITE CLAMP WIN (T50 3rd, T51R1): 9.f4 Nf6 10.Qd2 Be7 11.e5 Nxd4 12.Bxd4 Nd5 13.Nxd5 Bxd5 14.Bf3 (11 plies). Trade his d5-bishop (14...Bxf3 15.Rxf3), then 17.f5! d6 18.f6! gxf6 19.exf6 - NEVER Bxf6?? Rxf6; my e5 pawn vacates the d4-g7 line and his f6 capture loses a piece. His Be7 must crawl to d8, f7 and the f8-rook are walled, 20.fxe7 wins the bishop and his rook must go to e8.
- T51R1 finish: 21.Rg3! pins Qg6 to Kg8 (Q for R), 23.Bf6 hits his rook and covers g7, 24.Qh6 and Qg7#; his own Rd7 was blocked by his f7-pawn.
- 12.exf6! takes a knight with a PAWN whatever recaptures (T49R3, +piece by move 13). BAN premature f4-f5; f5 only after his ...d6 when the f6 wedge wins a piece.
- T50R2 9...d5 10.exd5 exd5: trade the f6-knight FIRST; never 11.Nxd5??.
- T49R4 12.Nxc6! after ...Nxe4?? 13.Nxe7+ Qxe7 14.Nxe4 - an in-between check beats resolving a queen attack.
- AS BLACK do NOT jump ...Nd5 into his Nc3. ...Qc7 covers c6 and eyes e5.
- Before moving my queen OFF the second rank check his ...Qxc2/...Qxb2 grab (T51R1 16.Qe3?! Qxc2 won a pawn; T51R2 14...Bxb2 did the same).

## Opening: Open Sicilian Dragon (me White)
- 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 Ng4 (16 plies): that Ng4 is GUARDED by Bc8 through d7-e6-f5. Answer with h3 or 9.Nxc6 bxc6 10.Bg5; NEVER Qxg4.
- T51R2: 9.h3?! met 9...Nxe3! (my Be3 taken by the knight, fxe3 doubles my e-pawns) and ...Bxb2 won a pawn; +1 for SF by move 10. Prefer 9.Nxc6 bxc6 10.Bg5, or h3 only after counting ...Nxe3 and accepting it for a concrete gain.
- T48R1 Dragon ...d5: 8.exd5 Nxd5 9.Nxd5 Qxd5! 10.Bf3 Qa5+ - do NOT block with Qd2??; use a guarded block (Bd2/c3).

## Opening: Taimanov as BLACK v Stockfish
- 1.e4 c5 2.Nf3 Nc6 3.Nc3 e6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.e5 Nd5 8.Qf3 Nxc3 (16 plies). The standard ...Be7/...O-O/...Qc7/...Bf4/...d6 is level to move 12, but ...Nxc3 hands him c3+d4+e5 - take it only for a concrete reason.
- T50R4 main branch: 9.bxc3 Qc7 10.Qg3 g6 11.h4 Bg7 12.Bf4 O-O 13.h5 (7 plies). Level to move 13; with queens on do NOT open the centre (13...c5?!) and NEVER take on e5: 14...Bxe5?? 15.Bxe5 Qxe5+ 16.Qxe5. Plan ...Bb7/...Rfc8 and wait; ...f6 only with his Bf4 off the c7 diagonal and his e5 pawn unable to capture (T51 Final 14...f6?? 15.exf6! Rxf6 16.Bxc7 won my queen).
- T49R1 (8...Qc7 9.Qg3 h6 10.Ne4): king on e8, Bf8 the ONLY g7 guard; 10...Be7? lost a rook to 11.Qxg7. ...O-O or keep Bf8 home; ...h6 is luft only for Kg8.
- T49 Final: 11...O-O? allowed 12.Bxc6! winning the a8 rook - after ...bxc6 nothing recaptures on c6. Play ...Qc7 FIRST.
- T50R1: after 12.Qxh8 down a rook, ...Nb4?? lost to 13.Nf6+ 14.Qxf8#. Down material, audit every enemy knight landing for check + fork + mate.

## Opponents
- Stockfish 19 (depth 4): instant, no second chances. Punishes any piece I call 'undefended' (hidden defender Bc8-g4), pounces on any capture that opens a bishop to g7, plays Bxc6! on an unguarded c6, plays ...Nxe3! on a kicked Ng4, takes a knight check with a PAWN (...exf6), builds a slow h4/h5/Bf4/Qg3 clamp and converts a piece up without gifts. Also punishes ...f6 by exf6 opening Bf4-c7 to my queen.
- DeepSeek V4.1 Flash (mirror): solid Taimanov both colours, 1-8 min thinks, converts without gifts (...Nxd5 ...Nxd4 ...Be6 ...Qd7, then 30...Re1#). T51R3: took my loose b5 with Nxb5!, then converted +Q for a pawn with zero gifts while I hung the queen on c2. T51S2G1 (as White, 6.Be2 clamp): 7:09 on 20.h3, 7:04 on 25.Rxf5, 0 illegal, but 17.Nc5?? let Qxe2 and 27.Qe3?? walked into Qxg2#. Win on the checklist, not on its clock.
- GLM 5.3 Flash: as White the English reversed QGD (1-5 s early, 2-3 min middlegame, punishes a rook on a pawn capture square, 3 illegal tries in T50R3). As BLACK the Taimanov (...a6/...b5/...Bb7/...Qc7/...Nf6/...Be7/...O-O, 1-3 min thinks). T51R1: allowed my e5 clamp and the f6 wedge, grabbed a loose c2-pawn, 1 invalid try, then with Qg6 in front of Kg8 missed my Rg3 pin and was mated by Bf6+Qh6. Plan: f4/e5 clamp, f5/f6 wedge, win his d5-bishop, look for the g-file pin.

## Record
- T47R1 White v GLM: 1-0 forfeit; one piece up after 19.Nxe4.
- T48R1 White v SF19: 0-1 mate. 11.Qd2?? lost a bishop in the queen trade; 2 illegal king tries.
- T48 Final Black v SF19: 0-1 (Qxg7# m15). 13...dxe5??; level to move 12.
- T49R1 Black v mirror: win by forfeit m13; 1 illegal (O-O with Ng8 home).
- T49R2 White v SF19: 0-1 m28. 10.Qxg4?? Bxg4 won my queen.
- T49R3 White v GLM: draw 3-fold. +piece after 12.exf6!; 18.Qxd8+?? Bxd8; then held 2R v Q.
- T49R4 White v GLM: 1-0 on time. +piece after 12.Nxc6 13.Nxe7+ 14.Nxe4; 21.Qd3?? cxd3.
- T49 Final Black v SF19: 0-1. 11...O-O? 12.Bxc6! won the a8 rook; ...Qc7 guards c6.
- T50R1 Black v SF19: 0-1 m14. 10...Be7? left g7 unguarded (Ke8), 11.Qxg7 Bf8 12.Qxh8; 12...Nb4?? 13.Nf6+ 14.Qxf8#.
- T50R2 White v mirror: 0-1 m30. 11.Nxd5?? knight for a pawn; 16.Qh6?? gxh6; 30...Re1#.
- T50R3 Black v GLM (English reversed QGD): 0-1 m56 (Rd8#). 12...Qxd4!, 18...Nxd5! built +piece; 44...Ra4+?? bxa4 gave a rook back and his a-pawn queened. 1 illegal try.
- T50R4 Black v SF19 (Taimanov): 0-1 m43. 14...Bxe5?? queen for a pawn; down Q from move 15, held 28 more moves, 0 illegal, 45 min left.
- T50 3rd White v GLM (Taimanov): 1-0 mate m51. 11.e5 clamp, traded to his doubled d-pawns; 23.fxe5 won a rook, ate a6/d4/b4/h7, promoted, 51.Rd8#. 3 invalid tries.
- T51R1 White v GLM (Taimanov): 1-0 mate m25. e5 clamp, 13.Nxd5 Bxd5 14.Bf3, 18.f6! gxf6 19.exf6 won his Be7 (20.fxe7), 21.Rg3! pinned Qg6 (22.Rxg6+ Q for R), 23.Bf6 24.Qh6 Qg7#. 0 invalid, ~48 min left; only 16.Qe3?! (c2 loose).
- T51R2 White v SF19 (Dragon): 0-1 m37 (Qxf3#). 9.h3?! Nxe3! (B for N, doubled e-pawns, ...Bxb2 won a pawn); 15.Nf6+?? exf6 gave a knight for nothing. 1 invalid try at 17.Bd5.
- T51R3 Black v mirror (Taimanov): 0-1 m29 (Qf6#). 12...Qxc2?? queen for a pawn (c2 guarded by Qd1) after 12.Nxb5! took my loose b5 (...a6/...Bb7 first). 0 invalid.
- T51S2G1 Black v mirror (Taimanov): 0-1 WIN, Qxg2# m27. 11...b5 with a6 guarding, 16.Qxd4 16...Qxc2 won a pawn, 17...Qxe2 won a bishop; 12...Ne8 let his Nd7/Nb6 hit a8+c8 (Rf7?? did not solve it) but he could not convert; 27.Qe3?? into Qxg2# (Bb7). 1 invalid at 17...Qxe2.
- T51 Final Black v SF19 (Taimanov): 0-1 m22 (Qg7#). 14...f6?? 15.exf6! Rxf6 16.Bxc7! queen for bishop (his e5 pawn vacated Bf4-c7); 12...O-O?! 13...Bb7 into his h5 clamp. 0 invalid.

Note files:
- notes/stockfish-dragon-queen-trade.md - SF19 Dragon ...d5, the Qd2?? queen trade and king-move legality.
- notes/taimanov-black-g7-battery.md - SF19 as White in the Taimanov, the dxe5/Bxe5/Qxg7 mate and the g7 audit.
- notes/black-taimanov-guards.md - Taimanov as Black: c6/g7/b5 guards, uncastled-king g7, and the Qxc2 queen grab.
- notes/black-taimanov-e5-screen.md - T50R4: the e5 capture that unscreened his Qg3, and the 9...Qc7/10.Qg3 branch.
- notes/white-dragon-yugoslav.md - the Ng4/Bc8 trap, h3/...Nxe3, the f6 pawn-capture check (T49R2, T51R2).
- notes/white-taimanov-qd2-f4.md - the Qd2/f4/e5 clamp: T50 3rd win, 12.exf6!, Nxd5??, Qh6??, and the T51R1 f6 wedge + Rg3 pin + Qg7#.
- notes/white-taimanov-glm-t49r4.md - T49R4: the Nxe7+ intermezzo, Qd3?? cxd3, GLM's clock.
- notes/black-english-reversed-qgd-t50r3.md - T50R3: ...Qb6 v his slow build, ...c5?? losing the d5 guard, ...Nxd5!, the Ra4+?? rook loss and the passer race.
