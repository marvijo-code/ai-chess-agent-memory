# Chess memory

## Move discipline
- Apply warnings BEFORE choosing. Each candidate needs its own forcing scan; rejecting one blunder does not validate another. Recognition without execution repeatedly loses material.
- Start with the enemy's last move: changed attacks, pawn controls, opened lines and abandoned guards. Scan checks, captures, forks, promotions and quiet mates; repeat on the proposed final board and after every recapture.
- PAWN DIAGONALS FIRST, then knight jumps and complete sliding rays. Rb3?? axb3, Qe4?? dxe4, Qd5?? exd5, Ng5? hxg5 and Qxe6?? fxe6 lost material. T35 Nb3 attacked Rc5 but c4xb3 took N. Support and tempo do not prevent a cheaper capture.
- Count LEGAL defenders and name their full paths. Maroczy ...Qa5 pins Nc3 to Ke1 through b4/c3/d2: Be3? did not defend e4 against ...Nxe4. Nf3 does NOT attack e4; Nc3 does NOT attack d4. A capturer does not guard its own landing square.
- PINNED PAWN RECAPTURE: T35 Ka1/b2 faced Bg7 through f6/e5/d4/c3. After ...Ra5+ bxa5 Qa4+, Qa3 was nominally guarded by b2, but ...Qxa3# could not meet bxa3: that exposes Bg7-a1. Check the pawn's king pin before counting a blocking piece's guard.
- Audit screens and the moved piece's abandoned guards. Nd2 blocks Qd1-d3; Be3 blocks Re1-e4; f7 blocks Rf8-f2. An offered trade is a gift unless the eventual recapture works on the actual board.
- SCREEN BECOMES TARGET: after O-O-O/Rhe1, Nc3 screened Qa5-e1. Nxd5 removed it; Rd1 still guarded Re1. Bd3/Bxd3/Rxd3 moved its LAST guard, allowing ...Qxe1+. Inspect the recapture's departure as well as its landing square.
- PAWN BREAKS: place the enemy capture first. f4?? exf4 forked Be3/Ng3 AND opened Qd6-e5-f4; Bxf4 Qxf4 lost B. ...f6/exf6 exposed Be6 to Qe2; f2-f3 abandoned Be3. Recount every affected guard.
- E-FILE CLEARANCE: e4 screened Re1-e6. ...Ke7?? abandoned Kf6's guard of Re6 AND blocked Re8-e6. exf5! attacked Re6/g6 and opened the rook file. Releasing a pin is insufficient.
- For every check test Kxchecker and ALL other captures. Qh2+/Rh7+/Qxb2+ lost heavy pieces to kings. Qe8+?? Rxe8 overlooked Re6-e8 and e4 blocking Re1's support. Name the actual defender.
- UNCASTLED DRAGON: ...h5 vacates h7, opening Rh8-h6. Bh6?? Bxh6 attacks Qd2 along h6-g5-f4-e3-d2, while Qxh6 loses Q to ...Rxh6. T35 repeated T16's stored failure; retreating Q saves it but forfeits B. Verify the entire exchange BEFORE Bh6, including Black's castling status.
- KING AS SCREEN: ...Kf7? blocked Rf8-f5; ...Kd4 blocked Bc3-h8 and allowed promotion. Trace friendly rays the king obstructs, guards it abandons and enemy checks from its destination.
- OPEN A-FILE: axb5 axb5 opens Ra8-a1. Bc1/Bb1 blocked rook recaptures; queen retreats then lost Ra1. Rxa8 resolved contact. Ra1/Rf1 defend each other only when b1-e1 are empty.
- Calculate through the LAST recapture and recount material. Nc4?? Qxc4 Qxc4 Rxc4 lost N despite its queen guard. Qxc1 Bxc1 Rxc1 Qxc1 costs Q+R for R+B. Equal trades preserve the earlier surplus or deficit.
- An attacked piece need not retreat. b3 attacked Rc4 but opened Bf6-a1: ...Bxa1! bxc4 Bc3 retained my extra B with tempo on Re1. T35 Rdb1 attacked Bb2, but ...Bxa1 took a rook. Scan forcing captures by OTHER pieces.
- Refresh pins when endpoints move. ...Nd4 Nxd4 cxd4 opens Rxd8+ against Qd8. Kb1 released Rd2; Kf1 released Nd2's pin to Ra2. A pinned rook can capture its pinning queen.
- Before forks/trades test captures and checking intermezzos. ...Nc3+ Qxc3 Rxd1 Rxd1 lost N; Bxd5 allowed ...Nd3+ before ...Qxd5. Dragon Nc7?? ignored Qd8's attack on Qg8: a fork did not answer my queen's danger.
- Trace vacated rays to their far endpoints, including OWN screens. ...b5/c6 exchanges and e5 uncovered Bf3-a8. Nf5 blocked Bf4-d6; exf5 screens Bc2-h7, while f6 clears it. ...dxe5 did not answer Bxa8.
- SELF-BLOCKED DEFENDER: ...Rc5 removed Rc8's guard of Rd8; ...Rc7 then screened Bb6-c7-d8. Kxd8! won R despite d7's pin. Recheck full defender rays after every opposing move.
- Trace checking rays BEYOND the king. Kb3 screened Rb1-b7; Ka4? allowed ...Rxb7. Examine legal blocks before exposing a rear piece; a block must survive the next capture.
- MATE FIRST, including quiet moves and queenless positions. ...Nxf4 attacked Qh5 but allowed Qxh7#; Rxe7 ignored ...Rh1#. Luft solves only the mate its flight prevents. exf6 can capture N AND support Qxg7#.
- MATING SCREEN: Qg3/Bd4 with f6 clear made Ne5 responsible for blocking g7. Nd5 attacked other units while Ne5 could not leave; Bxe5 removed the screen AND retained g7 support. A pawn guard does not remove a screen's mating duty.
- LONG-CASTLED KING: central exchanges emptied the c-file around Kc1. ...Qxe1+ Rd1 tied the rook down; ...Rfc8+ captured successive blockers. T35 ...Ra5+ sacrificed R to open ...Qa4+: accepting material still requires a fresh mate scan.
- Validate destination and full path before submission. After ONE rejected move reconstruct the board and choose a verified legal move; three invalid replies forfeit. Recovery still needs a capture scan. Opening memories apply only to matching positions.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3. Budget from the starting clock, especially Armageddon White's ten minutes.
- Name a target/break before shuffling and calculate its forcing reply. Long thinks missed f4's pawn fork, Ke7's clearance and Nb3's pawn capture. Spend critical time on changed guards and concrete races, not general activity.
- Verified recaptures/cycles need 1-5 seconds unless checks, pawn moves or changed rays alter them. T34 Rxd3 moved the last guard of Re1: a familiar recapture can need critical time.
- T35 White finished 3:13, no invalid moves. Nb3 took 74 seconds and still lost N to c4; late moves took 40-45 seconds below five minutes. Enforce the cap and scan pawn captures first. Clock shortage did not cause Bh6 at 14:53.
- Ahead: remove counterplay, simplify safely and preserve mating material. Before heavy-piece trades list cheaper capturers, legal recapturers and abandoned guards. ...Rf4?? Bd2xf4 lost the exchange despite Bxf4. Shorten verified forcing conversion.
- Recount the WHOLE board after exchanges. Four Knights ...Kxg7 left White b/c/d/g versus my a/c/c. Capturing a passer did not equalize; doubled pawns differ from separated pawns. Worse: seek safe activity/repetition without assuming gifts.
- Use an extra minor to remove a passer's blockader while retaining the advantage. Nxb7 exchanged N for B; Bf5/Bxd7 removed Nd7, leaving R+B versus R and a supported d-pawn.
- Supported passers tie down defenders while K invades. Kd4 screened Rd1-d6; Kc5 cleared it. Kc6 guarded d6, freeing Bg5+. Re8+ Rd8 Rxd8# used Bg5's support. Calculate checks before entering beside a blockader.
- Central breaks can create passers with tempo. ...Ne4/Nxe4/dxe4 left two bishops versus N; ...Bb7 guarded e4. ...e3 cleared Bb7-h1 and hit Nd2; ...e2 hit Nf1. Calculate successive advances before assigning a blockade.
- Stop advanced counterplay before remote raids. ...Re8 blockaded e6, ...bxc5 removed another advanced pawn, ...Rxe7 stopped promotion. Threats against g3 did not stop connected queenside passers.
- B+P: preserve the LAST pawn with king support before sending B to a remote passer. Bd8 alone guarded a5; ...Bxg5 let Ka4 approach while h6-h7 tied B to h8. A bishop alone cannot mate.
- Escort passers; scan straight AND capture-promotions two advances ahead. c2 attacks b1/d1. Nxd6 removed Ba3, but ...a2! outran Kxa3. Removing a defender helps only if capture/blockade precedes the next advance.
- Promotion can DISCOVER check. b8=Q+ uncovered Ra7-d7, making ...Rxb8 illegal; d8=Q+ uncovered Ra7-g7. A capture/block plan must answer ALL final-board checks.
- King activity needs legal targets and arrival times. ...Ke4 hit d4, but Kc5 guarded it. ...Ke6 attacked d7 but did NOT control d8. Before an adjacent two-square pawn push include en passant: ...b5 allowed a5xb6 and an outside passer.
- Verify mating support, legal blocks, flights and stalemate. ...Kxh6 abandoned Bf6. Bf6# used Re7/Ph7; Qh1# used Bb7's cleared diagonal. ...Rb1+ forced Bf1; ...Bh3 supported ...Rxf1#, and the pinned bishop could not take Bh3.

## White openings
- Scheveningen/Classical Sicilian: Be2/O-O/Be3/f4/Kh1, then a4/Bf3/Qe1-g3 suits me. Against GLM, ...b5? and ...Qb6? lost Nc6; central clearance exposed Ra8. Distinguish Dragon/Maroczy; wins depended on errors.
- DeepSeek T34: Bxd4 after ...Nxd4 kept the bishop-queen battery. ...Bc6/...Nd7 left f6 clear; Qg3 threatened mate. ...e5/fxe5/...Nxe5 created a mating screen; Nd5 exploited its duty and Bxe5 retained the battery. No forced opening win established.
- Maroczy ...Qa5 BEFORE f3: Be3? lost e4 because Nc3 was pinned. Nxc6/dxc6/Qd4/Nf6 did not recover it. Do not import the later f3/Qxd4 setup; no verified replacement supplied.
- T34 Qh4?! lost time to ...h5. O-O-O/Rhe1 put K/R behind lines central exchanges could clear; Bd3/Bxd3/Rxd3 abandoned Re1. The d-pawn and developed rooks did not compensate for king/rook exposure.
- Maroczy f3/Qxd4: before O-O?! calculate ...Ng4 hitting Be3 AND uncovering Bg7 against Qd4. Qd2/Qxe3 conceded the bishop pair. Rfd1?! allowed Bxc4 Bxc4 Rxc4, losing P; Nd5 cleared the route to Rc1.
- Long-castled Dragon: Bc4/f3/Be3/Qd2/O-O-O against ...h5/...Nc4 and Bxc4 bxc4. g4?! repeatedly traded my f/g/h pawns for Black's h-pawn. T35 h4 avoided that liquidation, but Bh6?? repeated the uncastled Rh8-h6 trap. No verified move-14 replacement supplied; the opening was near equal before Bh6.
- Short-castled Dragon: Bb3?!/...Nxe3/fxe3 retained material but conceded bishop pair. ...Bg4 attacked Qe2 through f3; Nf3 blocked it. ...Nxf3+ needed gxf3, ...Bh3 needed Rfe1, ...Bxc3 needed bxc3. Open f/g-files exposed K.
- Dragon Qh4?!/Rd3?! enabled ...Rc5-h5. ...Bc6 invalidated a plan assuming ...dxe5; e4 blocked Re1-e5. Qxa5 ignored ...Qg4+ and the rook/queen mating attack. Offered trades have no effect until accepted.
- Sonnet Zaitsev ...Nb4/...c5/d5/...Nd7 differs from ...Nb8. Nxe5 against ...Ne5 retains Qd1's d5 guard. ...g6/Qd6 stopped Nf5 and guarded f4 after ...exf4. Do NOT repeat f4 with Be3/Ng3 there; no verified replacement.
- Qg4/Qf6/Bxh6? underestimated ...Qg6!: interposition released g7's pin. Be3 saved B and hxg4 completed the exchange. Later ...Bd6? Nxd6 was a gift, not validation of Bxh6.
- Qxf3?! abandoned d5: ...Bxd5 won P because exd5 opened ...Rxe1+ with Bb1/Bc1 blocking Ra1's recapture. Bf4?? allowed ...Bxe4 with tempo on Qf3; e4 screened Bc6-f3 AND guarded Nf5. Qxe4 meets ...Rxe4.
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and hits Nf6. ...Nd7?? allows Qxd7 Qxd7 Rxd7, winning N; ...Bf6 exf6 wins B for P. Bc3 clears d2; Be1 guards Ng3 through f2.
- Chigorin: Nf1 restores Qd1-d4; Qf3 abandons b3. Na5 cannot reach b4. Qe3/Ng4 allowed ...Nxg4/hxg4/...Bxg4, losing h-pawn and hitting Rd1. ...Nb8 branch d5?/Bc2?! lost P; do not condemn d5 in every branch.
- f6 hits Re7 AND opens Bc2-h7. After ...Nxf4 compare fxe7 and king threats before automatic Qxf4. Qxh6+ provoked ...Qh7?? Bxh7: Qh5 guarded Bh7 and Bg7 blocked Re7-h7. Gifts do not prove sacrifices sound.
- Ruy d3: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. Qd3/Bb1 threatens Qh7#, answered by ...g6. Before g3/h4 calculate ...f5/...fxe4 and queen entry. SF's ...e4 displaced Nf3 and ...Ne5-d3-f4 invaded; f3 needs checking-fork calculation.
- Ruy ...Bg4/Qe2/Nc6: h3?! Nd4 hits Qe2/Bb3/Nf3; Qe3 Bxf3 Qxf3 loses Q. ...c4 Bc2? Nxc2 forks heavy pieces. ...Ba7/exd4 makes cxd4 open Ba7-d4; e5?! Nxe5 is supported by d6. Rxe5 needs ...Qf6+ calculation.

## Black openings
- English T35 vs GLM: 1.c4 e5 2.Nc3 Nf6 3.Nf3 Nc6 4.g3 d5 5.cxd5 Nxd5! Then ...Nb6/Be7/O-O/Be6/Qd7/Rad8 gave active development. This is a reversed Sicilian, not a Maroczy with White's c-pawn still present.
- English e4/d3: meet Nd5 with a calculated exchange; Be6 covered exd5. GLM played Rd1? instead of recapturing ...Nxd5, so ...Nf6 saved the extra piece. Qe3?? then lost Q to d4xe3. No forced opening edge established.
- Castled Four Knights: 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6. Equal material; distinguish Nd5 before castling. ...Qd4/Bg4/Bd6 and queen exchanges repeatedly reached near equality. Later losses do not refute the opening.
- Four Knights ...Qxe3/fxe3 differs from exchange on g5. ...Rae8/Be6/Rxe6 remained playable. ...f5/...g5 then ...Kf7? screened Rf8-f5; ...g6 allowed ...Rfe8, but e4 changed the e-file and ...Ke7?? failed anew. Bishop exchanges reached equal R+B endings; ...Rf4 later lost the exchange.
- Chigorin vs Sonnet: ...Na5/...c5/...Qc7, then ...cxd4/cxd4/...Nc6 returned N before ...a5-a4 and ...Bd7/Rfc8. ...Nb4? was adverse despite winning. Bd3?? hung B because Nd2 blocked Qd1-d3.
- Classical Caro: ...h6/Bh7/Nd7/Bxd3/e6/Ngf6/Be7/O-O. Against O-O/c4/Rfe1, ...c5? d5! was adverse. Long-castling ...Nxe5/dxe5/...Nd5 also lacked validation. Gifts do not certify either setup.
- Ruy d3 vs Sonnet: ...Re8/Bb7/Bf8, central ...d5 exchange, then ...f5/...Qd7/g6. ...Nxe3: Qxe3 permits ...f4 forking Q/Ng3, but fxe3 avoids it. Move Q off Rd1's file BEFORE ...e4 dxe4.
- SF Ruy 6.d4: ...exd4/...Nd5/...Nxd4, then ...Nb6/...Nxa4 and ...d6/...Bxd6/...Be6 reached near equality. Against Rad1/Bxd6, ...cxd6 retained d6; ...Qe7 lost it. ...Qb6?? dxe5 uncovers Be3-b6. Queens-on Berlin ...Be7?! Rd1 requires solving the open d-file.
- Advance Caro: ...f6? Nf4!/...Qd6?? exd6 repeatedly loses Q. Earlier ...f6 BEFORE cxd4 worked with c3 screening Qb3-d3 and Nd2 blocking Rd1-d3; this validates neither later exchanges nor queenless ...f6/Rxf6/Ne5.
- QGD: ...Bxf3 Qxf3 removes Nf3 and Qd1's d4 guard, permitting ...Nxd4 with tempo. ...Nb4 cleared Rc8-c4 AND Bb7-f3: Qe2 Bxf3 Qxf3?? abandoned c4; gxf3 retains its guard. Bd6?? lost B because d4 blocked Rd1-d6.
- QGD Bg5/IQP: ...Nbd7, ...dxc4/...c5/...cxd4, ...b6/Bb7/Rc8 developed smoothly. ...Nxf6 preserved pawns; ...Nd5 blockaded d4. Nxd5 Bxd5 retained e6. Playable, not forced: Nc4?? supplied the piece. ...h6?!/...Qc7?!/...Rfd8? were adverse despite winning.

## Opponents
- GLM 5.3 Flash: English g3/d3/e4 after exchanging c4; missed a recapture after an illegal attempt, then Qe3 walked onto d4's capture diagonal. Attacks and remote rook raids can ignore stronger captures or mate. As Black hangs pieces in the Scheveningen. Verify independently; expect no gift.
- Sonnet exploits blocked recaptures and pawn forks; ...g6/Qd6 adapted to Nf5 and ...exf4 won Be3. After queen trades can hang defenders: ...Bd6, ...Rc7 screening Bb6-d8, ...Bxf1 overlooking Kxd6. Pressure passers concretely; ignore its material claims.
- DeepSeek overlooks capture chains and opened rays. ...Nxd4/...Bc6/...Nd7 allowed Qg3/Bd4; ...Qd7/...Bxd5 addressed material while missing renewed mate. Speed varies sharply. Verify actual defenses rather than expecting gifts.
- SF punishes pinned guards, pawn-hit pieces, king screens and passers. T34 ...Qa5/...Nxe4 and ...Qxe1+/...Rfc8+; T35 uncastled Rh8-h6, c4xb3, then rook sacrifice and a pinned b2 recapture. Sometimes repeats far ahead, but T35 converted without repeating: no guaranteed rescue.

## Note files
- notes/accelerated-dragon.md - Uncastled h-rook trap, pawn captures, pinned blocks and king exposure.
- notes/berlin-endgame.md - D-file and clearance.
- notes/caro-kann-advance.md - Breaks and queenless mate.
- notes/deepseek.md - Classical Caro, d-file tactics and conversion.
- notes/four-knights.md - E-file clearance, king screens, pawn races and repetition.
- notes/qgd-exchange.md - IQP blockades, capture chains, clearance and mate.
- notes/ruy-lopez.md - Pawn forks, blocked defenders, conversion and passer support.
- notes/sicilian-maroczy.md - Pinned guards, rook-defense clearance, mating screens and passers.
