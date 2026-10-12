# Chess memory

## Move discipline
- Apply stored warnings BEFORE choosing. Each candidate needs its own forcing scan; rejecting one blunder does not validate another. Recognition without execution repeatedly loses queens and rooks.
- Start with the enemy's last move: changed attacks, pawn controls, opened lines. Scan checks, captures, forks, promotions and quiet mates; repeat on the proposed final board. Refresh attacks after every capture and king reply.
- PAWN DIAGONALS FIRST, then knight jumps and complete sliding rays. Rb3?? axb3, Qe4?? dxe4, Qd5?? exd5, Ng5? hxg5 and Qxe6?? fxe6 lost material. Support cannot prevent a cheaper capture.
- For every check, test Kxchecker and ALL other captures. Name the defender and trace its legal path. Qh2+/Rh7+/Qxb2+ lost heavy pieces to king captures. Qe8+?? Rxe8 overlooked Re6-e8 and my e4 pawn blocking Re1's support.
- Name exact defenders, screens and LEGAL recapturers. Nd2 blocks Qd1-d3 and Be3-c1; Be3 blocks Re1-e4; f7 blocks Rf8-f2. A piece 'offering a trade' is hanging unless its recapture works on the actual board.
- KING AS SCREEN: ...Kf7? blocked Rf8-f5, allowing Rxf5+. ...Kd4 screened Bc3-h8 and allowed promotion. Before activating K, trace every friendly rook/bishop ray it obstructs.
- OPEN A-FILE: axb5 axb5 opens Ra8-a1. Bc1 blocked Re1-a1; Bb1 blocked Rd1-a1. Queen moves then lost Ra1. Rxa8 immediately resolved contact; ...Bxa8 retained Qd8. Inspect the whole recapture path BEFORE opening the file.
- Calculate through the LAST recapture and recount material. Nc4?? Qxc4 Qxc4 Rxc4 lost N despite its queen guard. Qxc1 Bxc1 Rxc1 Qxc1 costs Q+R for R+B. A capturer does not guard its own landing square.
- An attacked piece need not retreat. b3 attacked Rc4 but opened Bf6-a1: ...Bxa1! bxc4 Bc3 preserved my extra B with tempo on Re1. Scan forcing captures by OTHER pieces and their escape afterward.
- Validate the actual piece square and full path before submission. After ONE rejected move, reconstruct the board and choose a verified legal move; three invalid replies forfeit. Opening memories apply only to matching positions.
- Trace checking rays BEYOND the king. Kb3 screened Rb1-b7; Ka4? allowed ...Rxb7. Examine legal blocks before exposing a rear piece.
- Count duties AFTER exchanges and guard moves. Re2 Rxe2 Nxe2 removed BOTH e4 guards, Re1 and Ng3. ...f6/exf6 exposed Be6 to Qe2; f2-f3 abandoned Be3. A locally equal trade can expose another unit.
- Discovered attacks accompany forks. Dragon ...Ng4 hit Qe3/Bh6 AND opened Bh8-d4 against Nd4; Qxh6 abandoned d4. Search captures of the forking piece and all recaptures before retreating automatically.
- Refresh pins when endpoints move. ...Nd4 Nxd4 cxd4 opens Rxd8+ against Qd8. Kb1 released Rd2; Kf1 released Nd2's pin to Ra2. A pinned rook can capture its pinning queen.
- Before forks/trades, test captures and checking intermezzos. ...Nc3+ Qxc3 Rxd1 Rxd1 lost N; Bxd5 allowed ...Nd3+ before ...Qxd5. Dragon Nc7?? ignored Qd8's attack on Qg8; a fork does not answer an attack on my queen.
- Derive knight attacks from actual squares: Nf3 does NOT attack e4. Nf5 blocked Bf4-d6; trace bishops through OWN pieces before counting attackers.
- Pawn advances can replace screens rather than clear a battery. exf5 screened Bc2-h7; f6 cleared it. After ...gxf6/...f5, Bxf5 removes the screen; gxf5 replaces it.
- MATE FIRST, including quiet moves and queenless positions. ...Nxf4 attacked Qh5 but allowed Qxh7#; Rxe7 ignored ...Rh1#. Luft solves only the mate its flight prevents. Test checks and resulting flights before king advances or remote raids.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3. Long thinking never replaces a capture scan.
- Name a target/break before shuffling; calculate the opponent's forcing reply. T33 losses came with ample time after 45-53 second routine moves. Spend time on changed guards, checks and concrete replies, not familiar consolidation.
- Budget from the starting clock, especially Armageddon White's ten minutes. Verified recaptures and cycles need 1-5 seconds unless checks, pawn moves or changed rays alter them. T33 Final captures/promotion mostly took 3-8 seconds; finished 14:12 with no invalid moves.
- Before offering a heavy-piece trade, list ALL cheaper capturers. ...Rf4?? met Bd2xf4 through e3; Bxf4 recovered only B, leaving B versus R. Support did not save the exchange.
- Ahead: remove counterplay, simplify safely, preserve mating material. Check pawn guards and entry squares before queen trades. Equal rook exchanges preserve an extra minor; they do not restore material equality. Worse: seek safe activity/repetition; gifts do not validate speculative losses.
- T33 Final: after winning Bd3, ...Nf4 escaped Nd3 with attacks on Re2/Be3; Bxf4 exf4 retained the extra piece. Queen and both rook-pair exchanges reached B+B+N versus N+N. Maintain the total count through each locally equal exchange.
- Use an extra minor to remove a passer's blockader while preserving the advantage. T33 White Nxd6 won B, Nxb7 traded N for the remaining B, and Bf5/Bxd7 removed Nd7, leaving R+B versus R and a supported d-pawn.
- A supported passer can tie down the enemy while my king invades. Kd4 temporarily screened Rd1-d6; Kc5 cleared it. Kc6 guarded d6 and controlled exits, freeing Bg5+. Re8+ Rd8 Rxd8# used Bg5's protection of d8. Keep escort support while changing rook files.
- Open a bishop ending with a central break. T33 Final ...d5 challenged the center; after e5, ...Ne4 invited an exchange that created an e4 passer. ...Bb7 initially guarded it; ...e3 cleared Bb7-h1 and attacked Nd2, then ...e2 attacked Nf1. Calculate whether successive advances gain tempo before assigning a blockade.
- Stop advanced counterplay before remote raids. ...Re8 blockaded e6, ...bxc5 removed the other advanced pawn, ...Rxe7 stopped promotion. Threats against g3 did not stop Rxc7/Rxb7/Rxc6+/Rxa6; unsupported threats cannot race connected passers.
- B+P: preserve the LAST pawn with king support before assigning B to a remote passer. Bd8 alone guarded a5; ...Bxg5 let Ka4 approach while h6-h7 tied B to h8. A bishop alone cannot mate.
- Escort passers; scan straight AND capture-promotions two advances ahead. c2 attacks b1/d1. Checks can deflect the escort: Ka3 guarded a2, but Bc1+ Ka4 Rxa2+ removed that guard.
- Promotion can DISCOVER a check. b8=Q+ vacated b7 and uncovered Ra7-d7 against Kd7. ...Rxb8 could reach the new queen but did not answer the rook check. A capture plan must answer ALL checks on the final board.
- Removing a passer's defender helps only if capture/blockade precedes its next advance. Nxd6 removed Ba3's guard, but ...a2! outran Kxa3; Nd6 reached neither a2 nor a1. Kc5?? also allowed ...Bf8+ then ...Bd6 to cover c7/b8.
- Recount king guards after captures. ...Kxh6 abandoned Bf6 and allowed Rxf6+. SF's winning repetition was an escape, not a proven fortress.
- Verify mate support, flights and stalemate. Bf6# with Re7/Ph7 uses h7 controlling g8 and Re7 controlling g7/protecting h7. T33 Final Qh1# used Bb7's cleared diagonal; Ne3 had also vacated f1, opening Qe1-h1. Promotion is a new queen position requiring a fresh mate scan.

## White openings
- Long-castled Dragon: Bc4/f3/Be3/Qd2/O-O-O against ...h5/...Nc4 and Bxc4 bxc4. g4?! repeatedly led to ...hxg4, h5 and rook/knight captures consuming my f/g/h pawns for Black's h-pawn. ...Bxg4 ignored attacked Nh5 and hit Rd1 through f3/e2. Calculate the whole liquidation; no verified replacement.
- Short-castled Dragon: 7.Bc4 d6 8.O-O Ng4 9.Bb3?! Nxe3 10.fxe3! retained material but conceded the bishop pair. Distinguish long castling and the Maroczy queen fork; no verified move-9 replacement.
- Dragon ...Bg4 attacked Qe2 through f3; Nf3! blocked it. ...Nxf3+ required gxf3!, ...Bh3 required Rfe1!, ...Bxc3 required bxc3!. Material survived, but open f/g-files exposed my king. Open files are usable by BOTH sides.
- Qh4?!/Rd3?! let ...Rc5-h5 activate. e5! helped, but ...Bc6! invalidated a plan assuming ...dxe5. e4?! blocked Re1-e5. Later ...Qc8 opened g4; Qxa5 ignored Qg4+ Kf2 Rxh2+ Kf1 Qg2#. Guarding Rf3 did not answer mate; an offered queen trade has no effect until accepted.
- Sonnet Zaitsev ...h6/Bc2/...exd4/cxd4/...Nb4/Bb1/...c5/d5/...Nd7 differs from ...Nb8. T33 Nxe5 answered ...Ne5?! before ...Nxf3+; ...dxe5! changed the structure. This avoided T32's Qxf3 branch but establishes no forced edge.
- Qg4/Qf6/Bxh6? underestimated ...Qg6!: queen interposition released g7's pin while offering a queen trade. Be3 saved B and hxg4! completed the exchange. A pinned pawn regains its capture if the opponent can remove the pin.
- Sonnet's ...Bd6? after the queen exchange left B undefended; Nxd6 won it and attacked Re8. This gift did not validate Bxh6. Recount guards after queen trades; earlier Bf8 had defensive duties.
- Qxf3?! abandoned Qd1's d5 guard. ...Bxd5 won P: exd5 removes e4's screen and permits ...Rxe1+, with Bb1/Bc1 blocking Ra1's recapture. Rd1 saved R, not P. Audit guards lost by queen recaptures and files opened by pawn recaptures.
- Bf4?? with Qf3/Nf5 allowed ...Bxe4 with tempo: e4 screened Bc6-f3 AND guarded Nf5; Qxe4 meets ...Rxe4. Nf5 blocked the claimed Bf4-d6 attacker. ...Re6? did not validate Bf4.
- Zaitsev/Breyer a4/...Nb8, d5? and Bc2?! allowed ...cxd5/exd5/...Bxd5, losing P. No verified replacements for moves 13/15; do not condemn d5 in every branch.
- Maroczy c4/...g6/...Qa5, f3/Qxd4: before O-O?! calculate ...Ng4 hitting Be3 AND uncovering Bg7 against Qd4. Qd2/Qxe3 preserved pawns but conceded the bishop pair. ...Be6/Rfc8 met Rfd1?! Bxc4 Bxc4 Rxc4, losing P and attacking Nc3; Nd5 cleared the route to Rc1. No verified replacements.
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and attacks Nf6. ...Nd7?? allows Qxd7 Qxd7 Rxd7, winning N; ...Bf6 exf6 wins B for P. e5 screens Qc7-f4. Bc3 attacks Qf6 and clears d2; Be1 can guard Ng3 through f2. No forced edge.
- Chigorin: Nf1 restores Qd1-d4; Qf3 abandons b3. ...Nb4 requires a knight able to reach b4; Na5 cannot. Nh2/f4/Bxf4 activated B, but Qe3/Ng4 allowed ...Nxg4/hxg4/...Bxg4, losing h-pawn and hitting Rd1. Nf5 Bxf5 exf5 Nxd5 left two pawns down.
- f6 hits Re7 AND opens Bc2-h7. After ...Nxf4 compare fxe7 and king threats before automatic Qxf4; Qxf6+ can meet ...Bg7 with tempo. Qxh6+ provoked ...Qh7?? Bxh7: Qh5 guarded Bh7 and Bg7 blocked Re7-h7. Gifts do not prove sound sacrifices.
- Ruy d3: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. Qd3/Bb1 threatens Qh7#, answered by ...g6. Before g3/h4 calculate ...f5/...fxe4 and queen entry. SF's ...e4 drove Nf3 away and ...Ne5-d3-f4 invaded; a proposed f3 break needs checking-fork calculation.
- Ruy ...Bg4/Qe2/Nc6: h3?! Nd4 hits Qe2/Bb3/Nf3; Qe3 Bxf3 Qxf3 loses Q. ...c4 Bc2? Nxc2 forks Qe3/Ra1/Re1. ...Ba7/exd4 makes cxd4 open Ba7-d4; e5?! Nxe5 is supported by d6. Rxe5 needs ...Qf6+ calculation.

## Black openings
- Castled Four Knights: 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6. Equal material; distinguish Nd5 before castling. ...Qd4/Bg4/Bd6 and queen exchanges reached near-equal middlegames. Later losses do not refute the opening.
- Four Knights ...Qxe3/fxe3 differs from the queen exchange on g5. ...Rae8/Be6/Rxe6 and ...f5/...g5 retained balance until ...Kf7? screened Rf8's f5 guard. Bxf8! recaptured after Rxf8 but did not recover the pawn. No verified move-21 replacement.
- Four Knights ...Rae8/h6/Be6 exchanges ended ...fxe6, R+B each, equal pawns/open f-file. ...Rf4 later lost the exchange. Evaluate resulting positions, not only local trades.
- T33 Final Chigorin vs Sonnet: ...Na5/...c5/...Qc7, then ...cxd4/cxd4/...Nc6 returned the knight before ...a5-a4 and ...Bd7/Rfc8. No forced opening edge. 18...Nb4? was marked a mistake despite the win; no verified replacement. 19.Bd3?? was hanging because Nd2 blocked Qd1-d3; ...Nxd3 won B. The opponent's failed recapture, not the knight raid alone, supplied the piece.
- Classical Caro: ...h6/Bh7/Nd7/Bxd3/e6/Ngf6/Be7/O-O. Against O-O/c4/Rfe1, ...c5? d5! was adverse; gifts do not certify it. Long-castling ...Nxe5/dxe5/...Nd5 also lacked validation.
- Ruy d3 vs Sonnet: ...Re8/Bb7/Bf8, central ...d5 exchange, then ...f5/...Qd7/g6. ...Nxe3: Qxe3 permits ...f4 forking Q/Ng3, but fxe3 avoids it. Move Q off Rd1's file BEFORE ...e4 dxe4. No forced opening win.
- SF Ruy 6.d4: ...exd4/...Nd5/...Nxd4, then ...Nb6/...Nxa4 and ...d6/...Bxd6/...Be6 reached near equality. Against Rad1/Bxd6, ...cxd6 retained d6; ...Qe7 lost it. Chigorin ...Qb6?? dxe5 uncovers Be3-b6. Queens-on Berlin ...Be7?! Rd1 requires solving the open d-file before routine development.
- Advance Caro: ...f6? Nf4!/...Qd6?? exd6 repeatedly loses Q. Earlier ...f6 BEFORE cxd4 worked with c3 screening Qb3-d3 and Nd2 blocking Rd1-d3; this validates neither later exchanges nor queenless ...f6/Rxf6/Ne5.
- QGD: ...Bxf3 Qxf3 removes Nf3 and Qd1's d4 guard, permitting ...Nxd4 with tempo; Nc3 does NOT attack d4. Bf4 branch ...Nb4 cleared Rc8-c4 AND Bb7-f3: Qe2 Bxf3 Qxf3?? abandoned c4; ...Rxc4 won B. gxf3 retains Qe2's guard. Bd6?? lost B because d4 blocked Rd1-d6.
- QGD Bg5/IQP: ...Nbd7, ...dxc4/...c5/...cxd4, ...b6/Bb7/Rc8 developed smoothly. ...Nxf6 preserved pawns; ...Nd5 challenged Ne5/blockaded d4. Nxd5 Bxd5 retained e6; the next bishop exchange centralized Qd5. Playable, not a forced win: Nc4?? supplied the piece.

## Opponents
- Sonnet exploits blocked recaptures: ...Rxa1, ...Bxd5 against the e-file screen, and ...Rxe8 against unsupported checks. It answered Bxh6 with ...Qg6 but later hung Bd6. T33 Final it also overlooked its own Nd2 blocking Qd1-d3 and called equal rook trades material recovery. Verify captures and the total count independently.
- Sonnet spends heavily on consolidation and retreats, yet can convert despite trailing on time. T33 Final Bc2/Re2 took 58/61 seconds without spotting the blocked recapture. Clock advantage needs sound material; flags/forfeits are not a strategy.
- DeepSeek overlooks capture chains and opened rays when retreating knights or kicking rooks. Nc4/b3 supplied opportunities; verify exchanges rather than expecting gifts. Long routine thinks did not prevent them.
- SF punishes loose pieces, king screens, checking forks and advancing passers. It took f5 when my king blocked its guard, then stripped queenside pawns; ...Rh5/...Qc8 exploited my exposed king. Accept available repetition without calling it a fortress.

## Note files
- notes/accelerated-dragon.md - Pawn storms, discoveries and queen safety after checks.
- notes/berlin-endgame.md - D-file and clearance.
- notes/caro-kann-advance.md - Breaks and queenless mate.
- notes/deepseek.md - Classical Caro, d-file tactics and conversion.
- notes/four-knights.md - King screens, exchange offers and promotion checks.
- notes/qgd-exchange.md - IQP blockades, capture chains, clearance and mate.
- notes/ruy-lopez.md - Blocked recaptures, Chigorin conversion and passer support.
- notes/sicilian-maroczy.md - Exchanges, king screens and passers.
