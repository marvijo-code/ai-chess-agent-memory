# Chess memory - Muse Spark 1.3 Contributor (3600+10)

## Record
- T84SF2G1 B vs DeepSeek win forfeit m21 level. Scheveningen a6 Bd7 Qc7 Rac8 Rfe8, Qb8?! Nb4 Nc6 wasted vs a4 a5, e5 dxe5 Be6 h6 Bb4 pin won 3 invalid. 0 illegal.
- T84R4 W vs Sonnet win forfeit m33 level. Ruy d3 c3 Re1 Bc2 Nf1 Ng3 Be3 Kh1 d4 Nxd4 Bxd4, c5 c4 clamp, Bf4 Nh5 Nxf4 Nf5 exf5 d5, Qd4 Qd2 Rxe1 trade level, won on 3 invalid after Qe3. 1 illegal.
- T84R3 B vs SF loss 1-0 m31 Rb8#. Morra dxc3 Nc6 Bd7 e6 Qc7 Nf6 Be7, Qb8 gated x2 burned 3:12, Nxd6+ Bxd6 Bxd6 bind +4 to +8, O-O-O into Rc1 battery, Qa7 Bxa6+ Qxa6 Rb8# mate. 2 illegal.
- T84R2 B vs DeepSeek loss 0-1 m28 Qh7#. Breyer shell d6 O-O Bd7 Re8 Bf8 h6 Ne7 Ng6 Rc8 c6 Nf4 Ng6 e5 break Re6 Ne5 Ne7 Qd5 Nd7 Rcc6 allowed Qd3-h7# (Bc2 covers). Re6 3:29 Ne5 4:09 burned level. 1 illegal.
- T84R1 W vs Flash win forfeit m27 level. English Attack Be3 f3 Qd2 O-O-O Kb1 Bd3 g4 plan, vs e5 Nb3 Be6 O-O Nc6 d5 break. g5?! Rh3? flagged vs h5 g6 lock, f4 f5 correct. Won on 3 invalid. 1 illegal.
- T83-3rd W vs Flash loss forfeit m32 down B Re8 f4 pin. Classical Bd3 Be3 Qe2 O-O-O Kb1 done, then Rc2 Rh1 Rg1 Qd1 Nd2 drift gated, Re8 plus f4 won e3 B. 1 illegal.
- T83SF1G1 B vs SF loss forfeit m24 down 2+ crushed. FourKnights Bb4 O-O Nd5 Nxd5 exd5 e4 book flagged x2, Bc4 Be6 fxe6 Qb3 Qb6 d6, Rab8 Ba5 Bb6 met b4 Kh8 Qc2 Qd5 Bf4 Re7 Re5 Qd5 Kg8 Rbe8 a6 Qd7 flagged then a5 trap won B forfeit. 3 illegal.
- T83R5 W vs Sonnet loss 0-1 m79 mate. Ruy d3 Breyer Kh1 Qc1 Bd2 d4, e5 dxe5 Rxe5 Bxd3 lost B, Bb2 Nd3 fork, Bc2/Bd3 shuffle burned to 6min vs 46min, Ra8 mate. 5 illegal.
- T83R4 B vs Flash draw threefold m44 down 2. Scheveningen Bd6 Rfe8 Kh8 Qb8 Rf7 Re7 held vs f4 d5 Bg5, drew via Kg8 Kh8 loop vs 2:39 bank. 4 illegal.
- T83R3 B vs Flash win forfeit m21 level. Scheveningen Re8 Be6 Nd7 Qc7 Qd7 Rac8 Ra8 a5 a6 Kh8 Ng4 Nf6 shell held vs g3 Bg2 e4 Be3 Nd5. Won on 3 invalid. 0 illegal.
- T83R1 W vs SF loss 0-1 m19 mate. Dragon Yugoslav Be2?? repeat left Be3 to Nxe3 then Bxd4. Down shell Ka1 Kb1 loop then Bxc3 Qxa2 mate. 0 illegal.

## Key lessons (read before EVERY move)
- LEGALITY FIRST: after 1 reject redraw FEN, pick different piece and idea, never resend stale UCI. 3 rejects forfeit, tool refusal = reject. In check list replies once and send in 5-10s. T83SF1 burned 2 on e4 book plus 1 on Qd7 then 3x on Ba6 trap forfeit: after 1 refusal NEVER resend same UCI, switch square at once. EXCEPT down 4+ rook ending where every move loses same pawn: resend BEST once, 2nd send passes. EXCEPT FourKnights e4 book false flag: RESEND e4 once, 2nd d6 keeper, never 3x e4. T84R4 d3 gated once: rewrite squares after his capture, walk path.
- MORRA C3 DXC3 POISON T84R3: vs 4.c3 dxc3 5.Nxc3 material LEVEL never extra pawn. Never Qc7 plus Nf6 plus Be7 while Bb5 plus Nb5 plus Rc1 eye d6/c6. Play a6 FIRST kicks Bb5/Ba4, keep d6 twice via e6 Nf6 Qd7, never Qc7 Qb8 on Nb5 ray. 11...Qb8 gated x2 burned 3:12 then 12.Nxd6+ Bxd6 13.Bxd6 bind (+4 to +8) won game. After Bxd6 never Qc8 Qd8 drift: trade or block c-file at once. Sweep Nb5-Nxd6+ before develop.
- MORRA O-O-O BATTERY POISON T84R3: never O-O-O while Rc1 plus Rfd1 live on c/d-files. Keep K central Kf8/Ke7 or O-O short only. Never Qa7 on Rb3 ray plus Bxa6 line: keep a6 twice, guard b7/b8 twice, meet Rb3 with Rc8/Rd8 block first. Sweep Bxa6+ plus Rb8# before any Qa7 Qb6 shuffle. 10-20s keepers never 2min.
- BREYER QH7 MATE POISON T84R2: Breyer shell left Kg8 boxed by own Bf8 plus Ng6 plus Re6 plus Rc6. Bc2 x-rays h7 via d3 e4 f5 g6, so Qd3-h7# mates (Q protected, f8 blocked, h8 hit). Sweep Qh7 plus Qg7 before any Re6 plus Rcc6 double. Never Rcc6 while Q eyes h7. Evacuate f8 via Be7 or Kh8 luft first. Re6?? Ne7? Nd7?? Rcc6?? all gated: keep tension, meet e5 only with exd4 counted, hold d6 twice, 10-20s keepers never 3-4min level.
- TOOL AVOID IS AN ORDER: after one refusal switch piece and idea at once, never resend flagged UCI. DOWN FALSE FLOOD: recount W and B from FEN, move king or rook off ray in ONE try, never burn 3 tries.
- FOUR KNIGHTS ND5 POISON: vs 6.Nd5 play Nxd5 only, never d6 Nxe4. After exd5 play e4 hits Nf3 (e5 vacates so Nxe5 flag FALSE). Then dxc6 exf3 Qxf3 dxc6. c6 has two guards via b7 and d7 so Bxc6 dxc6 safe. After Bc4 Be6 Bxe6 fxe6 Qb3 never Qd6 blocking d-pawn plus Rab8 passive: play Qe7 Be7 Rfe8 first. Never Ba5 Bb6 vs b4 a4 a5 storm: a5 wins B; meet b4 with Bd6 Bc5 once, retreat at once, never Kh8 Kg8 shuffle while Re1 Re5 press e6.
- DRAGON BE2 POISON REPEAT T83R1: vs O-O plus d5 never Be2 holding tension while Be3 loose to Nxe3. Play Nxc6 bxc6 or Nxd5 Qxd5 first. Sweep Nxe3 plus Bxd5 plus Nxg2 before develop. After Nxe3 play Qxe3 at once, never Nxc6 ignoring g2. T80R1 and T83R1 both 10.Be2 lost piece then Bxd4 plus Qa5 plus Rd8 battery won more. Keep Kb1 never Ka1 vs Qa5, guard a2 twice, Bd3 blocks Rd8.
- OPEN QA5 PLUS QXA2 POISON: 4.Qa5 after Nxd4 meets Nc3 tempo. Never Qxa2 under Ra1 to Rxa2. Play Nf6 Nc6 e6, never early queen sortie. If hit retreat at once. T83R1 Qxc3 left a2 so Qxa2 mate: keep Kb1 and a2 twice-held.
- RUY NA5 C5 C6 POISON: 10.c6 chases Nd5 weakens d6, 14.c5 hits Bd4 opens d5, 15.b5 meets c3 doubling. Keep Ne7 Nc6 Bd7 Re8, hold d6 twice, meet d4 exd4 only.
- YUGOSLAV BC4 POISON: T79R4 11.Bc4 abandoned Be3 to Nxe3 won piece, Rb8 Bd8 won game. Never Bc4 Bb3 while Be3 loose. Sweep Nxe3 Bxd5 first or guard Be3 twice. Keep Be2 then f3 then Qd2 then O-O-O order.
- ADVANCE C4 E6 FORK POISON: T80R5 Nd7 onto e6 fork met cxd5 exd5 e5 hitting Nd7 then Ne5 winning c6. Vs c4 resolve dxc4 or cxd5 at once, never retreat onto e-push. Before any Nd7 Nf6 list e6 fork. In check list flights then blocks then captures once.
- ENGLISH BB4 PIN SHELL: T82R1 Bb4 O-O d6 Re8 h6 Be6 Rc8, Bc5 Bd4?! exd4 Nd5 outpost on e4, Nd7 Nde5 Nxf3 Ne5 Nf3+ Bxf3, c6 c5 Be6 Kg8 g5?! Nh5 Re7 g4 Qf4 Kh7?? Nf6+ fork gated x3 forfeited. Keep Bc5, never Bd4 granting Nd5, never g5/g4 without Nf6+ sweep, never Kh8 while Ng4 Nf6 loops.
- CARO CLASSICAL WHITE CLOCK POISON: T83-3rd drift gated, Re8 plus f4 won e3 B. Keep Qc2 Qe2 once, no rook shuffle, list f4 e-file. T82R5 Rh3 plus Rh4 loop drew vs bank. Early pushes flagged. Routine 10-20s cap 60.
- NAJDORF E5 TIMING: T78R4 e5 shell burned shuffling Qc8 Qc7 Qb6 plus Re8 Re7 Rd7. Re8 Bd6 Be6 hold e5. Never Nc5 while Be3 loose, never Bf6 gxf6 while Qf3 lives, never queen rook king shuffle.
- DRAGON D5 QA5 BF5: Vs d5 resolve exd5 Nxc6 or Nxd5 at once, never Be2 Bc4 holding tension. Never c3 blocking Bc1 while Qa5 lives. Never Bd4 while b2 c3 loose and Qd2 faces Rd8 Qb6. Play Be2 then O-O-O first. MOVER ABANDONS GUARD: name what left and who hits it now.
- MAROCZY PIN POISON: 7.Bd2 met Nxd4 winning N, 8.Be3 met retreat holding it. Never block pin leaving knight loose. Support pawn first.
- CLASSICAL E5 BREAK PLUS BLACK SIMPLIFY: vs Bd6 Nd7 Re8 Qc7 e5 hits d4. Never dxe5 without Nxe5 counted twice. Never Bd4 while f4 Ng3 loose, never Ne4 while e4 loose, never b3 while c1 loose. As Black: Bf5 Bg6 h6 Bh7 Nf6 e6 Nbd7 then Be7 O-O Nd5 Nb4 Nxd3 then Bf6 Bxe5 Qxd3 levels. 10-20s each never 55s.
- CARO CLAMP PLUS ENGLISH GRABS: vs c5 c4 b5 b4 Qb6 b3 opens c3 to cxb3 won N, Nc4 met b3 tempo. Keep Kb1 never Ka2, Rd1 Rd2 Be1 Qf3. Only with Re8 d6 e5 held. Meet Nc4 with b3 once, c3 only with dxc5 counted, keep Rd1 not Rd2 Rd3.
- BLOCKER LEAVES QUEEN: Nd4 blocked Rd8 Qd7, Nb4 unblocked it so Rxd7 won Q. Before moving blocker move queen off file or guard it. Same for rook leaving rook: guard b8 before Rxc4. Ke2 Kd3 walked into check.
- ENGLISH NC2 FORK: Qe3 plus Re1 plus Ra1 all lose to Nd4 c2 triple fork wins exchange. Keep Nd4 until Q leaves d-file, play c5 Bxd5 Qd5 Qc7 Rac8, strike on Qe3. Routine 10-20 cap 60.
- UP PIECE FINISH NO SHUFFLE: Up = centralize Q, trade rook with recapture named, checks first, luft once. Down = 5-10s, invite repeats. Down P Bd3 blockade plus Nc5 Ne4 plus Qd1 Qd2 plus Kh1 Kh2 Kg1 loop draws. Down 5: keep Rd7 7th, Ke7 central, no b6 h7 loosening, 5-10s, invite repeat vs SF. T83R4 down 2 Bd6 Rf7 Re7 Qc7 blockade plus Kg8 Kh8 loop drew vs 2:39 bank: correct.
- SHELL CLOCK: Routine 10-20, cap 60, never 2-4min. T83R5 Kh1 Bd2 d4 burned to 6:01 vs 46:32 while level. T84R2 Re6 3:29 plus Qd5 3:54 plus Ne5 4:09 burned level. T84R3 Qb8 3:12 plus Qb6 1:51 burned lost. T84SF2 10-30s banked 45min vs 28min vs 2-8min burns.
- WHITE SCHEVENINGEN HASTE PLUS BF4 PIN: f3 Bxf4 vs e5 wedge level. Qe1 Qe2 waste tempi, f5 Bxd4, Rb1 missed recapture. RECAPTURE FIRST. Storm only e4 twice f5 counted. Nb5 f5 10-20s. T84R1 g5?! Rh3? vs h5 g6 lock flagged: f4 f5 first, no Rh3 while h5 walls.
- SCHEVENINGEN QB8 RB8 RE6 POISON: Qc7 Rac8 Rfe8 passive vs f4 e5. T83R4 Qb8 freed Rc8 ok but h6 h5 a5 b6 h4 loosened Kg8: keep Bd6 Nf6 blockading d5, Rfe8 Rf7 Re7 hold e5 g7, never h6 h5 h4 vs Bg5, never Rc5 vs Be3. T84SF2 Qb8?! Nb4 Nc6 vs a4 a5 wasted 2 tempi: never Nb4 while a5 kicks, strike e5 at once.
- RUY D3 LOCK: c3 Re1 Nbd2 Bc2 Nf1 g3 h3, d4 only with e4 twice after Be3 blocks Re1. T81R4 cxd4 left e-pawn to Nxe4; take back at once. T82R3 Bb1 Qb2 Bc4 Bc2 Qd2 all bad while d4 loose: keep Bd3 blockade plus Nc5 at once. T83R5 e5 dxe5 Rxe5?? Bxd3 won B plus Bb2/Re5 Nd3 fork won more: never e5 while Bd4 once-held, never Bb2 with Re5 loose. Vs d5 hold d6 twice. T84R4 Bg4 h6 Qd7 shell level to m33: keep Kh1, meet c5/c4 with Be3, Nh5 with Qe3, Nf5 exf5 d5.
- BB5 PIN SHELL: vs Bb4 Ba4 Bb3 play Bd7 a6 b5 tempo, e6 Be7 O-O Qc7. Ne5 Ng6 Nf4 hit Qe2, c4 b4 tempo, bxc3 wins N. Keep e6 closed.
- ARMAGEDDON CLOCK: White needs win so draw loss, Black draw odds so draw win. Both: level or down huge still 5-10s, no 1-2min thinks, no pushes, keep Qd2 Nc3 or Bd3 Nd7 only if instant. 60s thinks kill draw odds, keep 5-15s keepers, bank for endgame.

## Openings
- B Morra: vs 4.c3 meet Nf6 Nc6 e6 a6 first, never dxc3 counting extra. After Bb5/Nb5 sweep Nxd6+ at once, keep d6 twice.
- B Ruy Closed: a6 b5 Be7 d6 O-O Bd7 Re8 then Bf8 h6 Ne7 Ng6 Rc6 c6 Qc7. c6 for Qc7 after Rc8 ok, never c6 chasing Nd5, never Ra8 passive, never Nf4 exf4, never Rb5 while c4 fork lives. Hold d6 twice, Bc6 hits e4 vs Qe2 good.
- B Bb5: Bd7 a6 b5 e6 Be7 O-O Qc7. Ne5 Ng6 Nf4 hit Qe2, c4 b4 tempo, bxc3 wins N. Keep e6 closed.
- B Nxc6: bxc6 Bd3 e5 shell, Nd7 Nc5, Bb7 Qc7. Bans: queen sortie, rook trade, king shuffle. CXD4 FIRST.
- B English: d6 Be7 O-O Re8 Be6 Qc7 Nd7 then Nf6 Nd4 c5 Rac8 plus Nc2 fork vs Qe3. No Nd4 without exd4 named. No Qb6 on Be3 ray. Qc8 Qd7 Rac8 held level: no Rac8 Ra8 retreat, no a6 a5 loosening, no Kh8 while Ng4 Nf6 loops.
- B Scheveningen: Be7 O-O Bd7 Qc7 Nxd4 e5 d5 level, Rac8 Rfe8 Rf7 Re7 Bd6 blockade, Qb8 frees file ok. Vs e5 dxe5 Nxe5 only if Bf4 met Ng6. Never h6 h5 h4 vs Bg5 f5, never Rc5 vs Be3, hold d6 e5 f6 twice.
- B Advance: Bf5 e6 Nd7 Ne7 early. Meet f4 with f6 h5 first, never Bg6 park vs f4 g4, never c5 alone, keep Kg8 vs h-storm. Vs c4 meet dxc4 or cxd5 at once, never Nd7 onto e6 fork.
- W Ruy d3 Berlin: c3 Re1 Nbd2 Bc2 Nf1 g3 h3, d4 only held twice after Be3 blocks Re1. Before Ne6 list dxe6. No Qd2 Ne4 loop shuffle. No c4 vs b4 c5, meet Nf4 with g3 after Kh1.
- W Classical: Bd3, Be3 holds d4 twice, O-O-O Kb1, Rg1 holds g2. Vs c5 c4 b5 keep Rd1 Qf3, never b3 Kb2. Hold e5 f4 twice first.
- W Yugoslav: central bishop fix over risky develop. Keep Be2 then f3 then Qd2 then O-O-O order. Never Bc4 Bd4 while Be3 loose or b2 c3 loose vs Rd8 Qb6. Vs d5 Be2 O-O-O first.
- W Taimanov: Be2 f3 Qd2 Bd3 castle long Kb1. Storm g-push h-push Q-double vs shell.
- W Maroczy: c-pawn clamp, knight develops, bishop supports. Vs Qa5 pin support first then castle.

## Opponents
- Haiku: Open Sicilian Nxc6 patient, trades rooks, centralizes king, Nf5+. Never shuffle king.
- GLM: Taimanov loose, hangs Q, banks then drifts. T83R3 English g3 held level to m21 then 3 invalid forfeit. T84R1 Scheveningen e5/d5 level to m27 then 3 invalid forfeit. Fast 3-10s early, 1-3min mid, 3x invalid forfeits when forked. Takes free Bxd5 Bxe3. T79R3 Qc7 Kb8 lost Q to Bf4 after g3 blocked Qxh2.
- DeepSeek: keeps guarded, queenside dance. Fast 5-20s banks clock, flags when worse. T79R5 Italian 2-20s banked 53:05 vs shell. T82R5 Classical storm gated 3x forfeited m39: keep b3 c3 twice-held, no Ka1 Rd2 shuffle. T84R2 Breyer held level to m24 then Re6 Ne7 Qd5 Nd7 Rcc6 boxed Kg8 and Qd3-h7# mated: evacuate f8 plus Kh8 luft first. T84SF2 Scheveningen f4 e5 level, a4 a5 met, 10-30s banked 45min vs 2-8min burns then 3 invalid forfeit.
- Sonnet: Ruy Na5 Nxb3 Bb7 Re8 solid, Bg4 pin Nxe4 Nc4 clamp, Breyer Bd7 Re8 h6 Bf8 holds e5. Scheveningen patient 6-20s, shuffles Kg2 Kh2 Rd2 to flag. Takes every loose unit. T80R5 Advance c4 e6 fork won P vs Nd7 shell. T82R3 Chigorin d5 cxd4 exd4 held extra pawn, banks 40min: don't drift, keep Bd3 Nc5 blockade and force repeat. T83R5 Breyer Kh7 a5 b5 Rb8 Rc4 Nd3 fork won N: no Bc2/Bd3 shuffle. T84R4 Breyer Bg4 Bh5 Bg6 h6 Qd7 stayed level to m33 then 3 invalid forfeit after Qe3: keep e4 3x before d4, meet c5/c4 with Be3/Qd4, 10-20s keepers.
- SF: punishes loose, pins, back rank, breaks. Instant, no gifts. Dragon d5 break, bxc6 opens file, Qa5 Rb8 Rd8 double kills. Castle early never long into open file, guard second rank, keep shell for repeat. T84R3 Morra Nb5 Nxd6+ Bxd6 bind plus Rc1 battery plus Bxa6 Rb8 mate: never Qb8 passive, never O-O-O into Rc1.
- Fable: takes loose, trades queens when up, no luft. Model: fortress, checks, back-rank mate.

## Notes
- notes/caro-black.md - Advance loss and break and clock flag.
- notes/caro-white.md - Classical draw loss win, H5 shell and queen grab and Rb2 mate.
- notes/dragon-yugoslav-white.md - Dragon Yugoslav White file and bishop fix and sac patterns.
- notes/english-e5-black.md - English Nc2 fork win, shell and clock.
- notes/maroczy-white.md - Maroczy pin loss and shell clock.
- notes/sicilian-bb5-black.md - Bb5 pin win on time, Nf4 Qe2 tempo and up-piece shell.
- notes/sicilian-nxc6-black.md - Nxc6 forfeit, Qb6 Rxd8 Kh8 shell and tool trap.
- notes/taimanov-white.md - Storm win plan and mate finish.
