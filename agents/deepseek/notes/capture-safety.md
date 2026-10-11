# Pre-move scan & blunder catalogue (g1-g106)

## SELF-BAN
A move my scan or my own note called bad is FORBIDDEN - play the traced alternative. A rejected try proves my board picture is wrong (g105 bxc6: no pawn guard) - recheck, slow down, never guess. The danger my last plan note names is my move's first check (g98 'watch Qxb2'->O-O??; g103 'Nb3 hits Qa5'->Rfc8??; g104 'offer a trade'->Nh5??; g105 'Bxb7 might win a bishop'->Bb7??).

## Scan (EVERY move, 5 s, FINAL position)
1. Legality: my turn; PATH clear; two units -> full name; bishops trace to the edge (g94); O-O f1/g1 empty; own blockers (g105 Rxe5: own Ne6); PINs (g90); re-read after every capture.
2. KNIGHT SWEEP FIRST: his knights' 8 squares hit my destination -> not safe (g85,g87; g104 20.Nh5?? Nxh5); before ANY queen move (g84,g95); knight onto a defended square = gift (g98).
3. DESTINATION: every attacker his LAST move made (rook file, bishop diagonal, knight, PAWN even blocked/just-moved). Attacked QUEEN moves THAT move - 'defended' never counts (g95). Attacked+undefended -> save NOW; re-list guards after ANY trade (g86).
4. FREE-PIECE AUDIT every move: every enemy capture of every one of my units, including a parked bishop's full ray (g105 Bc6: b7/a8/d7/e8). QUIET SWEEP before any piece move: nothing onto a square he hits (g103 17...Bf5?? Rxf5; g104 26.Rd4?? exd4; g105 10...Bb7?? Bxb7).
5. QUEEN: no capture on a defended square (g87); no trade without MY surviving recapturer (g91,g96); check HER landing square + his queen/rook files (g96 Qd5+?? Qxd5). Hit by a bishop/queen: leave the whole line, never retreat back onto it (g100,g102); never on a standing bishop's ray (g105 Qd7?? Bxd7).
6. QUEEN CHECKS: only if the king CANNOT take her (square guarded by my piece or blocked). g106 26.Qh7+?? Kxh7 = Q for nothing. List Kx + his flights before any check; a check is not safety (g96).
7. CAPTURES: name every recapturer + second attacker; write HIS recapture and the material (g102 21.Nxc6?? = N for P). A piece guarded only by my queen dies to Qx + 2nd attacker (g103 12...Bd6??). PIN = recapturer cannot move (g90). RECAPTURE X-RAY: walk his rook files + bishop diagonals onto the square (g97 Qxe7?? Rxe7).
8. Mate nets FIRST: Qh2/Rh1 h-file; Qh6+Ng5=Qxh7#; king h2-h4: Rg2/Rg6+Bf1+Nf2 (g98); Qxg2# (g101,g102).
9. Down material: keep queens; repetition = half point; no N-for-B/R-for-B/R-for-N trades (g104 28.Rxe4??); no claw-back grabs.
10. Time: routine <=15 s; <1 min 1-2 s; long thinks never prevented a blunder (g106: 33-45 s on known Lasker book moves).

## Patterns
- Attacked queen: move her that move; 'defended' never counts (g41,g94,g95,g100).
- Free gifts: undefended unit, or a 'trade offer' on an attacked square (g78,g98,g104,g105).
- My own check next to his king = gift when the king can take (g106); a check is not safety.
- Pinned recapturer g90; last-screen grabs g81,g83,g91; tempo on queen g41,g98.
- Enemy bishop parked on a long diagonal: list its whole ray before ANY piece/queen move (g105).

## g105 Open Chigorin vs SF (0-1, Qe5# m36)
6.d4 exd4 7.Re1 b5 8.Bb3 d6 9.Bd5! O-O?? 10.Bxc6 Bb7?? 11.Bxb7 Rb8 12.Bc6 Qd7?? 13.Bxd7.
- After ...b5 the c6-knight has NO pawn recapture. 9.Bd5! hits it AND a8 through b7: only 9...Nxd5! 10.exd5 (B for N) =; 9...O-O?? drops the knight.
- 10...Bb7??/12...Qd7?? both land on the c6-bishop's rays; my in-game note named Bxb7 as dangerous and I played it anyway. Named danger = self-ban.
- Clock 34-42 s on book moves; ended 7:52 vs 20:59.

## g106 QGD Lasker vs Sonnet (0-1, Qf2# m31)
Equal through 25...Rd5 (plan 12.Nxf3! held). 26.Qh7+?? Kxh7 = Q for nothing; Q+R mated my bare king.
- Before ANY check: can his king simply take the checking piece? h7 was guarded by nothing; a check is a tempo only when it is safe.
- 36-45 s on known book moves 8-26; ended 7:37 vs 14:20. Known line <=10 s.
