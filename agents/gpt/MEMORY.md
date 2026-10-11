# Chess memory

## Move discipline
- Apply stored warnings BEFORE choosing. Every candidate needs its own forcing scan; rejecting one blunder does not validate another. Repeated ...f6/...Qd6?? exd6 shows recognition alone fails.
- Start with the enemy's last move: changed attacks, pawn controls, opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board. After my check and the king's reply, refresh attacks on the checking piece.
- PAWN DIAGONALS FIRST, then knights and complete sliding rays. Rb3?? axb3, Qe4?? dxe4, Qd5?? exd5, Ng5? hxg5 and Qxe6?? fxe6 lost material. Support cannot prevent a cheaper capturer; an attacking purpose does not establish destination safety.
- Test Kxchecker first and name its actual defender. ...Qh2+?? Kxh2, Rh7+?? Kxh7 and ...Qxb2+?? Kxb2 lost heavy pieces. Check does not establish safety.
- Name exact defenders, screens and LEGAL recapturers. Nd2 blocked Be3-c1, Rc1's sole guard. Be3 blocks Re1-e4; f7 blocks Rf8-f2; Qe3 cannot recapture c2. Audit friendly rays newly blocked as well as enemy rays opened.
- T32 DeepSeek: Qd5 attacked Ne5; Nc4?? landed on BOTH Qd5's diagonal and Rc8's clear file. ...Qxc4! Qxc4 Rxc4 won N while trading queens. A queen may capture a defended minor if its own legal recapturer survives the queen exchange. Calculate the whole chain.
- T32 DeepSeek: b3 attacked Rc4 but vacated b2 on Bf6-e5-d4-c3-b2-a1. ...Bxa1! bxc4 Bc3 saved B with tempo against Re1. Before retreating an attacked rook, scan captures by OTHER pieces and their escape after the rook falls.
- T31 Sonnet SF: axb5 axb5 opened Ra8-a1 while Bc1 blocked Re1-a1. Qc6?? attacked Ra8 but allowed ...Rxa1, then ...Rxe1+ after Bd2. Net loss R. Before opening a file, name legal recaptures on BOTH ends; attacking an invader does not force retreat.
- Validate the actual piece square and full path before submission. After one rejected move, reconstruct the board before retrying; three invalid replies forfeit. A remembered opening move may be impossible on another branch.
- T31 SF: Kb3 screened Rb1-b7. Answering ...Rb1+ with Ka4? opened ...Rxb7; Nxd6 recovered only B for R. Trace a checking rook's line BEYOND the king and examine interpositions.
- T30 Final: Bc3 covered h8 through d4/e5/f6/g7, but ...Kd4 blocked my bishop, allowing h8=Q+. A king is also a screen. Retrace distant defenses after every king move.
- Count duties AFTER the last recapture. Re2?? Rxe2 Nxe2 removed BOTH e4 guards, Re1 and Ng3; ...Nxe4 won P. A locally equal trade can lose material elsewhere.
- T31 Dragon: ...Ng4 attacked Qe3/Bh6 AND opened Bh8-f6-e5-d4 against Nd4. Qd2? followed by Qxh6 abandoned d4, allowing ...Bxd4. A queen guarding two attacked pieces may lose one after recapturing on the other. Examine Rxg4 and all recaptures; no verified best replacement.
- Refresh pins when endpoints move. ...Nd4?? Nxd4 cxd4 Rxd8+ exposed Qd8. Kb1 released Rd2; Kg2 pinned Nd2 to Ra2, Kf1 released it. A pinned rook can capture its pinning queen.
- T30 SF: Qg6 pinned g2 to Kg1. f3? allowed ...Nf4, then checking knight captures on h3/f2 won Q; gxh3 was ILLEGAL. A queen defending mate must also survive checking forks.
- Before moving a guard/screen, trace lost guards and exposed rays. ...f6/exf6 exposed Be6 to Qe2; f2-f3 abandoned Be3. Ne4 opened Ra2-e2 with Ba6 guarding e2.
- Before forks/trades, test captures and checking intermezzos. ...Nc3+ Qxc3 Rxd1 Rxd1 lost N; Bxd5?? allowed ...Nd3+ before ...Qxd5. An attacked queen can capture its attacker; a capturer does not guard its own square.
- T31 Dragon: Qg8+ Kd7 removed Ke8's screen from Qd8-g8. Nc7?? ignored ...Qxg8; after Nxa8, ...Qxa8 removed N too. Q+N lost for R. A fork does not answer an attack on my queen; calculate enemy captures before assuming forked pieces must respond.
- T30 Final: Bc3 guarded a5 through b4. ...Rxa5?? Bxa5 lost my last rook for P, unmarked. Pawn raids must pass the complete bishop-ray scan.
- Derive knight attacks from actual squares. Nf3 did NOT attack e4, and e3 blocked Re1-e4. Ng3xe4?? lost a minor after bishop and queen recaptures; the claimed three attackers were only two.
- Trace batteries through OWN pawns. exf5 cleared e4 but put a new screen on Bc2-h7; f6 cleared it. After ...gxf6/...f5, Bxf5 removed the screen; gxf5 would replace it with my pawn.
- MATE FIRST, including quiet threats and queenless positions. ...Nxf4 attacked Qh5 but allowed Qxh7#; Rxe7 ignored ...Rh1#. Luft solves only the mate its flight prevents. Before advancing an exposed king, test every enemy check and resulting flight.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3. Long thinking never replaces a capture scan.
- Name a target/break before shuffling. Repeated rook/bishop/knight shuffles consumed 36-56 seconds yet missed pawn captures, lost guards and checking forks. Spend calculation on the opponent's forcing reply.
- T32 DeepSeek: no invalid attempts, finished 15:25. Book mostly 3-7 seconds; ...Qxc4 took 21, ...Bxa1 26. Fast forced recaptures and blockade moves preserved time without missing the capture chains. Use extra time when a threat changes a ray, then shorten verified continuations.
- T31 Armageddon: fxg4 took 117 seconds, Bh6 68; finished 5:14. Neither think prevented later material losses. Budget from the actual starting clock: White had ten minutes.
- T31 Final: ...Rf4?? took 46 seconds; later bishop/pawn moves took 42-53. Finished 5:52. Once a defensive cycle is verified, use 1-5 seconds unless a pawn move, check or changed rook ray alters it.
- Track TOTAL material through the last recapture and actual reply. Qxc1 Bxc1 Rxc1 Qxc1 costs Q+R for R+B. ...Ne2+ followed by ...Nxc1 and Rxc1 wins the exchange. Taking B with ...Nxe4 is not a trade until a recapture occurs; f3 instead leaves B lost.
- T31 Final: ...Rf5-f4?? challenged Re4 but Bd2 attacked f4 through e3. Bxf4! Bxf4 left my B versus R with equal pawns. Bd6 and g5 supported f4 but could not prevent the cheaper capture. List ALL enemy capturers and compare complete material balances before offering a heavy-piece trade.
- Ahead: remove counterplay, simplify safely, preserve mating material. Check pawn guards and entry squares before queen trades. Worse: safe activity/repetition; later gifts do not validate earlier errors. Armageddon White needs a win, but speculative losses do not establish winning chances.
- T32 conversion: after ...Bxa1/bxc4/...Bc3, I still had the extra bishop; exchanging one rook each had not surrendered it. Rxe6?? fxe6 dxe6 left White only pawns. ...Re8 blockaded e6, ...bxc5 removed the other advanced pawn, and ...Rxe7 eliminated the passer before mate. Stop counterplay before remote pawn raids.
- B+P conversion: preserve the LAST pawn with king support before assigning the bishop to a remote passer. A bishop alone cannot mate. Count the enemy king's route to the pawn and how many moves the passer gives you.
- T30 Sonnet: Bd8 alone guarded a5; ...Bxg5?? let Ka4 approach it while h6-h7 forced the bishop to guard h8. ...Bf6 saved a draw but abandoned a5. Seek king support before taking a remote pawn.
- Escort passers; scan straight AND capture-promotions two advances ahead. c2 attacks b1/d1. A checking rook capture can remove a blockader; a rook trade can remove a pinned one. Ka3 guarded a2, but Bc1+ Ka4 Rxa2+ deflected the escort. Test checks before claiming a rook is tied down.
- T31 SF: Nxd6 removed Ba3's defender but allowed ...a2! before Kxa3. Nd6 could reach neither a2 nor a1; Ka3 then allowed ...a1=Q#. Removing a passer's guard helps only if capture/blockade occurs before its next advance.
- T31 Sonnet SF: Bf2 guarded c5; b5 prepared supported c6 while a rook down. Kc5?? allowed ...Bf8+ and ...Bd6, covering c7/b8. Later ...Bc7?? allowed king-supported Bb6 to exchange the blockader; Rd8 guarded neither c7 nor b6. Scan checking deflections of the escort. Time win, no completed conversion established.
- T31 Final defense: Be5 guarded c7/h8; Bd6 guarded c5/c7 and was protected by c7. After ...Bf6 blocked Rf8+, ...Kg5 still guarded Bf6, but ...Kxh6 abandoned it: Rxf6+ won B for P. Recount king guards after a pawn capture. SF's later repetition at roughly +7 was an escape, not a proven fortress.
- Verify mate support, all flights and stalemate. e5 clears Bb1-h7; ...Nf6xd5 can abandon h7. Qf2 supports Rd1# vs Kh1. Qg3/Ne4 supports ...Qxg3+ and ...Nf2#. With Re7/Ph7, Bf6# works because h7 covers g8 and Re7 covers g7/protects h7. Repetition with Q+R vs bare K proves no fortress.
- T31 Dragon: Qh7 threatened Qg8#, but ...Be6 vacated d7 for the king; Nd5 blocked Rd1-d7. Recompute flights after quiet defenses. A later king raid allowed ...Qa8+ and ...Qa5# despite five minutes remaining.
- DeepSeek back rank: T31 Rd2 vacated the last blocker and allowed ...Qe1#. T32 Kf1 allowed ...Re1#, protected by Bc3 through d2. With f2/g2/h2 occupied, count actual legal flights/blocks after simplification; scan mate before another trade or pawn grab.

## White openings
- Dragon: Bc4/f3/Be3/Qd2/O-O-O, with ...h5/...Nc4 and Bxc4 bxc4. T31 g4?! repeated T10: ...hxg4, h5 and rook/knight captures consumed my f/g/h pawns for Black's h-pawn. ...Bxg4 ignored the attack on Nh5 and attacked Rd1 through f3/e2. Two pawns down; no verified move-15 replacement. Count the full liquidation before g4.
- T31 Sonnet Zaitsev/Breyer: against ...Bb7/Re8/Bf8, a4 provoked ...Nb8?, but d5? and Bc2?! allowed ...cxd5/exd5/...Bxd5, losing a central pawn. Ne3 Bxf3?! Qxf3 retained the bishop pair but did not recover it. No verified replacements for moves 13/15.
- T31 Maroczy: c4 against ...g6/...Qa5, f3 and Qxd4 after ...Nxd4. Before O-O?! calculate ...Ng4: Nf6 leaves Bg7's ray against Qd4 while Ng4 attacks Be3. Qd2 and Qxe3 preserved pawns but conceded the bishop pair. No verified move-11 replacement.
- Same game: ...Be6/Rfc8 made c4 vulnerable. Rfd1?! Bxc4! Bxc4 Rxc4! lost P and attacked Nc3; Nd5 cleared the rook's route to c1. A bishop guard does not save a pawn when the attacking bishop has a rook behind it. Later queen raids/trade left R+N versus R+B, two pawns down. No verified replacements for moves 15/19.
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and attacks Nf6. ...Nd7?? permits Qxd7 Qxd7 Rxd7, winning N; ...Bf6 exf6 wins B for P even unmarked. e5 screens Qc7-f4 against ...Nxf4. No forced opening edge established.
- Caro ...Nd5/Bd2/...Nc7/Qe4: ...Bf6? exf6 Qxf6 Bc3 attacks Q and clears d2. After ...Qxf2, Be1 guards Ng3 through f2; against ...Qb6, Rd7 invades.
- Chigorin: Nf1 restores Qd1-d4; Qf3 abandons b3. Rc1/Bb1's queen trap needs actual c-file geometry; ...Qb7 avoids it. Against a knight on c6, d5/...Nb4/Bb1/...a5/a3/...Nc2 forced an equal exchange with an active enemy rook. T31's knight was on a5: d5 instead met ...Nc4/b3/...Nb6. Branch matters.
- T30 Sonnet: Nh2 enabled f4 and Bxf4 activated the bishop against ...Rfe8/Rac8. No forced opening edge or validation of d5 against ...Nb4. Nf5? and Ng4? remain errors; hxg4 opened an unused file. exf5 screened Bc2-h7, f6 cleared it, Bxf5 removed Black's replacement screen. ...Rxe1+?? enabled Qh7+/Qh8# with Bf5 support and Re1 denying e7; not proof of sound sacrifices.
- T31 Sonnet R3: Qe3?! and Ng4?? allowed ...Nxg4/hxg4/...Bxg4, losing h-pawn and attacking Rd1. ...Nxg4 also attacked Qe3. Nf5?! Bxf5 exf5 Nxd5 left White two pawns down. Calculate the capture AFTER the recapture.
- Same game: f6 attacked Re7 and opened Bc2-h7. Automatic Qxf4?? after ...Nxf4?? missed comparison with fxe7 and king threats; Qxf6+?? met ...Bg7 with tempo. Later Qxh6+! provoked ...Qh7?? Bxh7, winning Q; Qh5 guarded Bh7 and Bg7 blocked Re7-h7. Forfeit, not completed mate. No verified earlier replacements.
- Ruy d3: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. Qd3/Bb1 threatens Qh7#, answered by ...g6. Nbd2 blocks Qd1-d4; Be3 blocks Re1-e4. Before g3/h4 calculate ...f5/...fxe4 and Qh4 routes.
- T30 SF ...Bc5/d6/h6/Bb7: d5 and the c-file exchange activated Black. Central exchanges were safe, but ...f5/...e4 drove Nf3 away and ...Ne5-d3-f4 invaded. A proposed f3 break must calculate ...Nf4 and checking forks. No verified opening replacement.
- Ruy ...Bg4/Qe2/Nc6: Nf3 pinned to Qe2. h3?! Nd4 hits Qe2/Bb3/Nf3. After Qe3 Bxf3, Qxf3 loses Q to Nd4. ...c4 Bc2? Nxc2 forks Qe3/Ra1/Re1. No verified replacements.
- Ruy ...Ba7/Bg4 and ...exd4: e5?! Nxe5 gains tempo with d6 guarding Ne5; cxd4?! permits Ba7xd4 through b6/c5. Against ...Bc5/O-O/...d5, checking intermezzos matter: Bxd5?? allows ...Nd3+. Rxe5 requires ...Qf6+ calculation.

## Black openings
- Four Knights castled: 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6. Equal material. ...Qd4/Bg4/Bd6/Qf6, then a queen exchange on g5, reached near-equal queenless middlegames in T30/T31. Later exchange losses do not refute it. Distinguish Nd5 before castling.
- T31 Final: ...Rae8, ...h6 and ...Be6 enabled safe bishop/rook exchanges ending in ...fxe6, with R+B each, equal pawns and an open f-file. King activation and ...Rf7/g5/Rf5 were unmarked through move 25; ...Rf4?? lost the exchange. No verified replacement.
- T30 Final: reciprocal rook captures after ...Rg8/Rh8 left equal R/B counts but two pawns down and exposed. A reciprocal capture does not establish adequate defense; evaluate pawns, rook safety and king exposure AFTER the exchange.
- Classical Caro: ...h6/Bh7/Nd7/Bxd3/e6/Ngf6/Be7/O-O. Against O-O/c4/Rfe1, ...c5? d5! was adverse; later gifts do not certify it. Long-castling ...Nxe5/dxe5/...Nd5 also lacked validation.
- Ruy d3 T30 Sonnet: ...Re8/Bb7/Bf8, central ...d5 exchange, then ...f5/...Qd7/g6. ...Nxe3?! was inaccurate: Qxe3 would allow ...f4 to fork Q/Ng3, but fxe3 avoided it. Move Q off Rd1's file BEFORE ...e4 dxe4. Later ...Qe7/e4/fxe4 induced a piece gift, not a forced opening win.
- SF Ruy 6.d4: central exchanges with ...exd4/...Nd5/...Nxd4, then ...Nb6/...Nxa4 and ...d6/...Bxd6/...Be6 reached near equality. Against Rad1 and Bxd6, ...cxd6 retained d6; ...Qe7 lost it.
- Chigorin ...Qb6?? dxe5 uncovers Be3-b6. Open Ruy ...Ne6?! Qxd8 Rxd8 Bxb5 lost P. Berlin queens-on ...Be7?! Rd1: solve the open d-file before routine development.
- Advance Caro: ...f6? Nf4!/...Qd6?? exd6 repeatedly loses Q. Earlier ...f6 BEFORE cxd4 worked with c3 screening Qb3-d3 and Nd2 blocking Rd1-d3; it validates neither later exchanges nor queenless ...f6/Rxf6/Ne5.
- QGD: recount central guards after exchanges. Qe2 displaced Qd1; ...Bxf3 Qxf3 removed Nf3, allowing ...Nxd4 with tempo. Nc3 does NOT attack d4. ...Bg4/Bh5 were inaccurate. T29 Ne5?? Rac8? missed punishment; Nd7?? Nxd7 won N. No verified move-15 replacement.
- T31 QGD Bf4: ...c5/Nc6, central pawn exchanges, ...b6/Bb7/Rc8. ...Nb4 attacked Qd3 and cleared BOTH Rc8-c4 and Bb7-f3. After Qe2 Bxf3, Qxf3?? abandoned c4 and ...Rxc4 won B; gxf3 retains Qe2's guard. ...Nbd5 and knight recapture kept a blockade. Bd6?? lost B because d4 blocked Rd1-d6.
- T32 QGD Bg5/IQP: ...Nbd7, ...dxc4/...c5/...cxd4, ...b6/Bb7/Rc8 developed smoothly. Against Bxf6, ...Nxf6 preserved pawns; ...Nd5 challenged Ne5 and blockaded d4. After Nxd5, ...Bxd5 preserved e6; the next bishop exchange centralized Qd5. Playable in this game, not a forced win: Nc4?? supplied the piece.
- DeepSeek still overlooks capture chains when retreating an attacked knight or kicking a rook. T32 Nc4 and b3 gave concrete opportunities; verify rays and complete exchanges rather than expecting gifts. Its 35-41 second routine thinks did not prevent them.

## Note files
- notes/accelerated-dragon.md - Pawn storms, discovered attacks and queen safety after checks.
- notes/berlin-endgame.md - D-file and clearance.
- notes/caro-kann-advance.md - Breaks and queenless mate.
- notes/deepseek.md - Classical Caro, d-file tactics and conversion.
- notes/four-knights.md - Exchange offers, bishop defenses and promotion screens.
- notes/qgd-exchange.md - IQP blockades, capture chains, bishop clearance and mate.
- notes/ruy-lopez.md - A-file guards, bishop screens and passer blockades.
- notes/sicilian-maroczy.md - Maroczy exchanges, king screens and passers.
