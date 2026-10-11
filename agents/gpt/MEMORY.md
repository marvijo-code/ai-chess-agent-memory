# Chess memory

## Move discipline
- Apply stored warnings BEFORE choosing. Every candidate needs its own forcing scan; rejecting one blunder does not validate another. Repeated ...f6/...Qd6?? exd6 shows recognition alone fails.
- Start with the enemy's last move: changed attacks, pawn controls, opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board. After MY check and the king's reply, refresh attacks on my checking piece before pursuing another tactic.
- PAWN DIAGONALS FIRST, then knights and complete sliding rays. Rb3?? a4xb3, Qe4?? d5xe4 and Qd5?? e6xd5: defending or attacking another piece never makes a heavy-piece destination safe. Ng5? hxg5 lost N for P; Qxe6 fxe6 lost Q despite no marks. Support cannot prevent a cheaper capturer.
- Test Kxchecker first and name its actual defender. ...Qh2+?? Kxh2, Rh7+?? Kxh7 and ...Qxb2+?? Kxb2 lost heavy pieces. Check does not establish safety.
- Name exact defenders, screens and LEGAL recapturers. Nd2 blocked Be3-c1, Rc1's sole guard. Be3 blocks Re1-e4; f7 blocks Rf8-f2; Qe3 cannot recapture c2. Audit friendly rays newly blocked as well as enemy rays opened.
- T31 Sonnet SF: axb5 axb5 opened Ra8-a1 while Bc1 blocked Re1-a1. 20.Qc6?? Rxa1 21.Bd2 Rxe1+ 22.Bxe1 lost a rook. Attacking Ra8 did not force it to stay. Before opening a file, name the legal recapture on BOTH ends.
- Validate the actual piece square and full path before submission. After one rejected move, reconstruct the board before retrying; three invalid replies forfeit. A remembered opening move may be impossible on a different branch.
- T31 SF: Kb3 screened Rb1-b7. 39...Rb1+ 40.Ka4? opened ...Rxb7; 41.Nxd6 recovered only B for R. When answering a rook check, trace the line BEYOND the king and test interpositions as well as king moves.
- T30 Final: ...Bc3 covered h8 through d4/e5/f6/g7, but ...Kd4 blocked MY bishop, allowing h8=Q+. A king is also a screen. Retrace the entire promotion diagonal after every king move.
- Count duties AFTER the last recapture. Re2?? Rxe2 Nxe2 removed BOTH e4 guards, Re1 and Ng3; ...Nxe4 won P. A locally equal trade can lose material elsewhere.
- T31 Armageddon: ...Nf6-g4 attacked Qe3/Bh6 AND opened Bh8-g7-f6-e5-d4 against Nd4. Qd2? Nxh6 Qxh6 Bxd4 lost N: Qxh6 abandoned the queen's d4 guard. A queen guarding two attacked pieces may lose one after recapturing on the other. Examine capturing the forking knight with Rxg4 and all replies; no verified best replacement.
- Refresh pins when endpoints move. ...Nd4?? Nxd4 cxd4 Rxd8+ exposed Qd8. Kb1 released Rd2; Kg2 pinned Nd2 to Ra2, Kf1 released it. A pinned rook can capture its pinning queen.
- T30 SF: Qg6 pinned g2 to Kg1. f3? Nf4 Qf2 Nxh3+ Kh1 Nxf2+ lost Q for N; gxh3 was ILLEGAL. A queen defending mate must also survive checking forks.
- Before moving a guard/screen, trace lost guards and exposed rays. ...f6/exf6 exposed Be6 to Qe2; f2-f3 abandoned Be3. Ne4 opened Ra2-e2 with Ba6 guarding e2.
- Before forks/trades, test captures and checking intermezzos. ...Nc3+ Qxc3 Rxd1 Rxd1 lost N; Bxd5?? Nd3+ preceded ...Qxd5. An attacked queen can capture its attacker; a capturer does not guard its own square.
- T31 Armageddon: Qg8+ Kd7 removed Ke8's screen from Qd8-e8-f8-g8. Nc7?? Qxg8 Nxa8 Qxa8 lost Q+N for R. A fork does not answer an attack on my queen; calculate the opponent's captures before assuming the forked pieces must respond. This queen loss had no adverse mark.
- T30 Final: Bc3 guarded a5 through b4. ...Rxa5?? Bxa5 lost my last rook for P, despite no adverse mark. A pawn raid must pass the complete bishop-ray scan.
- Derive knight attacks from actual squares. Nf3 did NOT attack e4, and e3 blocked Re1-e4. Ng3xe4?? Bxe4 Bxe4 Qxe4 won a minor for a pawn; the claimed three attackers were only two.
- Trace attacking batteries through OWN pawns. exf5 cleared e4 but put a new screen on Bc2-h7; f6 cleared it. After ...gxf6/...f5, Bxf5 removed the screen; gxf5 would replace it with my pawn.
- MATE FIRST, including quiet threats and queenless positions. ...Nxf4 attacked Qh5 but allowed Qxh7#; Rxe7 ignored ...Rh1#. Luft solves only the mate its flight prevents. Before advancing an exposed king, test every enemy check and resulting flight.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3. Long thinking never replaces a capture scan.
- Name a target/break before shuffling. Re2/Rb4/Rb3 and Bxb6/Rf1/Nb3 consumed 36-56 seconds yet missed pawn captures, lost guards and checking forks. Spend calculation on the opponent's forcing reply.
- T31 Armageddon: fxg4 took 117 seconds and Bh6 68; finished 5:14, no invalid attempts. Neither think prevented later material losses. Budget from the actual starting clock: White had 10 minutes. Book/development in T31 DeepSeek mostly 4-12 seconds worked.
- T31 Final: ...Rf4?? took 46 seconds; later ...Bd6/...hxg3/...Be5 took 42/53/49. Finished 5:52. Once a defensive bishop cycle is verified, use 1-5 seconds unless a pawn move, check or changed rook ray alters it.
- Track TOTAL material through the last recapture and actual reply. Qxc1 Bxc1 Rxc1 Qxc1 costs Q+R for R+B. Ne2+ Nxc1 Rxc1 wins the exchange. ...Nxe4 taking B is not a trade until Qxe4 occurs; f3 instead leaves the captured bishop lost.
- T31 Final: ...Rf5-f4?? challenged Re4 but Bd2 attacked f4 through e3. Bxf4! Bxf4 left my B versus R with equal pawns: lost exchange. Bd6 and g5 supported f4 but neither prevented the cheaper capture. For any heavy-piece trade offer, list ALL enemy capturers and compare each complete material balance.
- Ahead: remove counterplay, simplify safely, preserve mating material. Check pawn guards and entry squares before queen trades. Worse: safe activity/repetition; later gifts do not validate earlier errors. Armageddon White needs a win, but speculative material losses do not create a verified winning chance.
- B+P conversion: preserve the LAST pawn with king support before using the bishop to stop a remote passer. A bishop alone cannot mate. Count the enemy king's route to the pawn and how many moves the passer gives you.
- T30 Sonnet: Kd5/Be7/a5 vs Kb3/g5/h5, ...Bxg5?? Ka4! Bd8 h6! Kc4 h7! Bf6! Kxa5 drew. Bd8 alone guarded a5; h7 forced it to guard h8 instead. ...Bf6 saved the draw, not the win; seek king support before taking g5.
- Escort passers; scan straight AND capture-promotions two advances ahead. c2 attacks b1/d1. Ba1 Rc1+ Kh2 Rxa1 removes a blockader. ...Rf8 Rxf8+ Nxf8 b8=Q removes a pinned blockader. Ka3 guarded a2, but Bc1+ Ka4 Rxa2+ deflected the escort. Calculate checks against the king before claiming the rook is tied down.
- T31 SF: Nxd6 removed Ba3's defender but allowed ...a2! before Kxa3. Nd6 could reach neither a2 nor a1; Ka3 then allowed ...a1=Q#. Removing a passer's guard helps only if capture/blockade occurs before its next advance.
- T31 Sonnet SF: Bf2 guarded c5; b5 prepared supported c6 while a rook down. Kc5?? allowed ...Bf8+ Kb5 Bd6!, covering c7/b8. Later ...Bc7?? Bb6 Bxb6 Kxb6 removed the blockader: Rd8 guarded neither c7 nor b6. Scan checking deflections of the escort and king-supported attacks on blockaders. Won on time; no completed conversion established.
- T31 Final defense: Be5 guarded c7 AND h8; Bd6 guarded c5/c7 and was protected by c7. After ...Bf6 blocked Rf8+, ...Kg5 kept Bf6 guarded, but ...Kxh6 abandoned it: Rxf6+ won B for the h-pawn. Recount king guards after a pawn capture. SF repeated at move 71 with R vs pawns and about +7; this was an escape, not a proven fortress.
- Verify mate support, all flights and stalemate. e5 clears Bb1-h7; ...Nf6xd5 can abandon h7. Qf2 supports Rd1# vs Kh1. Qg3/Ne4 supports Qxg3+ then Nf2#. Re7+ Kg8 h7+ Kh8 Bf6#: h7 controls g8, Re7 protects h7 and covers g7. Repetition with Q+R vs bare K proves no fortress.
- T31 Armageddon: Qh7 threatened Qg8#, but ...Be6 vacated d7 for the king. Qg8+ Kd7 was only check. Recompute flights after a quiet defense; Nd5 blocked Rd1's control of d7. Later Kxa6 Qa8+ Kb5 Qa5# punished a king raid despite five minutes remaining.
- T31 DeepSeek: ...Re8 Rxe8+ Qxe8 safely removed a rook. Rd2 allowed ...Qe1#: f2/g2/h2 occupied all second-rank flights, and Rd2 could neither reach f1 nor capture e1. After simplification, scan direct mate before another trade or pawn grab.

## White openings
- T31 Armageddon Dragon: Nc3/Bg7/Be3/Nf6/Bc4/d6/f3/Bd7/Qd2/a6/O-O-O/b5/Bb3/h5/Kb1/Na5/h4/Nc4/Bxc4 bxc4. g4?! hxg4! h5 Rxh5 Rxh5 Nxh5 fxg4 Bxg4! repeated the T10 loss: my f/g/h pawns for Black's h-pawn, two pawns down. Bxg4 ignored the attack on Nh5 and attacked Rd1 through f3/e2. Count the entire pawn liquidation before g4; no verified move-15 replacement.
- T31 Sonnet SF Zaitsev/Breyer: ...Bb7/Re8/Bf8, a4 Nb8? 13.d5? Nbd7 14.Nf1 c6 15.Bc2?! cxd5 16.exd5 Bxd5 lost a central pawn. Ne3 Bxf3?! Qxf3 kept the bishop pair but did not recover it. No verified replacements for moves 13/15.
- T31 Maroczy: e4/c5/Nf3/Nc6/d4/cxd4/Nxd4/g6/c4/Nf6/Nc3/Qa5/f3/Nxd4/Qxd4!/Bg7/Be3/d6/Be2/O-O. Before O-O?! calculate ...Ng4: Nf6 leaves Bg7-f6-e5-d4 open, attacking Qd4 while Ng4 attacks Be3. Qd2/Nxe3/Qxe3! preserved pawns but conceded the bishop pair. No verified move-11 replacement.
- Same game: ...Be6/Rac1/Rfc8/Rfd1?! Bxc4! Bxc4 Rxc4! lost c4 and activated the rook against Nc3. Nd5 cleared c3, allowing ...Rxc1 Qxc1. A bishop guard does not save a pawn when the attacking bishop has a rook behind it. Nf4?!/Qxa2/Rxd6/Qxb2/Nd3/Qxc1+/Nxc1 left R+N vs R+B, two pawns down. No verified replacements for moves 15/19.
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and attacks Nf6. ...Nd7?? Qxd7 Qxd7 Rxd7 wins N; ...Bf6 exf6 wins B for P even without a mark. e5 screens Qc7-f4 against ...Nxf4. No forced opening edge established.
- Caro ...Nd5 Bd2 ...Nc7 Qe4; ...Bf6? exf6 Qxf6 Bc3 attacks Q and clears d2. ...Qxf2 Be1 guards Ng3 through f2; ...Qb6 Rd7 invades.
- Chigorin: Nf1 restores Qd1-d4; Qf3 abandons b3 to ...Nb3. Rc1/Bb1's queen trap needs actual c-file geometry; ...Qb7 avoids it. ...Rac8/d5 Nb4/Bb1 a5/a3 Nc2 forced Bxc2 Qxc2 Qxc2 Rxc2: equal material, active enemy rook. Branch matters: Na5 cannot play ...Nb4. T31 instead had d5 Nc4 b3 Nb6!.
- T30 Sonnet SF: ...Rfe8/Rac8, d5 c4/Be3 Nb7/Qd2 Nc5/Nh2 Bf8/f4 exf4/Bxf4! Be7/Rad1 h6. Nh2 enabled f4 and activated Bf4; no forced opening edge or validation of d5 against ...Nb4.
- Same game: Nf5? Bxf5/exf5!/Nh5/Be3?! Nf6?/Ng4? Nxg4!/hxg4!/Bf8?/f6 gxf6/Bxh6 Bxh6?!/Qxh6! Rxe1+??. Knight errors remain errors; no verified replacements. The rook-trade blunder enabled Qh7+/Qh8#, with Bf5 supporting h7 and Re1 denying e7; not proof of a sound sacrifice.
- T31 Sonnet R3: Qe3?! Bf8 Ng4?? Nxg4 hxg4! Bxg4! lost h-pawn and attacked Rd1. ...Nxg4 also attacked Qe3. Opening the unused h-file did not compensate; calculate the capture AFTER the recapture. Nf5?! Bxf5 exf5! Nxd5 left White two pawns down.
- Same game: f6 Nxf4?? Qxf4?? gxf6?? Qxf6+?? Bg7! blocked with tempo. With f6 attacking Re7, compare fxe7 and forcing king threats before automatically recovering Nf4; no verified replacements. Rxf6/Bxf6/Qxh6+! Qh7?? Bxh7 won Q; final Q+R+B vs 2R+B, equal pawns. Forfeit was not completed mate or proof of a forced attack.
- Ruy d3: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. Qd3/Bb1 threatens Qh7#, answered by ...g6. Nbd2 blocks Qd1-d4; Be3 blocks Re1-e4. Before g3/h4 calculate ...f5/...fxe4 and Qh4 routes.
- T30 SF ...Bc5/d6/h6/Bb7: d5 Ne7 ...c6 dxc6 Bxc6 activated Black. ...d5/dxe4/Nxe4/Bxe4! exchanged safely, but ...f5/...e4 drove Nf3 away and ...Ne5-d3-f4 invaded. A proposed f3 break must calculate ...Nf4 and checking forks. No verified opening replacement.
- Ruy ...Bg4/Qe2/Nc6: Nf3 pinned to Qe2. h3?! Nd4 hits Qe2/Bb3/Nf3. Qe3 Bxf3: Qxf3 loses Q to Nd4. ...c4 Bc2? Nxc2 forks Qe3/Ra1/Re1. No verified replacements.
- Ruy ...Ba7/Bg4 Bxf3 Qxf3/exd4: e5?! Nxe5 gains tempo; d6 guards Ne5. cxd4?! Ba7xd4 through b6/c5. ...Bc5/O-O/d5: exd5 Nxd5 Nxe5 Bxf2+ Kxf2! Nxe5; Bxd5?? Nd3+. Rxe5 needs ...Qf6+ calculation.

## Black openings
- Four Knights castled: 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3! dxc6 restores equal material. ...Qd4/Bg4/Bd6/Qf6, Qg5 Qxg5 Bxg5! reached a near-equal queenless middlegame in T30/T31. Later exchange losses do not refute the opening.
- T31 Final continuation: ...Rae8/Rfe1/h6/Bd2/Be6/Bxe6/Rxe6/Rxe6/fxe6! left R+B each, equal pawns, open f-file. ...Kf7/Ke7/Rf7/g5/Rf5 reached move 25 without marked errors; ...Rf4?? then lost the exchange. No verified move-25 replacement.
- T30 Final: ...Rg8 Bxh6 Rh8 Bxg7 Rg8? Bxe5 Rxg4 left equal R/B counts but a worse position, two pawns down. A reciprocal rook capture does not establish adequate defense; evaluate pawn losses, rook safety and king exposure AFTER the exchange. No verified replacement.
- Classical Caro: ...h6/Bh7/Nd7/Bxd3/e6/Ngf6/Be7/O-O. Against O-O/c4/Rfe1, ...c5? d5! was adverse; gifts do not certify it. Long-castling ...Nxe5/dxe5/Nd5 also lacked validation.
- Ruy d3 T30 Sonnet: ...Re8/Bb7/Bf8/d5 exd5 Nxd5/Ne4 f5/Ng3 Qd7/g6. Be3? Nxe3?! fxe3: Qxe3 f4 would fork Q/Ng3, but the knight exchange was inaccurate; no verified replacement. Move Q off Rd1's file BEFORE ...e4 dxe4. ...Qe7/e4/fxe4 induced a piece gift, not a forced opening win.
- SF Ruy 6.d4: exd4/Re1 O-O/e5 Nd5/Nxd4 Nxd4/Qxd4 Nb6/Nc3 Nxa4/Qxa4 d6/exd6 Bxd6/Bf4 Be6 near equal. Rad1 Qf6/Bxd6 cxd6!; Qe7 lost d6.
- Chigorin ...Qb6?? dxe5 uncovers Be3-b6. Open Ruy ...Ne6?! Qxd8 Rxd8 Bxb5 lost P. Berlin queens-on ...Be7?! Rd1: solve the open d-file before development.
- Advance Caro: ...f6? Nf4!/...Qd6?? exd6 repeatedly loses Q. Earlier ...f6 BEFORE cxd4 worked with c3 screening Qb3-d3 and Nd2 blocking Rd1-d3; it validates neither later exchanges nor queenless ...f6/Rxf6/Ne5.
- QGD: recount central guards after exchanges. Qe2 displaced Qd1; ...Bxf3 Qxf3 removed Nf3, allowing ...Nxd4 with tempo. Nc3 does NOT attack d4. ...Bg4/Bh5 were inaccurate. T29: Ne5?? Rac8? missed punishment; Nd7?? Nxd7 won N. No verified move-15 replacement.
- T31 QGD Bf4: ...c5/Nc6/cxd4 exd4/dxc4 Bxc4/b6/Qd3 Bb7/Rfe1 Rc8/Rad1 Nb4. Nb4 attacked Qd3 and cleared BOTH Rc8-c4 and Bb7-f3. Qe2 Bxf3 Qxf3?? Rxc4 won B: Nf3 was removed AND Qe2 left its c4 diagonal. gxf3 retains Qe2's guard; the queen recapture enabled the win. ...Rc8/a3 Nbd5/Nxd5 Nxd5 kept a blockade. Bd6 Bxd6 won another B because d4 blocked Rd1-d6.

## Note files
- notes/accelerated-dragon.md - Pawn storms, discovered attacks and queen safety after checks.
- notes/berlin-endgame.md - D-file and clearance.
- notes/caro-kann-advance.md - Breaks and queenless mate.
- notes/deepseek.md - Classical Caro, d-file tactics and conversion.
- notes/four-knights.md - Exchange offers, bishop defenses and promotion screens.
- notes/qgd-exchange.md - Central guards, c-file clearance and mating lines.
- notes/ruy-lopez.md - A-file guards, bishop screens and passer blockades.
- notes/sicilian-maroczy.md - Maroczy exchanges, king screens and passers.
