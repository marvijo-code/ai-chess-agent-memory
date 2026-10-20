# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries on ONE move forfeit. Before sending, list the piece's CURRENT square, destination and path; before castling check king+rook unmoved and the two squares empty. After ONE rejection redraw a DIFFERENT move, never resend.
- ANY OF MY PIECES ON HIS PAWN'S CAPTURE SQUARE IS LOST - CHECKS AND ROOKS INCLUDED. T52R3 25...bxa3 took my whole Ra3 and 30...fxe6 my Be6; T50R3 44...Ra4+?? bxa4; T49R2 10.Qxg4?? Bxg4. Sweep every enemy pawn's two capture squares FROM THE BOARD before landing.
- HIS e5 PAWN OWNS f6 AND d6 - NEVER A PIECE THERE. T52 Final 11.e5! Nh5 12.g4 trapped that knight, and 12...Nf6?? 13.exf6 took my knight with a PAWN. Same class as 15.Nf6+?? exf6. I had this written and played into it: the rule is an order, not a fact to record after the game.
- A SQUARE COVERED BY HIS PAWNS IS NO FORK: 12...Nd5?! into Nc3. List every enemy capturer of the arrival square, pawns and knights first, before any knight check or queen landing (T52 Arm 16...Qe5?? Nf3xe5 won my queen).
- THE MOVING PIECE ABANDONS ITS DUTY: T52R3 20...Bb7?? left Nd7 loose on the d-file ...dxc5 had opened - 21.Rxd7; 38...Rb2?? ignored his Kc5 hitting Bc6 - 39.Kxc6. Before any quiet or developing move name what it guarded, what is loose on an open line, and answer any attacked piece that move.
- A CAPTURE THAT UNSCREENS A LINE RE-ARMS THE PIECE BEHIND IT. T50R4 14...Bxe5?? 15.Bxe5 Qxe5+ 16.Qxe5!; T51 Final 14...f6?? 15.exf6! 16.Bxc7 won my queen. In any 2+ capture chain redraw after EACH capture and name HIS last capturer.
- ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE PIECE (T50R3 18...Nxd5!); but a capture that leaves him a piece ahead is a SAC (T50R2 11.Nxd5??) and a RECAPTURE IS NOT A GAIN (T52S2G1 28.Rdxc4 Rxc4 29.Rxc4 was an EVEN rook trade I called +R). Write 'W pieces / B pieces' square by square after every chain.
- MY OWN PIECE ON THE RECAPTURE LINE = NO RECAPTURE: T52 Arm 8...Nxd4?? counted on ...Qxd4, but my Nd5 stood between Qd6 and d4; 9.Nxd4 won a knight. Trace the recapture path with MY blockers first.
- A PAWN LOST IS GONE - NEVER 'BALANCE' WITH A QUEEN GRAB. T51R3 12...Qxc2?? (Qd1 guarded c2) = queen for a pawn, mated. Check where his queen stands NOW.
- A 'DEFENDED' PAWN STILL FALLS TO Qxb2 + A FORCED TRADE: T52S2G1 18.Qd2?! 'covers b2' but 18...Qxb2 19.Rfb1 Qc3! 20.Qxc3 dxc3. Name every attacker AND the queen trade after the take.
- A WARNING I WRITE IS AN ORDER FOR THE NEXT MOVE (T49R1, T50R3, T52 Final). Re-read the last comment before choosing; a retreat square is not safe because my comment calls it safe (12...Nf6 'wins the e5 pawn' - it lost a knight).
- THE PIECE I MOVE MAY BE g7's ONLY GUARD: an uncastled king never guards g7, and ...h6 is luft only for Kg8. With his queen near g3 ask 'what guards g7 after this?' - or castle.
- COUNT EVERY DEFENDER BEFORE ANY CAPTURE, FULL DIAGONALS BOTH WAYS (T49R2 Bc8 guarded g4; T49R3 18.Qxd8+?? Bf6). A check is not a forcing win.
- A PAWN-ATTACKED PIECE MUST MOVE; defending it does not save it. Mirror: when HIS pawn attacks my piece, move it now; when MY pawn attacks his, take.
- Qg3 + his bishop on e5/f6 = Qxg7# (T48 Final 13...dxe5??). Never capture on e5 while his Qg3-Bf4 battery screens it.
- CHECKED? List block/capture squares and which of my pieces sit on the checker's line.
- QUEEN TRADE = RECAPTURE CHAIN ON MY CENTRAL KNIGHT (T48R1 11.Qd2?? Nxd4/Bxd4). Block with a guarded piece or keep queens.
- A QUEEN IN FRONT OF HER KING ON AN OPEN FILE IS PINNED: a rook lift to that file wins her (T51R1 21.Rg3! Q for R).
- DOWN A QUEEN OR PIECE v SF: no counterplay, guard every unit, 5-10 s moves. A king shuttle can still save half a point - T52 Final held threefold down Q+R at m25 - but treat that as luck, not a plan.

## Endings, king safety, conversion
- KING ON h1 + HIS QUEEN ON g3 = HIS ROOK ON e1 IS MATE (T50R2 30...Re1#). After Kh1 name the rank-1 squares his rooks reach.
- MY ...Bb7 + HIS Kg1 (g2 held only by his king) = Qxg2# (T51S2G1 27...Qxg2#; T52R3 29...Bxe4 first). Watch it whenever his f2-rook leaves or his queen steps off g2.
- Bf6 + Qh6 v his Kg8: Qg7# when g8/d8/h7/h8 are covered or blocked by HIS OWN pieces (T51R1).
- Q+R v BARE K (T52R3, m70): check from 2+ squares away and walk the king up, but NEVER park the rook where his king reaches it (42...Qd1?? 43.Kxb6). No repetition loops (Qd4+/Qd5+ three times = draw) - swing wide to grab his pawns first.
- K+Q v LONE K net verified: 69...Kd3! opposition (d2/e2 covered by my king, f1/f2 by the queen) 70.Qg1#. Distant checks drive him to the edge, then the king steps into opposition; check stalemate every move.
- R+B+passer v B: run ...a2-a1=Q, keeping the bishop on the promotion square's diagonal until no passers.
- UP A ROOK / 2R v R: take the first clean rook trade, then collect loose pawns; a bare king on my passer's square is driven off with a rook check.
- UP MATERIAL IN R+B vs R: STOP THE PASSER BEFORE RACING (T50R3). Racing pawns is the last plan.
- A ROOK NEEDS A SAFE SQUARE, NOT A CHECK (...Ra4+; ...Rb6+?? Kxb6). Every rook/queen move: his pawn capture squares, then sliders, then the purpose.
- LEVEL R+B vs R+B (T52S2G1): the rook-shuffle repetition draw is fine when nothing better exists, but do not burn 6-7 min on quiet shuffles; shuffles 15-30 s.
- TWO ROOKS (or R+R+N) v QUEEN: draw by blockade, not raids (T49R3).
- DOWN A QUEEN v SF: hold the blockade, keep every unit guarded, trade nothing into his queen's files (T50R4 held 28 moves).

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. My losses are scan misses, not the clock. T52 Final used ~34 min in 25 moves including 2:17 on a plain recapture (9...Nxd4) and 1:25 on the losing 12...Nf6: that think belonged at move 10, before ...Be7.
- ARMAGEDDON AS BLACK: draw odds. After an early material loss, fortify and use his clock; T52 Arm I was a knight down at m9 and a queen down at m17, but he flagged at 0:23 while I had 4:47. No 'active' queen into knight jumps.

## Opening: English reversed QGD as BLACK
- 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies), then ...Bf5/...Nbd7/...Re8/...Qb6.
- ...Qb6 wins the IQP d4 when HIS Nd2 blocks Qd1 (T50R3 12...Qxd4!). With the extra pawn, ...c5 took the c6 guard off d5 and lost it back - keep ...c6 or ...Ne4 support first.
- T52R2 v GLM: 17.Qd2 left b3 loose (17...Qxb3); 18.Qc2?? put his queen on my Qb3-c2 diagonal with NO c2 defender: 18...Qxc2! won her, then queen raids + knight checks to Qxf1# m33. When his queen lands on my queen's line, count his recapturers and take.

## Opening: Open Sicilian Taimanov (both colours)
- 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies; ...b5/...Bb7/...Qc7 first is the same setup). Then f4/Qd2/Rad1 (White) or ...Qc7/...b5/...Bb7/...Rfc8 (Black).
- AS BLACK v his f4/Qd2 clamp: ...b5 is safe once ...a6 guards it. When his e5 kicks the f6-knight do NOT park it on e8 with my a8-rook home - his Nc7/Nd6 forks a8+c8. Play ...Nd5 (accept Nxd5 exd5, count guards) or ...Nh5 - and only if e5 cannot be met by a pawn.
- AS BLACK, ...b5 NEEDS A GUARD BEFORE IT LANDS: ...a6 first or ...Bb7, else 12.Nxb5! wins it (T51R3).
- T52R3 (Black v mirror, won m70): after 18...dxc5 the d-file opened and his Rd1 hit my UNGUARDED Nd7 - 20...Bb7?? Rxd7; 21...Bc6! then forked his Na4 and Rd7 to recover. After any pawn capture, list my own undefended units on the new open file first.
- WHITE CLAMP WIN (T50 3rd, T51R1): after e5 and the Nxd5/Bxd5 trade, ...Bxf3 trades his d5-bishop and f5/f6 is the wedge: f6! gxf6 exf6 - NEVER Bxf6?? Rxf6, and 20.fxe7 then wins his Be7. BAN premature f4-f5.
- 12.exf6! takes a knight with a PAWN whatever recaptures (T49R3, T52 Final). T51R1 finish: Rg3 pins Qg6 to Kg8 (Q for R), Bf6 covers g7, Qh6 Qg7#.
- AS BLACK do NOT jump ...Nd5 into his Nc3; ...Qc7 covers c6 and eyes e5. T50R2 9...d5: trade the f6-knight FIRST; never 11.Nxd5??.
- T49R4 12.Nxc6! after ...Nxe4?? 13.Nxe7+ Qxe7 14.Nxe4 - an in-between check beats resolving a queen attack.
- Before moving my queen OFF the second rank check his ...Qxc2/...Qxb2 grab (T51R1 16.Qe3?!).

## Opening: Open Sicilian Dragon (me White)
- 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 Ng4 (16 plies): that Ng4 is GUARDED by Bc8 through d7-e6-f5. Answer with h3 or 9.Nxc6 bxc6 10.Bg5; NEVER Qxg4.
- T51R2: 9.h3?! met 9...Nxe3! (Be3 taken by the knight, fxe3 doubles my e-pawns) and ...Bxb2 won a pawn. Prefer 9.Nxc6 bxc6 10.Bg5.
- T48R1 Dragon ...d5: do NOT block his Qa5+ with Qd2??; use a guarded block (Bd2/c3).

## Opening: Taimanov as BLACK v Stockfish
- 1.e4 c5 2.Nf3 Nc6 3.Nc3 e6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.e5 Nd5 8.Qf3 Nxc3 (16 plies). The standard ...Be7/...O-O/...Qc7/...Bf4/...d6 is level to move 12; ...Nxc3 hands him c3+d4+e5 - take it only for a concrete reason.
- 7.Ndb5 Qb8! is the ONLY good retreat (the queen still guards c7 and d6, so Nc7+/Nd6+ just lose a knight). Keep this.
- T52 Final: 8...a6 9.Nd4 Nxd4 10.Qxd4 Be7? 11.e5! won my Nf6 - its retreats were all bad (d5 drops a pawn to Qxd5, h5 falls to g4, e8 gets forked). STOP e5 BEFORE castle: ...d6 or ...Qc7 at move 10.
- With queens on do NOT open the centre and NEVER take on e5: 14...Bxe5?? 15.Bxe5 Qxe5+ 16.Qxe5. ...f6 only with his Bf4 off the c7 diagonal and his e5 pawn unable to capture (14...f6?? 15.exf6! Rxf6 16.Bxc7). Plan ...Bb7/...Rfc8 and wait.
- T49R1 (king e8, Bf8 the ONLY g7 guard): 10...Be7? lost a rook to 11.Qxg7. ...O-O or keep Bf8 home; ...h6 is luft only for Kg8.
- T49 Final: 11...O-O? allowed 12.Bxc6! winning the a8 rook - after ...bxc6 nothing recaptures on c6. Play ...Qc7 FIRST.
- T50R1: after 12.Qxh8, ...Nb4?? lost to 13.Nf6+ 14.Qxf8#. Down material, audit every enemy knight landing for check + fork + mate.

## Opponents
- Stockfish 19 (depth 4): instant, no second chances. Punishes any piece I call 'undefended' (hidden defender Bc8-g4), any capture opening a bishop to g7, an unguarded c6 (Bxc6!), a kicked Ng4 (...Nxe3!), a retreat onto his e5-pawn's capture square (f6), and a blocked ...Be7/...f6 by exf6 opening Bf4-c7 to my queen. Builds the h4/h5/Bf4/Qg3 clamp and converts a piece up without gifts - but WILL take a threefold repetition when his only checks repeat (T52 Final, down Q+R).
- DeepSeek V4.1 Flash (mirror): solid Taimanov both colours, 20 s-6 min thinks, converts without gifts, never resigns. T51S2G1: 17.Nc5?? let Qxe2 and 27.Qe3?? walked into Qxg2#. T52R3 (I won): it played the Rf3-h3 rook lift, 21.Rxd7! to punish my loose Nd7, then 25.Ra3?? on my b4 pawn's capture square; 2 illegal tries. T52S2G1 (draw): as Black ...Qc7/...a6/...Nf6/...Bb4 before ...Be7, gave c3/c4 back but took b2/e5/f4 and held R+B vs R+B accurately. T52 Arm (I won on time): as White Alapin 2.c3/3.e5, won my knight after 8...Nxd4??, then 20.Qd3?? sat on my Rfd8 file and 22...Rxd3 won her; it flagged 0:23 vs my 4:47. It leaves its queen on a rook's file when chasing a bishop - check that capture.
- GLM 5.3 Flash: English reversed QGD as White (2-3 min middlegame, 3 illegal tries, punishes a rook on a pawn capture square); Taimanov as Black. T52R2: 18.Qc2?? Qxc2! lost his queen; I converted Q+N up, Qxf1# m33.

## Record
- T47R1 W v GLM: 1-0 forfeit (19.Nxe4). T48R1 W v SF19: 0-1; 11.Qd2?? lost a bishop in the queen trade.
- T48 Final B v SF19: 0-1 Qxg7# m15 (13...dxe5??); level to move 12.
- T49R1 B v mirror: win by forfeit m13 (O-O illegal). T49R2 W v SF19: 0-1 m28; 10.Qxg4?? Bxg4.
- T49R3 W v GLM: draw; 12.exf6! +piece, 18.Qxd8+?? Bxd8, held 2R v Q. T49R4 W v GLM: 1-0 on time; 13.Nxe7+!, 21.Qd3?? cxd3.
- T49 Final B v SF19: 0-1; 11...O-O? 12.Bxc6! won the a8 rook.
- T50R1 B v SF19: 0-1 m14; 10...Be7? 11.Qxg7. T50R2 W v mirror: 0-1 m30; 11.Nxd5??, 16.Qh6?? gxh6, 30...Re1#.
- T50R3 B v GLM: 0-1 m56; 12...Qxd4! 18...Nxd5!; 44...Ra4+?? bxa4. T50R4 B v SF19: 0-1 m43; 14...Bxe5?? queen for a pawn, held 28 moves.
- T50 3rd W v GLM: 1-0 m51; e5 clamp, 51.Rd8#. T51R1 W v GLM: 1-0 m25; f6 wedge, 21.Rg3! pin, Qg7#.
- T51R2 W v SF19: 0-1 m37; 9.h3?! Nxe3!, 15.Nf6+?? exf6. T51R3 B v mirror: 0-1 m29; 12.Nxb5! (b5 unguarded), 12...Qxc2?? queen for a pawn.
- T51S2G1 B v mirror: WIN Qxg2# m27; ...b5 with a6 guard, 12...Ne8 let Nc7/Nb6. T51 Final B v SF19: 0-1 m22; 14...f6?? 15.exf6! Bxc7.
- T52R2 B v GLM: WIN Qxf1# m33; 17...Qxb3, 18.Qc2?? Qxc2!.
- T52R3 B v mirror (Taimanov): WIN Qg1# m70. 18...dxc5 opened the d-file; 20...Bb7?? hung Nd7 to Rxd7, 21...Bc6! forked and recovered it; 25...bxa3 won a whole rook; a3-a1=Q; lost the rook to Kxb6 but mated with K+Q. 0 invalid.
- T52S2G1 W v mirror (Taimanov): draw by repetition. 18.Qd2?! Qxb2/Qc3 pawn down; 28-29 Rxc4 recaptured a TRADED rook (I miscounted +R); held R+B v R+B. 0 invalid.
- T52S2 Arm B v mirror (Alapin): WIN on time (0-1). 8...Nxd4?? lost N for P; 16...Qe5?? Nf3xe5 won my queen; 20.Qd3?? Rxd3 won his; he flagged 0:23 v my 4:47.
- T52 Final B v SF19 (Taimanov): draw by threefold m25. 7.Ndb5 Qb8! only move; 10...Be7? 11.e5! won my Nf6 (12...Nf6?? exf6 took it with a pawn). Down Q+R from m14, king shuttle Kf7/Ke8/Kf8 gave the repetition and SF took it. ~34 min used, 0 invalid.

Note files:
- notes/stockfish-dragon-queen-trade.md - SF19 Dragon ...d5, the Qd2?? queen trade and king-move legality.
- notes/taimanov-black-g7-battery.md - SF19 as White in the Taimanov, the dxe5/Bxe5/Qxg7 mate and the g7 audit.
- notes/black-taimanov-guards.md - Taimanov as Black: c6/g7/b5 guards, the d-file after ...dxc5, the Qxc2 grab, the T52R3 conversion.
- notes/black-taimanov-e5-screen.md - T50R4: the e5 capture that unscreened his Qg3, and the 9...Qc7/10.Qg3 branch.
- notes/white-dragon-yugoslav.md - the Ng4/Bc8 trap, h3/...Nxe3, the f6 pawn-capture check.
- notes/white-taimanov-qd2-f4.md - the Qd2/f4/e5 clamp (incl. T52S2G1: ...Qxb2/...Qc3, the phantom rook win, the repetition).
- notes/white-taimanov-glm-t49r4.md - T49R4: the Nxe7+ intermezzo, Qd3?? cxd3, GLM's clock.
- notes/black-english-reversed-qgd-t50r3.md - T50R3/T52R2: ...Qb6 v his slow build, ...c5?? losing the d5 guard, ...Nxd5!, the Ra4+?? rook loss, and the Qxc2 queen win.
