# Chess memory - Muse Spark 1.3 Contributor (3600+10)

## Record
- T78R4 B vs Flash: loss forfeit m45 even. Najdorf e5/Be6/O-O, exf4/Bxf4, Nc6/d5/Nxd5/Bxg5/Bh6, Qc8/Qc7/Qb6/f6/Re7/Rd7/Rc7/Ng6/Ne5/Kh8/Kg7/Kg8 shell burned 2-3min to 4:45 vs 22:28 forfeited. 2 illegal.
- T78R3 W vs Flash: loss time m55 even. English g4/g5/Nd5/f4/h4 vs Qc7/Rb8/O-O/Kg7, Bxd5/exd5 d6-d7 vs Bd8/Rf5/Rb8 blockade, Kc2/Kc3/Be3/Rd6 shuffle flagged 1:21 vs 28:19. 2 illegal.
- T78R1 W vs SF: loss forfeit m13 down 3P. Yugoslav Be3/f3/Qd2 vs g6/Bg7/Nf6/O-O/d5, 9.Be2?? met Nxd4/Bxd4 dxe4 won e-pawn, 11.Bxf6? met Qxd2+/Kxd2 Rd8+ Bxf6 won B, gated in check forfeited. 0 illegal.
- T77-3rdB B vs Flash: loss time m23 even. Caro h6 Bh7 Nd7 Bxd3 e6 Be7 shell, O-O Re8 Rc8 b6 Qd7 Kh8 Nd5 Nf6 burned 40-70s to 0:17 vs 11:37 flagged. 0 illegal.
- T77-3rd W vs Flash: draw m37 down N. h4/h5/Bd3/Qd2/O-O-O/Kb1 shell, Qe2/Qd2 vs Nd5/b5/Qb6, a3/Rc1/c5/Nd4/Ka2 5:08/d4 8:17/f4??/f5?!/Nc2?? met b3+/bxc2+ won N, Nxe3, Qf3/Qe3 loop drew. 4 illegal.
- T77SF1G1 B vs SF: loss forfeit m36 down 9. 6...d6??/7...a5?! met Bxc6/Ba4, 8...Nxe4?/12...d5?/21...gxh4 gated/34...Kf8 gated, 3x invalid forfeited. 4 illegal.
- T77R4 B vs Sonnet: loss forfeit m43 down R+P. d3 Ruy Nd8-Ne6-Kh8-Qb8-Rc6-Nf4 shell met Bxf4/d4/exd4/Bxd4/cxd4, 35...Re6??/36...Rb6? pinned Qf2-Qa7 met e5+/Rxd6/exd6/Re8+, 3 gated invalid forfeited. 4 illegal.
- T77R3 B vs Flash: draw m40 threefold up B. 8...Bg4/9...Bh5/10...Bg6 passive vs Be3/d4, 17...Rb8??/18...a6?? met Bd5/f3/Re3 clamp eyeing b7/f7, 24...c5 8:13/25...Qc7 5:47 burned to 0:52 vs 49:08, Qe2/Qd2/Kh shuffle drew. 3 illegal.
- T77R2 W vs SF: loss forfeit m14 Bd3. exd5/Nxd5/Qxd5/c3? met Nxd4/Bxd4, Rd8/Qa5/Bf5 won B, 3x tool-refused forfeited. 0 illegal.
- T77R1 W vs Flash: win forfeit m28 up P. g4/h4/h6/g5/f4/f5 storm vs Qc7/a6/b5/Bb7/Ne5/Nfd7/Bf6, 23.Nb5! hit Qd8, 24.f5! met gxf5 25.exf5 won P. 4 illegal.
- T76-3rd B vs Flash: loss forfeit m43. 10...c6??/14...c5??/15...b4?? met Nxf6+/Bxf6/Nd2-c4-a5-Nd5, 20...Ne7 3:59/22...Rfe8 3:02/23...Ne5 3:29/24...Qe7 3:21/25...Ng6 3:10 to 1:07 vs 44:58, 3x invalid forfeited. 2 illegal.
- T76SF2G2 W vs SF Armageddon: loss time m16 down piece. 10.Bc4?? vs Nxe3/Bxd4 to +9, Qd3/Qa5/Bg7/Qd2/Rd8 slow 1-2min burned to 1:19 vs 10:09 flagged. 0 illegal.
- T76SF2G1 B vs SF: draw m42 threefold down 8. 4...Nc6/d6/Nf6/e5-Ne4/Ng5?? met Bxg5/f6/exf6 to +9, Qb3/Bd3 clamp, Na5/Rb8/Ra8/Bb7/Bb4/Rc8 shell, Kg8/Kh8 15-30s loop drew. 3 illegal. Banked 27:08 vs 66:59.
- T76R5 B vs SF: draw m21 threefold down 6. 3...Nd7 before cxd4 met d5 clamp, Qc7 met Bc4+ fork cycle, Kg8/Kh8 shell drew vs +5/+7. 4 illegal.

## Key lessons (read before EVERY move)
- LEGALITY FIRST: after 1 reject redraw FEN, pick different piece AND idea, never resend stale UCI. 3 rejects forfeit, tool refusal = reject. T76-3rd 3x at m43 with 1:07 left forfeited; T77R2 3x after Bf5 forfeited; T77R4 3 gated in check forfeited; in check list replies once and send in 5-10s.
- TOOL AVOID IS AN ORDER: T76R1 Qxa2 x3 though tool flagged Rxa2; T75-3rd Kb1 x3 though tool named only -1P while down 2R; T77R2 3x after Bf5 down B forfeited; T78R1 Rd8+ gated in check forfeited. After one refusal switch piece and idea at once, never resend flagged UCI. DOWN LOST FLOOD: when every legal is flagged, read once, send least-bad DIFFERENT move in ONE try, never burn 3 tries proving lost.
- FOUR KNIGHTS ND5 POISON: vs 6.Nd5 Nxd5 only, never d6/Nxe4. d6 meets Bxc6 winning P, Nxe4 meets Nxc6/d4 fork. After Nxd5 exd5 e4 level, Bd6/Qh4 tempo. Castle early, no early queen sortie.
- OPEN QA5+/QXA2 POISON: 4...Qa5+?? after Nxd4 meets Nc3 tempo, no follow check. Never Qxa2 under Ra1 to Rxa2. Play Nf6/Nc6/e6, never early queen sortie. If queen hit retreat at once.
- RUY NA5/C5/C6/C5 POISON: T76-3rd 10...c6?? chases Nd5 weakens d6, 14...c5?? hits Bd4 opens d5, 15...b4?? meets c3/Bxf6 gxf6 doubling. Nd2-c4-a5-Nd5 outpost won. Keep Ne7/Nc6/Bd7/Re8, hold d6 twice, meet d4 exd4 only, never c5/b4 while d5 loose.
- YUGOSLAV BC4 POISON: T76SF2G2 10.Bc4?? vs Nxe3/Bxd4 to +9. Same as T63R3 11.Bc4? Nxe3. Never Bc4/Bb3 attacking d5 while Be3 loose to Nf6/Nd5. Before any Bc4 sweep Nxe3/Bxd5, trade Nxd5 first or guard Be3 twice. Keep Be2, f3/Qd2/O-O-O order.
- ITALIAN BG4/BB6/RB8 POISON: T77R3 8...Bg4?/9...Bh5/10...Bg6 passive vs Be3/d4, 17...Rb8??/18...a6?? met Bd5/f3/Re3 clamp eyeing b7/f7. Contest e/d with Rfe8/Rad8 first, Qe7/h6 after, never Rb8/a6 while Bd5 lives.
- NAJDORF E5/F4 SHELL POISON: T78R4 e5/Be6/O-O vs Be2/Be3/O-O/f4, exf4/Bxf4/Nc6/d5/Nxd5/Bxg5/Bh6 then Qc8??/Qc7?/Qb6?!/f6??/Re7?/Rd7?/Rc7??/Rfe8??/Ng6??/Ne5?/Kh8?!/Kg7?/Kg8? burned 2-3min each to 4:45 vs 22:28. Keep Be7/O-O/Qc7/Nc6/Rfd8, no Bh6/Rb8/Qc8 while Nc5 lives, no f6 while Bf3 lives, no queen/rook/king shuffle.
- DRAGON D5/QA5/BF5: T77R2 exd5/Nxd5/Qxd5/c3? met Nxd4/Bxd4 Rd8 pinning Qd2, Qa5 hit c3, Bd3?? Bf5 won B; T78R1 9.Be2?? vs d5 met Nxd4/Bxd4 dxe4 won e-pawn, 11.Bxf6? met Qxd2+/Rd8+ Bxf6 won B. Vs d5 resolve exd5/Nxc6 at once, never passive Be2 holding tension. Never c3 blocking Bc1 while Qa5 lives; never Bd4 vs Bf5; Bh6 drops c3 held only Be3+Qd2.
- QUEEN FORK AND E-FILE: Qe3 meets Nd5 hitting queen+knight. With Ke1 and empty e2 keep queen on e-file guarding d2/e2. Qc1 allows double plus Rd2+. List jumps, keep Rd1 first. Vs Qe3+ Kf1/Kh1 abandons Qd2 must Qxe3/block.
- DESTINATION SWEEP EVERY move, pawn captures first, then knights/sliders/king; quiet never makes square safe. MOVER ABANDONS GUARD: name what left and who hits it now.
- MAROCZY PIN POISON: 7.Bd2 met Nxd4 winning N, 8.Be3 met retreat holding it. Never block pin with bishop leaving knight loose. Support pawn first.
- ADVANCE F4/G4 F5 KILL: Bg6+e6/d5 vs f4/g4 means f5! hits e6+g6. Never park Bg6 vs f4; meet f4 with f6/h5 first, keep Bf5 mobile/trade before g4, never c5 leaving d5 on e6 only. Keep Kg8 vs h-storm.
- H-FILE BATTERY KILLS KG6: Rh1+Qh4+h5 vs Kh7/g6, 42.hxg6+ forced Kxg6, 43.f5+ opens, Qh5# with g5 blocking. Keep king g8 off h-file, keep f7 closed.
- CLASSICAL E5 BREAK WINS PAWN: vs Bd6/Nd7/Re8/Qc7 e5 hits d4. dxe5 allows Bxe5 won P then Ne5 hitting Q/Nf3. Meet e5 tense, never dxe5 without Nxe5 counted twice; Bd3 blocks c1, b3/a3 loosens.
- BD4/NE4 INVITE WINNING RECAPTURE: Bd4 blocking Be5 allows Bf4 hitting f4/Ng3 tempo, Bf4/Bxg5 wins, Bxc1/Rxd1/Rxc4 down exchange+. Prefer Qe2/f4 hold, never Bd4 while f4/Ng3 loose, never Ne4 while e4 loose to pawn, never c5 dropping e5, never b3 while c1 loose. Hold e5/f4 twice first.
- C-CLAMP+H-RUNNER MATE: c5-c4-c3 fixes b4/b2, h4 with Nf4 covers e2/g2, Rc1# mates Kf1 boxed. Vs Nf4 keep Ke1/d1 central, R second rank covering c1/e2, never Kf1 while Nf4 lives.
- F-FILE ABANDON/BLOCK SAC: Rfc1 left f-file to mate on f2. Bishop block invites rook sac into queen checks and mate. List sac plus checks, keep luft first.
- CARO CLAMP KILLS B3/KB2: vs c5/c4/b5/b4+Qb6 b3 opens c3 to cxb3 winning N, Rxc3/Rxc2+ won N+B. T77-3rd Ka2 walked into b3+ tempo, 28.Nc2?? met b3+ Kb1 bxc3+ won N; d4? met exd4 freeing c5, f4?? hit Be5 met Bf6. Keep Kb1 never Ka2, Rd1/Rd2, Be1/Bd2, Qf3, no push/Nc2 while b4/a5 lives.
- ENGLISH SUSPECT GRABS: Bxh3 costs dark bishop+Bf8 tempo; Bxc4 b3/b4/b5/b6 chases queen. Only with Re8/d6/e5 held. Vs dxe5 Nxe5 never Nh7 passive. Hold c5 twice or Qc6/Be6.
- ENGLISH ND4/NA5 POISON: Nd4 needs exd4 at once opening e-file vs Nc3, never Bf5/Be6 retreat leaving N en prise. Na5-Nc6 shuttle vs Qd3 loses 2 tempi. Vs e4 never d5 opening e6, hold c5/e5 first. Vs b4-b5 Na5 hits c4 once.
- BLOCKER LEAVES QUEEN: Nd4 blocked Rd1-Qd7, Nb4 unblocked it so Rxd7 won Q. Before moving blocker move queen off d-file or guard it.
- UP PIECE FINISH, NO SHUFFLE DRAW: T77R3 up B shuffled Qe2/Qd2/Qd1/Kh7/Kh8 into threefold; T75R1 up Q shuffled Qa7/Qa8/Qb8/Rc8/Rd8 while Kg1/Kg2 repeated. Up = centralize Q, trade rook with recapture named, checks first, luft once. Down N T77-3rd Qf3/Qe3 loop drew. T78R3 d7 vs Bd8/Rf5/Rb8 blockade Kc2/Kc3 shuffle flagged: passer needs rooks behind it, keep queens, no king shuffle.
- SHELL CLOCK: T77-3rdB 40-70s to 0:17 even; T77R3 3-8min x6 to 0:52 up B drew; T78R3 1-4min to 1:21 flagged even; T78R4 2-3min x10 to 4:45 vs 22:28 forfeited even. Routine 10-20, cap 60, never 2-4min. Down = 5-10s, invite repeats. Armageddon Black level = 5-15s shell.
- MATERIAL FROM BOARD EVERY move, equal trades preserve deficit.
- CLOCK: routine 10-20s, capture 30-40, cap 60, up 5-15, low 3-5.
- WHITE SCHEVENINGEN HASTE: T78R3 f4?!/Bxf4?? vs e5 wedge lost tempo into Re8 pin, Qc3??/Qd4??/a3??/Qxc5?! traded into dead blockade. Qe1/Qe2 waste tempi; f5?? Bxd4, 18.Rb1?? missed recapture. RECAPTURE FIRST. Storm only e4 twice/f5 counted; Bd3 blocks c1. T77R1 Nb5!/f5! 10-20s.
- E4 GRAB QA4+ TRAP: with Ke1 uncastled + Qa5 alive, Nxe4?? meets Nc6 hit plus b4 or Qa5+ Bd7 Qxe4. e4 held by nothing after cxd4/cxd4/d4. Before grab list Qa4+/Qb5+/Bb5+, keep Nc6 or second guard. Run tools/qa4-trap.py.
- NE4-NG5 POISON VS C3/QB3: T76SF2G1 Nc6/d6/Nf6/e5-Ne4/Ng5?? met Bxg5/f6/exf6 to +9. Never Ng5 vs Bd3/e5 clamp; keep Ne4 central or trade. Meet Qb3 with Qc7/a6, e6 only after Be7/Bd7, hold d5 twice first.
- SCHEVENINGEN QB8/RB8/RE6 POISON: Qc7/Rac8/Rfe8 passive vs f4/e5. Qb8 leaves Rb8 on Bg3 diagonal. T77R4 25...Qb8?/28...Rc6?/29...Nf4?/30...gxf4 opened, 35...Re6??/36...Rb6? blocked Qf2-Qa7 but got pinned met e5+/Rxd6/exd6/Re8+. Vs f4/Nf5/e5 never d5??. Never block queen-queen with rook that gets pinned.
- RUY BERLIN D3 LOCK: c3/Re1/Nbd2/Bc2/Nf1-g3/h3, d4 only with e4 twice, d5 locks knight must retreat. c4?! weakened, Bd3/Bc2 shuffled vs Nf4+Bxg5/Nf3/g3 only after Kh1/Qe3 hold f3, then Kg2/Kh2 shell fast.
- RUY E4 ABANDON: e4 held only by Nc3 vs Nf6/Re8/Bb7. Ncxd4 abandons e4 to Nxe4. Recapture Nfxd4 to keep Nc3 on e4, or hold e4 twice first.
- F3 KICK INVITES NXC3: f3 hits Ne4 but Ne4 has Nxc3 hitting Qe2 tempo, then c5 kicks Nd4. List escapes before pawn kick. Prefer Bxe4/Qxe4.
- SICILIAN CXD4 FIRST + C3: never Nf6/Nc6 holding vs d4, always cxd4 first. Vs 4.c3 never Nc6 holding: 5.cxd5 d5 forks. Answer c3 with Nf6/dxc3/e6 first. Hold e5/c5 with Be7/O-O/Nd7-Nc5/Bb7/Qc7. Bans: Qb6 allows b3, Rxd8 gives file, Kh8 shuffle, Qf6 lets king centralize. T76R5 Nd7 before cxd4 met d5 clamp into Bc4+/Nf7+/Nxd6+ cycle. 4 illegal.
- BB5 PIN SHELL: vs Bb5/Ba4/Bb3 play Bd7/a6/b5 tempo, e6/Be7/O-O/Qc7. Ne5-Ng6-Nf4 hit Qe2, c4/b4 tempo, bxc3 wins N. Keep e6 closed.
- ARMAGEDDON WHITE CLOCK: Black draw odds so draw = loss. Down huge still 5-10s, no 1-2min thinks, no pushes, keep Qd2/Nc3/a3 only if instant.
- RUY D3 LOCK EXTRA: d4 only held twice, c4 weak vs b4/c5. Meet Nf4 with g3 after Kh1.

## Openings
- B Ruy Closed: a6/b5/Be7/d6/O-O, Na5 only with tempo. Never c6 chasing Nd5, never c5/b4 while d5 loose. Hold d6 twice, Bd7/Re8/Qc7, meet d4 exd4 only.
- B Bb5: Bd7/a6/b5/e6/Be7/O-O/Qc7. Ne5-Ng6-Nf4 hit Qe2, c4/b4 tempo, bxc3 wins N. Keep e6 closed.
- B Nxc6: bxc6/Bd3/e5 shell, Nd7-Nc5, Bb7/Qc7. Bans: queen sortie, rook trade, king shuffle. CXD4 FIRST.
- B English: d6/Be7/O-O/Re8/Be6/Qc7. Bxh3/Bxc4 only if held else Be6/Qc6. Vs dxe5 Nxe5 at once never Nh7, Qd7 off d-file before blocker leaves. No Nd4 without exd4. Vs b4-b5 Na5 hits c4 once.
- B Scheveningen: Be7/O-O/Bd7/Qc7, no Rac8/Rfe8 vs f4/e5. Vs e5 dxe5 Nxe5 only if Bf4 met Ng6 with e5 held twice; no Qb8 leaving Rb8, no Nd5 without recapture. No d5?? vs Nf5. Vs c3/Qb3 hold d5 twice, Qc7/a6 first, never Ng5 vs Bd3.
- B Advance: Bf5 e6 Nd7 Ne7 early. Meet f4 with f6/h5 first, never Bg6 park vs f4/g4, never c5 alone, keep Kg8 vs h-storm.
- W Ruy d3 Berlin: c3/Re1/Nbd2/Bc2/Nf1-g3/h3, d4 only held twice, d5 locks, no c4 vs b4/c5, meet Nf4 with g3 after Kh1. Kg2/Kh2 shell fast.
- W Classical: Bd3, Be3 holds d4 twice, O-O-O Kb1, Rg1 holds g2. Vs c5/c4/b5/b4 keep Kb1/Rd1/Qf3, never b3/Kb2. Vs Bd6/e5 never dxe5, never Bd4/Ne4 while f4/Ng3/e4 loose, never c5 dropping e5, never b3 while c1 loose. Hold e5/f4 twice first.
- W Yugoslav: central bishop fix over risky develop. Dragon bxc6 opens file, Qa5 hits c3, Bh6 drops c3 held only by Be3+Qd2. Keep Be2, king central, no b3, contest b-file first. Never Bc4 while Be3 loose to Nxe3. Vs ...d5 Be2/O-O-O first, never c3/Bd3 into Rd8/Qa5/Bf5.
- W Taimanov: Be2 f3 Qd2 Bd3 castle long Kb1. Storm g-push/h-push/h-break/Q-double vs shell.
- W Maroczy: c-pawn clamp, knight develops, bishop supports. Vs Qa5 pin support first then castle.

## Opponents
- Haiku: Open Sicilian Nxc6 patient, trades rooks, centralizes king, Nf5+. Never shuffle king.
- GLM: Taimanov loose, hangs Q, banks then drifts. Fast 3-10s. Scheveningen Qc7/b6/Bb7/h6/Bf6/Rae8 solid to m20, takes free Bxd4/Bxe3/Nxb5, up +3/+6 drifts to allow threefold. T77R1 Bf6??/Nc6?!/Nd7?? forfeited replying f6. T78R3 even blockade Bd8/Rf5/Rb8 banked 28:19 vs 1:21 flagged me. English Rb1/Be3/Qd2/Rfd1 then b3-b6 passer. Punishes blocker leaving Qd7. Trade when up, luft first. Down shell fast 5-10s to draw.
- DeepSeek: keeps guarded, queenside dance. Classical Bd6/e5 won P then Bf4/Bxg3 wins N, c-clamp h-runner Rc1# vs Kf1+Nf4. Ruy Nc3/d3/Be3/Qd2/d4/Nd2-c4-a5-d5, punishes c5/b4, fast 5-20s banks clock (T76-3rd 44:58 vs 1:07). Flash fast when better, burns minutes when worse, 2-4 illegal tries, flags when down vs shell (T76R4 0:20 vs 20:39). Bank shell, no pushes.
- Sonnet: Ruy Na5/Nxb3/Bb7/Re8 solid, wins e5 after Ncxd4 via Nxe4/Nxc3; Berlin Bd7/Re8/h6/Bf8 shell holds e5, Nxe2/Nf4 outpost, avoids repeat Kg8/Kh7/Rb8/Rb7 to drain clock. Scheveningen patient 6-20s, shuffles Kg2/Kh2/Rd2/Red1 to flag when up. Takes every loose unit. T77R4 punished Nd8-Ne6/Qb8/Rc6/g5/Nf5 shell via Ng4/Nf5/h4/g4/d4.
- SF: punishes loose, pins, back rank, breaks. Instant, no gifts. Dragon d5 break, bxc6 opens file, Qa5/Rb8/Rd8 double kills. T75R3 Qc2! b4! won N to +5 in 2 moves. Castle early never long into open file, guard second rank, keep shell for repeat. T76SF2G1 +8 shell Kg8/Kh8 drew by repetition; no counterplay when down huge, invite loop.
- Fable: takes loose, trades queens when up, no luft. Model: fortress, checks, back-rank mate.

## Notes
- notes/caro-white.md - Classical draw win loss, H5 shell, queen grab poison and Rb2 mate.
- notes/caro-black.md - Advance loss and break and clock flag.
- notes/dragon-yugoslav-white.md - File and bishop fix and sac patterns.
- notes/english-e5-black.md - English win loss, Nh7/Nd5/Rxd7 and shell clock.
- notes/taimanov-white.md - Storm win plan and mate finish.
- notes/maroczy-white.md - Maroczy pin loss and shell clock.
- notes/sicilian-nxc6-black.md - Nxc6 forfeit, Qb6/Rxd8/Kh8 shell and tool trap.
- notes/sicilian-bb6-black.md - Bb5 pin win on time, Nf4/Qe2 tempo and up-piece shell.
