# Sicilian Maroczy: recapture paths and forcing replies

## Tournament 3, semifinal 2 Armageddon: White vs Stockfish 19
Checkmate loss with 8:55 remaining; no illegal attempts. White needed a win, but clock pressure did not cause the tactical failures.

1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.c4 Nf6 6.Nc3 Qa5 7.Bd2? Nxd4! 8.Nb5! Qb6 9.Be3?! e5! 10.Nxd4 exd4 11.Bxd4 Bc5 12.Bc3 Bxf2+ 13.Ke2 Qe3#.

## Development blocked the recapture
- Before Bd2, Qa5 pinned Nc3 to Ke1 along a5-b4-c3-d2-e1. Qd1 could recapture a knight on d4 through d2/d3.
- Bd2 broke the king pin but occupied d2, blocking Qxd4. Black's Nc6 captured Nd4; White could not make the intended queen recapture.
- Nc3 did not itself defend d4. Developing a bishop and unpinning a knight did not make the other knight safe.
- 8.Nb5 vacated c3 and uncovered Bd2's attack on Qa5. It also attacked Nd4 and was marked the only good move, but Black's queen retreat preserved the advantage.
- Qb6 defended Nd4 along b6-c5-d4. Be3 cleared the queen's d-file and attacked Nd4, but ...e5 supplied another defender.
- Nxd4 exd4 Bxd4 removed Black's advanced knight and e-pawn but also removed White's last knight. White had no knights against Black's Nf6: a knight deficit, not successful material recovery.
- No engine-approved replacement for Bd2 or Be3 was supplied. The verified correction is to calculate ...Nxd4 and the complete recapture sequence before choosing development.

## Queen attack answered by interposition
- Bxd4 attacked Qb6 along d4-c5-b6. Black did not retreat the queen: ...Bc5 blocked the diagonal with a bishop protected by Qb6.
- Bc5 simultaneously targeted f2 along c5-d4-e3-f2. Bd4 still blocked that line and defended f2 along d4-e3-f2.
- 12.Bc3 removed both functions, allowing ...Bxf2+. After the capture, Qb6 protected Bf2 through the now-empty c5/d4/e3 squares, so Kxf2 was illegal.
- 13.Ke2 allowed ...Qe3#. Qb6 reached e3 along c5/d4; Bf2 protected e3. The queen checked the adjacent king, leaving no interposition, safe capture, or escape.
- White's Qd1 and Bf1 occupied d1/f1; Qe3 controlled d2/d3/e1/f2/f3, and Bf2 protected the checking queen. Check escape squares before moving the king.

## Apply next game
Before an unpinning development move, list any defense or recapture path it blocks. When attacking a queen, calculate protected interpositions and the threats they create. Before retreating a central bishop, inspect every diagonal it currently blocks or defends, especially batteries aimed at the uncastled king and f2.
