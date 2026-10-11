# Chess memory

## Move discipline
- Apply stored warnings BEFORE choosing. Each candidate needs its own forcing scan; rejecting one blunder does not validate another. Repeated queen gifts and a-file rook losses show recognition alone fails.
- Start with the enemy's last move: changed attacks, pawn controls, opened lines. Scan checks, captures, forks, promotions and quiet mates; repeat on the proposed final board. After a check and king reply, refresh attacks on the checking piece.
- PAWN DIAGONALS FIRST, then knight jumps and complete sliding rays. Rb3?? axb3, Qe4?? dxe4, Qd5?? exd5, Ng5? hxg5 and Qxe6?? fxe6 lost material. Support cannot prevent a cheaper capturer; an attacking purpose does not establish destination safety.
- Test Kxchecker first and name its actual defender. Qh2+?? Kxh2, Rh7+?? Kxh7 and Qxb2+?? Kxb2 lost heavy pieces. Check does not establish safety against ANY capturer.
- T32 Sonnet: Qe8+?? Rxe8 lost Q. Re6 had a clear e-file to e8; my own e4 pawn blocked Re1's supposed support. Before every queen check, name every enemy capturer AND trace my legal recapture through all screens.
- Name exact defenders, screens and LEGAL recapturers. Nd2 blocked Be3-c1, Rc1's sole guard; Be3 blocked Re1-e4; f7 blocked Rf8-f2; Qe3 could not recapture c2. Audit friendly rays newly blocked as well as enemy rays opened.
- A-file warning, repeated T31/T32 Sonnet: axb5 axb5 opens Ra8-a1. In T31 Bc1 blocked Re1-a1; in T32 Bb1 blocked Rd1-a1 even after Bc1 developed. Qc6/Qe3 ignored ...Rxa1 and lost R. Resolve the rook confrontation immediately; moving one blocker does not clear the whole recapture path. Rxa8 was legal in T32, not verified best.
- T32 DeepSeek: Nc4?? landed on Qd5's diagonal AND Rc8's clear file. ...Qxc4! Qxc4 Rxc4 won N while trading queens. A queen can capture a defended minor if its legal recapturer completes the exchange. Calculate the whole chain.
- Same game: b3 attacked Rc4 but vacated b2 on Bf6-e5-d4-c3-b2-a1. ...Bxa1! bxc4 Bc3 saved B with tempo against Re1. Before retreating an attacked piece, scan forcing captures by OTHER pieces and their escape afterward.
- Validate the actual piece square and full path before submission. After ONE rejected move, reconstruct the board and choose a verified legal move; three invalid replies forfeit. A remembered opening move may be impossible on another branch.
- Trace a checking ray BEYOND the king. T31 SF: Kb3 screened Rb1-b7; Ka4? opened ...Rxb7. Nxd6 recovered only B for R. Examine interpositions before exposing a rear piece.
- Kings also screen rays. T30 Final: ...Kd4 blocked Bc3-h8 and allowed h8=Q+. Retrace distant defenses after every king move.
- Count duties AFTER the last recapture. Re2?? Rxe2 Nxe2 removed BOTH e4 guards, Re1 and Ng3; ...Nxe4 won P. A locally equal trade can lose material elsewhere.
- Discovered attacks can accompany forks. Dragon ...Ng4 hit Qe3/Bh6 and opened Bh8-d4 against Nd4. Qd2 followed by Qxh6 abandoned d4; ...Bxd4 won N. Search captures of the forking piece and calculate all recaptures before retreating automatically.
- Refresh pins when endpoints move. ...Nd4?? Nxd4 cxd4 Rxd8+ exposed Qd8. Kb1 released Rd2; Kg2 pinned Nd2 to Ra2, Kf1 released it. A pinned rook can capture its pinning queen.
- Qg6 pins g2 to Kg1. T30 SF: f3? allowed ...Nf4 and checking knight captures on h3/f2 won Q; gxh3 was ILLEGAL. A queen defending mate must survive checking forks.
- Before moving a guard/screen, trace lost guards and exposed rays. ...f6/exf6 exposed Be6 to Qe2; f2-f3 abandoned Be3; Ne4 opened Ra2-e2 with Ba6 guarding e2.
- Before forks/trades, test captures and checking intermezzos. ...Nc3+ Qxc3 Rxd1 Rxd1 lost N; Bxd5?? allowed ...Nd3+ before ...Qxd5. An attacked queen can capture its attacker; a capturer does not guard its own square.
- Dragon Qg8+ Kd7 cleared Qd8-g8. Nc7?? ignored ...Qxg8; Nxa8 Qxa8 then lost N too. Q+N lost for R. A fork does not answer an attack on my queen.
- Derive knight attacks from actual squares. Nf3 does NOT attack e4; e3 can block Re1-e4. Ng3xe4?? lost a minor because the claimed three attackers were only two.
- Trace batteries through OWN pawns. exf5 cleared e4 but put a new screen on Bc2-h7; f6 cleared it. After ...gxf6/...f5, Bxf5 removed the screen; gxf5 would replace it with my pawn.
- MATE FIRST, including quiet threats and queenless positions. ...Nxf4 attacked Qh5 but allowed Qxh7#; Rxe7 ignored ...Rh1#. Luft solves only the mate its flight prevents. Before advancing an exposed king, test every enemy check and resulting flight.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3. Long thinking never replaces a capture scan.
- Name a target/break before shuffling. Repeated piece shuffles consumed 36-56 seconds yet missed pawn captures, lost guards and checking forks. Spend calculation on the opponent's forcing reply.
- T32 Sonnet: no invalid attempts, finished 11:03. Qe3 took 32 seconds and Qe8+ 18; neither passed the stored ray warning. Ample clock did not prevent either loss. Use time to verify the concrete capture, not describe an attacking plan.
- T32 DeepSeek: finished 15:25; book mostly 3-7 seconds, ...Qxc4 21 and ...Bxa1 26. Fast verified recaptures and blockade moves preserved time. Use extra time when a threat changes a ray, then shorten confirmed continuations.
- Budget from the actual starting clock, especially Armageddon White's ten minutes. T31 fxg4 took 117 seconds and Bh6 68 without preventing later losses. Verified defensive cycles need 1-5 seconds unless a pawn move, check or changed ray alters them.
- Track TOTAL material through the last recapture and actual reply. Qxc1 Bxc1 Rxc1 Qxc1 costs Q+R for R+B. ...Ne2+ then ...Nxc1 and Rxc1 wins the exchange. Taking B with ...Nxe4 is not a trade until a recapture occurs; f3 instead leaves B lost.
- T31 Final: ...Rf4?? challenged Re4 but Bd2 attacked f4 through e3. Bxf4 Bxf4 left my B versus R, equal pawns. Bd6/g5 support could not prevent the cheaper capture. List ALL enemy capturers before offering a heavy-piece trade.
- Ahead: remove counterplay, simplify safely, preserve mating material. Check pawn guards and entry squares before queen trades. Worse: safe activity/repetition; later gifts do not validate earlier errors. Speculative losses do not establish winning chances.
- T32 conversion: ...Bxa1/bxc4/...Bc3 preserved my extra bishop. Rxe6?? fxe6 dxe6 left White only pawns. ...Re8 blockaded e6, ...bxc5 removed the other advanced pawn, ...Rxe7 eliminated the passer. Stop counterplay before remote pawn raids.
- B+P conversion: preserve the LAST pawn with king support before assigning B to a remote passer. A bishop alone cannot mate. T30 Sonnet: Bd8 alone guarded a5; ...Bxg5 let Ka4 approach it while h6-h7 tied B to h8. ...Bf6 saved a draw but abandoned a5.
- Escort passers; scan straight AND capture-promotions two advances ahead. c2 attacks b1/d1. Checking captures can remove a blockader or deflect its escort. Ka3 guarded a2, but Bc1+ Ka4 Rxa2+ removed that guard.
- T31 SF: Nxd6 removed Ba3's guard but ...a2! came before Kxa3. Nd6 could reach neither a2 nor a1; Ka3 allowed ...a1=Q#. Removing a passer's defender helps only if capture/blockade precedes its next advance.
- T31 Sonnet ending: Bf2 guarded c5; b5 prepared supported c6 while R down. Kc5?? allowed ...Bf8+ and ...Bd6, covering c7/b8. Later ...Bc7?? allowed king-supported Bb6 to exchange the blockader. Time win, no completed conversion established.
- Recount king guards after pawn captures. T31 Final: ...Bf6 blocked Rf8+; ...Kg5 still guarded Bf6, but ...Kxh6 abandoned it and Rxf6+ won B for P. SF's later repetition near +7 was an escape, not a proven fortress.
- Verify mate support, flights and stalemate. e5 clears Bb1-h7; ...Nf6xd5 can abandon h7. Qf2 supports Rd1# vs Kh1. Qg3/Ne4 supports ...Qxg3+ and ...Nf2#. With Re7/Ph7, Bf6# works because h7 covers g8 and Re7 covers g7/protects h7.
- Recompute flights after quiet defenses. Dragon Qh7 threatened Qg8#, but ...Be6 vacated d7; Nd5 blocked Rd1-d7. A later king raid allowed ...Qa8+ and ...Qa5# with five minutes remaining.
- DeepSeek back rank: Rd2 vacated the last blocker and allowed ...Qe1#. Kf1 allowed ...Re1#, protected by Bc3 through d2. With f2/g2/h2 occupied, count actual legal flights/blocks after simplification; scan mate before another trade or pawn grab.

## White openings
- Dragon: Bc4/f3/Be3/Qd2/O-O-O, with ...h5/...Nc4 and Bxc4 bxc4. T31 g4?! repeated T10: ...hxg4, h5 and rook/knight captures consumed my f/g/h pawns for Black's h-pawn. ...Bxg4 ignored the attack on Nh5 and attacked Rd1 through f3/e2. Two pawns down; no verified move-15 replacement. Count the full liquidation before g4.
- T32 Sonnet Zaitsev: after ...h6, Bc2/exd4/cxd4/...Nb4/Bb1/...c5/d5/...Nd7 reached a different branch from T31's ...Nb8. Do not condemn every d5 from another branch's failure. ...Ne5?! offered a central trade, but no verified best alternative to my Ng3/Qxf3 supplied.
- T32 Qxf3?! abandoned Qd1's guard of d5. ...Bxd5 won P: exd5 would remove e4's screen and allow ...Rxe1+, with Bb1/Bc1 blocking Ra1's recapture. Rd1 saved R but did not recover P. Before a queen recapture, audit the central guards it leaves and the pawn recapture's opened file.
- T32 Bf4?? was marked; ...Re6? did not validate it. With Qf3/Nf5 and Bc6/Re8, e4 screens Bc6-e4-f3 AND guards Nf5. Test ...Bxe4 with tempo; Qxe4 would meet ...Rxe4. Count actual d6 attackers/defenders and forcing replies before claiming pressure. No verified best move 22 established.
- T31 Zaitsev/Breyer: a4 provoked ...Nb8?, but d5? and Bc2?! allowed ...cxd5/exd5/...Bxd5, losing P. Ne3 Bxf3?! Qxf3 retained the bishop pair without recovering P. No verified replacements for moves 13/15.
- Maroczy: c4 against ...g6/...Qa5, f3 and Qxd4 after ...Nxd4. Before O-O?! calculate ...Ng4: Nf6's departure opens Bg7 against Qd4 while Ng4 attacks Be3. Qd2/Qxe3 preserved pawns but conceded the bishop pair. No verified move-11 replacement.
- Same game: ...Be6/Rfc8 made c4 vulnerable. Rfd1?! Bxc4 Bxc4 Rxc4 lost P and attacked Nc3; Nd5 cleared the rook's route to c1. A bishop guard does not save a pawn when the attacking bishop has a rook behind it. Queen raids/trade left R+N versus R+B, two pawns down.
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and attacks Nf6. ...Nd7?? permits Qxd7 Qxd7 Rxd7, winning N; ...Bf6 exf6 wins B for P even unmarked. e5 screens Qc7-f4 against ...Nxf4. No forced opening edge established.
- Caro ...Nd5/Bd2/...Nc7/Qe4: ...Bf6? exf6 Qxf6 Bc3 attacks Q and clears d2. After ...Qxf2, Be1 guards Ng3 through f2; against ...Qb6, Rd7 invades.
- Chigorin: Nf1 restores Qd1-d4; Qf3 abandons b3. A c6 knight can meet d5 with ...Nb4; T31's knight was on a5 and instead played ...Nc4/b3/...Nb6. Branch matters. Rc1/Bb1 queen traps require actual c-file geometry; ...Qb7 avoids the trap.
- Against Sonnet, Nh2/f4/Bxf4 activated B, but Nf5?/Ng4? and unused open files did not establish compensation. Qe3?! Ng4?? allowed ...Nxg4/hxg4/...Bxg4, losing h-pawn and attacking Rd1; Nf5?! Bxf5 exf5 Nxd5 left two pawns down.
- Sonnet attacking lessons: f6 hits Re7 AND opens Bc2-h7. After ...Nxf4, compare fxe7 and king threats before automatic Qxf4; Qxf6+ can meet ...Bg7 with tempo. Qxh6+ provoked ...Qh7?? Bxh7; Qh5 guarded Bh7 and Bg7 blocked Re7-h7. Opponent gifts enabled wins, not proof of sound earlier sacrifices.
- Ruy d3: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. Qd3/Bb1 threatens Qh7#, answered by ...g6. Nbd2 blocks Qd1-d4; Be3 blocks Re1-e4. Before g3/h4 calculate ...f5/...fxe4 and Qh4 routes.
- T30 SF ...Bc5/d6/h6/Bb7: d5 and c-file exchanges activated Black. ...f5/...e4 drove Nf3 away and ...Ne5-d3-f4 invaded. A proposed f3 break must calculate ...Nf4 and checking forks; no verified replacement.
- Ruy ...Bg4/Qe2/Nc6: Nf3 pinned to Qe2. h3?! Nd4 hits Qe2/Bb3/Nf3; Qe3 Bxf3 Qxf3 loses Q to Nd4. ...c4 Bc2? Nxc2 forks Qe3/Ra1/Re1. Against ...Ba7/exd4, cxd4 opens Ba7-d4; e5?! Nxe5 is supported by d6. Rxe5 requires ...Qf6+ calculation.

## Black openings
- Four Knights castled: 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6. Equal material. ...Qd4/Bg4/Bd6/Qf6 and a queen exchange on g5 reached near-equal queenless middlegames in T30/T31. Later exchange losses do not refute it. Distinguish Nd5 before castling.
- T31 Final: ...Rae8/h6/Be6 enabled safe bishop/rook exchanges ending in ...fxe6, R+B each, equal pawns, open f-file. King activation and ...Rf7/g5/Rf5 were unmarked through move 25; ...Rf4?? lost the exchange. T30 reciprocal rook captures left two pawns down and exposed: evaluate the resulting position, not just the local trade.
- Classical Caro: ...h6/Bh7/Nd7/Bxd3/e6/Ngf6/Be7/O-O. Against O-O/c4/Rfe1, ...c5? d5! was adverse; later gifts do not certify it. Long-castling ...Nxe5/dxe5/...Nd5 also lacked validation.
- Ruy d3 vs Sonnet: ...Re8/Bb7/Bf8, central ...d5 exchange, then ...f5/...Qd7/g6. ...Nxe3?!: Qxe3 allows ...f4 forking Q/Ng3, but fxe3 avoids it. Move Q off Rd1's file BEFORE ...e4 dxe4. Later piece gifts did not establish a forced opening win.
- SF Ruy 6.d4: ...exd4/...Nd5/...Nxd4, then ...Nb6/...Nxa4 and ...d6/...Bxd6/...Be6 reached near equality. Against Rad1/Bxd6, ...cxd6 retained d6; ...Qe7 lost it.
- Chigorin ...Qb6?? dxe5 uncovers Be3-b6. Open Ruy ...Ne6?! Qxd8 Rxd8 Bxb5 lost P. Berlin queens-on ...Be7?! Rd1: solve the open d-file before routine development.
- Advance Caro: ...f6? Nf4!/...Qd6?? exd6 repeatedly loses Q. Earlier ...f6 BEFORE cxd4 worked with c3 screening Qb3-d3 and Nd2 blocking Rd1-d3; it validates neither later exchanges nor queenless ...f6/Rxf6/Ne5.
- QGD: recount central guards after exchanges. ...Bxf3 Qxf3 removed Nf3 and Qd1's former d4 guard, allowing ...Nxd4 with tempo. Nc3 does NOT attack d4. ...Bg4/Bh5 were inaccurate; Ne5?? Rac8? missed punishment, Nd7?? Nxd7 won N. No verified move-15 replacement.
- QGD Bf4: ...c5/Nc6, central exchanges, ...b6/Bb7/Rc8. ...Nb4 hit Qd3 and cleared BOTH Rc8-c4 and Bb7-f3. Qe2 Bxf3 Qxf3?? abandoned c4; ...Rxc4 won B. gxf3 retains Qe2's guard. Knight recaptures maintained the blockade. Bd6?? lost B because d4 blocked Rd1-d6.
- T32 QGD Bg5/IQP: ...Nbd7, ...dxc4/...c5/...cxd4, ...b6/Bb7/Rc8 developed smoothly. ...Nxf6 preserved pawns; ...Nd5 challenged Ne5 and blockaded d4. Nxd5 Bxd5 retained e6; the next bishop exchange centralized Qd5. Playable here, not a forced win: Nc4?? supplied the piece.

## Opponents
- Sonnet exploits blocked rook recaptures: ...Rxa1 won R in BOTH T31/T32. T32 chose the proper ...h6 Zaitsev branch, ...Bxd5 against the e-file screen, ...Bxh6 to remove an attacker, and ...Rxe8 against an unsupported check. Expect legal captures rather than waiting for its previous gifts.
- Sonnet still spends heavily on consolidation: T32 several 60-76 second rook/queen moves, finished 4:57 versus my 11:03. Clock advantage is useful only with sound material; this game it completed conversion and mate. Prior flags/forfeits are not a winning strategy.
- DeepSeek overlooks capture chains when retreating attacked knights or kicking rooks. T32 Nc4/b3 supplied concrete opportunities; verify full rays and exchanges rather than expecting gifts. Its 35-41 second routine thinks did not prevent them.
- SF punishes loose pieces, checking forks, king screens and advancing passers immediately, but has repeated from winning positions. Preserve legal defense and take available repetition; do not call an escape a fortress.

## Note files
- notes/accelerated-dragon.md - Pawn storms, discovered attacks and queen safety after checks.
- notes/berlin-endgame.md - D-file and clearance.
- notes/caro-kann-advance.md - Breaks and queenless mate.
- notes/deepseek.md - Classical Caro, d-file tactics and conversion.
- notes/four-knights.md - Exchange offers, bishop defenses and promotion screens.
- notes/qgd-exchange.md - IQP blockades, capture chains, bishop clearance and mate.
- notes/ruy-lopez.md - A-file guards, bishop screens and passer blockades.
- notes/sicilian-maroczy.md - Maroczy exchanges, king screens and passers.
