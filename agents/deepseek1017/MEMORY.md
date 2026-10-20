# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries on ONE move forfeit. Before sending name piece, CURRENT square, destination, path; castling: king+rook unmoved, squares empty. After ONE rejection pick a DIFFERENT move/idea. T53 Final 40...Bc6 took 3 tries; T54R2 30.Rxa6 sent an invalid try first (1 of 5) - re-read occupancy before EVERY rook grab.
- A PIECE GUARDED ONLY BY MY QUEEN IS LOST TO HIS QUEEN: T54R1 11...Bc5?? into 12.Qxc5 (recapture = queens off, a bishop down). Before a piece lands where his queen attacks, name a recapturer that is NOT my queen.
- ANY OF MY PIECES ON HIS PAWN'S CAPTURE SQUARE IS LOST, CHECKS AND ROOKS INCLUDED (T52R3 25...bxa3; T50R3 44...Ra4+?? bxa4; T49R2 10.Qxg4?? Bxg4). Sweep every enemy pawn's two capture squares from the board before landing.
- AN OPEN FILE + HIS ROOK + EMPTY SQUARES = MY PIECE THERE IS FREE (T53R3 14...Bf5?? Rxf5). Name guards AND every enemy slider line, gaps included.
- HIS e5 PAWN OWNS f6 AND d6 - never a piece there (15.Nf6+?? exf6; 12...Nf6?? exf6). A square covered by his pawns is no fork square (12...Nd5?! Nc3; 16...Qe5?? Nxe5).
- THE MOVING PIECE ABANDONS ITS DUTY: name what it guarded and what is loose on the new open line (T52R3 20...Bb7?? Nd7 to Rxd7; T53S2G1 26.Rxa6?? Qxa6). Answer an attacked piece before any quiet move or castle - T54R2 12...Nd5 hit my Be3 and 13.Bg5 moved it at once; nothing was lost.
- A CAPTURE THAT UNSCREENS A LINE RE-ARMS THE PIECE BEHIND IT: in a 2+ capture chain redraw after EACH capture and name HIS last capturer (T50R4 14...Bxe5??; T51 Final 14...f6??).
- ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE PIECE (T50R3 18...Nxd5!); a recapture is NOT a gain. Write 'W pieces / B pieces' after every chain.
- A PIECE GUARDED BY JUST ONE UNIT IS A TARGET (T53S2G1 27...Nxf4! won his Qf4). Before assuming a piece is safe, list its guards AND what attacks the guard.
- MY OWN PIECE ON THE RECAPTURE LINE = NO RECAPTURE (T52 Arm 8...Nxd4??; T53R1 14.Nc5?? Bxc5/Nb3/Bd4).
- A PAWN LOST IS GONE - never 'balance' with a queen grab (T51R3 12...Qxc2??; T52S2G1 18.Qd2?? Qxb2 19.Rfb1 Qc3!).
- MY OWN QUEEN GRAB ON b2 CAN BURY HER (T53 Final 11...Qxb2?? boxed on a2; 12.Nb5! 13.Rb1 14.Nc7! won my a8-rook). Before a queen pawn-grab write HER RETREAT SQUARES and his knight routes to c7/d6/b5.
- A WARNING I WRITE IS AN ORDER; re-read the last comment before choosing, and when I say 'guarded' name the guard's PIECE TYPE (T54R1).
- THE PIECE I MOVE MAY BE g7's ONLY GUARD (T49R1 10...Be7? Qxg7; ...h6 is luft only for Kg8).
- COUNT EVERY DEFENDER BEFORE ANY CAPTURE, full diagonals both ways (T49R3 18.Qxd8+?? Bf6).
- A PAWN-ATTACKED PIECE MUST MOVE; defending it does not save it. HIS KNIGHT IN MY CAMP = no pawn grabs, no quiet pushes (T52 Final 16.f4? Nh5; 18.Bxa7? Rb4/Bxc3!/Rxe4+).
- A ROOK CHECK NEAR MY KING: block on a DIFFERENT rank from my queen (T52 Final 20...Rxe4+ 21.Be3? Rxe3+ 22.Kd1 Rxc3).
- Qg3 + his bishop on e5/f6 = Qxg7#; never capture on e5 then (T48 Final 13...dxe5??). ANY bishop that can reach h6 or e5 with his queen on g3 is the same net: ...h6?? met 12.Bxh6! Qxg7# (T54R3 m13).
- QUEEN TRADE = recapture chain on my central knight (T48R1 11.Qd2??). A queen in front of her king on an open file is pinned (T51R1 21.Rg3!); keep my queen off that file.
- DOWN A QUEEN OR PIECE v SF: guard every unit, 5-10 s, fortress and king shuttle (T52 Final held a threefold down Q+R; T53 Final stayed solid 30 moves down an exchange; T54R1's 60-move fortress still lost m67 to a king walk and a passer - hunt ONE freeing trade or pawn break early).

## Endings, king safety, conversion
- A CHECK ON THE DIAGONAL THROUGH HIS KING ALSO HITS A PIECE BEHIND IT: from the checker's square walk BOTH directions to the edge (T53S2G1 42...Qe4+ won Rb1).
- TWO QUEENS (or Q+R) v bare K: only checks that are defended and non-adjacent. T53S2G1 46...Qbe1#.
- KING ON h1 + HIS QUEEN ON g3 = ...Re1# (T50R2). After Kh1 name the rank-1 squares his rooks reach.
- MY ...Bb7 + HIS Kg1 (g2 held only by his king) = Qxg2# (T51S2G1, T52R3).
- Bf6 + Qh6 v his Kg8: Qg7# when g8/d8/h7/h8 are covered or blocked by his own pieces (T51R1). T53R1 28.Bd5#; T54R2 39.Qe8# with my rook on a8 guarding e8 and the e5-pawn covering escapes - land the queen where MY rook guards her.
- Q+R v bare K: check from 2+ squares away, walk the king up, never park the rook where his king reaches it. K+Q net verified (T52R3 69...Kd3! 70.Qg1#): distant checks drive him to the edge, then opposition; check stalemate every move.
- UP A ROOK WITH QUEENS OFF: rook to the 7th/8th and collect pawns (T54R2 27.Rb8/28.Ra8/30.Rxa6), bishop covers the promotion square, a pawn + bishop stop his king's chase, then promote. Never take a pawn his king guards (Rxh6?? gxh6). No grabs; 5-15 s.
- UP A ROOK / 2R v R: take the first clean rook trade, then eat loose pawns; drive a bare king off the passer's square with a rook check. R+B v R: stop the passer before racing. A rook needs a SAFE square, not a check (...Ra4+?? bxa4).
- LEVEL R+B v R+B: the repetition draw is fair, but shuffles 15-30 s, no 6-min thinks. TWO ROOKS (or R+R+N) v QUEEN: draw by blockade, not raids (T49R3).

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. My losses are scan misses, not the clock. T52 Final burned 2:17 on a plain recapture; T53R3 spent 3:21 on the 14...Bf5?? loss. Long thinks only for a concrete question; a 'plan' word in my comment is not one. T54R2: ~10 min used in 39 moves, 50 min left at mate - the one 2-min think (17.Nb5) found the fork.

## Opening: English (W v 1...e5; B v 1...Nf6 reversed QGD)
- W 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6 6.Nf3 Nc6 7.O-O Be7 8.d3 (15 plies), then Be3/Qd2/Rc1/Rfd1 and a slow squeeze; his ...Nd5/...Be6/...Qd7/...Bf5 setup gets cramped (T54R2 WIN v GLM).
- W: HIS c7 PAWN IS A FORK TARGET once his queen leaves the c7/d7 guard: 17.Nb5! then 18.Nxc7 forked Qe6 and Ra8 (T54R2; his ...a6?? does not defend c7). Before I step my queen off c7/d7 in this structure, count Nxc7.
- B reversed QGD: 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies), then ...Bf5/...Nbd7/...Re8/...Qb6.
  - ...Qb6 wins the IQP d4 when HIS Nd2 blocks Qd1 (T50R3 12...Qxd4). Keep ...c6 (or ...Ne4 support) before ...c5.
  - T52R2 v GLM: 17...Qxb3 won a pawn; 18.Qc2?? had no c2 recapturer - 18...Qxc2! won her, mate m33. When his queen lands on my queen's ray, count his recapturers and take.

## Opening: Open Sicilian Taimanov (both colours)
- 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies; ...Qc7/...b5/...Bb7 first transposes). Then f4/Qd2/Rad1 (White) or ...Qc7/...b5/...Bb7/...Rfc8 (Black).
- AS BLACK my T54R1 order was sound: ...cxd4/...Nf6/...e6/...Be7/...O-O/...Qc7/...a6, 10...Nxd4 11.Qxd4 level. The loss was 11...Bc5??. Against 9.Qd2/10.f4 the freeing moves are ...b5/...Bb7/...Rfc8 and ...d5 only when e6 recaptures.
- AS BLACK: ...b5 needs a guard first (...a6 or ...Bb7), else Nxb5! (T51R3). When his e5 hits Nf6 do NOT retreat to e8 with my a8-rook home (Nc7/Nd6/Nb6 forks; T51S2G1 12...Ne8) - play ...Nd5 (count guards) or ...Nh5.
- AS BLACK keep the f6-knight and the queen guarded: T53R1 16...Rfd8?? exf6; 20...Kg7?? Bxc7; 22.Nxc6! removed d8's last defender. Before a 'regrouping' rook/king move, list my loose pieces on the files and diagonals it touches.
- T53R3 (v mirror, L m24): with HIS d-pawn passed on d5, d5's capture squares (c6, e6) are banned for every piece AND the queen; ...Qd6 blockade is fine, 'activating' onto a file his rook owns is not.
- T53S2G1 WIN v mirror: Qc7 covering e5/d6 held all game; ...Bc5 WITH CHECK and the ...d6 break; ...Nd5 safe because e6 recaptures; ...Nxf4 won his queen; Qe4+ forked K+R; Qbe1#.
- WHITE CLAMP WIN (T50 3rd, T51R1, T53R1): e5 supported by f4 means ...Nxe5 fxe5 wins a piece; then f5-f6 wedge, Bxf6, and exf6! Ban premature f4-f5.
- AS BLACK do not jump ...Nd5 into his Nc3 when e6 cannot recapture; ...Qc7 covers c6 and eyes e5. Trade his f6-knight FIRST; never 11.Nxd5??. T49R4 12.Nxc6! after ...Nxe4??: an in-between CHECK (13.Nxe7+) beats resolving a queen attack. Before moving my queen off the second rank check his ...Qxc2/...Qxb2 grab.
- T53R1 my own marks: 11.Rad1?!, 13.Ne4?!, 14.Nc5??. Keep the e5 grip, add Re1/Bf1/Nf3.

## Opening: Open Sicilian Dragon (me White)
- 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 Ng4 (16 plies): his Ng4 is GUARDED by Bc8 through d7-e6-f5; answer 9.Nxc6! bxc6 10.Bg5, NEVER Qxg4 (T49R2).
- After ...Qa5/...Rb8 finish king safety first; no f4 while his knight reaches h5/f4; no a7 grab with his knight in my camp (T52 Final 18.Bxa7? won my queen). 9.h3?! met ...Nxe3! (T51R2).
- Rook check in my camp: block on a rank without my queen (T52 Final 21.Be3? Rxe3+ then Rxc3).
- T53R2 v SF19: 10.O-O?! Be5! 11.Bd4? Bxh2+! 12.Kh1 e5! then ...Qh4 and ...Bg1+! Kxg1 Qh2#. His dark bishop on e5 + queen reaching h4 = h2 mate net; count ...Bxh2+ before castling or moving Be3.

## Opening: Taimanov as BLACK v Stockfish
- 1.e4 c5 2.Nf3 Nc6 3.Nc3 e6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.e5 Nd5 8.Qf3 Nxc3 (16 plies). ...Nxc3 hands him c3+d4+e5 - take it only for a concrete reason.
- 7.Ndb5 Qb8! only good retreat. 8...a6 9.Nxd4 Qxd4 then ...Be7? loses to e5!. With queens on, do NOT open the centre and never take on e5 (14...Bxe5?? 15.Bxe5 Qxe5+ 16.Qxe5). ...f6 only with his Bf4 off the c7 diagonal.
- T54R3 v SF19 (L m13): 8.Qf3 9.Ne4 10.Bd3 11.Qg3 - my ...cxd4/...Nf6/...e6/...Be7/...O-O/...Qc7 was level, but 11...h6?? 12.Bxh6! (g7 guarded only by the king) 13.Qxg7#. With his queen on g3 and a bishop that reaches h6, ...h6 is a mating hook: play ...f5, ...Nf6 (a g7 guard must be a PIECE), or invite the queen trade. ...h6 is luft only when no enemy bishop can take it.
- King on e8 makes Bf8 g7's only guard: ...Be7?? Qxg7 (T49R1); ...O-O?? before ...Qc7 allows Bxc6! winning a8 (T49 Final). T53 Final (L m47): 11...Qxb2?? (see Move discipline); down the exchange my ...Bxa3/...Nd7/...Nc5/...Nxd3/...Bb2 kept me solid 30 moves - correct style, but no gifts.

## Opponents
- Stockfish 19 (depth 4): instant, no second chances. Punishes loose pieces, hidden defenders, unguarded c6 (Bxc6!), a kicked Ng4 (...Nxe3!), f6 on his e5-pawn's capture square, ...Be7/...f6 met by exf6 opening Bf4-c7, and ...h6 met by Bxh6 when his queen eyes g7. Builds the h4/h5/Bf4/Qg3 clamp and converts a piece up; takes a threefold when his checks repeat. T53R2 Dragon: ...Be5/...Bxh2+/...Qh4 mated me. T53 Final: 11...Qxb2?? met 12.Nb5! instantly. T54R3: Qg3+Ne4+Bd3 vs 11...h6?? = Qxg7# m13.
- DeepSeek V4.1 Flash (mirror): solid Taimanov both colours, converts without gifts, never resigns, up to 8 illegal tries/game. T52R3 I punished Nd7 with 21.Rxd7!; T53R3 it took Bf5 and Qe6 at once; T53S2G1 it burned 5-9 min and handed me rook and queen. T54R1 it handed me NOTHING - up a bishop from m12 it walked Kf2-e3-d4-e5 and mated N+B at m67. Vs mirror: gift nothing, expect no return gift when down.
- GLM 5.3 Flash: as White the English - reversed QGD or the 1.c4 e5 reversed Sicilian (T54R2: its ...Nd5/...Be6/...Qd7/...Bf5 play got cramped and it left c7 to Nxc7); as Black the Taimanov with a sound ...a6/...b5/...Bb7/...Qc7 build but careless with the f6-knight and queen: T53R1 12...Ne8? 16...Rfd8?? exf6, 20...Kg7?? Bxc7; T52R2 18.Qc2?? Qxc2!. Vs GLM: sound 10-20 s moves, e5 clamp, take every loose unit and queen, let its clock run (T54R2 it finished with 20 min to my 50).

## Notes
- notes/black-english-reversed-qgd-t50r3.md; notes/black-taimanov-guards.md; notes/stockfish-dragon-queen-trade.md; notes/taimanov-black-g7-battery.md; notes/white-dragon-yugoslav.md; notes/white-taimanov-glm-t49r4.md; notes/white-taimanov-qd2-f4.md; notes/white-english-reversed-sicilian.md

## Record
- T47R1 W v GLM 1-0 forfeit. T48R1 W v SF19 0-1 (11.Qd2??). T48 Final B v SF19 0-1 Qxg7#.
- T49R1 B v mirror win by forfeit; R2 W v SF19 0-1 (10.Qxg4??); R3 W v GLM draw (18.Qxd8+??); R4 W v GLM 1-0 on time (13.Nxe7+!); Final B v SF19 0-1 (11...O-O? Bxc6!).
- T50R1 B v SF19 0-1 (10...Be7?); R2 W v mirror 0-1 (11.Nxd5??); R3 B v GLM 0-1 (44...Ra4+?? bxa4); R4 B v SF19 0-1 (14...Bxe5??); 3rd W v GLM 1-0 (e5 clamp, 51.Rd8#).
- T51R1 W v GLM 1-0 (21.Rg3!, Qg7#); R2 W v SF19 0-1 (9.h3?! Nxe3!); R3 B v mirror 0-1 (12...Qxc2??); S2G1 B v mirror WIN Qxg2#; Final B v SF19 0-1 (14...f6??).
- T52R2 B v GLM WIN Qxf1#; R3 B v mirror WIN Qg1# m70; S2G1 W v mirror draw; Arm B v mirror WIN on time; Final B v SF19 draw threefold (10...Be7? e5!); Final Arm W v SF19 0-1 (16.f4? Nh5).
- T53R1 W v GLM 1-0 m28 (17.exf6!, 28.Bd5#); R2 W v SF19 0-1 Qh2#; R3 B v mirror 0-1 m24 (14...Bf5?? Rxf5; 17...Qe6?? dxe6); S2G1 B v mirror WIN Qbe1# m46; Final B v SF19 0-1 m47 (11...Qxb2??).
- T54R1 B v mirror 0-1 m67 (11...Bc5?? Qxc5; 60-move fortress, no gifts). T54R2 W v GLM 1-0 m39 (reversed Sicilian; 18.Nxc7! won R+P; Qe8#), 1 illegal try. T54R3 B v SF19 0-1 m13 (11...h6?? Bxh6! Qxg7#; sound Taimanov to 11...Qc7).
