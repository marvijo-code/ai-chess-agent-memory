# Chess memory

## Move discipline
- Apply warnings BEFORE choosing. Every candidate needs its own forcing scan; rejecting one blunder does not validate another. Recognition without execution repeatedly loses material.
- Start with the enemy's last move: changed attacks, pawn controls, opened lines and abandoned guards. Scan checks, captures, forks, promotions and quiet mates; repeat on the proposed final board and after every recapture.
- PAWN DIAGONALS FIRST, then EVERY knight and complete sliding rays. Rb3 axb3, Qe4 dxe4, Qd5 exd5, Ng5 hxg5 and Qxe6 fxe6 lost material. Nb3 attacked Rc5 but c4xb3 took N. Support and tempo do not prevent a cheaper capture.
- Count LEGAL defenders through their full paths, excluding the mover itself. Qa5 pinned Nc3 to Ke1 through b4/c3/d2, so Be3 did not defend e4 against Nxe4. Nf3 does NOT attack e4; Nc3 does NOT attack d4.
- PINNED PAWN RECAPTURE: Ka1/b2 behind Bg7-f6-e5-d4-c3. Qa3 was nominally guarded by b2, but Qxa3# could not meet bxa3 because that exposed Bg7-a1. Check king pins before counting a blocker's guard.
- Audit OWN screens and abandoned guards. Nd2 blocks Qd1-d3; Be3 blocks Re1-e4; f7 blocks Rf8-f2. Trace the eventual recapturer's departure as well as its landing square.
- SCREEN BECOMES TARGET: O-O-O/Rhe1 left Nc3 screening Qa5-e1 and Rd1 guarding Re1. Nxd5 removed the screen; Bd3/Bxd3/Rxd3 moved Re1's LAST guard, allowing Qxe1+. Development did not cure the ray.
- PAWN BREAKS: place the enemy capture first. f4 exf4 forked Be3/Ng3 AND opened Qd6-e5-f4; Bxf4 Qxf4 lost B. f6/exf6 exposed Be6 to Qe2; f2-f3 abandoned Be3. Recount every affected guard.
- E-FILE CLEARANCE: e4 screened Re1-e6. Ke7 abandoned Kf6's guard of Re6 AND blocked Re8-e6. exf5 attacked Re6/g6 and opened the rook file. Releasing a pin is insufficient; king moves can obstruct friendly rays.
- For every check test Kxchecker and ALL other captures. Qh2+/Rh7+/Qxb2+ lost heavy pieces to kings. Qe8+ Rxe8 overlooked Re6-e8 and e4 blocking Re1's support. Name the actual defender.
- UNCASTLED DRAGON: h5 vacates h7, opening Rh8-h6. Bh6 Bxh6 attacks Qd2 through g5/f4/e3; Qxh6 loses Q to Rxh6. T35 repeated the stored failure. Verify the ENTIRE exchange before Bh6, including castling status.
- OPEN A-FILE: axb5 axb5 opens Ra8-a1. Bc1/Bb1 blocked rook recaptures; queen retreats then lost Ra1. Rxa8 resolved contact. Ra1/Rf1 defend each other only when b1-e1 are empty.
- Calculate through the LAST recapture and recount the WHOLE board. Nc4 Qxc4 Qxc4 Rxc4 lost N despite its queen guard. Qxc1 Bxc1 Rxc1 Qxc1 costs Q+R for R+B. Equal trades preserve the earlier deficit.
- An attacked piece need not retreat. b3 attacked Rc4 but opened Bf6-a1: Bxa1 bxc4 Bc3 retained my extra B with tempo on Re1. Rdb1 attacked Bb2, but Bxa1 took R. Nh5 attacked Qg3, but Bf3xh5 removed N. Scan captures by OTHER pieces.
- Refresh pins when endpoints move. Nd4 Nxd4 cxd4 opens Rxd8+ against Qd8. Kb1 released Rd2; Kf1 released Nd2's pin to Ra2. A pinned rook can capture its pinning queen.
- Before forks/trades test captures and checking intermezzos. Nc3+ Qxc3 Rxd1 Rxd1 lost N; Bxd5 allowed Nd3+ before Qxd5. Dragon Nc7 ignored Qd8's attack on Qg8: a fork did not answer my queen's danger.
- Trace vacated rays to their far endpoints. Pawn exchanges and e5 uncovered Bf3-a8. Nf5 blocked Bf4-d6; exf5 screens Bc2-h7, while f6 clears it. Rc5 abandoned Rc8's guard of Rd8; Rc7 then screened Bb6-d8, allowing Kxd8.
- Trace checking rays BEYOND the king. Kb3 screened Rb1-b7; Ka4 allowed Rxb7. Ke5 allowed Bc3+ skewering g7 beyond K. A checking block must survive the next capture.
- MATE FIRST, including quiet moves and queenless positions. Nxf4 attacked Qh5 but allowed Qxh7#; Rxe7 ignored Rh1#. exf6 can capture N/B AND support Qxg7#; a remote rook capture does not answer it. Luft solves only the mate its flight prevents.
- MATING SCREEN: Qg3/Bd4 with f6 clear made Ne5 responsible for blocking g7. Nd5 exploited that duty; Bxe5 removed the screen AND retained g7 support. With Nf6 still blocking the battery, Qg3 alone does not establish mate.
- LONG-CASTLED KING: central exchanges emptied the c-file around Kc1. Qxe1+ Rd1 tied R down; Rfc8+ captured successive blockers. Ra5+ sacrificed R to open Qa4+: accepting material requires a fresh mate scan.
- CHECKING PAWN FORK: T36 Ke5/Bc5 faced d4+, attacking K AND B. Kd5 dxc5 Kxc5 recovered only P for B. Inspect the checking pawn's other diagonal before choosing a king reply; test saving the bishop by answering the check with a piece capture. No verified replacement supplied.
- DISCOVERED CHECK BREAKS RECAPTURES: T36 Bc3/Rd4 faced Ke5 and my Rg4/Rg8. Rxg4+ vacated d4, opening Bc3-d4-e5; Rg8xg4 could not answer the bishop check. A king move then allowed Rxg8. Before offering a rook trade, move the enemy capturer on the board and inspect the ray it VACATES. Rear-rook support alone is insufficient.
- Validate destination and full path before submission. After ONE rejected move reconstruct the board and choose a verified legal move; three invalid replies forfeit. Recovery still needs a capture scan. Opening memories apply only to matching positions.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below five minutes cap 15; below 90 seconds use 1-3. Budget from the starting clock, especially Armageddon White's ten minutes.
- Name a target/break before shuffling and calculate its forcing reply. Spend critical time on changed guards, checking forks and concrete races. Long thought is not evidence that a move passed the scan.
- Verified recaptures/cycles need 1-5 seconds unless checks, pawn moves or changed rays alter them. Rxd3 moved Re1's last guard: a familiar recapture can need critical time.
- T36 SF: no invalid moves, finished 6:59. Kd5 took 56 seconds and missed the pawn fork; Rcg6 took 58, Rg4 31 and missed discovered check. Book 4-9 seconds worked. T36 Sonnet quiet moves used 56-58 seconds; routine moves still used 18-34 below five minutes. Enforce caps.
- Ahead: remove counterplay, simplify safely and preserve mating material. Before heavy-piece trades list cheaper capturers, legal recapturers and abandoned guards. Rf4 Bd2xf4 lost the exchange despite Bxf4. Shorten verified forcing conversion.
- Material comes from the board, not comments. T36 SF after Kxc5 I was a B down with one extra pawn, not merely behind in pawn structure. The g-passer supplied counterplay, not material equality. T36 Sonnet's claims also miscounted R+N versus B.
- Supported passers can force useful exchanges without promoting. Qc7 Qxc7 dxc7 retained the passer; Bxc7 would remove it. Rxb6 axb6 won the exchange. Removing Rc8/Bc8 later left R+N versus B despite losing both passers. Count final material before choosing the recapture.
- Use an extra minor to remove a passer's blockader while retaining the advantage. Nxb7 exchanged N for B; Bf5/Bxd7 removed Nd7, leaving R+B versus R and a supported d-pawn.
- Supported passers tie down defenders while K invades. Kd4 screened Rd1-d6; Kc5 cleared it. Kc6 guarded d6, freeing Bg5+. Re8+ Rd8 Rxd8# used Bg5's support. Calculate checks before entering beside a blockader.
- R+N versus B: Ra8 pinned Bd8 to Ke8; f6 allowed Nxf6+ because B could not recapture. Keep N safe, advance K and stop the a-passer before collecting central pawns. Nf6/Bxf6/Kxf6 removed the last bishop into a won rook ending; a flag did not demonstrate final mate.
- Central breaks can create passers with tempo. Ne4/Nxe4/dxe4 left two bishops versus N; Bb7 guarded e4. e3 cleared Bb7-h1 and hit Nd2; e2 hit Nf1. Calculate successive advances before assigning a blockade.
- Stop advanced counterplay before remote raids. Re8 blockaded e6, bxc5 removed another advanced pawn, Rxe7 stopped promotion. Threats against g3 did not stop connected queenside passers.
- B+P: preserve the LAST pawn with king support before sending B to a remote passer. Bd8 alone guarded a5; Bxg5 let Ka4 approach while h6-h7 tied B to h8. A bishop alone cannot mate.
- Escort passers; scan straight AND capture-promotions two advances ahead. c2 attacks b1/d1. a2 outran Kxa3. Promotion can DISCOVER check: b8=Q+ uncovered Ra7-d7, making Rxb8 illegal; d8=Q+ uncovered Ra7-g7. Answer all final-board checks.
- King activity needs legal targets, arrival times and an escape map. Ke4 hit d4, but Kc5 guarded it; Ke6 attacked d7, not d8. Include en passant before an adjacent two-square pawn push: b5 allowed a5xb6 and an outside passer.
- Verify mating support, legal blocks, flights and stalemate. Kxh6 abandoned Bf6. Bf6# used Re7/Ph7; Qh1# used Bb7's cleared diagonal. Rb1+ forced Bf1; Bh3 supported Rxf1#, and the pinned bishop could not take Bh3.

## White openings
- Scheveningen/Classical Sicilian: Be2/O-O/Be3/f4/Kh1, then a4/Bf3/Qe1-g3 suits me. Against GLM, b5/Qb6 lost Nc6; central clearance exposed Ra8. Distinguish Dragon/Maroczy; wins depended on errors.
- DeepSeek battery: Bxd4 after Nxd4 kept B active. With f6 clear, Qg3/Bxe5 enabled mate; Nf6 blocks it. Qb6 can lose Q to Bxb6. e5/dxe5/fxe5 opened Rd1 and hit Nf6; Nh5 lost N to Bxh5; Bf6 exf6 supported mate. No forced opening edge established.
- Maroczy Qa5 BEFORE f3: Be3 lost e4 because Nc3 was pinned. Nxc6/dxc6/Qd4/Nf6 did not recover it. Do not import the later f3/Qxd4 setup; no verified replacement supplied.
- Maroczy long castling: Qh4 lost time to h5. O-O-O/Rhe1 put K/R behind lines central exchanges could clear; Bd3/Bxd3/Rxd3 abandoned Re1. With f3/Qxd4, Ng4 hits Be3 AND uncovers Bg7 against Qd4. Rfd1 allowed Bxc4 Bxc4 Rxc4, losing P; Nd5 cleared the route to Rc1.
- Long-castled Dragon: Bc4/f3/Be3/Qd2/O-O-O against h5/Nc4 and Bxc4 bxc4. g4 repeatedly traded my f/g/h pawns for Black's h-pawn. h4 avoided that liquidation, but Bh6 repeated the uncastled Rh8-h6 trap. Near equal before Bh6; no verified replacement supplied.
- Short-castled Dragon: Bb3/Nxe3/fxe3 conceded bishop pair. Bg4 attacked Qe2 through f3; Nf3 blocked it. Nxf3+ needed gxf3, Bh3 needed Rfe1, Bxc3 needed bxc3. Qh4/Rd3 enabled Rc5-h5; Qxa5 ignored Qg4+ and the mating attack. An offered trade has no effect until accepted.
- Sonnet Zaitsev: Nb4/c5/d5/Nd7 differs from Nb8. Nxe5 against Ne5 retains Qd1's d5 guard. g6/Qd6 stopped Nf5 and guarded f4 after exf4. Do NOT repeat f4 with Be3/Ng3 there.
- T36 Zaitsev: h4-h5 induced g5, freeing Nf5 with tempo on Qd6. My g4/f3 were mistakes; Bc2/Rad1 inaccurate. Bc2 allowed Nb4 to trade for my light bishop. Supported d6 and the queen trade worked, but the flag does not certify the pawn storm. No verified replacements supplied.
- Ruy guard losses: Qxf3 abandoned d5; exd5 could expose Rxe1+ with Bb1/Bc1 blocking Ra1's recapture. Bf4 allowed Bxe4 with tempo on Qf3; e4 screened Bc6-f3 AND guarded Nf5. Qxe4 meets Rxe4. Qg6 interposition can release g7's pin after Bxh6.
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and hits Nf6. Nd7 allows Qxd7 Qxd7 Rxd7, winning N; Bf6 exf6 wins B for P. Bc3 clears d2; Be1 guards Ng3 through f2.
- Chigorin: Nf1 restores Qd1-d4; Qf3 abandons b3. Qe3/Ng4 allowed Nxg4/hxg4/Bxg4, losing h-pawn and hitting Rd1. Nb8 branch d5/Bc2 lost P; do not condemn d5 in every branch. f6 hits Re7 AND opens Bc2-h7; compare fxe7 and mate before automatic Qxf4 after Nxf4.
- Ruy d3: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. Qd3/Bb1 threatens Qh7#, answered by g6. Before g3/h4 calculate f5/fxe4 and queen entry. SF's e4 displaced Nf3 and Ne5-d3-f4 invaded; f3 needs checking-fork calculation.
- Ruy Bg4/Qe2/Nc6: h3 Nd4 hits Qe2/Bb3/Nf3; Qe3 Bxf3 Qxf3 loses Q. c4 Bc2 Nxc2 forks heavy pieces. Ba7/exd4 makes cxd4 open Ba7-d4; e5 Nxe5 is supported by d6. Rxe5 needs Qf6+ calculation.

## Black openings
- English vs GLM: e5/Nf6/Nc6/d5/cxd5/Nxd5, then Nb6/Be7/O-O/Be6/Qd7/Rad8 gave active development. White's c-pawn was gone: not a Maroczy. Nxd5 had Be6 covering exd5; GLM omitted the recapture, then Qe3 lost Q to d4xe3. No forced opening edge established.
- Castled Four Knights: Nd5 Nxd5 exd5 e4 dxc6 exf3 Qxf3 dxc6 exchanges both knights and e-pawns; material equal. Qd4/Bg4/Bd6 and queen exchanges repeatedly reached near equality. Distinguish Nd5 before castling; later losses do not refute the opening.
- Four Knights Qxe3/fxe3: Rae8/Be6/Rxe6 remains playable. T36 Rfe8/f5/g6/c5 reached near equality through the kingside exchanges. The loss came from Ke5/d4+ and Kd5 losing Bc5, then Rg4's failed recapture. No verified replacement supplied for Kd5; do not turn a tactical loss into an opening ban.
- Four Knights defenders differ by board: T33 Kf7 blocked Rf8-f5; T35 rooks on e6/e8 did not guard f5, so c5 ignored Rxf5+. Ke5 allowed Bc3+ skewering g7; queenside king raids led to Ra1#. T36 d4+ forked Ke5/Bc5. Centralization requires enemy bishop rays AND checking pawn pushes.
- Chigorin vs Sonnet: Na5/c5/Qc7, cxd4/cxd4/Nc6, then a5-a4/Bd7/Rfc8. Bb1 can clear Rc1-c6-c7, pinning Nc6 to Qc7; routine Rfe8 ignored d5 winning N. Resolve that pin first. Nb4 was adverse despite winning; Bd3 hung B because Nd2 blocked Qd1-d3.
- Classical Caro: h6/Bh7/Nd7/Bxd3/e6/Ngf6/Be7/O-O. Against O-O/c4/Rfe1, c5 d5 was adverse. Long-castling Nxe5/dxe5/Nd5 also lacked validation. Gifts certify neither setup.
- Ruy d3 vs Sonnet: Re8/Bb7/Bf8, central d5 exchange, then f5/Qd7/g6. Nxe3: Qxe3 permits f4 forking Q/Ng3, but fxe3 avoids it. Move Q off Rd1's file BEFORE e4 dxe4. Be7 can block Re8's defense of e5; recount exchanges instead of assuming a knight gain.
- SF Ruy 6.d4: exd4/Nd5/Nxd4, then Nb6/Nxa4 and d6/Bxd6/Be6 reached near equality. Against Rad1/Bxd6, cxd6 retained d6; Qe7 lost it. Qb6 dxe5 uncovers Be3-b6. Queens-on Berlin Be7/Rd1 requires solving the open d-file.
- Advance Caro: f6 Nf4/Qd6 exd6 repeatedly loses Q. Earlier f6 BEFORE cxd4 worked with c3 screening Qb3-d3 and Nd2 blocking Rd1-d3; this validates neither later exchanges nor queenless f6/Rxf6/Ne5. In the queenless branch, dxe5 cleared Be3-b6 while hitting Rf6.
- QGD: Bxf3 Qxf3 removes Nf3 and Qd1's d4 guard, permitting Nxd4 with tempo. Nb4 cleared Rc8-c4 AND Bb7-f3: Qe2 Bxf3 Qxf3 abandoned c4; gxf3 retains its guard. Bd6 lost B because d4 blocked Rd1-d6.
- QGD Bg5/IQP: Nbd7, dxc4/c5/cxd4, b6/Bb7/Rc8 developed smoothly. Nxf6 preserved pawns; Nd5 blockaded d4; Nxd5 Bxd5 retained e6. Nc4 supplied the piece. h6/Qc7/Rfd8 were adverse despite winning.

## Opponents
- GLM 5.3 Flash: English g3/d3/e4 after exchanging c4; missed a recapture after an illegal attempt, then Qe3 walked onto d4's capture diagonal. Attacks and remote rook raids can ignore stronger captures or mate. As Black hangs pieces in the Scheveningen. Verify independently.
- Sonnet: Zaitsev g6/Qd6 adapted to Nf5 and exf4 won Be3. Exploits blocked recaptures and pawn forks, but after queen trades can hang defenders or miscount material. T36 spent repeated 50-63-second thinks on bishop shuffles and flagged in a lost rook ending. Maintain concrete passer pressure and my own clock caps; never depend on a flag.
- DeepSeek overlooks capture chains, undefended developed pieces and opened rays. Qg3/Bd4 mates only when f6 is clear; Qb6 can land on Bd4's diagonal. T36 Italian Bf4 hung B and Qxb2 lost Q to Qf6's clear diagonal. Speed and illegal attempts vary; verify actual defenses rather than expecting gifts.
- SF punishes pinned guards, pawn-hit pieces, king screens and passers. T36 used d4+ to fork K/B, then Bc3/Rd4 discovered check to break my rook recapture. Read quiet bishop moves as changes to exchange legality. Sometimes repeats far ahead, but converts when passers advance: no guaranteed rescue.

## Note files
- notes/accelerated-dragon.md - Uncastled h-rook trap, pawn captures, pinned blocks and king exposure.
- notes/berlin-endgame.md - D-file and clearance.
- notes/caro-kann-advance.md - Breaks and queenless mate.
- notes/deepseek.md - Italian/Classical Caro, capture chains and conversion.
- notes/four-knights.md - E-file clearance, king screens, pawn races and repetition.
- notes/qgd-exchange.md - IQP blockades, capture chains, clearance and mate.
- notes/ruy-lopez.md - Pawn forks, blocked defenders, conversion and passer support.
- notes/sicilian-maroczy.md - Pinned guards, rook-defense clearance, mating screens and passers.
