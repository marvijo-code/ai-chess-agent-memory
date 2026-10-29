# Chess memory - Muse Spark 1.3 Contributor (3600+10)

## Record
- T75R3 B vs SF: loss on time m30. c3 Nc6 cxd4 Nf6 d5 Nb8 retreat. Qa4 b6?! Nd4 Nxe4 Nc6 b4 Bf5 bxc5. Bd3 Bg6 Bxe4 f5 down +10. Rc7 Qd7 e6 Qe7 Kd8 c4-c3 d5 Be7. Flagged 0:26 vs 64:59. 2 illegal.
- T75R2 W vs Sonnet: draw threefold m51. Ruy d3 Berlin, d4/d5 lock, Nxe2/Nf4 outpost, Bd3/Bc2 shuffle 4x, g3 kick, Kg2/Kh2 loop vs Kg8/Kh7/Rb8/Rb7/Rf8/Rc8 held draw 2:57 vs 57:40. 1 illegal.
- T75R1 B vs DeepSeek V4.1 Flash: draw threefold m42 up Q. Nf6 before cxd4 (2 tries illegal) Nc6?! e5 d5?? met Nxe7+/Nxd5/Nxf6+ Qxd7 winning pieces, Rxd4?? met Qxb6 winning Q, Qa7/Qa8/Qb8/Qc8/Rc8/Rd8 shuffle drew Kg1/Kg2. 3 illegal, left 26:52 vs 40:11.
- T74R5 B vs Sonnet: loss on time m35. Scheveningen Nf6?! before cxd4 (2 tries stale), Nc6 (2 tries), e5 break level, Rac8/Rfe8/Rcd8/Rd7/Bf8/Ree7 shuffles 2-5min each, flagged 0:17 vs 57:55. 2 illegal.
- T74R4 B vs SF: loss mate m47. Sicilian d6 cxd4 c3 Nc6 cxd4 Nf6 d5 Nb8 Be3 Nxe4?? met Qa4+ Bd7 Qxe4 winning N. Shell down N to Qxh6+ Nf6#. 6 illegal, left 7:24 vs 67:49.
- T74R3 W vs DeepSeek: loss mate m48. Classical h4/h5/Bh7/Bd3/O-O-O/Kb1, c3 met Bd6/e5 dxe5 Bxe5 won P, Bd4? met Bf4/Bxg3 won N, Qb4/Qxb4/cxb4 R ending down N+P, c5-c4-c3 h4 runner Rc1# Nf4 covers e2/g2. 2 illegal.
- T74R1 B vs GLM: loss on time m51. English d6/Be7/O-O/Re8/Be6/Qd7/Rad8/h6/Bf8/a6, Na5-Nc6 shuttle 2 tempi, d5??/Ne5??/Qd6?? met cxd5/dxe6 winning B, Qxd4 won N, Rxd4/Rxd2/Rxb2 up exchange, burned 2-4min, flagged 0:42 vs 25:12. 2 illegal.
- T73-3rd B vs DeepSeek V4.1 Flash: loss forfeit m24 Bxd5+. Scheveningen Qc7/Rac8/Rfe8 passive, Nxe5! won P, Qb8?/Ng6??/Nd5??/Bc6?? lost it, Qxb8?/Rxb8 hung R to Bg3, Bxd5+ repeat Kf8 x3 over AVOID. 1 illegal.
- T73SF2G1 B vs SF: loss mate m27. Advance Bg6/Nf5/Bxf5/Be7/O-O, Bg6 vs f4+c5?! met f5! win, Bxf5/gxf5 dropped piece, g5/Kh8/Kh7/gxh4 into Qxh6/Qg7#. 1 illegal.
- T73R5 B vs Flash: draw threefold m46. Sicilian missed cxd4, Qe2 met Nxe4 winning P, up-P shell Qc6/Rad8/Kh8/Rb8/h6/g6/Bf8/Bf8/Bg7 held, Nh5/Nf6 vs Bg3/Bf4 loop drew. Banked 19:28 vs 2:07. 1 illegal.
- T73R4 W vs Sonnet: loss forfeit m30 Qe3+. Ruy Ba4/Bb3/Be3/d4, Ncxd4 left e4 to Nxe4, f3 met Nxc3 tempo Qe2, c5/cxd4 won N, Bg5/Bxe3+ won B, Rxe3/Rxe1+ won Rs. 3x Kf1 over AVOID forfeit. 3 illegal.
- T73R3 B vs GLM: win forfeit m14. English e5 Re8/Be6/Qd7/Rad8/h6/Bf8/a6, b4-b5 met Na5 hit c4, 3 invalid forfeit. 1 illegal.
- T73R1 W vs SF: loss mate m25. Maroczy Qa5 held then won bishop, f-file left for queen plus rook mate. 3 illegal.
- T72-3rd B vs GLM: loss on time m43. English shell burned 1-3min, Bf5??/Ne5?? lost piece, flagged 0:31 vs 11:31. 5 illegal.
- T72SF2G1 W vs Flash: loss forfeit m37. Classical H5 shell vs c5/c4/b5/b4 clamp, b3?? met cxb3/bxc3+ winning N, Rxc3/Rxc2+ won N+B. 2 illegal.
- T72R3/R2/R1+T71R4/R3: wins flag/forfeit vs GLM/Flash (Bb5 pin bxc3 won N, e5 shell), losses time/mate vs GLM/SF/Sonnet (Qf2#, Qh5#). 14 illegal total.

## Key lessons (read before EVERY move)
- LEGALITY FIRST: walk piece from actual square to destination. T75R3 cxd4 first took 2 tries illegal, Qc7 return 2 tries stale; T75R2 Bd3 took 2 tries invalid; T75R1 Nf6 before cxd4 took 2 tries illegal, Qxf6/Rcd4/Rc8 each 2 tries stale; T74R5 Nf6/Nc6 each 2 tries stale before cxd4, T74R4 cxd4/Nc6/Bd7/Kg8/b3, T72 exd5/Bd3/Kg1, T73 Kf1/Bf3/Qf2 each 2-3 tries stale. After 1 reject pick different piece AND idea, never resend. 3 rejects forfeit. Use tools/legal-list.py UCI list.
- TOOL AVOID IS AN ORDER: T73R4 Kf1 x3 over AVOID, T71R1 Kd7 x3, T73-3rd Kf8 x3 each forfeited. After one refusal switch piece and idea at once, never resend flagged UCI even if legal.
- E4 GRAB QA4+ TRAP: with Ke8 uncastled + Qa4 alive, Nxe4?? meets Nc6 hitting Q plus b4 opening (T75R3 b4! won N, +2 to +10) or Qa4+ Bd7 Qxe4 winning N (T74R4). e4 held by nothing after cxd4/cxd4/d5 (Nf3/d4 do not guard e4). Before any Nxe4/Bxc3 grab list Qa4+/Qb5+/Bb5+ checks, keep Nc6 on board or second guard, need Bd7 covered twice. Run tools/qa4-trap.py.
- SCHEVENINGEN QB8/RB8 HANG: Qc7/Rac8/Rfe8 vs f4/e5 passive. Qb8 to hold e5 leaves Rb8 on Bg3-b8 diagonal. Before Qxb8 recapture walk Bg3-f4-e5-d6-c7-b8. Ng6 hits Bf4 but abandons e5/d5; Nd5 needs Nxd5 counted; Bc6 holds once. Vs f4/Nf5/e5 never d5?? opening (T75R1 Nxe7+/Nxd5/Nxf6+ Qxd7 won pieces).
- QXE3 HOLDS QUEEN IN CHECK: vs Qe3+ on g1-a7 diagonal Kf1/Kh1 abandons Qd2 to Qxd2. Must capture Qxe3 or block. Name what king move abandons.
- RUY BERLIN D3 LOCK: c3/Re1/Nbd2/Bc2/Nf1-g3/h3/Bb2, d4 only with e4 twice, d5 locks knight must retreat. T75R2 c4?! weakened, Bd3/Bc2 shuffled 4x vs Nf4 guarded by e5 (marks ?!). Meet Nf4+Bxg5 with Nf3/g3 only after Kh1/Qe3 hold f3, then Kg2/Kh2 shell. Never shuffle bishop while e5 holds knight.
- RUY E4 ABANDON: e4 held only by Nc3 vs Nf6/Re8/Bb7. Ncxd4 abandons e4 to Nxe4. Recapture Nfxd4 to keep Nc3 on e4, or hold e4 twice first.
- F3 KICK INVITES NXC3: f3 hits Ne4 but Ne4 has Nxc3 hitting Qe2 tempo, then c5 kicks Nd4. List knight escapes before pawn kick. Prefer Bxe4/Qxe4.
- SICILIAN CXD4 FIRST + C3: never Nf6/Nc6 hold vs d4 (T75R1 Nf6 2 tries illegal, T74R5 Nf6?!), always cxd4 first. Vs 4.c3 never Nc6 holding d4 pawn: 5.cxd4 d5 forks Nc6/Nf6 forcing Nb8 retreat losing tempo (T75R3, T74R4). Answer c3 with Nf6/dxc3/e6 first. Vs bxc6/Bd3/e5 hold e5/c5 with Be7/O-O/Nd7-Nc5/Bb7/Qc7. Bans: Qb6 allows b3, Rxd8 gives file, Kh8 shuffle, Qf6 lets king centralize.
- BB5 PIN SHELL: vs Bb5/Ba4/Bb3 play Bd7/a6/b5 tempo, e6/Be7/O-O/Qc7. Ne5-Ng6-Nf4 hit Qe2, c4/b4 with tempo, bxc3 wins N. Keep e6 closed. T75R3 b6?! without Bd7 weakened c6/a7 to Nd4/Nc6/Qc2/b4.
- DRAGON BXC6 QA5: after bxc6 Qa5 hits c3 at once. Bh6/Qxh6 abandons c3 held only by Be3+Qd2. Keep Be2, king central, no b3, contest b-file first.
- QUEEN FORK AND E-FILE: Qe3 meets Nd5 hitting queen+knight. With Ke1 and empty e2 keep queen on e-file guarding d2/e2. Qc1 allows double plus Rd2+. List knight jumps, keep Rd1 first.
- DESTINATION SWEEP EVERY move: pawn captures first, then knights/sliders/king; development/quiet never makes square safe. MOVER ABANDONS GUARD: name what left and who hits it now.
- MAROCZY PIN POISON: 7.Bd2 met Nxd4 winning N, 8.Be3 met retreat holding it. Never block queen pin with bishop leaving knight loose. Support pawn first.
- ADVANCE F4/G4 F5 KILL: Bg6+e6/d5 vs f4/g4 means f5! hits e6+g6. Never park Bg6 vs f4; meet f4 with f6/h5 first, keep Bf5 mobile/trade before g4, never c5 leaving d5 on e6 only. After f5 Bxf5/gxf5 drops piece. Keep Kg8, h6 covered.
- H-FILE BATTERY KILLS KG6: Rh1+Qh4+h5 vs Kh7/g6 means hxg6+ forces Kxg6, f5+ opens, Qh5# with g5 blocking. Keep king g8 off h-file, keep f7 closed.
- CLASSICAL E5 BREAK WINS PAWN: vs Bd6/Nd7/Re8/Qc7 e5 hits d4. dxe5 allows Bxe5 winning P then Ne5 hitting Q/Nf3. Meet e5 tense, never dxe5 without Nxe5 counted twice. List e5 fork before dxe5.
- BD4 INVITES BF4 WINNING N: Bd4 blocking Be5 allows Bf4 hitting Ng3 tempo, Bxg3 wins N, Be5 blocks then Bxd4 simplifies down N. Prefer Qe2/f4 hold, never Bd4 while Ng3 loose to Bf4.
- C-CLAMP+H-RUNNER MATE: c5-c4-c3 fixes b4/b2, h4 with Nf4 covers e2/g2, Rc1# mates Kf1 boxed. Vs Nf4 keep Ke1/d1 central, R second rank covering c1/e2, never Kf1 while Nf4 lives.
- F-FILE ABANDON/BLOCK SAC: Rfc1 left f-file to queen+rook mate on f2. Bishop block invites rook sac into queen checks and mate. List sac plus checks, keep luft first. Use f2-guard idea.
- CARO C4/B4 CLAMP KILLS B3/KB2: vs c5/c4/b5/b4+Qb6/Rc6 b3 opens c3 to cxb3/bxc3+ winning N, then Rxc3/Rxc2+ win N+B. Keep Kb1 never Kb2, Rd1/Rd2, Be1/Bd2, Qf3, no push while c4 lives.
- ENGLISH SUSPECT GRABS: Bxh3 wins h-pawn but costs dark bishop+Bf8 tempo; Bxc4 wins pawn but b3/b4/b5/b6 chases queen. Only with Re8/d6/e5 held. Vs dxe5 Nxe5 never Nh7 passive. Hold c5 twice or Qc6/Be6.
- ENGLISH ND4/NA5 POISON: Nd4 needs exd4 at once opening e-file vs Nc3, never Bf5/Be6 retreat leaving N en prise. Na5-Nc6 shuttle vs Qd3 loses 2 tempi. Vs e4 never d5 opening e6, hold c5/e5 first. Vs b4-b5 Na5 hits c4 once.
- BLOCKER LEAVES QUEEN: Nd4 blocked Rd1-Qd7, Nb4 unblocked it so Rxd7 won Q. Before moving blocker move queen off d-file or guard it.
- UP QUEEN FINISH, NO SHUFFLE DRAW: T75R1 up Q shuffled Qa7/Qa8/Qb8/Qc8+Rc8/Rd8/Rfe8/h6/g6/Kg7/Kg8 while Kg1/Kg2 repeated. Up Q = centralize Q, trade one rook with recapture named, checks first, give luft once. Repeating a loop up Q is a loss. UP P no Nh5/Nf6 repeat vs Bg3/Bf4 drew; trade not shuffle.
- SHELL CLOCK: T75R3 down +9 burned 5:45 Nxe4, 5:24 Bg6, 3:35 Bf5, 3:36 Rc8, 7:22 Qc7, flagged 0:26 vs 64:59; T75R2 burned 1-3min moves 13-36 vs 6-24s and left 2:57 vs 57:40; T75R1 burned 2-4min on e5/d5/Qd6/Qc8/Bb3/c3 while level/up and kept 26:52 vs 40:11; T74R5 flagged 0:17 with Rac8/Rfe8/Rcd8/Rd7/Ree7 each 2-5min; T74R1 flagged 0:42. Symmetric/up shuffle 5-10s, routine 10-20s, cap 60, never 2-4min in shell. Down huge = 5-10s, invite repeats. Bank clock.
- MATERIAL FROM BOARD EVERY move, recount guards, equal trades preserve deficit.
- CLOCK: routine 10-20s, capture 30-40, cap 60, up 5-15, low time 3-5. Time goes on destination list, never narrative.

## Openings
- B Sicilian Bb5: Bd7/a6/b5/e6/Be7/O-O/Qc7. Ne5-Ng6-Nf4 hit Qe2, c4/b4 tempo, bxc3 wins N. Keep e6 closed.
- B Sicilian Nxc6: bxc6/Bd3/e5 shell, Nd7-Nc5, Bb7/Qc7. Bans: queen sortie, rook trade, king shuffle. CXD4 FIRST.
- B English: d6/Be7/O-O/Re8/Be6/Bf8 hold d6/e5. Bxh3/Bxc4 only if held else Be6/Qc6. Vs dxe5 Nxe5 at once never Nh7, Qd7 off d-file before blocker leaves. No Nd4 without exd4, no Kh8/a6/Bf8 shuffle. Vs b4-b5 Na5 hits c4 once.
- B Scheveningen: Be7/O-O/Bd7/Qc7, no Rac8/Rfe8 vs f4/e5. Vs e5 dxe5 Nxe5 only if Bf4 met Ng6 with e5 held twice; no Qb8 leaving Rb8, no Nd5 without recapture. No d5?? vs Nf5.
- B Advance: Bf5 e6 Nd7 Ne7 early. Meet f4 with f6/h5 first, never Bg6 park vs f4/g4, never c5 alone, keep Kg8 vs h-storm.
- W Ruy d3 Berlin: c3/Re1/Nbd2/Bc2/Nf1-g3/h3/Bb2, d4 only held twice, d5 locks, no c4 vs b4/c5, meet Nf4 with g3 after Kh1. Kg2/Kh2 shell fast.
- W Classical: Bd3, Be3 holds d4 twice, O-O-O Kb1, Rg1 holds g2. Vs c5/c4/b5/b4 keep Kb1/Rd1/Qf3, never b3/Kb2. Vs Bd6/e5 never dxe5, never Bd4 while Ng3 loose.
- W Yugoslav: central bishop fix over risky develop. Dragon bxc6 opens b-file, Qa5 hits c3, Bh6 drops guard. Keep Be2, king central, no b3, contest b-file first.
- W Taimanov: Be2 f3 Qd2 Bd3 castle long Kb1. Storm g-push h-push g-break Q-double vs shell.
- W Maroczy: c-pawn clamp, knight develops, bishop supports. Vs Qa5 pin support first then castle.

## Opponents
- Haiku: Open Sicilian Nxc6 patient, trades rooks, centralizes king, Nf5+. Never shuffle king.
- GLM: Taimanov loose, hangs Q, banks then drifts. Fast 3-10s. English Rb1/Be3/Qd2/Rfd1 then b3-b6 passer. Punishes blocker leaving Qd7. Take free units after sweep, trade when up, luft first. Match pace, cap 60s.
- DeepSeek: keeps guarded, queenside dance. Classical Bd6/e5 wins P then Bf4/Bxg3 wins N, c-clamp h-runner Rc1# vs Kf1+Nf4. V4.1 Flash can play fast when better (T75R1 2-47s) while opponent burns; earlier burns minutes, 2 illegal tries, flags when down vs shell. Bank shell, no pushes.
- Sonnet: Advance e4/c3/Nbd7/a4, takes h4/g6 with tempo, doubles Rh1+Qh4 for h5 break. Ruy Na5/Nxb3/Bb7/Re8 solid, wins e4 after Ncxd4 via Nxe4/Nxc3; Berlin d6/Be7/O-O/Bd7/Re8/h6/Bf8/a6/b5/Na5/c5/Qc7 holds e5 4x, Nxe2/Nf4 outpost, avoids repeat Kg8/Kh7/Rb8/Rb7/Rf8/Rc8 to drain clock (T75R2). Scheveningen patient 6-20s, shuffles Kg2/Kh2/Rd2/Red1 to flag when up (T74R5 4 invalid tries). Takes every loose unit.
- SF: punishes loose, pins, back rank, breaks. Instant, no gifts. Dragon d5 break, bxc6 opens file, Qa5/Rb8/Rd8 double kills. T75R3 Qc2! b4! won N to +5 in 2 moves. Castle early never long into open file, guard second rank, keep shell for repeat.
- Fable: takes loose, trades queens when up, no luft. Model: fortress, checks, back-rank mate.

## Notes
- notes/caro-white.md - Classical draw win loss, H5 shell, queen grab poison and Rb2 mate.
- notes/caro-black.md - Advance loss break and clock flag.
- notes/dragon-yugoslav-white.md - File and bishop fix and sac patterns.
- notes/english-e5-black.md - English win loss, Nh7/Nd5/Rxd7 and shell clock.
- notes/taimanov-white.md - Storm win plan and mate finish.
- notes/maroczy-white.md - Maroczy pin loss and shell clock.
- notes/sicilian-nxc6-black.md - Nxc6 forfeit, Qb6/Rxd8/Kh8 shell and tool trap.
- notes/sicilian-bb5-black.md - Bb5 pin win on time, Nf4/Qe2 tempo and up-piece shell.
