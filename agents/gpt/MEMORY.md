# Chess memory

## Move discipline
- Apply stored warnings BEFORE choosing. Each candidate needs its own forcing scan; rejecting one blunder does not validate another. Recognition without execution repeatedly loses queens and rooks.
- Start with the enemy's last move: changed attacks, pawn controls, opened lines. Scan checks, captures, forks, promotions and quiet mates; repeat on the proposed final board. Refresh attacks after every capture and king reply.
- PAWN DIAGONALS FIRST, then knight jumps and complete sliding rays. Rb3?? axb3, Qe4?? dxe4, Qd5?? exd5, Ng5? hxg5 and Qxe6?? fxe6 lost material. Support cannot prevent a cheaper capture.
- For every check, test Kxchecker and ALL other captures. Name the defender and trace its legal path. Qh2+/Rh7+/Qxb2+ lost heavy pieces to king captures. T32 Qe8+?? Rxe8: Re6 reached e8; my e4 pawn blocked Re1's supposed support.
- Name exact defenders, screens and LEGAL recapturers. Nd2 blocked Be3-c1; Be3 blocked Re1-e4; f7 blocked Rf8-f2; Qe3 could not recapture c2. Audit friendly rays blocked as well as enemy rays opened.
- KING AS SCREEN: T33 ...Kf7? blocked Rf8-f5, abandoning a pawn to Rxf5+. ...Kd4 screened Bc3-h8 and allowed promotion. Before activating K, trace every friendly rook/bishop ray it obstructs.
- OPEN A-FILE: axb5 axb5 opens Ra8-a1. T31 Bc1 blocked Re1-a1; T32 Bb1 blocked Rd1-a1. Queen moves ignored ...Rxa1 and lost R. T33 Rxa8 immediately resolved contact; ...Bxa8 retained Black's queen on d8. Inspect the whole recapture path BEFORE opening the file.
- Calculate through the LAST recapture and recount material. T32 Nc4?? Qxc4 Qxc4 Rxc4 lost N despite its queen guard. Qxc1 Bxc1 Rxc1 Qxc1 costs Q+R for R+B. A capturer does not guard its own landing square.
- An attacked piece need not retreat. T32 b3 attacked Rc4 but opened Bf6-a1: ...Bxa1! bxc4 Bc3 preserved my extra B with tempo on Re1. Scan forcing captures by OTHER pieces and their escape afterward.
- Validate the actual piece square and full path before submission. After ONE rejected move, reconstruct the board and choose a verified legal move; three invalid replies forfeit. Opening memories apply only to matching positions.
- Trace checking rays BEYOND the king. T31 Kb3 screened Rb1-b7; Ka4? allowed ...Rxb7. Examine legal blocks before exposing a rear piece.
- Count duties AFTER exchanges and guard moves. Re2 Rxe2 Nxe2 removed BOTH e4 guards, Re1 and Ng3. ...f6/exf6 exposed Be6 to Qe2; f2-f3 abandoned Be3. A locally equal trade can expose another unit.
- Discovered attacks accompany forks. Dragon ...Ng4 hit Qe3/Bh6 AND opened Bh8-d4 against Nd4; Qxh6 abandoned d4. Search captures of the forking piece and all recaptures before retreating automatically.
- Refresh pins when endpoints move. ...Nd4 Nxd4 cxd4 opens Rxd8+ against Qd8. Kb1 released Rd2; Kf1 released Nd2's pin to Ra2. A pinned rook can capture its pinning queen.
- Before forks/trades, test captures and checking intermezzos. ...Nc3+ Qxc3 Rxd1 Rxd1 lost N; Bxd5 allowed ...Nd3+ before ...Qxd5. Dragon Nc7?? ignored Qd8's attack on Qg8; a fork does not answer an attack on my queen.
- Derive knight attacks from actual squares: Nf3 does NOT attack e4. Nf5 blocked Bf4-d6; trace bishops through OWN pieces before counting attackers.
- Pawn advances can replace screens rather than clear a battery. exf5 screened Bc2-h7; f6 cleared it. After ...gxf6/...f5, Bxf5 removes the screen; gxf5 replaces it.
- MATE FIRST, including quiet moves and queenless positions. ...Nxf4 attacked Qh5 but allowed Qxh7#; Rxe7 ignored ...Rh1#. Luft solves only the mate its flight prevents. Test checks and resulting flights before king advances or remote raids.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3. Long thinking never replaces a capture scan.
- Name a target/break before shuffling; calculate the opponent's forcing reply. T33 Black finished with 9:27 after 45-53 second routine moves yet missed king screens and promotion checks. T33 White spent 93 seconds on Be3 and 44 on Kf2; ample time still did not make Bxh6 sound. Spend time on concrete replies.
- Budget from the starting clock, especially Armageddon White's ten minutes. T31 fxg4/Bh6 took 117/68 seconds without preventing losses. Verified recaptures and cycles need 1-5 seconds unless checks, pawn moves or changed rays alter them.
- Before offering a heavy-piece trade, list ALL cheaper capturers. T31 ...Rf4?? met Bd2xf4 through e3; Bxf4 recovered only B, leaving B versus R. Support did not save the exchange.
- Ahead: remove counterplay, simplify safely, preserve mating material. Check pawn guards and entry squares before queen trades. Worse: seek safe activity/repetition; later gifts do not validate speculative losses.
- T33 White conversion: Nxd6 took an undefended bishop and forked Re8. Nxb7 exchanged N for the remaining B while retaining the extra B. Bc3 cleared Rd1's file; Bf5 attacked the d7 blockader, and Bxd7 left R+B versus R with a supported passer. Count the remaining advantage after each trade.
- A supported passer can tie down the enemy while my king invades. T33 d6 had Rd1/Bf4 support; Kd4 temporarily screened Rd1, then Kc5 cleared it. Re1-e8 supplied the second entry. Bg5+ forced Kc8; Re8+ Rd8 Rxd8# used Bg5's protection of d8 and Kc6's control of exits. Keep escort support while changing rook files.
- Stop advanced counterplay before remote raids. T32 ...Re8 blockaded e6, ...bxc5 removed the other advanced pawn, ...Rxe7 stopped promotion. T33 Black's threats against g3 did not stop Rxc7/Rxb7/Rxc6+/Rxa6; unsupported threats cannot race connected passers.
- B+P: preserve the LAST pawn with king support before assigning B to a remote passer. T30 Bd8 alone guarded a5; ...Bxg5 let Ka4 approach while h6-h7 tied B to h8. A bishop alone cannot mate.
- Escort passers; scan straight AND capture-promotions two advances ahead. c2 attacks b1/d1. Checks can deflect the escort: Ka3 guarded a2, but Bc1+ Ka4 Rxa2+ removed that guard.
- Promotion can DISCOVER a check. T33 b8=Q+ vacated b7 and uncovered Ra7-d7 against Kd7. Rg8 could reach b8, but ...Rxb8 did not answer the rook check. A capture plan must answer ALL checks on the final board.
- Removing a passer's defender helps only if capture/blockade precedes its next advance. T31 Nxd6 removed Ba3's guard, but ...a2! outran Kxa3; Nd6 reached neither a2 nor a1. Kc5?? also allowed ...Bf8+ then ...Bd6 to cover c7/b8.
- Recount king guards after captures. ...Kxh6 abandoned Bf6 and allowed Rxf6+. SF's winning repetition was an escape, not a proven fortress.
- Verify mate support, legal flights and stalemate. Bf6# with Re7/Ph7 uses h7 controlling g8 and Re7 controlling g7/protecting h7. Recompute flights after quiet defenses: ...Be6 vacated d7 against Qg8+, while Nd5 blocked Rd1-d7.

## White openings
- Long-castled Dragon: Bc4/f3/Be3/Qd2/O-O-O against ...h5/...Nc4 and Bxc4 bxc4. T31 g4?! repeated T10: ...hxg4, h5 and rook/knight captures consumed my f/g/h pawns for Black's h-pawn. ...Bxg4 ignored attacked Nh5 and hit Rd1 through f3/e2. Calculate the whole liquidation; no verified move-15 replacement.
- T32 short-castled Dragon: 7.Bc4 d6 8.O-O Ng4 9.Bb3?! Nxe3 10.fxe3! retained material but conceded the bishop pair. Distinguish long castling and the Maroczy queen fork; no verified move-9 replacement.
- Dragon ...Bg4 attacked Qe2 through f3; Nf3! blocked it. ...Nxf3+ required gxf3!, ...Bh3 required Rfe1!, ...Bxc3 required bxc3!. Material survived, but open f/g-files exposed my king. Open files are usable by BOTH sides.
- Qh4?!/Rd3?! let ...Rc5-h5 become active. e5! helped, but ...Bc6! invalidated my plan assuming ...dxe5. e4?! screened Bc6-f3 but blocked Re1-e5. Later ...Qc8 opened a route to g4; Qxa5 ignored Qg4+ Kf2 Rxh2+ Kf1 Qg2#. Guarding Rf3 did not answer mate. An offered queen trade has no effect until accepted.
- Sonnet Zaitsev ...h6/Bc2/...exd4/cxd4/...Nb4/Bb1/...c5/d5/...Nd7 differs from T31's ...Nb8 branch. T33 Nxe5 answered ...Ne5?! before ...Nxf3+; ...dxe5! changed the pawn structure. This avoided T32's Qxf3 branch, but establishes no forced opening edge or best replacement.
- T33 Qg4/Qf6/Bxh6? underestimated ...Qg6!: the queen interposed on the g-file, freeing g7 to capture Bh6 while offering a queen trade. Be3 saved B and hxg4! completed the exchange. A pawn pinned to K is capturable only while the pin survives the opponent's reply; do not count the extra pawn as proof of a sound grab.
- T33 ...Bd6? after the queen exchange left B undefended; Nxd6 won it and attacked Re8. This was an opponent gift, not validation of Bxh6 or the opening. Bf8 had previously retained useful defensive duties.
- T32 Qxf3?! abandoned Qd1's d5 guard. ...Bxd5 won P: exd5 removes e4's screen and permits ...Rxe1+, with Bb1/Bc1 blocking Ra1's recapture. Rd1 saved R, not P. Audit guards lost by queen recaptures and files opened by pawn recaptures.
- T32 Bf4?? with Qf3/Nf5 allowed ...Bxe4 with tempo: e4 screened Bc6-f3 AND guarded Nf5; Qxe4 meets ...Rxe4. ...Re6? did not validate Bf4. Nf5 blocked the claimed Bf4-d6 attacker.
- T31 Zaitsev/Breyer a4/...Nb8, d5? and Bc2?! allowed ...cxd5/exd5/...Bxd5, losing P. No verified replacements for moves 13/15; retaining the bishop pair did not recover the pawn.
- Maroczy c4/...g6/...Qa5, f3/Qxd4: before O-O?! calculate ...Ng4 hitting Be3 AND uncovering Bg7 against Qd4. Qd2/Qxe3 preserved pawns but conceded the bishop pair. ...Be6/Rfc8 met Rfd1?! Bxc4 Bxc4 Rxc4, losing P and attacking Nc3; Nd5 cleared the route to Rc1. No verified replacements.
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and attacks Nf6. ...Nd7?? allows Qxd7 Qxd7 Rxd7, winning N; ...Bf6 exf6 wins B for P. e5 screens Qc7-f4. Against ...Nd5/...Nc7, Bc3 attacks Qf6 and clears d2; Be1 can guard Ng3 through f2. No forced opening edge.
- Chigorin: Nf1 restores Qd1-d4; Qf3 abandons b3. ...Nb4 needs Nc6; a knight still on a5 cannot use that branch. Sonnet Nh2/f4/Bxf4 activated B, but Qe3/Ng4 allowed ...Nxg4/hxg4/...Bxg4, losing h-pawn and hitting Rd1. Nf5 Bxf5 exf5 Nxd5 left two pawns down.
- f6 hits Re7 AND opens Bc2-h7. After ...Nxf4 compare fxe7 and king threats before automatic Qxf4; Qxf6+ can meet ...Bg7 with tempo. Qxh6+ provoked ...Qh7?? Bxh7: Qh5 guarded Bh7 and Bg7 blocked Re7-h7. Gifts do not prove sound sacrifices.
- Ruy d3: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. Qd3/Bb1 threatens Qh7#, answered by ...g6. Before g3/h4 calculate ...f5/...fxe4 and queen entry. SF's ...e4 drove Nf3 away and ...Ne5-d3-f4 invaded; a proposed f3 break needs checking-fork calculation.
- Ruy ...Bg4/Qe2/Nc6: h3?! Nd4 hits Qe2/Bb3/Nf3; Qe3 Bxf3 Qxf3 loses Q. ...c4 Bc2? Nxc2 forks Qe3/Ra1/Re1. ...Ba7/exd4 makes cxd4 open Ba7-d4; e5?! Nxe5 is supported by d6. Rxe5 needs ...Qf6+ calculation.

## Black openings
- Castled Four Knights: 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6. Equal material; distinguish Nd5 before castling. ...Qd4/Bg4/Bd6 and queen exchanges reached near-equal T30/T31/T33 middlegames. Later losses do not refute the opening.
- T33 ...Qxe3/fxe3 differs from T31's queen exchange on g5. ...Rae8/Be6/Rxe6 and ...f5/...g5 retained balance until ...Kf7? screened Rf8's f5 guard. Bxf8! correctly recaptured after Rxf8 but did not recover the lost pawn. No verified move-21 replacement.
- T31 ...Rae8/h6/Be6 exchanges ended ...fxe6, R+B each, equal pawns/open f-file. ...Rf4 later lost the exchange. Evaluate resulting positions, not only local trades.
- Classical Caro: ...h6/Bh7/Nd7/Bxd3/e6/Ngf6/Be7/O-O. Against O-O/c4/Rfe1, ...c5? d5! was adverse; gifts do not certify it. Long-castling ...Nxe5/dxe5/...Nd5 also lacked validation.
- Ruy d3 vs Sonnet: ...Re8/Bb7/Bf8, central ...d5 exchange, then ...f5/...Qd7/g6. ...Nxe3: Qxe3 permits ...f4 forking Q/Ng3, but fxe3 avoids it. Move Q off Rd1's file BEFORE ...e4 dxe4. No forced opening win established.
- SF Ruy 6.d4: ...exd4/...Nd5/...Nxd4, then ...Nb6/...Nxa4 and ...d6/...Bxd6/...Be6 reached near equality. Against Rad1/Bxd6, ...cxd6 retained d6; ...Qe7 lost it. Chigorin ...Qb6?? dxe5 uncovers Be3-b6. Queens-on Berlin ...Be7?! Rd1 requires solving the open d-file before routine development.
- Advance Caro: ...f6? Nf4!/...Qd6?? exd6 repeatedly loses Q. Earlier ...f6 BEFORE cxd4 worked with c3 screening Qb3-d3 and Nd2 blocking Rd1-d3; this validates neither later exchanges nor queenless ...f6/Rxf6/Ne5.
- QGD: ...Bxf3 Qxf3 removes Nf3 and Qd1's d4 guard, permitting ...Nxd4 with tempo; Nc3 does NOT attack d4. Bf4 branch ...Nb4 cleared Rc8-c4 AND Bb7-f3: Qe2 Bxf3 Qxf3?? abandoned c4; ...Rxc4 won B. gxf3 retains Qe2's guard. Bd6?? lost B because d4 blocked Rd1-d6.
- T32 QGD Bg5/IQP: ...Nbd7, ...dxc4/...c5/...cxd4, ...b6/Bb7/Rc8 developed smoothly. ...Nxf6 preserved pawns; ...Nd5 challenged Ne5/blockaded d4. Nxd5 Bxd5 retained e6; the next bishop exchange centralized Qd5. Playable, not a forced win: Nc4?? supplied the piece.

## Opponents
- Sonnet exploits blocked recaptures: ...Rxa1 won R in T31/T32; T32 also used ...Bxd5 against the e-file screen and ...Rxe8 against unsupported checks. T33 correctly answered Bxh6 with ...Qg6, but later left Bd6 undefended. Expect legal captures; exploit gifts only after verifying them.
- Sonnet spends heavily on consolidation and retreating pieces. T33 finished under four minutes versus my over seven; T32 still converted and mated despite trailing on time. Clock advantage needs sound material; flags/forfeits are not a strategy.
- DeepSeek overlooks capture chains and opened rays when retreating knights or kicking rooks. T32 Nc4/b3 supplied opportunities; verify exchanges rather than expecting gifts. Long routine thinks did not prevent them.
- SF punishes loose pieces, king screens, checking forks and advancing passers. T33 took f5 as soon as my king blocked its guard, then stripped queenside pawns. T32 ...Rh5/...Qc8 exploited an exposed king. Accept available repetition without calling it a fortress.

## Note files
- notes/accelerated-dragon.md - Pawn storms, discoveries and queen safety after checks.
- notes/berlin-endgame.md - D-file and clearance.
- notes/caro-kann-advance.md - Breaks and queenless mate.
- notes/deepseek.md - Classical Caro, d-file tactics and conversion.
- notes/four-knights.md - King screens, exchange offers and promotion checks.
- notes/qgd-exchange.md - IQP blockades, capture chains, clearance and mate.
- notes/ruy-lopez.md - A-file guards, bishop screens and passer blockades.
- notes/sicilian-maroczy.md - Exchanges, king screens and passers.
