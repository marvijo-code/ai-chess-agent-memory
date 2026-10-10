# Pre-move scan & blunder catalogue (g1-g105)

## SELF-BAN
A move my scan called bad/illegal is FORBIDDEN; play the traced alternative; a rejected try proves the recapture does not exist (g105 illegal bxc6: no pawn guards c6) and my board picture is wrong - recheck, slow down. The danger my last plan note names is the first thing to check (g98 'watch Qxb2'->O-O??; g103 'Nb3 hits Qa5'->Rfc8??; g104 'offer a trade'->Nh5??; g105 'Bxb7 might just win a bishop'->Bb7?? anyway).

## Scan (EVERY move, 5 s, FINAL position)
1. Legality: my turn; PATH clear; two units -> full name; bishops trace to the edge (g94); O-O f1/g1 empty (g98); own blockers (g105 Rxe5: own Ne6); PINs (g90). Re-read after every capture.
2. KNIGHT SWEEP FIRST: his knights' 8 squares hit my destination -> recapture (g85,g87; g104 20.Nh5?? Nxh5); before ANY queen placement (g84,g95); knight onto a defended square = gift (g98).
3. HIS last move: list every attacker of my destination (rook, bishop, knight, PAWN). Attacked QUEEN moves THAT move - 'defended' never counts (g95). Attacked+undefended -> save NOW; re-list guards after ANY trade (g86).
4. FREE-PIECE AUDIT before every move: every enemy capture of every one of my units, including a bishop already parked on a long ray (g105 11.Bxb7, 13.Bxd7 - two one-movers). QUIET SWEEP: before any non-capture piece move list his attackers of the square - pawns (even blocked/just-moved), knights, rook files, bishop diagonals (g103 17...Bf5?? Rxf5; g104 26.Rd4?? exd4; g105 10...Bb7?? Bxb7).
5. QUEEN: no capture on a defended square (g87); no trade without MY surviving recapturer (g91,g96); check HER landing square and his queen/rook files (g96 Qd5+?? Qxd5). Hit by a bishop: leave the whole diagonal (g100,g101); never onto a standing bishop's ray (g105 12...Qd7?? Bxd7).
6. CAPTURES: name every recapturer + second attacker; write HIS recapture and the material (g102 21.Nxc6?? Bxc6; g104 25.Bxc2 Rxc2). A piece defended ONLY by my QUEEN dies to Qx + 2nd attacker (g103 12...Bd6??). RECAPTURE X-RAY: walk his rook files + bishop diagonals onto the recapture square (g97 Qxe7?? Rxe7).
7. Loose minor/rook: destination attacked by NOTHING; walk his bishop diagonals to the edge (g86,g78). A check is not safety.
8. Mate nets FIRST: Qh2/Rh1 h-file; Qh6+Ng5=Qxh7#; king h2-h4: Rg2/Rg6+Bf1+Nf2 (g98); Qxg2# (g101,g102).
9. Down material: keep queens; repetition = half point; no N-for-B/R-for-B/R-for-N trades (g104 28.Rxe4?? Rxe4); no claw-back grabs.
10. Time: routine <=15 s; <1 min 1-2 s. Long thinks never prevented a blunder (g86-g105; g105: 34-42 s on book moves).

## Patterns
- Attacked queen: move her that move; 'defended' never counts (g41,g94,g95,g100).
- Free gifts: undefended unit, or a 'trade offer' on an attacked square (g78,g98,g104,g105).
- Pinned recapturer g90; last-screen grabs g81,g83,g91; tempo on queen g41,g98.
- Quiet piece onto a square his rook/bishop owns, undefended: g103 17...Bf5??; g105 10...Bb7??.
- Enemy bishop parked on a long diagonal: list its whole ray before ANY piece/queen move (g105 Bc6 -> b7/a8/d7/e8).

## g105 Open Chigorin vs SF (0-1, Qe5# m36) - castled into Bxc6, then B and Q hung to one-movers
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.d4 exd4 7.Re1 b5 8.Bb3 d6 9.Bd5! O-O?? 10.Bxc6 Bb7?? 11.Bxb7 Rb8 12.Bc6 Qd7?? 13.Bxd7.
- With ...b5 played the c6-knight has NO pawn recapture (b5 covers a4/c4; d6 covers c5/e5). 9.Bd5 attacks it AND a8 through b7: only 9...Nxd5! 10.exd5 (B for N) =. Moving the knight away loses Ra8 to Bxa8; 9...O-O?? drops the knight.
- 10...Bb7?? 11.Bxb7 and 12...Qd7?? 13.Bxd7 both put a piece on the c6-bishop's rays (b7/a8, d7/e8). My in-game note said 'Bxb7 might just win a bishop - reconsider' and I played it anyway: named danger = self-ban.
- Clock: 34-42 s on moves 6-12 book moves; ended 7:52 vs 20:59. Open Chigorin book <=10 s.
