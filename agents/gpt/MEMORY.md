# Chess memory

## Move discipline
- Apply warnings BEFORE choosing. Every candidate needs its own scan on the proposed board. Start with the enemy's last move; inspect checks, captures, forks, promotions and quiet mates. Rejecting one blunder does not validate another.
- DESTINATION BEFORE PURPOSE: Bc6 defended b5 but Nd4xc6 won B; neither b5 nor d5 guarded c6. A defensive task, developing tempo or blockade does not make the destination safe.
- PAWN DIAGONALS FIRST, then every knight and complete sliding rays. Nb3 attacked Rc5 but c4xb3 won N; Bc4 lost to b5xc4; Rc3+ lost R to b2xc3. Support and check do not prevent cheaper captures.
- Name LEGAL defenders by current square, excluding the mover. Qa5 pinned Nc3 to Ke1, so Be3 did not defend e4. Nf3 does not attack e4; Nc3 does not attack d4. Trace every intervening square.
- OWN SCREENS: Nd2 blocks Qd1-d3; Be3 blocks Re1-e4; f7 blocks Rf8-f2. Audit abandoned guards and the recapturer's departure. Clearing one line does not clear another.
- KING SCREEN, T40 SF19: Ke7 unpinned f5 but BLOCKED Re8-e6 and abandoned Kf7's guard of Re6. exf5 attacked the rook. Before centralizing K, trace both my rook rays and the enemy pawn capture; removing a pin may expose another piece.
- LAST GUARD: Nc3 screened Qa5-e1; Rd1 guarded Re1. Nxd5 removed the screen, while Bd3/Bxd3/Rxd3 moved Re1's last guard. Development did not prevent Qxe1+.
- PAWN BREAKS: place the enemy capture first. f4 exf4 forked Be3/Ng3 and opened Qd6-f4; Bxf4 Qxf4 lost B. f6/exf6 exposed Be6 to Qe2; f2-f3 abandoned Be3.
- PAWN SCREEN: T40 Taimanov, f4/f5 screened Rf8 from Qf3. fxe6 cleared the entire file and allowed Rxf3. Before a pawn capture trace its OLD file and both opened diagonals to their far endpoints.
- For every check test Kxchecker and ALL other captures. Qh2+/Rh7+/Qxb2+ lost heavy pieces to kings; Qe8+ overlooked Re6-e8 and e4 blocking Re1's support. Name the actual guard.
- BACKWARD BISHOPS: Bf4 reached c1 through empty e3/d2; Qc1+ was Bxc1. Bh6 reached Rc1 through g5/f4/e3/d2. Trace both directions when blockers disappear.
- UNCASTLED DRAGON: h5 vacates h7, opening Rh8-h6. Bh6 Bxh6 attacks Qd2 through g5/f4/e3; Qxh6 loses Q to Rxh6. Verify the LAST capture and castling status before Bh6.
- OPEN A-FILE: axb5 axb5 opens Ra8-a1. Bc1/Bb1 can block a rook recapture; queen retreats then lose Ra1. Resolve rook contact first. Ra1/Rf1 defend each other only with b1-e1 empty.
- Calculate through the LAST recapture and recount the whole board. Nc4 Qxc4 Qxc4 Rxc4 lost N despite queen support. Opponent may STOP exchanging: Qd5 allowed Rxd5, winning Q for R despite Nc3/Rd1 support.
- RECAPTURE CLEARANCE, T40 Sonnet: Qe2 stood behind Rc2. Ra2 Rxa2 Qxa2 Qxa2 lost my WHOLE Q after exchanging one rook each. Rxa2 vacated c2, uncovering the queen's rank. Sweep my recapturer's destination after the enemy capture; first support is insufficient.
- An attacked piece need not retreat. b3 attacked Rc4 but opened Bf6-a1: Bxa1 bxc4 Bc3 retained extra B. Rdb1 attacked Bb2, but Bxa1 took R. Scan captures by OTHER pieces.
- Refresh pins when endpoints move. Nd4 Nxd4 cxd4 opens Rxd8+ against Qd8. Kb1 released Rd2; Kf1 released Nd2's pin to Ra2. A pinned rook can capture its pinning queen.
- Before forks/trades test captures and checking intermezzos. Nc3+ Qxc3 Rxd1 Rxd1 lost N; Bxd5 allowed Nd3+ before Qxd5. Nc7's fork did not answer Qd8's attack on Qg8.
- Trace vacated rays to far endpoints. e5 uncovered Bf3-a8. Nf5 blocked Bf4-d6; exf5 screens Bc2-h7 while f6 clears it. Rc7 can screen Bb6-d8 and permit Kxd8.
- Trace checking rays BEYOND K. Kb3 screened Rb1-b7; Ka4 allowed Rxb7. Ke5 allowed Bc3+ skewering g7. A checking block must survive its capture.
- MATE FIRST, including quiet moves and queenless positions. Nxf4 hit Qh5 but allowed Qxh7#; Rxe7 ignored Rh1#. exf6 can win a minor AND support Qxg7#. Luft solves only the mate its flight prevents.
- MATING SCREEN: Qg3/Bd4 with f6 clear made Ne5 responsible for blocking g7. Bxe5 removed the screen and retained g7 support. Nf6 still blocks the battery.
- LONG-CASTLED K: central exchanges can clear the c-file around Kc1. Qxe1+ Rd1 ties R down. Ka1 behind b2 on Bg7's diagonal made bxa3 illegal after Qa3 Qxa3#.
- CHECKING PAWN FORK: Ke5/Bc5 faced d4+, hitting K AND B. Kd5 dxc5 Kxc5 recovered only P for B. Inspect the pawn's other diagonal and captures of the checker before moving K.
- DISCOVERED CHECK: Bc3/Rd4 screened Bc3-e5 against Ke5. Rxg4+ vacated d4 and discovered bishop check; Rg8xg4 could not answer it. Inspect the capturer's VACATED ray.
- CHASABLE SCREEN: Qb3 aimed up the b-file behind Bb4. c3 drove B away and exposed b7. A safe bishop retreat does not protect the target behind its old square.
- QUEEN CONTACT: Qb6 attacked Qc7 but Qxb6 won Q; neither N guarded b6. Rb8 attacked Qb7 but Qxb8+ won R; c7 blocked Qd6-b8. Name the legal recapturer before claiming a forced retreat.
- A pawn blocking a rook is not necessarily pinned. Rg1/g3 faced Rg6, but Kh2 was off the g-file: Qxh4+ gxh4 lost Q. Trace the ray to K before excluding a capture.
- My threat does not stop checks. Rg2/h2 threatened Kh1, but rook checks drove Kg3-f2-f1 and Rb1# used Rc2 to seal rank 2. Map checks and flights before entering a rook cage.
- DEVELOPING A SCREEN: Italian Be6 blocked Re8-e5. Nxe5 Nxe5 Rxe5 conceded P; a planned later Bxc4 did not defend e5 now. Test central captures before putting B on my rook's file.
- DOUBLE ATTACK is not safety: Qg4 hit Qg5/Nf4 but Be6-f5-g4 was clear, so Bxg4 won Q. Rxd4 took a loose B but allowed Qxg2#. Inspect uninvolved capturers and mate.
- Validate destination and full path before submission. After ONE rejection reconstruct the board and choose a verified legal move; three invalid replies forfeit. Recovery still needs a capture scan. Opening memories require matching blockers and piece placement.

## Clock and endings
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below five minutes cap 15; below 90 seconds use 1-3. Budget from the starting clock, especially Armageddon White's ten minutes.
- Long thought does not prove the scan passed. T40 Ke7/Re5 took 33/55 seconds; finished 12:10 with zero invalid moves. Time pressure did not cause the loss. Spend critical time naming captures, screens and flights, not explaining activity.
- Verified recaptures/cycles need 1-5 seconds unless checks, pawn moves or changed rays alter them. A familiar recapture can move a last guard. Shorten routine conversion once support and threats are checked.
- Ahead: remove counterplay and simplify safely. Before heavy-piece trades list cheaper capturers, legal recapturers and abandoned guards. Rf4 Bd2xf4 Bxf4 loses the exchange.
- Material comes from the board, not comments. Kxc5 left B down with one extra P. Rxf8 took SF's offered Q but still left 2R versus R. Nxc6/Bxe3/fxe3 left six pawns against N+five pawns.
- CONNECTED PASSERS NEED A BREAK: Astra's Nd4/e3/K blockaded c4/d5 while N collected g7/h6. Remote king raids did not dislodge it; d4 allowed exd4. Compare blockade removal and promotion tempi before raiding.
- Supported passers can purchase exchanges without promoting. Qc7 Qxc7 dxc7 retained the passer; Bxc7 removed it. Count final material before choosing a recapturer.
- Stop advanced counterplay before remote raids. Re8 blockaded e6; bxc5 removed another advanced pawn; Rxe7 stopped promotion. Threats against g3 did not stop connected queenside passers.
- KING AS SOLE ROOK GUARD: T40 Re6 beside Ke7 was vulnerable to Rf7+, protected by g6. The check drove K away, then Rxe6 won R. When relying on K support, test checks that deflect K and pawn-controlled checking squares.
- A pawn capture can create BOTH a passer and checking support: T40 fxg6 threatened promotion and guarded f7, enabling Rf7+. Re5's bishop support did not solve the pawn's next capture or rook entry. Evaluate the resulting pawn, not only the rook retreat.
- B+P: preserve the LAST pawn with K support before sending B away. Bd8 alone guarded a5; Bxg5 let Ka4 approach while h6-h7 tied B to h8. Evaluate pawn endings and access to the chain's base before exchanging B.
- Escort passers; scan straight AND capture-promotions two advances ahead. c2 attacks b1/d1; a2 outran Kxa3. b8=Q+ can discover Ra7-d7, making Rxb8 illegal. Include en passant beside two-square pushes.
- King activity needs legal targets, arrival times and an escape map. Ke4 hit d4 but Kc5 guarded it. Two active enemy rooks, supporting pawns and my enclosing pawns require a scan of pawn checks and all eight exits before a material raid.
- Verify mating support, blocks, flights and stalemate. Rb1+ Bf1 Bh3 supported Rxf1#; pinned B could not take Bh3. Qa8+ Bd8 Qxd8# exploited occupied flights.

## White openings
- Quiet Open Sicilian: Be2/O-O/Be3/f4/Kh1, then a4/Bf3/Qe1-g3 suits me; distinguish Dragon/Maroczy. Wins depended on errors. Taimanov Qe1 and automatic Nxc6 after Qxe5 were inaccurate; compare immediate queen exchange.
- Taimanov battery: Bxd4 after Nxd4 keeps B active. With f6 clear, Qg3/Bxe5 can enable mate; Nf6 blocks it. e5/dxe5/fxe5 opens Rd1 and hits Nf6; Bf6 exf6 supports mate. With Qf3/Rf8, retain the f-pawn screen or move Q before fxe6.
- Maroczy Qa5 BEFORE f3: Be3 loses e4 because Nc3 is pinned. With f3/Qxd4, Ng4 hits Be3 AND uncovers Bg7 against Qd4. After b3, Bf2 can uncover Qa5-c3 and lose Nc3.
- Long-castled Maroczy: O-O-O/Rhe1 exposes K/R to central clearance. Bd3/Bxd3/Rxd3 abandons Re1; Nxd5 removes Qa5-e1's screen. Rfd1 allowed Bxc4 Bxc4 Rxc4, losing P.
- Short-castled Maroczy: Nd5 clears Qa5-d2; queen exchange/Bxd5/exd5 enable Bd4+ forking Kg1/Ra1 if b2 is empty. c5 permits Rxc5; Bc4 loses to b5xc4. Re1 ignored Rf7-f4 against Bf4. Must-win repetition loses the match.
- Long-castled Dragon: Bc4/f3/Be3/Qd2/O-O-O against h5/Nc4. g4 liquidated my f/g/h pawns for Black's h-pawn. h4 avoided that but Bh6 repeated the uncastled Rh8-h6 trap. Near equal before Bh6; no verified replacement.
- Short-castled Dragon: Bb3/Nxe3/fxe3 concedes bishop pair. Bg4 hits Qe2 through f3; Nf3 blocks. Nxf3+ needed gxf3, Bh3 needed Rfe1, Bxc3 needed bxc3. Qh4/Rd3 allowed Rc5-h5; Qxa5 ignored Qg4+ and mate. Trade offers work only if accepted.
- Zaitsev: distinguish Nb4/c5/d5/Nd7 from Nb8. g6/Qd6 guards f4 after exf4: avoid f4 with Be3/Ng3. h4-h5 induced g5 and freed Nf5 with tempo, but g4/f3 were mistakes. Qd6/Rd8 cannot recapture Bb1xc2.
- Ruy guards: Qxf3 abandons d5; exd5 can expose Rxe1+ with Bb1/Bc1 blocking Ra1. Bf4 permits Bxe4 with tempo on Qf3. e4 screens Bc6-f3 AND guards Nf5; Qxe4 meets Rxe4.
- Chigorin: Nf1 restores Qd1-d4; Qf3 abandons b3. Nxd4/Qxd4 can lose loose Bc2 on the cleared Qc7-c2 file. Rdc1 can abandon d5's sole guard. f6 hits Re7 AND opens Bc2-h7: compare mate before Qxf4. En passant is optional.
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and hits Nf6. Nd7 permits Qxd7 Qxd7 Rxd7, winning N; Bf6 exf6 wins B for P. Be1 guards Ng3 through f2.
- Ruy d3: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. Qd3/Bb1 threatens Qh7#, answered by g6. Before g3/h4 calculate f5/fxe4 and queen entry. SF's e4 displaces Nf3 and Ne5-d3-f4 invades.
- Ruy Bg4/Qe2/Nc6: h3 Nd4 hits Qe2/Bb3/Nf3; Qe3 Bxf3 Qxf3 loses Q. c4 Bc2 Nxc2 forks heavy pieces. Ba7/exd4 makes cxd4 open Ba7-d4; e5 Nxe5 is supported by d6. Rxe5 needs Qf6+ calculation.

## Black openings
- Italian vs DeepSeek: Bc5/Nf6/O-O/d6/a6/Ba7 is usable. Re8/d5/Nxd5/Nf4 met errors, but Be6 screened Re8-e5 and conceded P. Bg4-h5-g6 avoids that screen. Qe7/e4 enabled Nxe5/dxe5/Qxe5 to win ONE pawn; Qd5 then lost Q to Nf6xd5. Wins do not certify every move.
- English vs GLM: e5/Nf6/Nc6/d5/cxd5/Nxd5, then Nb6/Be7/O-O/Be6/Qd7/Rad8 developed actively. White's c-pawn was gone: not a Maroczy. Its Nxd4/Qxd4 lost Q on the open Qd8-d4 file. Distinguish e4 before Bg2 from d3.
- Castled Four Knights: Nd5 Nxd5 exd5 e4 dxc6 exf3 Qxf3 dxc6 leaves equal material. Qd4/Bg4/Bd6 and queen exchanges repeatedly reached near equality. T40 was balanced before Ke7 screened Re8-e6; the opening was not the cause.
- Four Knights alternatives: other players obtained an extra pawn with Bd6/Qh4 before Qd4; compare this setup on the matching board, not as a forced improvement. My early Be6/fxe6 left e6 weak; Rf6 ignored c3 chasing Bb4 and exposing b7. Rb8 lost R to Qxb8+.
- Four Knights queenless: Rae8/Be6/Rxe6 remains playable. Rfe8/f5/g6/c5 previously reached near equality. Re6/Re8 do not guard f5; Kf7 can block Rf8-f5; Ke7 can block Re8-e6. Calculate e4/exf5 before king moves or further pawn expansion.
- Chigorin vs Sonnet: Na5/c5/Qc7, central exchanges/Nc6, a5-a4/Bd7/Rfc8. Rc1/Bb1 clears Rc1-c7 and pins Nc6; move Q off c7 BEFORE d5. T40 Qb7 passed this check, but Na5/Be6 allowed supported Bxb5/Bxa4. Later Ra2 lost Q through rook-capture clearance.
- Astra Chigorin: Qb7 released Nc6; Bd8-b6, Na5-c4 and Bxf5/Nxf5 reached equal material before Qb6 hung Q. a3/Qc7 were adverse; b4 later required. No verified move-34 replacement.
- Astra Zaitsev: Bb7/Re8/Bf8, exd4/Nb4/c5, Nd7/f5 gave active play. N7f6/d5 were inaccurate. Queen exchange left bishop pair plus P; Bc6 lost B. No verified earlier repairs; loss does not refute the opening.
- Classical Caro: h6/Bh7/Nd7/Bxd3/e6/Ngf6/Be7/O-O. Against O-O/c4/Rfe1, c5 d5 was adverse. Long-castling Nxe5/dxe5/Nd5 lacked validation. Gifts certify neither setup.
- Ruy d3: Re8/Bb7/Bf8, central d5 exchange, f5/Qd7/g6. Nxe3 Qxe3 permits f4 forking Q/Ng3, but fxe3 avoids it. Move Q off Rd1's file BEFORE e4 dxe4. Be7 can screen Re8-e5.
- SF Ruy 6.d4: exd4/Nd5/Nxd4, Nb6/Nxa4, d6/Bxd6/Be6 reached near equality. Against Rad1/Bxd6, cxd6 retained d6; Qe7 lost it. Qb6 dxe5 uncovers Be3-b6. Solve the open d-file.
- Advance Caro: f6 Nf4/Qd6 exd6 repeatedly loses Q. Earlier f6 BEFORE cxd4 worked with c3 screening Qb3-d3 and Nd2 blocking Rd1-d3. Queenless f6/Rxf6/Ne5 differs: dxe5 clears Be3-b6 while hitting Rf6.
- QGD: Bxf3 Qxf3 removes Nf3 and Qd1's d4 guard, permitting Nxd4. Nb4 clears Rc8-c4 AND Bb7-f3; Qe2 Bxf3 Qxf3 abandons c4, gxf3 retains its guard. Bd6 loses B if d4 blocks Rd1-d6.
- QGD Bg5/IQP: Nbd7, dxc4/c5/cxd4, b6/Bb7/Rc8 developed smoothly. Nxf6 preserved pawns; Nd5 blockaded d4; Nxd5 Bxd5 retained e6. Nc4 supplied the piece. h6/Qc7/Rfd8 were adverse despite winning.

## Opponents
- SF19: takes loose material, exploits pinned guards and king screens, and uses checks to deflect sole defenders. T40 e4/exf5 exposed Re6; fxg6 supported Rf7+ and promotion. Never rely on repetition or treat an offered Q as full recovery; recount the board.
- Astra: coordinated Closed Ruy bishops/knight; takes unsupported Q/B immediately. Nd4/e3/K blockaded my passers while N took g7/h6 and a g-pawn promoted. Calculate replies to its adverse moves independently.
- Sonnet: exploits blocked recaptures, clearance and pawn forks. T40 Rec1 put Qe2 behind Rc2; Rxa2 uncovered Qxa2. Uses coordinated exchanges and supported passers to convert. Preserve concrete threats and clock caps.
- DeepSeek: Italian central play; identifies loose pieces but can miss the forcing reply. Took Qf3 after my f-pawn clearance, then lost Rc8 by moving its queen screen and offered Qe1+ to Rxe1. Verify gifts and conversion; do not assume recovery.
- GLM: English g3/e4 or d3 after exchanging c4; can omit recaptures or lose Q on an opened file/pawn diagonal. As Black hangs pieces in Sicilian structures. Remote raids may ignore bishop captures or mate.
- Fable: missed Qxc2 after central exchanges; Qc1+ ignored Bf4-c1, then Nd5 hung N. Verify remote captures independently.

## Note files
- notes/accelerated-dragon.md - Uncastled h-rook trap, pawn captures, pinned blocks and king exposure.
- notes/berlin-endgame.md - D-file, clearance and English capture chains.
- notes/caro-kann-advance.md - Breaks and queenless mate.
- notes/deepseek.md - Italian rook screens, capture chains and conversion.
- notes/four-knights.md - King screens, rook guards, pawn checks and races.
- notes/qgd-exchange.md - IQP blockades, capture chains, clearance and mate.
- notes/ruy-lopez.md - Rook invasions, final captures, unsafe defenders and blockades.
- notes/sicilian-maroczy.md - Pawn screens, pinned guards, mating batteries and passers.
