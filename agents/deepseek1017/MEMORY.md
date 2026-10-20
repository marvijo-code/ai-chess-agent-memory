# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries on ONE move forfeit. Before sending, list the piece's CURRENT square, destination and path; before castling check king+rook unmoved and the two squares empty. After ONE rejection redraw a DIFFERENT move, never resend.
- ANY OF MY PIECES ON HIS PAWN'S CAPTURE SQUARE IS LOST - CHECKS AND ROOKS INCLUDED. The mirror wins games: T52R3 25...bxa3 took his whole Ra3 (b4's capture square) and 30...fxe6 his Be6 (f7's square); T50R3 44...Ra4+?? bxa4 lost mine; T49R2 10.Qxg4?? Bxg4. Sweep every enemy pawn's two capture squares FROM THE BOARD before landing.
- A SQUARE COVERED BY HIS PAWNS IS NO FORK: 12...Nd5?! into Nc3; T51R2 15.Nf6+?? exf6 (his e7 and g7 pawns). List every enemy capturer of the arrival square, pawns first, before any knight check.
- THE MOVING PIECE ABANDONS ITS DUTY: T52R3 20...Bb7?? left my Nd7 loose on the d-file that ...dxc5 had just opened - 21.Rxd7 won a knight; 38...Rb2?? ignored his Kc5 hitting my Bc6 - 39.Kxc6 won the bishop. Before any quiet or developing move name what it guarded, what is loose on an open line, and answer any attacked piece that move.
- A CAPTURE THAT UNSCREENS A LINE RE-ARMS THE PIECE BEHIND IT. T50R4 14...Bxe5?? 15.Bxe5 Qxe5+ 16.Qxe5!; T51 Final 14...f6?? 15.exf6! (his e5 pawn left the Bf4-c7 line) 16.Bxc7 won my queen. In any 2+ capture chain redraw after EACH capture and name HIS last capturer.
- HIS PIECE GUARDED ONLY BY HIS QUEEN IS FREE IF MY OTHER PIECE COVERS THE RECAPTURE SQUARE (T50R3 18...Nxd5! won a bishop). A CAPTURE THAT LEAVES HIM A PIECE AHEAD IS A SAC (T50R2 11.Nxd5??): write 'W pieces / B pieces' after every chain.
- A PAWN LOST IS GONE - NEVER 'BALANCE' WITH A QUEEN GRAB. T51R3 12...Qxc2?? (Qd1 guarded c2) = queen for a pawn, mated. Mirror: his queen LEAVING a guard frees that square (T51S2G1 16.Qxd4 then ...Qxc2). Check where his queen stands NOW.
- A WARNING I WRITE IS AN ORDER FOR THE NEXT MOVE (T49R1, T50R3). Re-read the last comment before choosing.
- THE PIECE I MOVE MAY BE g7's ONLY GUARD: an uncastled king never guards g7; ...h6 is luft only for Kg8. With his queen near g3 ask 'what guards g7 after this?' - or castle.
- COUNT EVERY DEFENDER BEFORE ANY CAPTURE, FULL DIAGONALS BOTH WAYS (T49R2 Bc8 guarded g4; T49R3 18.Qxd8+?? Bf6). A check is not a forcing win.
- A PAWN-ATTACKED PIECE MUST MOVE; defending it does not save it. Mirror: when HIS pawn attacks my piece, move it now; when MY pawn attacks his, take.
- Qg3 + his bishop on e5/f6 = Qxg7# (T48 Final 13...dxe5??). Never capture on e5 while his Qg3-Bf4 battery screens it.
- CHECKED? List block/capture squares and which of my pieces sit on the checker's line.
- QUEEN TRADE = RECAPTURE CHAIN ON MY CENTRAL KNIGHT (T48R1 11.Qd2?? Nxd4/Bxd4). Block with a guarded piece or keep queens.
- A QUEEN IN FRONT OF HER KING ON AN OPEN FILE IS PINNED: a rook lift to that file wins her (T51R1 21.Rg3! Q for R). Every queen landing: is an enemy rook on that file?
- DOWN A QUEEN OR PIECE v SF: no rescue; guard every unit, 5-10 s moves. An initiative sac only accelerates mate.

## Endings, king safety, conversion
- KING ON h1 + HIS QUEEN ON g3 = HIS ROOK ON e1 IS MATE (T50R2 30...Re1#). After Kh1 name the rank-1 squares his rooks reach.
- MY ...Bb7 + HIS Kg1 (g2 held only by his king) = Qxg2# (T51S2G1 27...Qxg2#; T52R3 29...Bxe4 took the loose e4-pawn first). Look for it whenever his f2-rook leaves or his queen steps off g2.
- Bf6 + Qh6 v his Kg8: Qg7# when f8/d8/h7/h8 are covered or blocked by HIS OWN pieces (T51R1).
- Q+R v BARE K (T52R3, m70): check from 2+ squares away and walk the king up, but NEVER park the rook where his king reaches it (42...Qd1?? 43.Kxb6 lost a whole rook; ...Rb6+?? Kxb6 the same). No repetition loops (Qd4+/Qd5+ three times = draw) - swing wide to grab his pawns (47...Qh1 Qxh2 Qxg3 Qxg4), then mate.
- K+Q v LONE K net verified: 69...Kd3! opposition (his d2/e2 covered by my king, f1/f2 by the queen) 70.Qg1#. Distant checks drive him to the edge, then the king steps into opposition; check stalemate every move.
- R+B+passer v B: run ...a2-a1=Q, keeping the bishop on the promotion square's diagonal until no passers.
- UP A ROOK, 2R v R (T50 3rd): take the first clean rook trade, then collect loose pawns with the last rook; a bare king on my passer's square is driven off with a rook check.
- UP MATERIAL IN R+B vs R: STOP THE PASSER BEFORE RACING (T50R3). Racing pawns is the last plan.
- A ROOK NEEDS A SAFE SQUARE, NOT A CHECK (T50R3 ...Ra4+; T52R3 ...Rb6+?? Kxb6). Every rook/queen move: his pawn capture squares, then sliders, then the purpose.
- TWO ROOKS (or R+R+N) v QUEEN: draw by blockade, not raids (T49R3).
- DOWN A QUEEN v SF: hold the blockade, keep every unit guarded, trade nothing into his queen's files (T50R4 held 28 moves to move 43).

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. My losses are scan misses, not the clock: T52R3 finished with 2:46 h... (I used ~38 min of 60). Speed is fine only when the per-move list is written.

## Opening: English reversed QGD as BLACK
- 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies), then ...Bf5/...Nbd7/...Re8/...Qb6.
- ...Qb6 wins the IQP d4 when HIS Nd2 blocks Qd1 (T50R3 12...Qxd4!). With the extra pawn, ...c5 took the c6 guard off d5 and lost it back - keep ...c6 or ...Ne4 support first.
- T52R2 v GLM: 17.Qd2 left b3 loose (17...Qxb3 won a pawn); 18.Qc2?? put his queen on my Qb3-c2 diagonal with NO c2 defender: 18...Qxc2! won her, then queen raids + knight checks to Qxf1# m33. Whenever his queen lands on my queen's line, count his recapturers and take.

## Opening: Open Sicilian Taimanov (both colours)
- 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies; ...b5/...Bb7/...Qc7 first is the same setup). Then f4/Qd2/Rad1 (White) or ...Qc7/...b5/...Bb7/...Rfc8 (Black).
- AS BLACK v his f4/Qd2 clamp: ...b5 is safe once ...a6 guards it. When his e5 kicks the f6-knight do NOT park it on e8 with my a8-rook home - his Nc7/Nd7-b6 then forks a8+c8 (T51R3 11...Ne8?, T51S2G1 12...Ne8). Play ...Nd5 (accept Nxd5 exd5, count guards) or ...Nh5.
- AS BLACK, ...b5 NEEDS A GUARD BEFORE IT LANDS: ...a6 first or ...Bb7, else 12.Nxb5! wins it (T51R3).
- T52R3 (Black v mirror, won m70): after 18...dxc5 the d-file opened and his Rd1 hit my UNGUARDED Nd7 - 20...Bb7?? Rxd7; 21...Bc6! then forked his Na4 and Rd7 to recover the piece. After any pawn capture, list my own undefended units on the new open file first.
- WHITE CLAMP WIN (T50 3rd, T51R1): after e5 and the Nxd5/Bxd5 trade, ...Bxf3 trades his d5-bishop and f5/f6 is the wedge: f6! gxf6 exf6 - NEVER Bxf6?? Rxf6, and 20.fxe7 then wins his Be7. BAN premature f4-f5; f5 only after his ...d6.
- 12.exf6! takes a knight with a PAWN whatever recaptures (T49R3). T51R1 finish: Rg3 pins Qg6 to Kg8 (Q for R), Bf6 covers g7, Qh6 Qg7#.
- AS BLACK do NOT jump ...Nd5 into his Nc3; ...Qc7 covers c6 and eyes e5. T50R2 9...d5: trade the f6-knight FIRST; never 11.Nxd5??.
- T49R4 12.Nxc6! after ...Nxe4?? 13.Nxe7+ Qxe7 14.Nxe4 - an in-between check beats resolving a queen attack.
- Before moving my queen OFF the second rank check his ...Qxc2/...Qxb2 grab (T51R1 16.Qe3?!; T51R2 14...Bxb2).

## Opening: Open Sicilian Dragon (me White)
- 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 Ng4 (16 plies): that Ng4 is GUARDED by Bc8 through d7-e6-f5. Answer with h3 or 9.Nxc6 bxc6 10.Bg5; NEVER Qxg4.
- T51R2: 9.h3?! met 9...Nxe3! (Be3 taken by the knight, fxe3 doubles my e-pawns) and ...Bxb2 won a pawn. Prefer 9.Nxc6 bxc6 10.Bg5.
- T48R1 Dragon ...d5: do NOT block his Qa5+ with Qd2??; use a guarded block (Bd2/c3).

## Opening: Taimanov as BLACK v Stockfish
- 1.e4 c5 2.Nf3 Nc6 3.Nc3 e6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.e5 Nd5 8.Qf3 Nxc3 (16 plies). The standard ...Be7/...O-O/...Qc7/...Bf4/...d6 is level to move 12; ...Nxc3 hands him c3+d4+e5 - take it only for a concrete reason.
- With queens on do NOT open the centre and NEVER take on e5: 14...Bxe5?? 15.Bxe5 Qxe5+ 16.Qxe5. ...f6 only with his Bf4 off the c7 diagonal and his e5 pawn unable to capture (T51 Final 14...f6?? 15.exf6! Rxf6 16.Bxc7). Plan ...Bb7/...Rfc8 and wait.
- T49R1 (king e8, Bf8 the ONLY g7 guard): 10...Be7? lost a rook to 11.Qxg7. ...O-O or keep Bf8 home; ...h6 is luft only for Kg8.
- T49 Final: 11...O-O? allowed 12.Bxc6! winning the a8 rook - after ...bxc6 nothing recaptures on c6. Play ...Qc7 FIRST.
- T50R1: after 12.Qxh8, ...Nb4?? lost to 13.Nf6+ 14.Qxf8#. Down material, audit every enemy knight landing for check + fork + mate.

## Opponents
- Stockfish 19 (depth 4): instant, no second chances. Punishes any piece I call 'undefended' (hidden defender Bc8-g4), any capture opening a bishop to g7, an unguarded c6 (Bxc6!), a kicked Ng4 (...Nxe3!), a knight check taken by a PAWN (...exf6); builds the h4/h5/Bf4/Qg3 clamp and converts a piece up without gifts. Also punishes ...f6 by exf6 opening Bf4-c7 to my queen.
- DeepSeek V4.1 Flash (mirror): solid Taimanov both colours, 1-8 min thinks, converts without gifts. T51S2G1: 17.Nc5?? let Qxe2 and 27.Qe3?? walked into Qxg2#. T52R3 (I won): it played f4/Qd2, the Rf3-h3 rook lift, 21.Rxd7! to punish my loose Nd7, then 25.Ra3?? on my b4 pawn's capture square and 26.Bxa6/d7 pawn hunts; 2 illegal tries (19.f5, 32.Rxa3-type). It never resigns - keep scanning every move to the end.
- GLM 5.3 Flash: English reversed QGD as White (2-3 min middlegame, 3 illegal tries, punishes a rook on a pawn capture square); Taimanov as Black. T52R2: 18.Qc2?? Qxc2! lost his queen; I converted Q+N up 0 invalid, Qxf1# m33. When his queen steps onto my queen's line under pressure, take it.

## Record
- T47R1 W v GLM: 1-0 forfeit (19.Nxe4).
- T48R1 W v SF19: 0-1; 11.Qd2?? lost a bishop in the queen trade.
- T48 Final B v SF19: 0-1 Qxg7# m15 (13...dxe5??); level to move 12.
- T49R1 B v mirror: win by forfeit m13 (O-O with Ng8 home illegal).
- T49R2 W v SF19: 0-1 m28; 10.Qxg4?? Bxg4.
- T49R3 W v GLM: draw; 12.exf6! +piece, 18.Qxd8+?? Bxd8, held 2R v Q.
- T49R4 W v GLM: 1-0 on time; 13.Nxe7+!, 21.Qd3?? cxd3.
- T49 Final B v SF19: 0-1; 11...O-O? 12.Bxc6! won the a8 rook.
- T50R1 B v SF19: 0-1 m14; 10...Be7? 11.Qxg7.
- T50R2 W v mirror: 0-1 m30; 11.Nxd5??, 16.Qh6?? gxh6, 30...Re1#.
- T50R3 B v GLM: 0-1 m56; 12...Qxd4! 18...Nxd5!; 44...Ra4+?? bxa4.
- T50R4 B v SF19: 0-1 m43; 14...Bxe5?? queen for a pawn, held 28 moves.
- T50 3rd W v GLM: 1-0 m51; e5 clamp, 51.Rd8#.
- T51R1 W v GLM: 1-0 m25; f6 wedge, 21.Rg3! pin, Qg7#.
- T51R2 W v SF19: 0-1 m37; 9.h3?! Nxe3!, 15.Nf6+?? exf6.
- T51R3 B v mirror: 0-1 m29; 12.Nxb5! (b5 unguarded), 12...Qxc2?? queen for a pawn.
- T51S2G1 B v mirror: WIN Qxg2# m27; ...b5 with a6 guard, 12...Ne8 let Nc7/Nb6.
- T51 Final B v SF19: 0-1 m22; 14...f6?? 15.exf6! Bxc7.
- T52R2 B v GLM: WIN Qxf1# m33; 17...Qxb3, 18.Qc2?? Qxc2!.
- T52R3 B v mirror (Taimanov): WIN Qg1# m70. 18...dxc5 opened the d-file; 20...Bb7?? hung Nd7 to Rxd7, 21...Bc6! forked and recovered it; 25...bxa3 won a whole rook; a3-a1=Q; lost the rook to Kxb6 but mated with K+Q. 0 invalid (his 2).

Note files:
- notes/stockfish-dragon-queen-trade.md - SF19 Dragon ...d5, the Qd2?? queen trade and king-move legality.
- notes/taimanov-black-g7-battery.md - SF19 as White in the Taimanov, the dxe5/Bxe5/Qxg7 mate and the g7 audit.
- notes/black-taimanov-guards.md - Taimanov as Black: c6/g7/b5 guards, the d-file after ...dxc5, the Qxc2 grab, and the T52R3 conversion.
- notes/black-taimanov-e5-screen.md - T50R4: the e5 capture that unscreened his Qg3, and the 9...Qc7/10.Qg3 branch.
- notes/white-dragon-yugoslav.md - the Ng4/Bc8 trap, h3/...Nxe3, the f6 pawn-capture check.
- notes/white-taimanov-qd2-f4.md - the Qd2/f4/e5 clamp: 12.exf6!, Nxd5??, Qh6??, the f6 wedge + Rg3 pin + Qg7#.
- notes/white-taimanov-glm-t49r4.md - T49R4: the Nxe7+ intermezzo, Qd3?? cxd3, GLM's clock.
- notes/black-english-reversed-qgd-t50r3.md - T50R3/T52R2: ...Qb6 v his slow build, ...c5?? losing the d5 guard, ...Nxd5!, the Ra4+?? rook loss, and the Qxc2 queen win.
