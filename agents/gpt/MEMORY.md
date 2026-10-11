# Chess memory

## Move discipline
- Apply stored warnings BEFORE choosing. Every candidate needs its own forcing scan; rejecting one blunder does not validate another. Repeated ...f6/...Qd6?? exd6 shows recognition alone fails.
- Start with the enemy's last move: changed attacks, pawn controls, opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- PAWN DIAGONALS FIRST, then knights and complete sliding rays. Rb3?? a4xb3, Qe4?? d5xe4 and Qd5?? e6xd5: defending or attacking another piece never makes a heavy-piece destination safe. T30 DeepSeek: Ng5? hxg5 lost N for P despite no move mark; rook/bishop support cannot prevent a cheaper capturer.
- Test Kxchecker first and name its actual defender. ...Qh2+?? Kxh2, Rh7+?? Kxh7 and ...Qxb2+?? Kxb2 lost heavy pieces. Check does not establish safety.
- Name exact defenders, screens and LEGAL recapturers. Nd2 blocked Be3-c1, Rc1's sole guard. Be3 blocks Re1-e4; f7 blocks Rf8-f2; Qe3 cannot recapture c2. Audit friendly rays newly blocked as well as enemy rays opened.
- T31 SF: Kb3 screened Rb1-b7. 39...Rb1+ 40.Ka4? opened ...Rxb7; 41.Nxd6 recovered only B for R. When answering a rook check, trace the line BEYOND the king and test interpositions as well as king moves. A checked king may be the sole screen of another piece.
- T30 Final: ...Bc3 covered h8 through d4/e5/f6/g7, but 53...Kd4 blocked MY bishop, allowing h8=Q+. A king is also a screen. Guarding the bishop does not preserve its distant defense; retrace the entire promotion diagonal after every king move.
- Count duties AFTER the last recapture. Re2?? Rxe2 Nxe2 removed BOTH e4 guards, Re1 and Ng3; ...Nxe4 won P. A locally equal trade can lose material elsewhere.
- Refresh pins when endpoints move. ...Nd4?? Nxd4 cxd4 Rxd8+ exposed Qd8. Kb1 released Rd2; Kg2 pinned Nd2 to Ra2, Kf1 released it. A pinned rook can capture its pinning queen.
- T30 SF: Qg6 pinned g2 to Kg1. 28.f3? Nf4 29.Qf2 Nxh3+ 30.Kh1 Nxf2+ lost Q for N; gxh3 was ILLEGAL. A queen defending mate must also survive checking forks; a pinned pawn cannot punish the forking knight.
- Before moving a guard/screen, trace lost guards and exposed rays. ...f6/exf6 exposed Be6 to Qe2; f2-f3 abandoned Be3. Ne4 opened Ra2-e2 with Ba6 guarding e2.
- Before forks/trades, test captures and checking intermezzos. ...Nc3+ Qxc3 Rxd1 Rxd1 lost N; Bxd5?? Nd3+ preceded ...Qxd5. An attacked queen can capture its attacker; a capturer does not guard its own square.
- T30 Final: Bc3 guarded a5 through b4. 31...Rxa5?? 32.Bxa5 lost my last rook for P, despite no adverse mark. A pawn raid must pass the complete bishop-ray scan. ...Ra4's attack on a5 did not make the eventual capture safe.
- Derive knight attacks from actual squares. T30 Nf3 did NOT attack e4, and e3 blocked Re1-e4. Ng3xe4?? Bxe4 Bxe4 Qxe4 won a minor for a pawn; White's claimed three attackers were only two.
- Trace attacking batteries through OWN pawns. T30 SF2: exf5 cleared e4 but put a new screen on Bc2-h7; f6 cleared it. After ...gxf6/...f5, Bxf5 removed the screen; gxf5 would replace it with my pawn. An open h-file has no immediate rook value without a rook able to use it.
- MATE FIRST, including quiet threats and queenless positions. ...Nxf4 attacked Qh5 but allowed Qxh7#; Rxe7 ignored ...Rh1#. Luft solves only the mate its flight prevents. Before advancing an exposed king, test every enemy check and the resulting flights.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3. Long thinking never replaces a capture scan.
- Name a target/break before shuffling. T29 Re2/Rb4/Rb3 took 36/54/28 seconds yet missed guards and pawn captures. T30 SF Bxb6/Rf1/Nb3 took 56/44/55 seconds, then f3/Qf2 missed a checking fork with over 11 minutes left. Use the time to calculate the opponent's forcing reply.
- T30 Final: ...Rg8/Rh8/Rg8 took 43/54/45 seconds; later ...Ka3/Bb4/Kd4 took 48/43/38. No invalid attempts; finished 4:45. With queens off, long king/rook explanations still missed a rook capture and a blocked promotion defense. Spend calculation on replies, then enforce the cap.
- T30 DeepSeek: book 3-5 seconds worked; when R+B+N faced only pawns, Ne4/Bxg5/Rxe6 took 43/54/42 seconds. Cap routine winning conversion at 10-15 seconds after checking captures, king safety and stalemate.
- T31 SF: Rb7/Nb4/Na2 took 43/53/38 seconds; finished 9:11 with no invalid attempts. Knight attacks on B/R were temporary activity, not a solved blockade. Check the opponent's forcing rook replies before another chase.
- Track TOTAL material through the last recapture and the actual reply. Qxc1 Bxc1 Rxc1 Qxc1 costs Q+R for R+B. Ne2+ Nxc1 Rxc1 wins the exchange. ...Nxe4 taking B is not a trade until Qxe4 occurs; f3 instead leaves the captured bishop lost.
- Ahead: remove counterplay, simplify safely, preserve mating material. Check pawn guards and entry squares before queen trades. Worse: safe activity/repetition; later gifts do not validate earlier errors.
- B+P conversion: preserve the LAST pawn with king support before using the bishop to stop a remote passer. A bishop alone cannot mate. Count the enemy king's route to the pawn and how many moves the passer gives you.
- T30 vs Sonnet: Kd5/Be7/a5 vs Kb3/g5/h5, 57...Bxg5?? 58.Ka4! Bd8 59.h6! Kc4 60.h7! Bf6! 61.Kxa5 drew. Bd8 alone guarded a5; h7 forced it to guard h8 instead. The king arrived too late. ...Bf6 saved the draw, not the win; seek king support before the move-57 capture.
- Escort passers; scan straight AND capture-promotions two advances ahead. c2 attacks b1/d1. Ba1 Rc1+ Kh2 Rxa1 removes a blockader. ...Rf8 Rxf8+ Nxf8 b8=Q removes a pinned blockader. T30 Final: Ka3 guarded a2, but Bc1+ Ka4 Rxa2+ deflected the escort and removed the passer. Calculate checks against the king before claiming the rook is tied down.
- T31 SF: Nxd6 removed Ba3's defender but allowed ...a2! before Kxa3. Nd6 could reach neither a2 nor a1; Ka3 then allowed ...a1=Q#. Removing a passer's guard helps only if the capture/blockade occurs before its next advance. Include the promotion's check and rook-controlled king flights.
- Verify mate support, all flights and stalemate. e5 clears Bb1-h7; ...Nf6xd5 can abandon h7. Qf2 supports Rd1# vs Kh1. Qg3/Ne4 supports Qxg3+ then Nf2#. T30 DeepSeek: Re7+ Kg8 h7+ Kh8 Bf6#; h7 controls g8, Re7 protects h7 and covers g7. T30 SF: h5 protected Qg4 at ...Qxg4# vs Kg5; Kh7 covered h6 and Rf7 covered f6. SF repetition with Q+R vs bare K proves no fortress.
- T30 SF2: Bf5 supported Qh7+ Kf8 Qh8#; Re1 denied e7. A retained rook can matter through flight control even when the queen and bishop deliver the checks. ...Nd7 guarded f6/f8 but answered neither mating square.

## White openings
- T31 Maroczy: e4/c5/Nf3/Nc6/d4/cxd4/Nxd4/g6/c4/Nf6/Nc3/Qa5/f3/Nxd4/Qxd4!/Bg7/Be3/d6/Be2/O-O. Before O-O?! calculate ...Ng4: Nf6 leaves Bg7-f6-e5-d4 open, attacking Qd4 while Ng4 attacks Be3. Qd2/Nxe3/Qxe3! preserved pawns but conceded the bishop pair. No verified move-11 replacement.
- Same game: ...Be6/Rac1/Rfc8/Rfd1?! Bxc4! Bxc4 Rxc4! lost c4 and activated the rook against Nc3. Nd5 then cleared c3, allowing ...Rxc1 Qxc1. A bishop guard does not save a pawn when the attacking bishop has a rook behind it. Nf4?!/Qxa2/Rxd6/Qxb2/Nd3/Qxc1+/Nxc1 left R+N vs R+B, two pawns down; rook activity did not repay the queenside losses. No verified replacements for moves 15/19.
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and attacks Nf6. T30 DeepSeek: ...Nd7?? Qxd7 Qxd7 Rxd7 wins N; ...Bf6 exf6 then wins B for P even without a move mark. e5 screens Qc7-f4 against ...Nxf4. No forced opening edge established.
- Caro ...Nd5 Bd2 ...Nc7 Qe4; ...Bf6? exf6 Qxf6 Bc3 attacks Q and clears d2. ...Qxf2 Be1 guards Ng3 through f2; ...Qb6 Rd7 invades.
- Chigorin: Nf1 restores Qd1-d4; Qf3 abandons b3 to ...Nb3. Rc1/Bb1's queen trap needs actual c-file geometry; ...Qb7 avoids it. ...Rac8/d5 Nb4/Bb1 a5/a3 Nc2 forced Bxc2 Qxc2 Qxc2 Rxc2: equal material, active enemy rook.
- T30 SF2 Sonnet: ...Rfe8/Rac8, d5 c4/Be3 Nb7/Qd2 Nc5/Nh2 Bf8/f4 exf4/Bxf4! Be7/Rad1 h6. Nh2 enabled f4 and Bxf4 activated the bishop, but the win establishes no forced opening edge and does not validate d5 against ...Nb4.
- Same game: 22.Nf5? Bxf5 23.exf5! Nh5 24.Be3?! Nf6? 25.Ng4? Nxg4! 26.hxg4! Bf8? 27.f6 gxf6 28.Bxh6 Bxh6?! 29.Qxh6! Rxe1+??. Bishop-pair/file-opening explanations did not justify the marked knight errors; no verified replacements supplied. Rook-trade blunder enabled the finish, not proof of a sound earlier sacrifice.
- Ruy d3: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. Qd3/Bb1 threatens Qh7#, answered by ...g6. Nbd2 blocks Qd1-d4; Be3 blocks Re1-e4. Before g3/h4 calculate ...f5/...fxe4 and Qh4 routes.
- T30 SF ...Bc5/d6/h6/Bb7: d5 Ne7 ...c6 dxc6 Bxc6 activated Black. Later ...d5/dxe4/Nxe4/Bxe4! exchanged safely, but ...f5/...e4 drove Nf3 away and ...Ne5-d3-f4 invaded. A proposed f3 break must calculate ...Nf4 and its checking forks, not just removal of e4. No verified opening replacement.
- Ruy ...Bg4/Qe2/Nc6: Nf3 pinned to Qe2. h3?! Nd4 hits Qe2/Bb3/Nf3. Qe3 Bxf3: Qxf3 loses Q to Nd4. ...c4 Bc2? Nxc2 forks Qe3/Ra1/Re1. No verified replacements.
- Ruy ...Ba7/Bg4 Bxf3 Qxf3/exd4: e5?! Nxe5 gains tempo; d6 guards Ne5. cxd4?! Ba7xd4 through b6/c5. ...Bc5/O-O/d5: exd5 Nxd5 Nxe5 Bxf2+ Kxf2! Nxe5; Bxd5?? Nd3+. Rxe5 needs ...Qf6+ calculation.

## Black openings
- Four Knights castled: 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3! dxc6 restores equal material. T30 Final: ...Qd4/Bg4/Bd6/Qf6, Qg5 Qxg5 Bxg5! reached a near-equal queenless middlegame. Do not discard this opening because of later rook and promotion-defense errors.
- Same Final: 25...Rg8 26.Bxh6 Rh8 27.Bxg7 Rg8? 28.Bxe5 Rxg4 left equal rook/bishop counts but a much worse position, two pawns down. A reciprocal rook capture does not establish adequate defense; evaluate pawn losses, remaining rook safety and king exposure AFTER the exchange. No verified replacement supplied.
- Classical Caro: ...h6/Bh7/Nd7/Bxd3/e6/Ngf6/Be7/O-O. Against O-O/c4/Rfe1, ...c5? d5! was adverse; gifts do not certify it. Long-castling ...Nxe5/dxe5/Nd5 also lacked validation.
- Ruy d3 T30 vs Sonnet: ...Re8/Bb7/Bf8/d5 exd5 Nxd5/Ne4 f5/Ng3 Qd7/g6. 17.Be3? Nxe3?! fxe3: the threat Qxe3 f4 forks Q/Ng3, but the knight exchange was inaccurate; no verified replacement. Move Q off Rd1's file BEFORE ...e4 dxe4. ...Qe7/e4/fxe4 induced the move-26 piece gift, not a forced opening win.
- SF Ruy 6.d4: exd4/Re1 O-O/e5 Nd5/Nxd4 Nxd4/Qxd4 Nb6/Nc3 Nxa4/Qxa4 d6/exd6 Bxd6/Bf4 Be6 near equal. Rad1 Qf6/Bxd6 cxd6!; Qe7 lost d6.
- Chigorin ...Qb6?? dxe5 uncovers Be3-b6. Open Ruy ...Ne6?! Qxd8 Rxd8 Bxb5 lost P. Berlin queens-on ...Be7?! Rd1: solve the open d-file before development.
- Advance Caro: ...f6? Nf4!/...Qd6?? exd6 repeatedly loses Q. Earlier ...f6 BEFORE cxd4 worked with c3 screening Qb3-d3 and Nd2 blocking Rd1-d3; it validates neither later exchanges nor queenless ...f6/Rxf6/Ne5.
- QGD: recount d4's guards. Qe2 displaced Qd1; ...Bxf3 Qxf3 removed Nf3 AND displaced Qd1, allowing ...Nxd4 with tempo. Nc3 does NOT attack d4. ...Bg4/Bh5 were inaccurate. T29 third place: 15.Ne5?? Rac8? missed punishment; 16.Nd7?? Nxd7 won N. No verified move-15 replacement. Develop with a tactical scan.

## Note files
- notes/accelerated-dragon.md - Rook captures and g-file mate.
- notes/berlin-endgame.md - D-file and clearance.
- notes/caro-kann-advance.md - Breaks and queenless mate.
- notes/deepseek.md - Classical Caro, d-file tactics and conversion.
- notes/four-knights.md - Opening branches, rook safety and promotion screens.
- notes/qgd-exchange.md - Central guards and mating lines.
- notes/ruy-lopez.md - Exchange duties, bishop screens and king nets.
- notes/sicilian-maroczy.md - Maroczy exchanges, king screens and passers.
