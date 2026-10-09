# QGD: skewers, defenders, and file clearance

## T7 semifinal 2, game 1: White vs Sonnet, checkmate win
1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.cxd5 Nxc3 10.bxc3 exd5 11.Bd3 Nd7 12.O-O Nf6 13.Qc2 Be6 14.Rfe1 Rfe8 15.e4 dxe4 16.Bxe4! Nxe4 17.Rxe4 c6 18.Rae1 Rad8.

### Active pieces still require safety checks
- 19.Ne5?? left Re4/Qc2 aligned on f5-e4-d3-c2. ...Bf5 would skewer rook and queen; moving Be6 also opens Qe7's attack on Ne5. Black instead played ...Qd6??. A supported knight does not make the whole position safe.
- 20.h3 f6 21.Ng6 Bf7 22.Nf4?! Rxe4 23.Rxe4! Rd7 24.Qd3??.
- Qd6 attacked Nf4 through e5; Re4 defended the knight along the fourth rank. ...f5 would attack Re4 while the queen attacked Nf4. Moving the rook abandons the knight; moving the knight leaves the rook attacked. Scan attacks on a defender and its charge together.
- Black instead played ...g5?! 25.Ne2 Kg7? 26.Ng3 Be6?? 27.Nh5+? Kf7?! 28.c4??. Now ...Bf5 again skewered Re4/Qd3 along f5-e4-d3. Pawn mobility did not address the tactical alignment.
- No engine-best replacements were supplied for the marked errors. Do not treat the eventual win as validation of these choices.

### Bishop screen and alternative recaptures
28...Qe7?? 29.d5 cxd5 30.cxd5?? Bxd5?? 31.Rxe7+ Kxe7.
- Be6 was the only blocker between Re4 and Qe7. ...Bxd5 vacated e6, allowing the queen capture with check. White exchanged rook for queen and retained Q+N against R+B, not an extra queen with otherwise equal material.
- Black could instead capture with ...Rxd5, preserving Be6 and attacking Qd3 along the cleared d-file. The pawn attack did not force the bishop to leave its screening square.
- Before a central recapture, compare every capturing piece and reconstruct the resulting file. A bishop shielding its queen has a concrete defensive function even when attacked.

### Conversion
32.Qd4 Rd6 33.Nxf6 Be6 34.Qe5 Rd1+ 35.Kh2 Kf7 36.Ne4 Rd5 37.Qf6+ Ke8 38.Qxe6+ Kf8.
- Qd4 attacked Bd5, whose rook defender was on d6. ...Rxf6 would abandon the bishop to Qxd5; calculate this exchange before claiming a free knight capture.
- Qe5 pinned Be6 to Ke7; ...Kf7 released that pin. Ne4 then protected Qf6, and Qf6+ drove the king away from Be6, allowing Qxe6+.
- After ...Kf8, Qxd5 could safely remove the last rook. I instead collected h6/g5 and later used Ne6+ Rxe6 Qxe6. Prefer immediate safe simplification.
- Queen-only finish: approach with the king while the queen restricts Black. With Kc7/Qd7 against Ka8, my king blocked Qd7-b7; Qc8+ Ka7 Qb7# delivered protected mate.
- Finished with 10:13 and no illegal attempts. Routine king approach took 5 - 12 seconds; some simple attacking moves still took 24 - 40 seconds.

## Earlier QGD losses
### T4 Exchange QGD
- Ng3 was a mistake; exd5 was inaccurate. Nf4 moved Nd5 onto Ne6's capture square. Bf2 did not defend f4: its diagonals pass through e3/d4 and g3/h4.
- Bd3 blocked Rd1's attack on Qd7. Bh7+ removed the blocker with check, enabling Rxd7 Bxd7. This resource did not validate the earlier knight loss.
- With Kh7/Rg7/Bf8 against Qb7/Ng3, Qxa7?? allowed Rxa7. A rook pinned along a rank can move along that rank or capture the pinning queen. The earlier diagonal pin no longer existed.
- Later a king move released Nf4's pin, but ...Bd2 added another attacker. Ignoring it allowed ...Bxf4+, protected by Rf2.

### T3 Lasker QGD
- d5 exd5 Bxd5 Nb4 gained Black a bishop tempo. After ...Nd4, exd4 would uncover Qe7's attack on Qe2 through the vacated e3 square.
- Nxd4 cxd4 attacked Rc3. Rc5?? attacked Bf5 but landed undefended on Qe7-d6-c5; Qxc5 won the rook. Attacking a bishop does not force retreat.
- After Qxc5, the old e-file restriction disappeared. Refresh constraints after captures.
- Bc6 attacked Rd5/b7 but allowed bxc6. Test pawn captures of the attacking piece, including from starting squares.
