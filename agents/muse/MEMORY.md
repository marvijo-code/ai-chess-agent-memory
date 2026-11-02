# Chess memory - Muse Spark 1.3 Contributor (3600+10)

## Record
- T78R5 B vs Sonnet: loss forfeit m42 even. Najdorf e6 Be7 O-O Nc6 Bd7 Qc7 Rac8 Rfd8, e5 Nxc6 bxc6 fxe5 dxe5, Re8 Bd6 Be6, Bb4 Nd7 Kh8 f6, 26...Nc5?? met Bxe6, Qf5+ flood flagged e5 forfeited. 2-4min to 16:09 vs 52:15.
- T78R4 B vs Flash: loss forfeit m45 even. Najdorf e5 Be7 O-O, exf4 Bxf4 Nc6 d5, Qc8 Qc7 Qb6 f6 Re7 Rd7 shell burned 2-3min to 4:45 vs 22:28. 2 illegal.
- T78R3 W vs Flash: loss time m55 even. English g4 g5 Nd5 f4 h4 vs Qc7 Rb8 O-O, d6-d7 vs Bd8 Rf5 blockade, Kc2 Kc3 shuffle flagged 1:21 vs 28:19. 2 illegal.
- T78R1 W vs SF: loss forfeit m13 down 3P. Yugoslav Be3 f3 Qd2 vs g6 Bg7 Nf6 O-O d5, 9.Be2?? met Nxd4 dxe4, 11.Bxf6? met Qd2+ Rd8+ won B, gated in check. 0 illegal.
- T77-3rdB B vs Flash: loss time m23 even. Caro h6 Bh7 Nd7 e6 Be7 shell, O-O Re8 Rc8 b6 burned 40-70s to 0:17 vs 11:37. 0 illegal.
- T77-3rd W vs Flash: draw m37 down N. h4 h5 Bd3 Qd2 O-O-O Kb1 shell vs Nd5 b5 Qb6, a3 Rc1 c5 Nd4 Ka2, f4 f5 Nc2 met b3+ won N. 4 illegal.
- T77SF1G1 B vs SF: loss forfeit m36 down 9. 6...d6 7...a5 met Bxc6 Ba4, 8...Nxe3 12...d5 gated, 3x invalid forfeited. 4 illegal.
- T77R4 B vs Sonnet: loss forfeit m43 down R+P. Ruy Nd8 Ne6 Kh8 Qb8 Rc6 Nf4 shell met Bxf4 d4 exd4, 35...Re6 36...Rb6 pinned met e5+ Rxd6. 4 illegal.
- T77R3 B vs Flash: draw m40 threefold up B. 8...Bg4 9...Bh5 passive vs Be3 d4, 17...Rb8 18...a6 met Bd5 f3 clamp, 24...c5 burned to 0:52 vs 49:08. 3 illegal.
- T77R2 W vs SF: loss forfeit m14 Bd3. exd5 Nxd5 Qxd5 c3 met Nxd4 Bxd4, Rd8 Qa5 Bf5 won B, 3x tool-refused. 0 illegal.
- T77R1 W vs Flash: win forfeit m28 up P. g4 h4 h6 g5 f4 f5 storm vs Qc7 a6 b5 Bb7, 23.Nb5 hit Qd8, 24.f5 met gxf5 won P. 4 illegal.
- T76-3rd B vs Flash: loss forfeit m43. 10...c6 14...c5 15...b4 met Nxf6 Bxf6 Nd2-c4-a5, 20...Ne7 22...Rfe8 burned 3min to 1:07 vs 44:58. 2 illegal.
- T76SF2G2 W vs SF Armageddon: loss time m16 down piece. 10.Bc4 vs Nxe3 Bxd4 to +9, Qd3 Qa5 slow 1-2min to 1:19 vs 10:09. 0 illegal.
- T76SF2G1 B vs SF: draw m42 threefold down 8. 4...Nc6 d6 Nf6 e5-Ne4 Ng5 met Bxg5 f6 exf6 to +9, Na5 Rb8 Bb7 shell, Kg8 Kh8 loop drew. 3 illegal.
- T76R5 B vs SF: draw m21 threefold down 6. 3...Nd7 before cxd4 met d5, Qc7 met Bc4+ cycle, Kg8 Kh8 shell drew. 4 illegal.

## Key lessons (read before EVERY move)
- LEGALITY FIRST: after 1 reject redraw FEN, pick different piece AND idea, never resend stale UCI. 3 rejects forfeit, tool refusal = reject. In check list replies once and send in 5-10s.
- TOOL AVOID IS AN ORDER: after one refusal switch piece and idea at once, never resend flagged UCI. T78R5 Qf5+ every block left e5 to Qxe5 so all flagged: read once, send least-bad DIFFERENT in ONE try. DOWN LOST FLOOD: never burn 3 tries proving lost.
- FOUR KNIGHTS ND5 POISON: vs 6.Nd5 Nxd5 only, never d6 Nxe4. d6 meets Bxc6 won P, Nxe4 meets Nxc6 d4 fork. After Nxd5 exd5 e4 level, Bd6 Qh4 tempo. Castle early, no early queen sortie.
- OPEN QA5+ QXA2 POISON: 4...Qa5+ after Nxd4 meets Nc3 tempo. Never Qxa2 under Ra1 to Rxa2. Play Nf6 Nc6 e6, never early queen sortie. If hit retreat at once.
- RUY NA5 C5 C6 POISON: 10...c6 chases Nd5 weakens d6, 14...c5 hits Bd4 opens d5, 15...b4 meets c3 Bxf6 doubling. Keep Ne7 Nc6 Bd7 Re8, hold d6 twice, meet d4 exd4 only.
- YUGOSLAV BC4 POISON: 10.Bc4 vs Nxe3 Bxd4 to +9. Never Bc4 Bb3 while Be3 loose to Nf6 Nd5. Sweep Nxe3 Bxd5 first or guard Be3 twice. Keep Be2, f3 Qd2 O-O-O order.
- ITALIAN BG4 BB6 RB8 POISON: 8...Bg4 9...Bh5 passive vs Be3 d4, 17...Rb8 18...a6 met Bd5 f3 clamp. Contest e-file with Re8 first, Qe7 h6 after, never Rb8 a6 while Bd5 lives.
- NAJDORF E5 TIMING: T78R4 e5 Be6 O-O vs Be2 Be3 O-O f4 burned 2-3min shuffling Qc8 Qc7 Qb6 f6 Re7 Rd7. T78R5 e5 hit Nd4 worked: Nxc6 bxc6 fxe5 dxe5! level, Re8 Bd6 Be6 hold e5. Never Nc5 while Be6 loose (Bxe6 wins pair), never f6 while Bf3 lives, never queen rook king shuffle.
- DRAGON D5 QA5 BF5: Vs d5 resolve exd5 Nxc6 at once, never passive Be2 holding tension. Never c3 blocking Bc1 while Qa5 lives. Never Bd4 vs Bf5. Bh6 drops c3 held only Be3+Qd2.
- DESTINATION SWEEP EVERY move, pawn captures first, then knights sliders king. Quiet never makes square safe. MOVER ABANDONS GUARD: name what left and who hits it now.
- MAROCZY PIN POISON: 7.Bd2 met Nxd4 winning N, 8.Be3 met retreat holding it. Never block pin leaving knight loose. Support pawn first.
- F4 G4 F5 KILL + H-FILE: Bg6 e6 d5 vs f4 g4 means f5 hits e6+g6. Never park Bg6 vs f4. Meet f4 with f6 h5 first. Keep Kg8 off h-file, keep f7 closed vs Rh1 Qh4 h5.
- CLASSICAL E5 BREAK: vs Bd6 Nd7 Re8 Qc7 e5 hits d4. dxe5 allows Bxe5 won P then Ne5. Never dxe5 without Nxe5 counted twice. Never Bd4 while f4 Ng3 loose, never Ne4 while e4 loose, never b3 while c1 loose.
- CARO CLAMP + ENGLISH GRABS: vs c5 c4 b5 b4 Qb6 b3 opens c3 to cxb3 won N, Nc2 met b3+ tempo. Keep Kb1 never Ka2, Rd1 Rd2 Be1 Qf3. Bxh3 costs dark bishop, Bxc4 b3 b4 chase queen. Only with Re8 d6 e5 held.
- BLOCKER LEAVES QUEEN: Nd4 blocked Rd1-Qd7, Nb4 unblocked it so Rxd7 won Q. Before moving blocker move queen off d-file or guard it.
- UP PIECE FINISH NO SHUFFLE: Up = centralize Q, trade rook with recapture named, checks first, luft once. Down = 5-10s, invite repeats. T78R3 d7 vs Bd8 Rf5 blockade: passer needs rooks behind it, keep queens, no king shuffle.
- SHELL CLOCK: Routine 10-20, cap 60, never 2-4min. T78R5 2-4min x8 to 16:09 vs 52:15 forfeited even. Down = 5-10s. Material from board every move, equal trades preserve deficit.
- WHITE SCHEVENINGEN HASTE: f4 Bxf4 vs e5 wedge level. Qe1 Qe2 waste tempi, f5 Bxd4, Rb1 missed recapture. RECAPTURE FIRST. Storm only e4 twice f5 counted. Nb5 f5 10-20s.
- E4 GRAB QA4+ TRAP: With Ke1 uncastled + Qa5 alive, Nxe4 meets Nc3 hit plus b4 or Qa5+ Bd7 Qxe4. Before grab list Qa4 Qb5 Bb5, keep Nc6 or second guard.
- SCHEVENINGEN QB8 RB8 RE6 POISON: Qc7 Rac8 Rfe8 passive vs f4 e5. Qb8 leaves Rb8 on Bg3. Never block queen-queen with rook that gets pinned. Vs Nf5 e5 never d5.
- RUY D3 LOCK: c3 Re1 Nbd2 Bc2 Nf1-g3 h3, d4 only with e4 twice, d5 locks knight must retreat. c4 weak vs b4 c5. Meet Nf4 with g3 after Kh1. Kg2 Kh8 shell fast.
- F3 KICK INVITES NXC3: f3 hits Ne4 but Ne4 has Nxc3 hitting Qe2 tempo, then c5 kicks Nd4. List escapes before pawn kick. Prefer Bxe4 Qxe4.
- SICILIAN CXD4 FIRST + C3: never Nf6 Nc6 holding vs d4, always cxd4 first. Vs 4.c3 never Nc6 holding: 5.cxd5 d5 forks. Answer c3 with Nf6 dxc3 e6 first. Bans: Qb6 b3, Rxd8 gives file, Kh8 shuffle.
- BB5 PIN SHELL: vs Bb5 Ba4 Bb3 play Bd7 a6 b5 tempo, e6 Be7 O-O Qc7. Ne5 Ng6 Nf4 hit Qe2, c4 b4 tempo, bxc3 wins N. Keep e6 closed.
- ARMAGEDDON WHITE CLOCK: Black draw odds so draw = loss. Down huge still 5-10s, no 1-2min thinks, no pushes, keep Qd2 Nc3 a3 only if instant.

## Openings
- B Ruy Closed: a6 b5 Be7 d6 O-O, Na5 only with tempo. Never c6 chasing Nd5, never c5 b4 while d5 loose. Hold d6 twice, Bd7 Re8 Qc7.
- B Bb5: Bd7 a6 b5 e6 Be7 O-O Qc7. Ne5 Ng6 Nf4 hit Qe2, c4 b4 tempo, bxc3 wins N. Keep e6 closed.
- B Nxc6: bxc6 Bd3 e5 shell, Nd7 Nc5, Bb7 Qc7. Bans: queen sortie, rook trade, king shuffle. CXD4 FIRST.
- B English: d6 Be7 O-O Re8 Be6 Qc7. Bxh3 Bxc4 only if held else Be6 Qc6. Vs dxe5 Nxe5 at once. No Nd4 without exd4.
- B Scheveningen: Be7 O-O Bd7 Qc7, no Rac8 Rfe8 vs f4 e5. Vs e5 dxe5 Nxe5 only if Bf4 met Ng6. No Qb8 leaving Rb8, no d5 vs Nf5.
- B Advance: Bf5 e6 Nd7 Ne7 early. Meet f4 with f6 h5 first, never Bg6 park vs f4 g4, never c5 alone, keep Kg8 vs h-storm.
- W Ruy d3 Berlin: c3 Re1 Nbd2 Bc2 Nf1-g3 h3, d4 only held twice, d5 locks, no c4 vs b4 c5, meet Nf4 with g3 after Kh1.
- W Classical: Bd3, Be3 holds d4 twice, O-O-O Kb1, Rg1 holds g2. Vs c5 c4 b5 keep Kb1 Rd1 Qf3, never b3 Kb2. Hold e5 f4 twice first.
- W Yugoslav: central bishop fix over risky develop. Keep Be2, king central, no b3, contest b-file first. Never Bc4 while Be3 loose. Vs d5 Be2 O-O-O first.
- W Taimanov: Be2 f3 Qd2 Bd3 castle long Kb1. Storm g-push h-push h-break Q-double vs shell.
- W Maroczy: c-pawn clamp, knight develops, bishop supports. Vs Qa5 pin support first then castle.

## Opponents
- Haiku: Open Sicilian Nxc6 patient, trades rooks, centralizes king, Nf5+. Never shuffle king.
- GLM: Taimanov loose, hangs Q, banks then drifts. Fast 3-10s. Scheveningen solid to m20, takes free Bxd4 Bxe3 Nxb5. Punishes blocker leaving Qd7. Trade when up, luft first.
- DeepSeek: keeps guarded, queenside dance. Classical Bd6 e5 won P then Bf4 Bg3 wins N, c-clamp h-runner Rc1# vs Kf1 Nf4. Fast 5-20s banks clock. Flags when worse.
- Sonnet: Ruy Na5 Nxb3 Bb7 Re8 solid, wins e5 after Ncxd4 via Nxe4 Nxc3. Berlin Bd7 Re8 h6 Bf8 shell holds e5. Scheveningen patient 6-20s, shuffles Kg2 Kh2 Rd2 to flag. Takes every loose unit. T78R5 punished Nc5 Be6 shuffle via Bxe6 h4 Nxh6.
- SF: punishes loose, pins, back rank, breaks. Instant, no gifts. Dragon d5 break, bxc6 opens file, Qa5 Rb8 Rd8 double kills. Castle early never long into open file, guard second rank, keep shell for repeat.
- Fable: takes loose, trades queens when up, no luft. Model: fortress, checks, back-rank mate.

## Notes
- notes/caro-white.md - Classical draw win loss, H5 shell, queen grab and Rb2 mate.
- notes/caro-black.md - Advance loss and break and clock flag.
- notes/dragon-yugoslav-white.md - File and bishop fix and sac patterns.
- notes/english-e5-black.md - English win loss, Nh7 Nd5 Rxd7 and shell clock.
- notes/taimanov-white.md - Storm win plan and mate finish.
- notes/maroczy-white.md - Maroczy pin loss and shell clock.
- notes/sicilian-nxc6-black.md - Nxc6 forfeit, Qb6 Rxd8 Kh8 shell and tool trap.
- notes/sicilian-bb6-black.md - Bb5 pin win on time, Nf4 Qe2 tempo and up-piece shell.
