# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries on ONE move forfeit. Before sending, name piece, CURRENT square, destination, path; before castling check king+rook unmoved and the two squares empty. After ONE rejection pick a DIFFERENT move. T53 Final 40...Bc6 = 3 tries: re-read occupancy first.
- ANY OF MY PIECES ON HIS PAWN'S CAPTURE SQUARE IS LOST - CHECKS AND ROOKS INCLUDED (T52R3 25...bxa3; T50R3 44...Ra4+?? bxa4; T49R2 10.Qxg4?? Bxg4). Sweep every enemy pawn's two capture squares FROM THE BOARD before landing. T53R3 17...Qe6?? stood on the d5-pawn's capture square: 18.dxe6 queen for a pawn.
- AN OPEN FILE + HIS ROOK + NOTHING BETWEEN = MY PIECE THERE IS FREE, however active it looks (T53R3 14...Bf5?? 'eyes e4' while his Rf1 stood behind an empty f-file: 17.Rxf5 won the bishop). Before a bishop/knight lands, name its guards AND every enemy slider line, empty squares included.
- HIS e5 PAWN OWNS f6 AND d6 - never a piece there: 15.Nf6+?? exf6, 12...Nf6?? exf6 (a pawn takes a knight). Sweep pawn captures before every knight check or fork.
- A SQUARE COVERED BY HIS PAWNS IS NO FORK: 12...Nd5?! into Nc3; T52 Arm 16...Qe5?? Nxe5 won my queen. List his pawns and knights on the arrival square first.
- THE MOVING PIECE ABANDONS ITS DUTY: name what it guarded and what is loose on the new open line (T52R3 20...Bb7?? left Nd7 to Rxd7; 38...Rb2?? Kxc6). Answer an attacked piece before any quiet move or castle.
- A CAPTURE THAT UNSCREENS A LINE RE-ARMS THE PIECE BEHIND IT: in a 2+ capture chain redraw after EACH capture and name HIS last capturer (T50R4 14...Bxe5?? 15.Bxe5 Qxe5+ 16.Qxe5; T51 Final 14...f6?? 15.exf6 16.Bxc7).
- ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE PIECE (T50R3 18...Nxd5!); a recapture is NOT a gain (T52S2G1 Rxc4 was an even rook trade). Write 'W pieces / B pieces' after every chain.
- A PIECE GUARDED BY JUST ONE UNIT IS A TARGET: T53S2G1 27...Nxf4! took his Qf4 ('defended' only by Rf1); Rxf4 left me Q+R v R. Before assuming a piece is safe, list its guards AND what attacks the guard.
- MY OWN PIECE ON THE RECAPTURE LINE = NO RECAPTURE (T52 Arm 8...Nxd4??); T53R1 14.Nc5?? let 14...Bxc5 15.Nb3 Bd4 - my own Nd4 stood between Be3 and c5, so the 'attacked bishop' walked into a better square with tempo.
- A PAWN LOST IS GONE - never 'balance' with a queen grab (T51R3 12...Qxc2??; his Qd1 guarded c2).
- A 'DEFENDED' PAWN STILL FALLS to Qxb2 + a forced trade (T52S2G1 18.Qd2?? Qxb2 19.Rfb1 Qc3!).
- MY OWN QUEEN GRAB ON b2 CAN BURY HER: T53 Final 11...Qxb2?? boxed her on a2 - 12.Nb5! 13.Rb1 Qa2 14.Nc7! Rb8 15.Rxb8+ won my a8-rook (exchange and the game). Before a queen pawn-grab write HER RETREAT SQUARES and his knight routes to c7/d6/b5.
- A WARNING I WRITE IS AN ORDER for the next move; re-read the last comment before choosing.
- THE PIECE I MOVE MAY BE g7's ONLY GUARD (T49R1 10...Be7? 11.Qxg7; ...h6 is luft only for Kg8).
- COUNT EVERY DEFENDER BEFORE ANY CAPTURE, full diagonals both ways (T49R3 18.Qxd8+?? Bf6).
- A PAWN-ATTACKED PIECE MUST MOVE; defending it does not save it.
- HIS KNIGHT IN MY CAMP = no pawn grabs, no quiet pushes (T52 Final 16.f4? Nh5 17...Nxf4; 18.Bxa7? Rb4/Bxc3!/Rxe4+ won my queen).
- A ROOK CHECK NEAR MY KING: block on a DIFFERENT rank from my queen (T52 Final 20...Rxe4+ 21.Be3? Rxe3+ 22.Kd1 Rxc3).
- Qg3 + his bishop on e5/f6 = Qxg7#; never capture on e5 then (T48 Final 13...dxe5??).
- CHECKED? list block/capture squares and which of my pieces stand on the checker's line.
- QUEEN TRADE = recapture chain on my central knight (T48R1 11.Qd2??).
- A QUEEN IN FRONT OF HER KING on an open file is pinned: T51R1 21.Rg3! won her for a rook. Mine reversed: keep my queen off that file.
- DOWN A QUEEN OR PIECE v SF: guard every unit, 5-10 s, fortress and king shuttle (T52 Final held a threefold down Q+R - luck; T53 Final stayed solid 30 moves down an exchange, no gifts, mate only m47).

## Endings, king safety, conversion
- A CHECK ON THE DIAGONAL THROUGH HIS KING ALSO HITS A PIECE BEHIND IT: T53S2G1 42...Qe4+ saw Kg2 along e4-f3-g2 and Rb1 along e4-d3-c2-b1: king steps, Qxb1. From the checker's square walk BOTH directions to the edge.
- TWO QUEENS (or Q+R) v bare K: only checks that are defended and non-adjacent; never Qxf2+ Kxf2. T53S2G1 46...Qbe1#: one queen defends the checker, the other seals the rank.
- KING ON h1 + HIS QUEEN ON g3 = ...Re1# (T50R2). After Kh1 name the rank-1 squares his rooks reach.
- MY ...Bb7 + HIS Kg1 (g2 held only by his king) = Qxg2# (T51S2G1, T52R3).
- Bf6 + Qh6 v his Kg8: Qg7# when g8/d8/h7/h8 are covered by him or blocked by HIS OWN pieces (T51R1). T53R1 28.Bd5#: Qf6 seals f7/g7/f8/h8 and the bishop's long diagonal covers g8.
- Q+R v bare K: check from 2+ squares away, walk the king up, never park the rook where his king reaches it (T52R3 lost the rook to Kxb6 but mated with K+Q). No repetition loops.
- K+Q v lone K net verified (T52R3 69...Kd3! opposition, 70.Qg1#): distant checks drive him to the edge, then king into opposition; check stalemate every move.
- UP A ROOK / 2R v R: take the first clean rook trade, then collect loose pawns; drive a bare king off the passer's square with a rook check. R+B v R: stop the passer before racing.
- A ROOK NEEDS A SAFE SQUARE, NOT A CHECK (...Ra4+?? bxa4; ...Rb6+?? Kxb6).
- LEVEL R+B v R+B: the repetition draw is fair, but shuffles 15-30 s, no 6-min thinks.
- TWO ROOKS (or R+R+N) v QUEEN: draw by blockade, not raids (T49R3). DOWN A QUEEN v SF: guard everything, trade nothing into her files (T50R4 held 28 moves).

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. My losses are scan misses, not the clock. T52 Final burned 2:17 on a plain recapture. T53R3 spent 3:21 on the 14...Bf5?? bishop loss. Long thinks only for a concrete question; a 'plan' word in my comment is not one. T53S2G1 WIN used ~24 min in 46 moves (~30 s/move), 0 invalid - sound but keep quiet moves at 10-20 s.

## Opening: English reversed QGD as BLACK
- 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies), then ...Bf5/...Nbd7/...Re8/...Qb6.
- ...Qb6 wins the IQP d4 when HIS Nd2 blocks Qd1 (T50R3 12...Qxd4). Keep ...c6 (or ...Ne4 support) before ...c5, else d5 loses its guard.
- T52R2 v GLM: 17...Qxb3 won a pawn (his Qd2 left b3 loose); 18.Qc2?? had NO c2 recapturer - 18...Qxc2! won her, then queen raids + knight checks to Qxf1# m33. When his queen lands on my queen's line, count his recapturers and take.

## Opening: Open Sicilian Taimanov (both colours)
- 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies; ...Qc7/...b5/...Bb7 first transposes). Then f4/Qd2/Rad1 (White) or ...Qc7/...b5/...Bb7/...Rfc8 (Black).
- AS BLACK: ...b5 needs a guard first (...a6 or ...Bb7), else Nxb5! (T51R3). When his e5 hits Nf6 do NOT retreat to e8 with my a8-rook home (Nc7/Nd6/Nb6 fork a8+c8; T51S2G1 12...Ne8) - play ...Nd5 (count guards) or ...Nh5.
- AS BLACK keep the f6-knight and the queen guarded: T53R1 16...Rfd8?? left Nf6 to 17.exf6 and 20...Kg7?? left Qc7 to 21.Bxc7; 22.Nxc6! removed d8's last defender. Before a 'regrouping' rook/king move, list my loose pieces on the files and diagonals it touches.
- T53R3 (v mirror, L m24): after 13...dxe5 and 15...Nxd5 I was level, then 14...Bf5?? lost a bishop to 17.Rxf5 and 17...Qe6?? lost the queen to 18.dxe6. With HIS d-pawn passed on d5, d5's capture squares (c6, e6) are banned for every piece AND the queen; ...Qd6 blockade is fine, 'activating' onto a file his rook owns is not. Develop ...Bd7/...Rd8 first, keep ...Bf5 for a board where his f-file is closed or the bishop is guarded.
- T53S2G1 WIN v mirror (0 invalid, no gifts): Qc7 covering e5/d6 held all game; his e5+f4 clamp met ...Bc5 WITH CHECK and the ...d6 break. ...Nd5 safe because e6 recaptures (Rxd5 exd5); ...Ne8 fine once my c8-bishop is traded. Then Nxf4 won his queen, Qe4+ forked K+R.
- WHITE CLAMP WIN (T50 3rd, T51R1, T53R1): e5 supported by f4 means ...Nxe5 fxe5 wins a piece; then f5-f6 wedge, Bxf6, and exf6! Ban premature f4-f5.
- AS BLACK do not jump ...Nd5 into his Nc3 when e6 cannot recapture; ...Qc7 covers c6 and eyes e5. Trade his f6-knight FIRST; never 11.Nxd5??.
- T49R4 12.Nxc6! after ...Nxe4??: an in-between CHECK (13.Nxe7+) beats resolving a queen attack.
- Before moving my queen off the second rank check his ...Qxc2/...Qxb2 grab (T51R1 16.Qe3?!).
- T53R1 my own marks: 11.Rad1?!, 13.Ne4?!, 14.Nc5??. An outpost knight that only invites ...Bxc5/...Bd4 trades my good bishop; keep the e5 grip, add Re1/Bf1/Nf3.

## Opening: Open Sicilian Dragon (me White)
- 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 Ng4 (16 plies): his Ng4 is GUARDED by Bc8 through d7-e6-f5; answer 9.Nxc6! bxc6 10.Bg5, NEVER Qxg4 (T49R2 queen for a knight).
- After ...Qa5/...Rb8 finish king safety first; no f4 while his knight reaches h5/f4; no a7 grab with his knight in my camp (T52 Final 18.Bxa7? won my queen). 9.h3?! met ...Nxe3! (T51R2).
- Rook check in my camp: block on a rank without my queen (T52 Final 21.Be3? Rxe3+ then Rxc3).
- T53R2 v SF19: 10.O-O?! allowed 10...Be5! 11.Bd4? Bxh2+! 12.Kh1 e5! 13...Qh4 14...Bg1+! 15.Kxg1 Qh2#. His dark bishop on e5 + queen reaching h4 = h2 mate net; before O-O or moving Be3 count ...Bxh2+ and the ...Bg1+ deflection, and do not put Bd4 on that sac line.

## Opening: Taimanov as BLACK v Stockfish
- 1.e4 c5 2.Nf3 Nc6 3.Nc3 e6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.e5 Nd5 8.Qf3 Nxc3 (16 plies). ...Nxc3 hands him c3+d4+e5 - take it only for a concrete reason; otherwise ...Be7/...O-O/...Qc7.
- 7.Ndb5 Qb8! only good retreat (the queen still guards c7 and d6).
- 8...a6 9.Nxd4 Qxd4 then ...Be7? loses to e5!: his Nf6 has no good square (d5 drops a pawn to Qxd5, h5 g4, e8 forked, f6 is the e5-pawn's capture square).
- With queens on, do NOT open the centre and never take on e5 (14...Bxe5?? 15.Bxe5 Qxe5+ 16.Qxe5). ...f6 only with his Bf4 off the c7 diagonal and his e5 unable to capture.
- King on e8 makes Bf8 g7's only guard: ...Be7?? Qxg7 (T49R1); ...h6 is luft only for Kg8. ...O-O?? before ...Qc7 allows Bxc6! winning a8 (T49 Final). Down material, audit every enemy knight landing.
- T53 Final (L m47): 7.Bd3 d5 8.exd5 cxd5 9.Bf4 Be7 10.a3 Qb6 11.O-O was sound, level to m11. The loss was 11...Qxb2?? (see Move discipline): b2 was loose but his Nb5!-c7 plus Rb1 on the half-open b-file cost me the a8-rook. With queens on, play ...Bd7/...Qc7 and keep the queen on a square with a named retreat. Down the exchange my ...Bxa3/...Nd7/...Nc5/...Nxd3/...Bb2 kept me solid and cost 30 moves to lose - correct style, but do not gift.

## Opponents
- Stockfish 19 (depth 4): instant, no second chances. Punishes loose pieces, hidden defenders (Bc8-g4), captures that open a bishop to g7, an unguarded c6 (Bxc6!), a kicked Ng4 (...Nxe3!), a retreat onto his e5-pawn's capture square (f6), and ...Be7/...f6 met by exf6 opening Bf4-c7. Builds the h4/h5/Bf4/Qg3 clamp and converts a piece up - but takes a threefold when his checks repeat. T53R2 Dragon: ...Be5/...Bxh2+/...Qh4 mated me. T53 Final: punished 11...Qxb2?? with 12.Nb5! 13.Rb1 14.Nc7! instantly.
- DeepSeek V4.1 Flash (mirror): solid Taimanov both colours, converts without gifts, never resigns, 1-3 illegal tries/game. T52R3 (I won): punished my loose Nd7 with 21.Rxd7!; 25.Ra3?? sat on my b4 pawn's capture square. T53R3 (I lost): it took the loose Bf5 with Rxf5 and the Qe6 with dxe6 at once. T53S2G1 (I WON): it burned 5:20/9:14/5:05 on 17.Bf3/20.Nc5/21.Rd6, then handed me a full rook with 26.Rxa6?? Qxa6 and hung Qf4 to Nxf4 - it punishes loose units but its own grabs go unverified, and its clock bleeds on quiet moves.
- GLM 5.3 Flash: as White the English reversed QGD (slow, punishes a rook on a pawn capture square); as Black the Taimanov with a sound ...a6/...b5/...Bb7/...Qc7 build but careless with the f6-knight and queen: T53R1 12...Ne8? then 16...Rfd8?? exf6, 20...Kg7?? Bxc7, 22.Nxc6!; T52R2 18.Qc2?? Qxc2! lost his queen. Vs GLM: sound 10-20 s moves, e5 clamp, take every loose unit and queen, let its clock run.

## Record
- T47R1 W v GLM 1-0 forfeit. T48R1 W v SF19 0-1 (11.Qd2??). T48 Final B v SF19 0-1 Qxg7# (13...dxe5??).
- T49R1 B v mirror win by forfeit. T49R2 W v SF19 0-1 (10.Qxg4?? Bxg4). T49R3 W v GLM draw (12.exf6!, 18.Qxd8+??). T49R4 W v GLM 1-0 on time (13.Nxe7+!, 21.Qd3?? cxd3). T49 Final B v SF19 0-1 (11...O-O? Bxc6!).
- T50R1 B v SF19 0-1 (10...Be7? Qxg7). T50R2 W v mirror 0-1 (11.Nxd5??, 30...Re1#). T50R3 B v GLM 0-1 (12...Qxd4!, 44...Ra4+?? bxa4). T50R4 B v SF19 0-1 (14...Bxe5??). T50 3rd W v GLM 1-0 (e5 clamp, 51.Rd8#).
- T51R1 W v GLM 1-0 (21.Rg3! pin, Qg7#). T51R2 W v SF19 0-1 (9.h3?! Nxe3!). T51R3 B v mirror 0-1 (12.Nxb5!, 12...Qxc2??). T51S2G1 B v mirror WIN Qxg2#. T51 Final B v SF19 0-1 (14...f6??).
- T52R2 B v GLM WIN Qxf1#. T52R3 B v mirror WIN Qg1# m70. T52S2G1 W v mirror draw (18.Qd2?! Qxb2/Qc3). T52S2 Arm B v mirror WIN on time. T52 Final B v SF19 draw threefold (7.Ndb5 Qb8!, 10...Be7? e5!). T52 Final Arm W v SF19 0-1 (16.f4? Nh5).
- T53R1 W v GLM 1-0 m28 (Taimanov clamp, 17.exf6!, 28.Bd5#). T53R2 W v SF19 0-1 Qh2# (Dragon; 10.O-O?! Be5! Bxh2+). T53R3 B v mirror 0-1 (Taimanov: level to m16, then 14...Bf5?? Rxf5 and 17...Qe6?? dxe6; mate m24). T53S2G1 B v mirror WIN Qbe1# m46 (Taimanov: ...Bc5 with check, ...d6 break, 27...Nxf4! won the queen, 42...Qe4+ forked K+R; 0 invalid).
- T53 Final B v SF19 0-1 m47 (Taimanov ...d5 line level to m11; 11...Qxb2?? boxed the queen, 12.Nb5! 14.Nc7! won my a8-rook; 3 illegal tries on 40...Bc6).
