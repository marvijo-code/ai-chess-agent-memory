# Pre-move scan & blunder catalogue (g1-g103)

## SELF-BAN
A move my scan called bad/illegal is FORBIDDEN; play the traced alternative. The danger my last plan note names is the first check (g98 'watch Qxb2'->O-O??; g100 'bishop hits queen'->Qc6??; g103 'Nb3 hits Qa5'->Rfc8?? class).

## Scan (EVERY move, 5 s, FINAL position)
1. Legality: my turn; my pieces; PATH clear; two units to one square -> full name; BISHOPS trace to the edge (g94); O-O needs f1/g1 empty (g98); PIN: a unit between his B/R/Q and my K/Q cannot move or recapture (g90). Re-read the board after every capture.
2. KNIGHT SWEEP FIRST: his knights' 8 squares hit my destination -> recapture (g85,g87); before ANY queen placement (g84,g95); a 'fork' onto a defended square = gift (g98 Nd7?? Bxd7).
3. HIS last move: list every attacker of my destination (rook, bishop, knight, PAWN). Attacked QUEEN moves THAT move - 'defended' never counts (g95 7...e6 8.Nxd5 = Q for N). Undefended+attacked -> save NOW (g78).
4. QUIET-MOVE SWEEP: before ANY non-capture piece move list his attackers of the destination - pawns (even blocked/just-moved), knights, AND his rook files + bishop diagonals (g103 17...Bf5?? Rxf5, open f-file, no defender; 12...Bd6?? Qxd6 + Bxd6). No piece onto an attacked square unless it stays defended and the exchange wins.
5. QUEEN: no capture on a defended square (g87); no trade without MY recapturer that SURVIVES (g91,g96). Check his queen/rook files AND her landing square (g96 Qd5+?? Qxd5). Hit by a BISHOP: retreat OFF that whole diagonal (g100 Qc6??; g101 Qd3??).
6. CAPTURES: name every recapturer + his second attacker; write MY recapture; his last -> don't start. A piece defended ONLY by my QUEEN dies to Qx + his 2nd attacker (g103 12...Bd6?? 13.Qxd6 Qxd6 14.Bxd6 = B+Q for Q). RECAPTURE X-RAY: walk his rook files + bishop diagonals onto the recapture square (g97 Qxe7?? Rxe7 = Q for N).
7. Loose minor/rook: destination attacked by NOTHING; walk his bishop diagonals to the edge (g86,g78). A check is not safety.
8. Mate nets FIRST: Qh2/Rh1 h-file; Qh6+Ng5=Qxh7#; king h2-h4: Rg2/Rg6+Bf1+Nf2 (g98 Rg4#; g101 Qxg2#: his Bd5 guarded g2, my h3 blocked the flight).
9. Down material: keep queens; repetition = half point; no N-for-B/R-for-B trades; no claw-back grabs (g87-g91,g98,g101,g103). Hold, trade pawns, make him prove it.
10. Time: routine <=15 s; <1 min 1-2 s. Long thinks never prevented a blunder (g86-g103; g103: 36-38 s on both blunders).

## Patterns
- Attacked queen: move her that move; 'defended' never counts (g41,g94-g96,g100); never retreat onto a square his bishop/queen ray covers (g101).
- Queen hit by a line: leave the ENTIRE line (g100,g101).
- Pawn-guarded square, even defended: g89,g96,g101. Last-screen grabs: g91,g83,g81. Pinned recapturer: g90. Tempo on the queen: g41,g98. Illegal sends cost clock: g94,g98.
- Quiet piece onto an open file/diagonal his rook/bishop owns, undefended: g103 17...Bf5?? Rxf5.
- Piece whose only defender is my queen: g103 12...Bd6??.

## g103 Sicilian Taimanov vs Sol (0-1, Rf8# m33)
- 12.Bxe5 attacked Nf6 and won a pawn; Nf6 had to move: 12...Nxe4! 13.Nxe4 = pawns level. Instead 12...Bd6?? lost B+Q for Q (13.Qxd6 Qxd6 14.Bxd6) - sole defender Qd8, second attacker Be5.
- 17...Bf5?? Rxf5: a quiet bishop to the open f-file (f2-f5 empty, Rf1) with no defender, attacking only a defended knight. Down material, every move passes the destination sweep first.

## g101 QGD Lasker vs Sonnet (0-1, Qxg2# m33)
- 21.Nxc6??: the c6-pawn was guarded by the e4-bishop (e4-d5-c6); before a knight capture list every bishop diagonal through the target - N (3) for P (1).
- 26.Qd3??: her retreat square sat on the attacking bishop's diagonal (Qe2 safe, Qd3 not) - same class as g100.
