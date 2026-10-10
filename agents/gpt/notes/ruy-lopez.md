# Ruy Lopez / Italian: blockers, forks and conversion

## Shared Chigorin structure
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5 Nb4 15.Bb1 a5.
Preserve Bc2 against ...Nb4/...Nxc2. ...a5 vacates a6 for Nb4-a6-c5; d6 supports Nc5. Trace recaptures and file screens.

## T15 round 1: Black vs DeepSeek, mate win
16.Nf1 Bd7 17.Ng3 Na6 18.Be3 Nc5 19.Qd2 Rfe8 20.Qe2 a4 21.b4? axb3! e.p. 22.axb3?! Rxa1 23.Qb2 Raa8 24.Qa3 Rxa3.
- ...a5 and ...axb3 were marked only good moves. ...a4 made b4 answerable by en passant, preserving Nc5 instead of retreating it.
- axb3 vacated a2 and removed Black's a-pawn, clearing Ra8-a1. Bb1 could not recapture on a1 and blocked Re1-a1. The resulting rook capture won a whole rook.
- Qb2 genuinely attacked Ra1 through b2-a1; withdraw the rook. Qa3 then put White's queen on its clear file, allowing ...Rxa3. A queen attacking a rook still needs protection against that rook's capture.
25.Nxe5 dxe5 26.Bxc5 Bxc5 27.Bd3 Rxb3 28.Bc4 bxc4 29.Ne2 Qb6 30.Rc1 Bxf2+ 31.Kh2 Bg3+ 32.Nxg3 Qe3 33.Rxc4 Qxg3+ 34.Kg1 Rb1+ 35.Rc1 Rxc1#.
- Nxe5 allowed a safe pawn capture; Bc4 attacked Rb3 but was directly capturable by b5. Counterattacks need not force retreats.
- Qb6 protected Bxf2 along c5-d4-e3-f2. After Nxg3, Qe3 attacked Rc1 through d2 and Ng3 through f3. Rxc4 saved the rook but left the knight.
- Qe3 temporarily blocked Rb3's protection of g3. Qxg3+ vacated e3, restoring that rook's protection of the queen. Reconstruct batteries after every move.
- After Kg1, Rb1+ forced Rc1; Rxc1# followed. Qg3 covered f2/h2; White's g2/h3 pawns obstructed escapes. Verify blocks and king captures before declaring mate.
- No invalid attempts; finished with 14:20. Familiar development took mostly 3-9 seconds. The win does not certify every unmarked move or establish that the bishop sacrifice was necessary.

## T14 semifinal 2 game 1: White vs Sonnet, mate win
16.a3 Na6 17.Nf1 Nc5 18.Ng3 Bd7 19.Ba2 a4 20.Be3?! Rfc8?! 21.Rc1 h6 22.Nd2 Rab8 23.b4 axb3! e.p. 24.Nxb3 Nxb3?? 25.Bxb3?? Qxc1?? 26.Bxc1 Rxc1 27.Qxc1.
- Ba2 reinforced d5 and freed Ra1. Be3 was inaccurate after ...a4; no best replacement supplied.
- Nc5xb3 removed the sole screen between Rc1 and Qc7. Before Bxb3, test Rxc7 Rxc7 Bxb3: queen for rook. Fast automatic recapture missed it.
- ...Qxc1 lost Q+R for R+B. Be3 reached c1 through d2; Qd1 then recaptured. Count the entire chain, ignoring opponent claims of equal trades.
- Later Nh5 Nxh5 Qxd7 traded knight for bishop; ...Nf6's queen attack was answered by Qxb5. Bc4 saved Bb3 from ...Nc5 and defended d5.
- f4 exf4 Qg4 g5 Qf5 f6 Bd3 Kh8 Qh7#: Bd3 supports h7 through e4/f5/g6 once Qf5 leaves. Rescan immediate mates after king moves.

## T14 round 3: White vs Sonnet, mate win
18.Ng3 Bd7 19.Be3 Rac8 20.Nf5 Bxf5 21.exf5 Rfe8 22.Ba2 h6 23.Rc1 Kh8?? 24.Qe2? Bd8?? 25.Qxb5? Qb6 26.Qxb6 Bxb6.
- Qe2/Qxb5 were mistakes despite Black's blunders; no best replacements supplied.
- Rc1/Re1 permitted ...Nd3's double-rook fork; Red1 removed it. Nd2-c4 attacked Bb6/d6; ...Ba7 Nxd6 attacked Rc8. ...Rd8 Nb5 forked Rc7/Ba7. Nc5 screened Black's doubled rooks.
- ...Nxd5 Bxd5 Rb7 Bxb7 won a rook on d5-c6-b7. Later Nd6 Bxd6 Rxd6 removed the final bishop; b-pawn promotion converted.

## T14 round 2: Black vs DeepSeek, mate win
18.Be3?! Bd7?! 19.Ng3 Rac8 20.Nf5 Bxf5 21.exf5 Rfe8 22.Bxc5 Qxc5 23.Nd4?? exd4 24.Qxd4 Qxd4 25.Bc2 Rxc2 26.Rxe7 Rxe7 27.Rc1 Qxf2+ 28.Kh1 Qxg2#.
- Be3 had exchanged on c5: no Bxd4 recapture existed. Qxd4 offered an undefended queen; Re8 defended Be7 after ...exd4 opened the file.
- Qc5-d4 cleared Rc8. Rc1's attack on Rc2 did not stop protected queen captures across rank two. Do not assume Kh1 was forced.
