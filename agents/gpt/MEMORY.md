# Chess memory

## Move discipline
- Apply warnings BEFORE choosing. Every candidate needs its own forcing scan; rejecting one blunder does not validate another. Recognition without execution repeatedly loses material.
- Start with the enemy's last move: changed attacks, pawn controls, opened lines and abandoned guards. Scan checks, captures, forks, promotions and quiet mates; repeat on the proposed board and after every recapture.
- PAWN DIAGONALS FIRST, then EVERY knight and complete sliding rays. Support and tempo do not prevent a cheaper capture. Nb3 attacked Rc5 but c4xb3 won N; supported Bc4 still lost to b5xc4.
- Count LEGAL defenders through actual blockers, excluding the mover. Qa5 pinned Nc3 to Ke1, so Be3 did not defend e4. Nf3 does NOT attack e4; Nc3 does NOT attack d4.
- Audit OWN screens and abandoned guards, including the recapturer's departure. Nd2 blocks Qd1-d3; Be3 blocks Re1-e4; f7 blocks Rf8-f2. Ke7 can abandon Re6's king guard AND block Re8-e6.
- LAST GUARD: Nc3 screened Qa5-e1 and Rd1 guarded Re1. Nxd5 removed the screen; Bd3/Bxd3/Rxd3 moved Re1's last guard, allowing Qxe1+. Development did not cure the ray.
- PAWN BREAKS: place the enemy capture first. f4 exf4 forked Be3/Ng3 and opened Qd6-f4; Bxf4 Qxf4 lost B. f6/exf6 exposed Be6 to Qe2; f2-f3 abandoned Be3.
- For every check test Kxchecker and ALL other captures. Qh2+/Rh7+/Qxb2+ lost heavy pieces to kings. Qe8+ overlooked Re6-e8 and e4 blocking Re1's support. Name the actual defender.
- BACKWARD BISHOP CAPTURES: Bf4 reached c1 through empty e3/d2. After rook exchanges, Qc1+ was Bxc1. Trace every bishop in BOTH directions after blockers disappear.
- UNCASTLED DRAGON: h5 vacates h7, opening Rh8-h6. Bh6 Bxh6 attacks Qd2 through g5/f4/e3; Qxh6 loses Q to Rxh6. Verify the entire exchange BEFORE Bh6, including castling status.
- OPEN A-FILE: axb5 axb5 opens Ra8-a1. Bc1/Bb1 can block a rook recapture; queen retreats then lose Ra1. Resolve rook contact first. Ra1/Rf1 defend each other only with b1-e1 empty.
- Calculate through the LAST recapture and recount the WHOLE board. Nc4 Qxc4 Qxc4 Rxc4 lost N despite its queen guard. Equal trades preserve an earlier deficit; name the final recapturer.
- An attacked piece need not retreat. b3 attacked Rc4 but opened Bf6-a1: Bxa1 bxc4 Bc3 retained my extra B. Rdb1 attacked Bb2, but Bxa1 took R. Scan captures by OTHER pieces.
- Refresh pins when endpoints move. Nd4 Nxd4 cxd4 opens Rxd8+ against Qd8. Kb1 released Rd2; Kf1 released Nd2's pin to Ra2. A pinned rook can capture its pinning queen.
- Before forks/trades test captures and checking intermezzos. Nc3+ Qxc3 Rxd1 Rxd1 lost N; Bxd5 allowed Nd3+ before Qxd5. Nc7's fork did not answer Qd8's attack on my Qg8.
- Trace vacated rays to their far endpoints. e5 uncovered Bf3-a8. Nf5 blocked Bf4-d6; exf5 screens Bc2-h7, while f6 clears it. Rc7 can screen Bb6-d8 and permit Kxd8.
- Trace checking rays BEYOND the king. Kb3 screened Rb1-b7; Ka4 allowed Rxb7. Ke5 allowed Bc3+ skewering g7. A checking block must survive the next capture.
- MATE FIRST, including quiet moves and queenless positions. Nxf4 hit Qh5 but allowed Qxh7#; Rxe7 ignored Rh1#. exf6 can win a minor AND support Qxg7#. Luft solves only the mate its flight prevents.
- MATING SCREEN: Qg3/Bd4 with f6 clear made Ne5 responsible for blocking g7. Bxe5 removed the screen and retained g7 support. Nf6 still blocks this battery.
- LONG-CASTLED KING: central exchanges can empty the c-file around Kc1. Qxe1+ Rd1 ties R down; Rfc8+ then captures blockers. Ka1 behind b2 on Bg7's diagonal made bxa3 illegal: Qa3 Qxa3# defeated the nominal pawn guard.
- CHECKING PAWN FORK: Ke5/Bc5 faced d4+, hitting K AND B. Kd5 dxc5 Kxc5 recovered only P for B. Inspect the pawn's other diagonal and piece captures before replying with K.
- DISCOVERED CHECK BREAKS RECAPTURES: Bc3/Rd4 faced Ke5 and my Rg4/Rg8. Rxg4+ vacated d4, discovering bishop check; Rg8xg4 could not answer it. Inspect the enemy capturer's VACATED ray.
- CHASABLE SCREEN: T37 Qb3 aimed up the b-file, initially blocked by Bb4. c3 drove B away and exposed b7. A defended bishop destination does not solve the target behind its old square.
- COUNTERATTACK MUST SURVIVE CAPTURE: T37 SF Qxb7 Rb8 Qxb8+ lost R; c7 blocked Qd6-b8. T37 Astra Qc7 attacked Na5/d6; my Qb6?? defended both and attacked Qc7 but Qxb6 won Q outright. Neither knight guarded b6. Before a queen/rook tempo name the legal recapturer after Qxpiece; attacking their queen does not force retreat. No verified move-34 replacement supplied.
- A PAWN BLOCKING A ROOK IS NOT NECESSARILY PINNED. T37 Rg1/g3 faced my Rg6; Kh2 was off the g-file. Qxh4+ allowed gxh4. Trace the ray to the KING before excluding a pawn capture.
- MY MATE THREAT DOES NOT STOP CHECKS. T37 Rg2/h2 looked dangerous against Kh1, but rook checks drove Kg3-f2-f1; Rb1# used Rc2 to seal rank 2. Map checks and flights before advancing into a rook cage.
- Validate destination and full path before submission. After ONE rejected move reconstruct the board and choose a verified legal move; three invalid replies forfeit. Recovery still needs a capture scan. Opening memories apply only to matching positions.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below five minutes cap 15; below 90 seconds use 1-3. Budget from the starting clock, especially Armageddon White's ten minutes.
- Name a target/break before shuffling and calculate its forcing reply. Spend critical time on changed guards, checking forks and races. Long thought is not evidence that the scan passed.
- Verified recaptures/cycles need 1-5 seconds unless checks, pawn moves or changed rays alter them. Familiar recaptures can move a last guard. T37 Astra Qb6 took 28 seconds and hung Q; finished 13:54, zero invalid attempts. Clock shortage did not cause the loss.
- Ahead: remove counterplay, simplify safely and preserve mating material. Before heavy-piece trades list cheaper capturers, legal recapturers and abandoned guards. Rf4 Bd2xf4 lost the exchange despite Bxf4.
- Material comes from the board, not comments. T36 Kxc5 left me B down with one extra pawn. T37 Rxf8 took White's offered Q but still left 2R versus R. Passers supply counterplay, not automatic equality.
- Supported passers can purchase useful exchanges without promoting. Qc7 Qxc7 dxc7 retained the passer; Bxc7 removed it. Count final material before choosing a recapture or removing a blockader.
- Supported passers tie down defenders while K invades. Kd4 screened Rd1-d6; Kc5 cleared it. Kc6 guarded d6, freeing Bg5+. Re8+ Rd8 Rxd8# used bishop support. Calculate checks before entering beside a blockader.
- Stop advanced counterplay before remote raids. Re8 blockaded e6, bxc5 removed another advanced pawn, Rxe7 stopped promotion. Threats against g3 did not stop connected queenside passers.
- B+P: preserve the LAST pawn with king support before sending B away. Bd8 alone guarded a5; Bxg5 let Ka4 approach while h6-h7 tied B to h8. Before exchanging bishops evaluate the pawn ending and whether K can take the chain's base.
- Escort passers; scan straight AND capture-promotions two advances ahead. c2 attacks b1/d1. a2 outran Kxa3. b8=Q+ can discover Ra7-d7, making Rxb8 illegal. Include en passant before an adjacent two-square push.
- King activity needs legal targets, arrival times and an escape map. Ke4 hit d4, but Kc5 guarded it; Ke6 attacked d7, not d8. Do not chase a remote pawn while enemy K+B can liquidate the central chain.
- Verify mating support, legal blocks, flights and stalemate. Rb1+ Bf1 Bh3 supported Rxf1#; the pinned bishop could not take Bh3. Qa8+ Bd8 Qxd8# exploited f7/g7/h7 occupying flights.

## White openings
- Scheveningen/Classical Sicilian: Be2/O-O/Be3/f4/Kh1, then a4/Bf3/Qe1-g3 suits me. Distinguish Dragon/Maroczy; wins depended on errors. T36 Taimanov Qe1 and the Nxc6 detour after Qxe5 were inaccurate; compare immediate queen exchange.
- DeepSeek battery: Bxd4 after Nxd4 keeps B active. With f6 clear, Qg3/Bxe5 enables mate; Nf6 blocks it. Qb6 can lose Q to Bxb6. e5/dxe5/fxe5 opens Rd1 and hits Nf6; Bf6 exf6 supports mate.
- Maroczy Qa5 BEFORE f3: Be3 loses e4 because Nc3 is pinned. Do not import the later f3/Qxd4 setup. With f3/Qxd4, Ng4 hits Be3 AND uncovers Bg7 against Qd4.
- Maroczy long castling: O-O-O/Rhe1 puts K/R behind lines central exchanges can clear; Bd3/Bxd3/Rxd3 abandons Re1. Rfd1 allowed Bxc4 Bxc4 Rxc4, losing P; Nd5 clears Rc8-c1.
- Short-castled Maroczy: Nd5 clears Qa5-d2; queen exchange and Bxd5/exd5 enable Bd4+, forking Kg1/Ra1 if b2 is empty. c5 does not prevent Rxc5. Bc4 loses to b5xc4; Re1 can ignore Rf7-f4 against Bf4. Repetition with White's must-win odds is a match loss.
- Long-castled Dragon: Bc4/f3/Be3/Qd2/O-O-O against h5/Nc4 and Bxc4 bxc4. g4 repeatedly liquidated my f/g/h pawns for Black's h-pawn. h4 avoided that, but Bh6 repeated the uncastled Rh8-h6 trap. Near equal before Bh6; no verified replacement supplied.
- Short-castled Dragon: Bb3/Nxe3/fxe3 concedes bishop pair. Bg4 attacks Qe2 through f3; Nf3 blocks it. Nxf3+ needed gxf3, Bh3 needed Rfe1, Bxc3 needed bxc3. Qh4/Rd3 enabled Rc5-h5; Qxa5 ignored Qg4+ and mate. An offered trade has no effect until accepted.
- Zaitsev: distinguish Nb4/c5/d5/Nd7 from Nb8. g6/Qd6 guards f4 after exf4; do NOT play f4 with Be3/Ng3 there. h4-h5 induced g5 and freed Nf5 with tempo, but g4/f3 were mistakes. Qd6/Rd8 cannot recapture Bb1xc2; other Chigorin boards have Qc7/Rc8 recapturers.
- Ruy guard losses: Qxf3 abandons d5; exd5 can expose Rxe1+ with Bb1/Bc1 blocking Ra1. Bf4 permits Bxe4 with tempo on Qf3; e4 screens Bc6-f3 AND guards Nf5. Qxe4 meets Rxe4.
- Chigorin: Nf1 restores Qd1-d4; Qf3 abandons b3. Ng4 exchanges can lose h-pawn and hit Rd1. d5 is branch-dependent. f6 hits Re7 AND opens Bc2-h7: compare mate before automatic Qxf4.
- T37 Chigorin: Nxd4 after Nf1/exd4 allowed Nxd4/Qxd4 with Bc2 undefended on cleared Qc7-c2 file. Against Sonnet, Rdc1 abandoned d5's sole rook guard. En passant fxg6 let Kxg6 activate and hit Nf7; capture is optional. No verified replacements supplied.
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and hits Nf6. Nd7 allows Qxd7 Qxd7 Rxd7, winning N; Bf6 exf6 wins B for P. Bc3 clears d2; Be1 guards Ng3 through f2.
- Ruy d3: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. Qd3/Bb1 threatens Qh7#, answered by g6. Before g3/h4 calculate f5/fxe4 and queen entry. SF's e4 displaces Nf3 and Ne5-d3-f4 invades; f3 needs checking-fork calculation.
- Ruy Bg4/Qe2/Nc6: h3 Nd4 hits Qe2/Bb3/Nf3; Qe3 Bxf3 Qxf3 loses Q. c4 Bc2 Nxc2 forks heavy pieces. Ba7/exd4 makes cxd4 open Ba7-d4; e5 Nxe5 is supported by d6. Rxe5 needs Qf6+ calculation.

## Black openings
- English vs GLM: e5/Nf6/Nc6/d5/cxd5/Nxd5, then Nb6/Be7/O-O/Be6/Qd7/Rad8 gave active development. White's c-pawn was gone: not a Maroczy. Be6 could recapture exd5; GLM omitted the recapture, then Qe3 lost Q to d4xe3. No forced opening edge established.
- Castled Four Knights: Nd5 Nxd5 exd5 e4 dxc6 exf3 Qxf3 dxc6 exchanges both knights and e-pawns; material equal. Qd4/Bg4/Bd6 and queen exchanges repeatedly reached near equality. Distinguish Nd5 before castling; later losses do not refute the opening.
- T37 Four Knights: Be6 was inaccurate; Bxe6 fxe6 was required and left e6 weak. Qb3/Qd6/d4 Rf6 was a mistake: c3 chased Bb4 and exposed b7; Rb8 then lost R to Qxb8+. Open f-file does not justify a rook lift before checking queenside targets. Bd6 is a previously playable setup, not verified best here.
- Four Knights Qxe3/fxe3: Rae8/Be6/Rxe6 remains playable. T36 Rfe8/f5/g6/c5 reached near equality. Loss came from Ke5/d4+ losing Bc5, then an imagined rook recapture against discovered check. Re6/Re8 do not guard f5; Kf7 can block Rf8-f5.
- Chigorin vs Sonnet: Na5/c5/Qc7, central exchanges/Nc6, then a5-a4/Bd7/Rfc8. Bb1 can clear Rc1-c7 and pin Nc6 to Qc7; routine Rfe8 ignored d5 winning N. Resolve pin first. Bd3 hangs B if Nd2 blocks Qd1-d3.
- T37 Astra Chigorin: after Rc1/Bb1, Qb7 removed Q from the c-file and released Nc6 before d5. Bd8-b6, Na5-c4 and Bxf5/Nxf5 led to a queen-and-minor-piece position with material equal before my queen blunder. a3 was inaccurate; b4 was marked required. Qc7 was marked a mistake despite hitting Na5/d6: a double attack still needs calculation. Qb6?? lost Q, not an opening refutation; no verified best reply supplied.
- Classical Caro: h6/Bh7/Nd7/Bxd3/e6/Ngf6/Be7/O-O. Against O-O/c4/Rfe1, c5 d5 was adverse. Long-castling Nxe5/dxe5/Nd5 also lacked validation. Gifts certify neither setup.
- Ruy d3 vs Sonnet: Re8/Bb7/Bf8, central d5 exchange, then f5/Qd7/g6. Nxe3 Qxe3 permits f4 forking Q/Ng3, but fxe3 avoids it. Move Q off Rd1's file BEFORE e4 dxe4. Be7 can block Re8's defense of e5.
- SF Ruy 6.d4: exd4/Nd5/Nxd4, then Nb6/Nxa4 and d6/Bxd6/Be6 reached near equality. Against Rad1/Bxd6, cxd6 retained d6; Qe7 lost it. Qb6 dxe5 uncovers Be3-b6. Queens-on Berlin Be7/Rd1 requires solving the open d-file.
- Advance Caro: f6 Nf4/Qd6 exd6 repeatedly loses Q. Earlier f6 BEFORE cxd4 worked with c3 screening Qb3-d3 and Nd2 blocking Rd1-d3. This validates neither later exchanges nor queenless f6/Rxf6/Ne5, where dxe5 clears Be3-b6 while hitting Rf6.
- QGD: Bxf3 Qxf3 removes Nf3 and Qd1's d4 guard, permitting Nxd4. Nb4 clears Rc8-c4 AND Bb7-f3: Qe2 Bxf3 Qxf3 abandons c4; gxf3 retains its guard. Bd6 loses B if d4 blocks Rd1-d6.
- QGD Bg5/IQP: Nbd7, dxc4/c5/cxd4, b6/Bb7/Rc8 developed smoothly. Nxf6 preserved pawns; Nd5 blockaded d4; Nxd5 Bxd5 retained e6. Nc4 supplied the piece. h6/Qc7/Rfd8 were adverse despite winning.

## Opponents
- Astra: T37R4 White used the closed Chigorin with Nb3/Be3, Rc1/Bb1, Nf1-g3/h4-f5 and d5; after Bxf5 recaptured Nxf5. Contested the c-file, took my undefended Qb6 immediately, then coordinated Q/N/B and g4# against the exposed king. Qf3 and Qc7 were marked adverse; calculate actual replies rather than assuming every threat is sound. Zero invalid attempts; mostly brisk opening moves, later 20-53 seconds. One game against me.
- Fable 5.1: T37 Chigorin missed Qxc2 after central exchanges; Qc1+ ignored Bf4-c1, then Nd5 hung N. Simplification and pawn-grab checks can miss remote captures. Verify independently.
- GLM 5.3 Flash: English g3/d3/e4 after exchanging c4; omitted a recapture, then Qe3 landed on d4's capture diagonal. Remote rook raids can ignore bishop captures or mate. As Black hangs pieces in Sicilian structures.
- Sonnet: exploits blocked recaptures and pawn forks; g6/Qd6 punished f4. Queenless play can miscount defenders. Repeated bishop shuffles and flags are not my plan: preserve concrete passer pressure and clock caps.
- DeepSeek: overlooks capture chains, undefended developed pieces and opened rays. T36 Bf4 hung B; Qxb2 lost Q to Qf6's diagonal. Speed and illegal attempts vary; verify actual defenses.
- SF19: punishes pinned guards, pawn-hit pieces, king screens and passers. T37 c3 removed my b-file screen; Qxb7/Qxb8+ took the undefended rook, gxh4 took my queen, and rook checks outran my h-pawn attack. Offered Qf8+ to Rxf8 but retained an extra rook. Accept real gifts and recount; never depend on repetition or an engine error.

## Note files
- notes/accelerated-dragon.md - Uncastled h-rook trap, pawn captures, pinned blocks and king exposure.
- notes/berlin-endgame.md - D-file and clearance.
- notes/caro-kann-advance.md - Breaks and queenless mate.
- notes/deepseek.md - Italian/Classical Caro, capture chains and conversion.
- notes/four-knights.md - E-file clearance, king screens, pawn races and repetition.
- notes/qgd-exchange.md - IQP blockades, capture chains, clearance and mate.
- notes/ruy-lopez.md - Pawn forks, blocked defenders, conversion and passer support.
- notes/sicilian-maroczy.md - Pinned guards, rook-defense clearance, mating screens and passers.
