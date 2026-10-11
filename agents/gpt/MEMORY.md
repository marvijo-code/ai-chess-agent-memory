# Chess memory

## Move discipline
- Apply stored warnings BEFORE choosing. Each candidate needs its own forcing scan; rejecting one blunder does not validate another. Recognition without execution has repeatedly lost queens and a-file rooks.
- Start with the enemy's last move: changed attacks, pawn controls, opened lines. Scan checks, captures, forks, promotions and quiet mates; repeat on the proposed final board. Refresh attacks after every capture and king reply.
- PAWN DIAGONALS FIRST, then knight jumps and complete sliding rays. Rb3?? axb3, Qe4?? dxe4, Qd5?? exd5, Ng5? hxg5 and Qxe6?? fxe6 lost material. Support cannot prevent a cheaper capture; attacking intent does not establish safety.
- For every check, test Kxchecker and ALL other captures. Name the actual defender and trace its legal path. Qh2+/Rh7+/Qxb2+ lost heavy pieces to king captures. T32 Qe8+?? Rxe8 lost Q: Re6 reached e8, while my e4 pawn blocked Re1's supposed support.
- Name exact defenders, screens and LEGAL recapturers. Nd2 blocked Be3-c1; Be3 blocked Re1-e4; f7 blocked Rf8-f2; Qe3 could not recapture c2. Audit friendly rays newly blocked as well as enemy rays opened.
- A-file warning, repeated T31/T32 Sonnet: axb5 axb5 opens Ra8-a1. Bc1 blocked Re1-a1 in T31; Bb1 blocked Rd1-a1 in T32. Qc6/Qe3 ignored ...Rxa1 and lost R. Resolve rook contact immediately; clearing one blocker may leave another. Rxa8 was legal in T32, not verified best.
- A defended minor can fall to a queen backed by a rook. T32 DeepSeek: Nc4?? Qxc4 Qxc4 Rxc4 won N. Calculate through the LAST recapture, then recount material and remaining duties.
- An attacked piece need not retreat. T32 b3 attacked Rc4 but opened Bf6-e5-d4-c3-b2-a1: ...Bxa1! bxc4 Bc3 preserved my extra B, with tempo on Re1. Scan captures by OTHER pieces and their escape afterward.
- Validate the actual piece square and full path before submission. After ONE rejected move, reconstruct the board and choose a verified legal move; three invalid replies forfeit. Opening memories apply only to matching positions.
- Trace checking rays BEYOND the king. T31 SF: Kb3 screened Rb1-b7; Ka4? allowed ...Rxb7. Examine legal blocks before exposing a rear piece. Kings also block friendly defenses: ...Kd4 screened Bc3-h8 and allowed h8=Q+.
- Count duties AFTER exchanges. Re2 Rxe2 Nxe2 removed BOTH e4 guards, Re1 and Ng3; ...Nxe4 won P. Moving a guard can expose another piece even when the local trade is equal.
- Discovered attacks accompany forks. Dragon ...Ng4 hit Qe3/Bh6 AND opened Bh8-d4 against Nd4. Qxh6 then abandoned d4. Search captures of the forking piece and calculate all recaptures before retreating automatically.
- Refresh pins when endpoints move. ...Nd4 Nxd4 cxd4 opens Rxd8+ against Qd8. Kb1 released Rd2; Kg2 pinned Nd2 to Ra2, Kf1 released it. A pinned rook can capture its pinning queen.
- Qg6 pins g2 to Kg1. f3? allowed ...Nf4 and checking knight captures on h3/f2 that won Q; gxh3 was illegal. A queen defending mate must survive checking forks.
- Before moving a guard/screen, trace lost defenses: ...f6/exf6 exposed Be6 to Qe2; f2-f3 abandoned Be3; Ne4 opened Ra2-e2 with Ba6 guarding e2.
- Before forks/trades, test captures and checking intermezzos. ...Nc3+ Qxc3 Rxd1 Rxd1 lost N; Bxd5 allowed ...Nd3+ before ...Qxd5. An attacked queen can capture its attacker; a capturer does not guard its own landing square.
- After Dragon Qg8+ Kd7, Qd8 directly attacked Qg8. Nc7?? ignored ...Qxg8; Nxa8 Qxa8 then lost N too. A fork does not answer an attack on my queen.
- Derive knight attacks from actual squares: Nf3 does NOT attack e4. Ng3xe4 lost a minor because three claimed attackers were only two. Trace bishops through OWN pieces: Nf5 blocked Bf4-d6.
- Pawn advances can replace screens rather than clear a battery. exf5 put a new screen on Bc2-h7; f6 cleared it. After ...gxf6/...f5, Bxf5 removes the screen; gxf5 replaces it.
- MATE FIRST, including quiet moves and queenless positions. ...Nxf4 attacked Qh5 but allowed Qxh7#; Rxe7 ignored ...Rh1#. Luft solves only the mate its flight prevents. Test every check and resulting flight before exposed king advances or remote raids.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3. Long thinking never replaces a capture scan.
- Name a target/break before shuffling. Spend calculation on the opponent's forcing reply. T32 losses finished with 11:03 and 11:08: ample clock did not prevent unsupported checks or mate. Qd2/Bd5/Qxa5 took 46/56/41 seconds against SF without resolving king danger.
- Budget from the actual starting clock, especially Armageddon White's ten minutes. T31 fxg4 took 117 seconds and Bh6 68 without preventing losses. Verified defensive cycles and recaptures need 1-5 seconds unless a pawn move, check or changed ray alters them.
- Track TOTAL material through the actual final reply. Qxc1 Bxc1 Rxc1 Qxc1 costs Q+R for R+B. ...Ne2+ then ...Nxc1 and Rxc1 wins the exchange. ...Nxe4 is not a bishop trade if f3 replaces the expected recapture.
- Before offering a heavy-piece trade, list ALL cheaper capturers. T31 ...Rf4?? met Bd2xf4 through e3; Bxf4 recovered only B, leaving B versus R. Bd6/g5 support did not save the exchange.
- Ahead: remove counterplay, simplify safely, preserve mating material. Check pawn guards and entry squares before queen trades. Worse: seek safe activity/repetition; later gifts do not validate speculative losses.
- T32 DeepSeek conversion: ...Bxa1/bxc4/...Bc3 preserved the extra B. Rxe6?? fxe6 dxe6 left White only pawns; ...Re8 blockaded e6, ...bxc5 removed the other advanced pawn, ...Rxe7 stopped promotion. Stop advanced counterplay before remote pawn raids.
- B+P: preserve the LAST pawn with king support before assigning B to a remote passer. T30 Bd8 alone guarded a5; ...Bxg5 let Ka4 approach while h6-h7 tied B to h8. A bishop alone cannot mate.
- Escort passers; scan straight AND capture-promotions two advances ahead. c2 attacks b1/d1. Checks can deflect the escort: Ka3 guarded a2, but Bc1+ Ka4 Rxa2+ removed that guard.
- T31 SF: Nxd6 removed Ba3's guard, but ...a2! preceded Kxa3. Nd6 reached neither a2 nor a1; Ka3 allowed ...a1=Q#. Removing a defender helps only if capture/blockade precedes the next advance.
- Test checking deflections of an escort. T31 Kc5?? allowed ...Bf8+ then ...Bd6, covering c7/b8. Later king-supported Bb6 could exchange ...Bc7's blockade; the flag did not establish a completed conversion.
- Recount king guards after pawn captures. ...Bf6 blocked Rf8+ and ...Kg5 still guarded it; ...Kxh6 abandoned Bf6, allowing Rxf6+. SF's repetition near +7 was an escape, not a proven fortress.
- Verify mate support, legal flights and stalemate. e5 clears Bb1-h7; ...Nf6xd5 can abandon h7. Qf2 supports Rd1# against Kh1. With Re7/Ph7, Bf6# uses h7 controlling g8 and Re7 controlling g7/protecting h7.
- Recompute flights after quiet defenses. Dragon ...Be6 vacated d7 against Qg8+, while Nd5 blocked Rd1-d7. DeepSeek back rank: Rd2 allowed ...Qe1#; Kf1 allowed ...Re1#, protected by Bc3 through d2. Count actual blocks and flights before another trade or grab.

## White openings
- Long-castled Dragon: Bc4/f3/Be3/Qd2/O-O-O against ...h5/...Nc4 and Bxc4 bxc4. T31 g4?! repeated T10: ...hxg4, h5 and rook/knight captures consumed my f/g/h pawns for Black's h-pawn. ...Bxg4 ignored attacked Nh5 and hit Rd1 through f3/e2. Two pawns down; no verified move-15 replacement. Calculate the whole liquidation before g4.
- T32 SF, short-castled Dragon: 7.Bc4 d6 8.O-O Ng4 9.Bb3?! Nxe3 10.fxe3! retained material but yielded the bishop pair. Distinguish this from my f3/long-castling setup and the Maroczy queen fork. No verified move-9 replacement.
- Same game: ...Bg4 attacked Qe2 through f3, not Rd1; Nf3! blocked it. ...Nxf3+ required gxf3!, then ...Bh3 required Rfe1! and ...Bxc3 required bxc3!. These legal defenses preserved material but left open f/g-files and an exposed king. Open files are usable by BOTH sides.
- T32 SF: Qh4?!/Rd3?! and queen retreats let ...Rc5-h5 become active. e5! was a useful break, but ...Bc6! changed the board; my note covered only ...dxe5. e4?! screened Bc6-f3 yet did not secure the king. Recalculate the actual reply; a blocked bishop diagonal does not stop rook/queen entry elsewhere. No verified move-24 replacement.
- T32 SF mate pattern: after Rf3 and ...Qc8, the clear c8-d7-e6-f5-g4 diagonal enabled ...Qg4+. Qxa5 ignored Qg4+ Kf2 Rxh2+ Kf1 Qg2#. Rh5 reached h2 through h4/h3 and supported Qg2; my open g-file admitted the queen. A king guarding Rf3 did not answer the mating net. Test checks before remote pawn grabs, even when offering queen trades has failed.
- Sonnet Zaitsev: ...h6/Bc2/...exd4/cxd4/...Nb4/Bb1/...c5/d5/...Nd7 differs from T31's ...Nb8 branch. Do not condemn every d5 from a different branch's failure. No forced opening edge or verified best alternatives established.
- T32 Qxf3?! abandoned Qd1's d5 guard. ...Bxd5 won P: exd5 removes e4's screen and permits ...Rxe1+, with Bb1/Bc1 blocking Ra1's recapture. Rd1 saved R but did not recover P. Audit guards lost by queen recaptures and files opened by pawn recaptures.
- T32 Bf4?? with Qf3/Nf5 allowed ...Bxe4 with tempo: e4 both screened Bc6-f3 and guarded Nf5; Qxe4 meets ...Rxe4. ...Re6? did not validate Bf4. Count actual d6 attackers, including friendly screens, before claiming pressure.
- T31 Zaitsev/Breyer: a4/...Nb8, d5? and Bc2?! allowed ...cxd5/exd5/...Bxd5, losing P. No verified replacements for moves 13/15. Keeping the bishop pair after ...Bxf3 did not recover the pawn.
- Maroczy c4/...g6/...Qa5, f3/Qxd4: before O-O?! calculate ...Ng4 hitting Be3 AND uncovering Bg7 against Qd4. Qd2/Qxe3 preserved pawns but conceded the bishop pair; no verified move-11 replacement.
- Maroczy ...Be6/Rfc8: Rfd1?! Bxc4 Bxc4 Rxc4 lost P and attacked Nc3; Nd5 cleared the route to Rc1. A bishop guard does not save a pawn from a bishop backed by a rook. Queen raids/trade left R+N versus R+B, two pawns down.
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and attacks Nf6. ...Nd7?? allows Qxd7 Qxd7 Rxd7, winning N; ...Bf6 exf6 wins B for P. e5 screens Qc7-f4. No forced opening edge established.
- Caro ...Nd5/Bd2/...Nc7/Qe4: ...Bf6 exf6 Qxf6 Bc3 attacks Q and clears d2. After ...Qxf2, Be1 guards Ng3 through f2; against ...Qb6, Rd7 invades.
- Chigorin: Nf1 restores Qd1-d4; Qf3 abandons b3. ...Nb4 against d5 needs Nc6; T31's Na5 instead used ...Nc4/b3/...Nb6. Branch matters. Rc1/Bb1 queen traps require actual c-file geometry; ...Qb7 avoids the trap.
- Sonnet: Nh2/f4/Bxf4 activated B, but Qe3/Ng4 allowed ...Nxg4/hxg4/...Bxg4, losing h-pawn and hitting Rd1. Nf5 Bxf5 exf5 Nxd5 left two pawns down. Unused open files did not establish compensation.
- f6 hits Re7 AND opens Bc2-h7. After ...Nxf4 compare fxe7 and king threats before automatic Qxf4; Qxf6+ can meet ...Bg7 with tempo. Qxh6+ provoked ...Qh7?? Bxh7, with Qh5 guarding Bh7 and Bg7 blocking Re7-h7. Gifts enabled wins, not proof of sound sacrifices.
- Ruy d3: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. Qd3/Bb1 threatens Qh7#, answered by ...g6. Nbd2 blocks Qd1-d4; Be3 blocks Re1-e4. Before g3/h4 calculate ...f5/...fxe4 and queen entry.
- SF Ruy ...Bc5/d6/h6/Bb7: d5/c-file exchanges activated Black; ...f5/...e4 drove Nf3 away and ...Ne5-d3-f4 invaded. A proposed f3 break needs ...Nf4/checking-fork calculation; no verified replacement.
- Ruy ...Bg4/Qe2/Nc6: Nf3 pinned to Qe2. h3?! Nd4 hits Qe2/Bb3/Nf3; Qe3 Bxf3 Qxf3 loses Q. ...c4 Bc2? Nxc2 forks Qe3/Ra1/Re1. ...Ba7/exd4 makes cxd4 open Ba7-d4; e5?! Nxe5 is supported by d6. Rxe5 needs ...Qf6+ calculation.

## Black openings
- Castled Four Knights: 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6. Equal material. ...Qd4/Bg4/Bd6/Qf6 and queen exchange on g5 reached near-equal T30/T31 middlegames. Later exchange losses do not refute it; distinguish Nd5 before castling.
- T31 Four Knights: ...Rae8/h6/Be6 enabled exchanges ending ...fxe6, R+B each, equal pawns/open f-file. King activation and ...Rf7/g5/Rf5 were unmarked through move 25; ...Rf4 lost the exchange. Evaluate resulting positions, not only local trades.
- Classical Caro: ...h6/Bh7/Nd7/Bxd3/e6/Ngf6/Be7/O-O. Against O-O/c4/Rfe1, ...c5? d5! was adverse; later gifts do not certify it. Long-castling ...Nxe5/dxe5/...Nd5 also lacked validation.
- Ruy d3 vs Sonnet: ...Re8/Bb7/Bf8, central ...d5 exchange, then ...f5/...Qd7/g6. ...Nxe3: Qxe3 permits ...f4 forking Q/Ng3, but fxe3 avoids it. Move Q off Rd1's file BEFORE ...e4 dxe4. Later gifts did not establish a forced opening win.
- SF Ruy 6.d4: ...exd4/...Nd5/...Nxd4, then ...Nb6/...Nxa4 and ...d6/...Bxd6/...Be6 reached near equality. Against Rad1/Bxd6, ...cxd6 retained d6; ...Qe7 lost it.
- Chigorin ...Qb6?? dxe5 uncovers Be3-b6. Open Ruy ...Ne6?! Qxd8 Rxd8 Bxb5 lost P. Berlin queens-on ...Be7?! Rd1: solve the open d-file before routine development.
- Advance Caro: ...f6? Nf4!/...Qd6?? exd6 repeatedly loses Q. Earlier ...f6 BEFORE cxd4 worked with c3 screening Qb3-d3 and Nd2 blocking Rd1-d3; this validates neither later exchanges nor queenless ...f6/Rxf6/Ne5.
- QGD: ...Bxf3 Qxf3 removes Nf3 and Qd1's former d4 guard, permitting ...Nxd4 with tempo. Nc3 does NOT attack d4. ...Bg4/Bh5 were inaccurate; Ne5?? Rac8? missed punishment, Nd7?? Nxd7 won N. No verified move-15 replacement.
- QGD Bf4: ...c5/Nc6, exchanges, ...b6/Bb7/Rc8. ...Nb4 hit Qd3 and cleared BOTH Rc8-c4 and Bb7-f3. Qe2 Bxf3 Qxf3?? abandoned c4; ...Rxc4 won B. gxf3 retains Qe2's guard. Bd6?? lost B because d4 blocked Rd1-d6.
- T32 QGD Bg5/IQP: ...Nbd7, ...dxc4/...c5/...cxd4, ...b6/Bb7/Rc8 developed smoothly. ...Nxf6 preserved pawns; ...Nd5 challenged Ne5/blockaded d4. Nxd5 Bxd5 retained e6; the next bishop exchange centralized Qd5. Playable here, not a forced win: Nc4?? supplied the piece.

## Opponents
- Sonnet exploits blocked recaptures: ...Rxa1 won R in BOTH T31/T32. T32 also used ...Bxd5 against the e-file screen, ...Bxh6 and ...Rxe8 against unsupported checks. Expect legal captures rather than previous gifts.
- Sonnet spends heavily on consolidation: T32 several 60-76 second moves, finished 4:57 versus my 11:03, yet completed conversion/mate. Clock advantage helps only with sound material; prior flags/forfeits are not a strategy.
- DeepSeek overlooks capture chains and newly opened rays when retreating knights or kicking rooks. T32 Nc4/b3 supplied concrete opportunities; verify exchanges rather than expecting gifts. Its long routine thinks did not prevent them.
- SF immediately punishes loose pieces, checking forks, king screens and advancing passers. T32 ...Rh5/...Qc8 built a mating attack after pawn recaptures exposed my king; do not raid while its heavy pieces have entry squares. It sometimes repeats when winning: preserve legal defense and take repetition without calling it a fortress.

## Note files
- notes/accelerated-dragon.md - Pawn storms, discoveries and queen safety after checks.
- notes/berlin-endgame.md - D-file and clearance.
- notes/caro-kann-advance.md - Breaks and queenless mate.
- notes/deepseek.md - Classical Caro, d-file tactics and conversion.
- notes/four-knights.md - Exchange offers, bishop defenses and promotion screens.
- notes/qgd-exchange.md - IQP blockades, capture chains, clearance and mate.
- notes/ruy-lopez.md - A-file guards, bishop screens and passer blockades.
- notes/sicilian-maroczy.md - Exchanges, king screens and passers.
