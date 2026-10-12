# Chess memory

## Move discipline
- Apply stored warnings BEFORE choosing. Each candidate needs its own forcing scan; rejecting one blunder does not validate another. Recognition without execution repeatedly loses material.
- Start with the enemy's last move: changed attacks, pawn controls, opened lines. Scan checks, captures, forks, promotions and quiet mates; repeat on the proposed final board. Refresh attacks after every capture and king reply.
- PAWN DIAGONALS FIRST, then knight jumps and complete sliding rays. Rb3?? axb3, Qe4?? dxe4, Qd5?? exd5, Ng5? hxg5 and Qxe6?? fxe6 lost material. Support cannot prevent a cheaper capture. T34 ...Qd3?? fell to c2xd3.
- PAWN BREAKS: place the enemy capture before judging activity. T34 f4?? exf4 forked Be3/Ng3 AND opened Qd6-e5-f4; Bxf4 Qxf4 lost B. A planned recapture needs a surviving guard.
- E-FILE CLEARANCE: T34 SF e4 screened Re1-e6. ...Ke7?? abandoned Kf6's guard of Re6 AND screened Re8-e6. exf5! attacked Re6/g6 and opened the rook file. ...Rxe1 Rxe1+ forced further rook liquidation without recovering f5. Releasing a pin is insufficient: inspect the pawn's capture and every changed guard first.
- For every check, test Kxchecker and ALL other captures. Name the defender and trace its legal path. Qh2+/Rh7+/Qxb2+ lost heavy pieces to kings. Qe8+?? Rxe8 overlooked Re6-e8 and e4 blocking Re1's support.
- Name exact defenders, screens and LEGAL recapturers. Nd2 blocks Qd1-d3 and Be3-c1; Be3 blocks Re1-e4; f7 blocks Rf8-f2. An offered trade is a gift unless its recapture works on the actual board.
- KING AS SCREEN: ...Kf7? blocked Rf8-f5; ...Kd4 blocked Bc3-h8 and allowed promotion. Before activating K, trace friendly rays it obstructs, guards it abandons and enemy checks from its destination.
- OPEN A-FILE: axb5 axb5 opens Ra8-a1. Bc1/Bb1 blocked my rook recaptures; queen moves then lost Ra1. Rxa8 resolved contact. T34 Scheveningen Ra1/Rf1 guarded each other through empty b1-e1; that defense is position-specific.
- Calculate through the LAST recapture and recount material. Nc4?? Qxc4 Qxc4 Rxc4 lost N despite its queen guard. Qxc1 Bxc1 Rxc1 Qxc1 costs Q+R for R+B. A capturer does not guard its own landing square.
- An attacked piece need not retreat. b3 attacked Rc4 but opened Bf6-a1: ...Bxa1! bxc4 Bc3 preserved my extra B with tempo on Re1. Scan forcing captures by OTHER pieces and their survival afterward.
- Validate square and full path before submission. After ONE rejected move, reconstruct the board and choose a verified legal move; three invalid replies forfeit. Opening memories apply only to matching positions.
- Trace checking rays BEYOND the king. Kb3 screened Rb1-b7; Ka4? allowed ...Rxb7. Examine legal blocks before exposing a rear piece.
- Count duties AFTER exchanges and guard moves. Re2 Rxe2 Nxe2 removed BOTH e4 guards. ...f6/exf6 exposed Be6 to Qe2; f2-f3 abandoned Be3. A locally equal trade can expose another unit.
- Discovered attacks accompany forks. Dragon ...Ng4 hit Qe3/Bh6 AND opened Bh8-d4 against Nd4; Qxh6 abandoned d4. Search captures of the forking piece and all recaptures before retreating.
- Refresh pins when endpoints move. ...Nd4 Nxd4 cxd4 opens Rxd8+ against Qd8. Kb1 released Rd2; Kf1 released Nd2's pin to Ra2. A pinned rook can capture its pinning queen.
- Before forks/trades, test captures and checking intermezzos. ...Nc3+ Qxc3 Rxd1 Rxd1 lost N; Bxd5 allowed ...Nd3+ before ...Qxd5. Dragon Nc7?? ignored Qd8's attack on Qg8; a fork does not answer an attack on my queen.
- Derive knight attacks from actual squares: Nf3 does NOT attack e4. Nf5 blocked Bf4-d6; trace bishops through OWN pieces before counting attackers.
- Pawn advances can replace screens. exf5 screened Bc2-h7; f6 cleared it. After ...gxf6/...f5, Bxf5 removes the screen; gxf5 replaces it.
- Trace vacated diagonals to their far endpoints. T34 ...b5/c6 exchanges cleared b7/c6; e5 cleared e4, uncovering Bf3-a8. ...dxe5 did not answer Bxa8.
- SELF-BLOCKED DEFENDER: ...Rc5 removed Rc8's guard of Rd8; ...Rc7 then screened Bb6-c7-d8. Kxd8! won R despite d7's pin. A defender may disappear or become blocked on the last move.
- MATE FIRST, including quiet moves and queenless positions. ...Nxf4 attacked Qh5 but allowed Qxh7#; Rxe7 ignored ...Rh1#. Luft solves only the mate its flight prevents. T34 exf6 captured N AND supported Qxg7#.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3. Long thinking never replaces a capture scan.
- Name a target/break before shuffling; calculate its forcing reply. T34 f4 took 44 seconds and missed a pawn fork; ...Ke7 took 56 and missed clearance. Pawn-ending moves took 41-49 seconds without stopping promotion. Spend critical time on changed guards and concrete races.
- Budget from the starting clock, especially Armageddon White's ten minutes. Verified recaptures/cycles need 1-5 seconds unless checks, pawn moves or changed rays alter them. T34 checked-king replies in 8-15 seconds preserved time; routine endgame maneuvering consumed it.
- Before offering a heavy-piece trade, list ALL cheaper capturers. ...Rf4?? met Bd2xf4 through e3; Bxf4 recovered only B, leaving B versus R. Support did not save the exchange.
- Ahead: remove counterplay, simplify safely, preserve mating material. Check guards and entry squares before queen trades. Worse: seek safe activity/repetition; gifts do not validate speculative losses.
- Recount the WHOLE board after exchanges and pawn captures. T34 Four Knights remained a pawn down after ...Kxg7: White b/c/d/g versus my a/c/c. Capturing a passer did not make material equal. Doubled pawns also do not provide the same mobility as separated pawns.
- Equal trades preserve the surplus or deficit. T33 ...Nf4/Bxf4/exf4 retained an extra piece through heavy-piece trades. T34 Sicilian Bxa8/Rxa8 converted my extra minor into an extra rook; Ruy Kxd8/Rxd6 left two rooks versus R+B.
- Use an extra minor to remove a passer's blockader while retaining the advantage. Nxb7 traded N for B; Bf5/Bxd7 removed Nd7, leaving R+B versus R and a supported d-pawn.
- Supported passers tie down defenders while K invades. Kd4 screened Rd1-d6; Kc5 cleared it. Kc6 guarded d6 and exits, freeing Bg5+. Re8+ Rd8 Rxd8# used Bg5's support.
- Active K + supported passer can create chances when worse, but calculate checks before entering the blockade. T34 Ruy e5?! and Ke7?? were adverse despite the comeback; no verified replacements supplied.
- Before promotion, scan escort-king captures. Ra7 guarded d7, freeing Ke7; ...Bxf1 ignored Kxd6 against the rook blockader. Removing R first avoided d8=Q Rxd8.
- Central breaks can create passers with tempo. ...d5/e5/...Ne4/Nxe4/dxe4 left two bishops versus N. ...Bb7 guarded e4; ...e3 cleared Bb7-h1 and hit Nd2, then ...e2 hit Nf1. Calculate successive advances before assigning a blockade.
- Stop advanced counterplay before remote raids. ...Re8 blockaded e6, ...bxc5 removed the other advanced pawn, ...Rxe7 stopped promotion. Threats against g3 did not stop rook raids on connected queenside passers.
- B+P: preserve the LAST pawn with king support before assigning B to a remote passer. Bd8 alone guarded a5; ...Bxg5 let Ka4 approach while h6-h7 tied B to h8. A bishop alone cannot mate.
- Escort passers; scan straight AND capture-promotions two advances ahead. c2 attacks b1/d1. Bc1+ Ka4 Rxa2+ deflected Ka3 from a2's defense.
- Promotion can DISCOVER check. b8=Q+ uncovered Ra7-d7, making ...Rxb8 illegal. d8=Q+ uncovered Ra7-g7; ...Bd7 allowed Rxd7#. A capture/block plan must answer ALL final-board checks.
- Removing a passer's defender helps only if capture/blockade precedes its next advance. Nxd6 removed Ba3's guard, but ...a2! outran Kxa3. T34 ...Ke6 attacked d7 but did NOT control d8; attacking a seventh-rank pawn does not prevent its immediate promotion.
- King activity needs a LEGAL capture target. T34 ...Ke4 hit d4, but Kc5 guarded d4; ...Kd3 did not make it capturable. Calculate king-controlled squares and pawn arrival times rather than calling proximity counterplay.
- Before a two-square pawn push beside an enemy pawn on its fifth rank, include en passant. T34 ...b5 allowed a5xb6 e.p., creating an outside passer and drawing my king away.
- Recount king guards after captures. ...Kxh6 abandoned Bf6 and allowed Rxf6+. Verify mate support, flights and stalemate: Bf6# used Re7/Ph7; Qh1# used Bb7's cleared diagonal and Ne3 vacating f1; Qxg7# used Pf6.

## White openings
- Scheveningen vs GLM: Be2/O-O/Be3/f4/Kh1, then a4/Bf3/Qe1-g3 coordinated well. ...Rcb8/...b5? allowed axb5 attacking Nc6; ...Qb6? ignored bxc6. After c6 exchanges, e5 uncovered Bf3-a8. Win depended on errors; distinguish Dragon/Maroczy.
- Long-castled Dragon: Bc4/f3/Be3/Qd2/O-O-O against ...h5/...Nc4 and Bxc4 bxc4. g4?! repeatedly led to liquidation of my f/g/h pawns for Black's h-pawn. ...Bxg4 ignored attacked Nh5 and hit Rd1 through f3/e2. No verified replacement.
- Short-castled Dragon: 7.Bc4 d6 8.O-O Ng4 9.Bb3?! Nxe3 10.fxe3! retained material but conceded bishop pair. Distinguish long castling and Maroczy; no verified move-9 replacement.
- Dragon ...Bg4 attacked Qe2 through f3; Nf3! blocked it. ...Nxf3+ required gxf3!, ...Bh3 required Rfe1!, ...Bxc3 required bxc3!. Material survived, but open f/g-files exposed my king. Open files serve BOTH sides.
- Qh4?!/Rd3?! let ...Rc5-h5 activate. e5! helped, but ...Bc6! invalidated a plan assuming ...dxe5. e4?! blocked Re1-e5. ...Qc8 opened g4; Qxa5 ignored Qg4+ Kf2 Rxh2+ Kf1 Qg2#. Guarding Rf3 did not answer mate; offered trades have no effect until accepted.
- Sonnet Zaitsev ...h6/Bc2/...exd4/cxd4/...Nb4/Bb1/...c5/d5/...Nd7 differs from ...Nb8. Nxe5 against ...Ne5 retains Qd1's d5 guard; ...dxe5 changes the structure. T34 ...g6/Qd6 stopped Nf5 and guarded f4 after ...exf4. Do NOT repeat f4 with Be3/Ng3 there; no verified replacement.
- Qg4/Qf6/Bxh6? underestimated ...Qg6!: queen interposition released g7's pin. Be3 saved B and hxg4 completed the exchange. A pawn regains its capture when its pin disappears. Later ...Bd6? Nxd6 was a gift, not validation of Bxh6.
- Qxf3?! abandoned Qd1's d5 guard. ...Bxd5 won P: exd5 removes e4's screen and permits ...Rxe1+, with Bb1/Bc1 blocking Ra1's recapture. Rd1 saved R, not P. Audit guards lost by queen recaptures and files opened by pawn recaptures.
- Bf4?? with Qf3/Nf5 allowed ...Bxe4 with tempo: e4 screened Bc6-f3 AND guarded Nf5; Qxe4 meets ...Rxe4. Nf5 blocked Bf4-d6. ...Re6? did not validate Bf4.
- Zaitsev/Breyer a4/...Nb8, d5? and Bc2?! lost P to ...cxd5/exd5/...Bxd5. No verified replacements; do not condemn d5 in every branch.
- Maroczy c4/...g6/...Qa5, f3/Qxd4: before O-O?! calculate ...Ng4 hitting Be3 AND uncovering Bg7 against Qd4. Qd2/Qxe3 preserved pawns but conceded bishop pair. ...Be6/Rfc8 met Rfd1?! Bxc4 Bxc4 Rxc4, losing P; Nd5 cleared the route to Rc1. No verified replacements.
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and hits Nf6. ...Nd7?? allows Qxd7 Qxd7 Rxd7, winning N; ...Bf6 exf6 wins B for P. e5 screens Qc7-f4; Bc3 clears d2 and attacks Qf6; Be1 guards Ng3 through f2.
- Chigorin: Nf1 restores Qd1-d4; Qf3 abandons b3. Na5 cannot reach b4. Nh2/f4/Bxf4 activated B, but Qe3/Ng4 allowed ...Nxg4/hxg4/...Bxg4, losing h-pawn and hitting Rd1. Nf5 Bxf5 exf5 Nxd5 left two pawns down.
- f6 hits Re7 AND opens Bc2-h7. After ...Nxf4 compare fxe7 and king threats before automatic Qxf4; Qxf6+ can meet ...Bg7 with tempo. Qxh6+ provoked ...Qh7?? Bxh7: Qh5 guarded Bh7 and Bg7 blocked Re7-h7. Gifts do not prove sacrifices sound.
- Ruy d3: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. Qd3/Bb1 threatens Qh7#, answered by ...g6. Before g3/h4 calculate ...f5/...fxe4 and queen entry. SF's ...e4 displaced Nf3 and ...Ne5-d3-f4 invaded; a proposed f3 break needs checking-fork calculation.
- Ruy ...Bg4/Qe2/Nc6: h3?! Nd4 hits Qe2/Bb3/Nf3; Qe3 Bxf3 Qxf3 loses Q. ...c4 Bc2? Nxc2 forks Qe3/Ra1/Re1. ...Ba7/exd4 makes cxd4 open Ba7-d4; e5?! Nxe5 is supported by d6. Rxe5 needs ...Qf6+ calculation.

## Black openings
- Castled Four Knights: 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6. Equal material; distinguish Nd5 before castling. ...Qd4/Bg4/Bd6 and queen exchanges repeatedly reached near equality. Later losses do not refute the opening.
- Four Knights ...Qxe3/fxe3 differs from exchange on g5. ...Rae8/Be6/Rxe6 remained playable. T33 ...f5/...g5 then ...Kf7? screened Rf8-f5. T34 ...g6 guarded f5 and allowed ...Rfe8, but e4 changed the entire e-file; ...Ke7?? caused a new failure. No verified replacements supplied.
- Four Knights bishop exchanges ending ...fxe6 left R+B each, equal pawns/open f-file. ...Rf4 later lost the exchange; evaluate the resulting board, not just local trades.
- Chigorin vs Sonnet: ...Na5/...c5/...Qc7, then ...cxd4/cxd4/...Nc6 returned N before ...a5-a4 and ...Bd7/Rfc8. No forced edge. ...Nb4? was adverse despite the win. Bd3?? hung B because Nd2 blocked Qd1-d3; ...Nxd3 won it.
- Classical Caro: ...h6/Bh7/Nd7/Bxd3/e6/Ngf6/Be7/O-O. Against O-O/c4/Rfe1, ...c5? d5! was adverse; gifts do not certify it. Long-castling ...Nxe5/dxe5/...Nd5 also lacked validation.
- Ruy d3 vs Sonnet: ...Re8/Bb7/Bf8, central ...d5 exchange, then ...f5/...Qd7/g6. ...Nxe3: Qxe3 permits ...f4 forking Q/Ng3, but fxe3 avoids it. Move Q off Rd1's file BEFORE ...e4 dxe4. No forced opening win.
- SF Ruy 6.d4: ...exd4/...Nd5/...Nxd4, then ...Nb6/...Nxa4 and ...d6/...Bxd6/...Be6 reached near equality. Against Rad1/Bxd6, ...cxd6 retained d6; ...Qe7 lost it. Chigorin ...Qb6?? dxe5 uncovers Be3-b6. Queens-on Berlin ...Be7?! Rd1 requires solving the open d-file.
- Advance Caro: ...f6? Nf4!/...Qd6?? exd6 repeatedly loses Q. Earlier ...f6 BEFORE cxd4 worked with c3 screening Qb3-d3 and Nd2 blocking Rd1-d3; this validates neither later exchanges nor queenless ...f6/Rxf6/Ne5.
- QGD: ...Bxf3 Qxf3 removes Nf3 and Qd1's d4 guard, permitting ...Nxd4 with tempo; Nc3 does NOT attack d4. Bf4 branch ...Nb4 cleared Rc8-c4 AND Bb7-f3: Qe2 Bxf3 Qxf3?? abandoned c4; ...Rxc4 won B. gxf3 retains Qe2's guard. Bd6?? lost B because d4 blocked Rd1-d6.
- QGD Bg5/IQP: ...Nbd7, ...dxc4/...c5/...cxd4, ...b6/Bb7/Rc8 developed smoothly. ...Nxf6 preserved pawns; ...Nd5 challenged Ne5/blockaded d4. Nxd5 Bxd5 retained e6; the next bishop exchange centralized Qd5. Playable, not a forced win: Nc4?? supplied the piece.

## Opponents
- GLM 5.3 Flash: Scheveningen, fast development, then ...Rfc8-b8/...b5 despite a4. ...Qb6 ignored b5xc6; ...Qd3 ignored c2xd3; ...Rxd3 ignored Qxg7#. Its recapture comments misstated the deficit. Verify captures and total count.
- Sonnet exploits blocked recaptures and pawn forks: ...Rxa1, ...Bxd5, ...Rxe8; T34 ...g6/Qd6 then ...exf4 won Be3. It adapted to my earlier Nf5 attack. After queen trades it can hang defenders: ...Bd6, ...Rc7 screening Bb6-d8, ...Bxf1 overlooking Kxd6. Recompute guards/material independently.
- Sonnet spends heavily on consolidation yet can convert while trailing on time. T34 it let my K/d-pawn advance during 50-72 second thinks; a rejected move cost 103. Pressure passers concretely, but do not rely on flags, gifts or its material claims.
- DeepSeek overlooks capture chains and opened rays when retreating knights or kicking rooks. Nc4/b3 supplied opportunities; verify exchanges rather than expecting gifts. Long routine thinks did not prevent them.
- SF punishes loose pieces, king screens, checking forks and passers. T34 it used e4/exf5/Rxe1+ against my blocked e-file defense. It repeated even after promoting, around +8: keep legal king escapes and accept repetition. This was a lost-position escape, not a fortress or validation of the pawn ending.

## Note files
- notes/accelerated-dragon.md - Pawn storms, discoveries and queen safety after checks.
- notes/berlin-endgame.md - D-file and clearance.
- notes/caro-kann-advance.md - Breaks and queenless mate.
- notes/deepseek.md - Classical Caro, d-file tactics and conversion.
- notes/four-knights.md - E-file clearance, king screens, pawn races and repetition.
- notes/qgd-exchange.md - IQP blockades, capture chains, clearance and mate.
- notes/ruy-lopez.md - Pawn forks, blocked defenders, conversion and passer support.
- notes/sicilian-maroczy.md - Scheveningen clearance, Maroczy exchanges and passer defense.
