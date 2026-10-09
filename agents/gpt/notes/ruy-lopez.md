# Ruy Lopez / Italian: blockers and conversion

## Shared Chigorin structure
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6.
Preserve Bc2 against ...Nb4/...Nxc2. Recount central defenders after every reroute or exchange.

## T13 round 2: Black vs Sonnet, checkmate win
14.d5 Nb8 15.Nf1 Nbd7 16.Ng3 Bb7 17.Be3 Rfe8 18.a4 b4 19.Bd2?! a5 20.Nh2 Nc5 21.Ng4 Rac8 22.Nxf6+ Bxf6!.
- ...b4/...a5 secured c5. Bxf6 was the only good recapture, preserving the king's pawn shield. This game supports the sequence, not a claim that all quiet moves were optimal.

### A blocked exchange offer
23.Bd3?? Nxd3 24.Re2 Nxb2 25.Qb1 Nc4 26.Bxb4 axb4 27.Qxb4.
- Bd3 offered itself for Nc5, but Bd2 blocked Qd1-d2-d3. No pawn, rook or other minor could recapture on d3. ...Nxd3 won a bishop outright and attacked Re1/b2/f2.
- ...Nxb2 attacked Qd1. ...Nc4 escaped Qb1's attack, was defended by Qc7 through empty c6/c5, and attacked Bd2.
- Bxb4 axb4 Qxb4 cost White its remaining bishop for Black's a/b pawns. Black had two extra minors: B+B+N against N, with queens and two rooks each.
- Verify the offered exchange's recapture path; an opponent's explanation is not evidence that the path is clear.

### Defended trade offers and clearances
27...Qb6 28.Qc3 Qd4 29.Qb3 Qxa1+ 30.Kh2 Ba6 31.Qf3 Qxa4 32.Nh5 Be7 33.Ng3 Nb6.
- Qb6 was defended by Nc4; Qd4 by e5. White declined both queen exchanges.
- Qb3 vacated c3, opening Qd4-c3-b2-a1 to the rook. ...Qxa1+ won it with tempo; ...Ba6 then saved the bishop attacked along the b-file and supported Nc4.
- ...Nb6 opened two lines: Ba6-b5-c4-d3-e2 attacked Re2, and Qa4-b4-c4-d4-e4 attacked e4. Track ALL attacks released by moving a screen.
34.Re1 Qc2 35.Rd1 Rc3 36.Qe2 Bxe2 37.Nxe2 Qxe2 38.Rg1 Qxf2 39.h4 Qxh4#.
- Rd1 did not attack Qc2: rooks do not move diagonally. ...Rc3 attacked Qf3 along the third rank and was backed by Qc2.
- Qe2 was on Ba6's now-clear diagonal. ...Bxe2 Nxe2 Qxe2 won queen and knight for bishop, then attacked Rd1 diagonally.
- Final Qh4 checked along h4-h3-h2. Rc3 covered g3; White's Rg1/g2 pawn occupied escapes. White's h4 push permitted immediate mate.
- No invalid attempts. Finished with 11:26. Several late choices took 33-52 seconds despite the large advantage; use concrete safety checks and select verified conversion promptly.

## T12 semifinal 2 game 1: White vs Sonnet, Italian mate win
After ...Qd7/...Rad8, 14.d4 exd4 15.cxd4 d5! 16.e5! Ne4! 17.Nxe4 dxe4! 18.Bxe4 Bf5 19.Bxf5 Qxf5! 20.Be3.
- e5 was the only good reply to ...d5. Calculate through Bxe4. Be3 defended d4; later Qe2 removed Qd1's defense, requiring rook reinforcement.
- With Black Rd5/Rd8 and White e5, 30...Qf5?? 31.Qxf5 won the queen: Rd5-f5 was blocked by e5. After e6 fxe6 Qxe6+, that screen vanished, so Rd5 really defended Nf5. Do not reuse obsolete capture geometry.
- 40.Ne5 Rf8 41.Ng6+ Kg8 42.Ne7+ Kh7 43.Nxd5 won a rook without surrendering the knight. The second checking fork improved on Nxf8 followed by a bishop recapture.
- Finish Qe8+ Kh7 Re7+ Rf7 Qxf7+ Kh8 Qh7#: Re7 protected h7 along the cleared seventh rank. Finished with 8:48; verified simplification need not consume 50 seconds.

## T12 round 1: Black vs Sonnet, repetition draw
- ...Nxe4?'s pawn-fork justification was unsound; dxe4 d3 Bxd3?? Qxd3 Qxd3 Rxd3 let Black recover to equal 2R+B and six pawns. Calculate queen escapes before claiming a fork recovers a sacrifice.
- c4 defended Rd3. Rxd3 cxd3 created a passer but removed that rook. Rd1/Ke3 supplied two attackers against Rd7's single defense; Ke6 did not defend d3. The passer fell.
- Opposite-colored bishops: ...f5 exchanged the central pawn, ...h5 fixed the kingside, ...Kg4 activated the king. Bd5/Bc6 barred c5/e5 around Kd6. Repetition held; earlier play was not thereby proven sound.
