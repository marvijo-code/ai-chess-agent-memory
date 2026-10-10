# Four Knights: branches, checking defenses and deadlines

## T17 final: Black vs Stockfish 19, checkmate loss
1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.Nd5 Nxd5 6.exd5 Ne7 7.Nxe5 Nxd5 8.a3 Be7 9.Nxf7 Kxf7! 10.Qh5+! Ke6 11.O-O Nf6?? 12.Re1+ Ne4 13.Rxe4+ Kf6 14.Rf4+ Ke6 15.Qf5+ Kd6 16.Rd4#.
- This is the uncastled ...Ne7 branch, distinct from ...e4 and the castled variation. After Kxf7 Black had an extra knight for a pawn, but an exposed king. Kxf7 was the only good move; shallow evaluations before Nf6 did not establish a forced loss or secure consolidation.
- After O-O, Rf1 can enter the open e-file with check against Ke6. Nf6 attacked Qh5, but White did not need to move the queen. Calculate every check before assuming a queen attack earns a tempo.
- Nd5 could interpose on e3 against Re1+ and controlled f4. Nf6 abandoned both functions. This identifies lost defenses, not a verified best alternative to Nf6; no replacement was supplied.
- Ne4 blocked Re1+ but was captured with check. It also STOPPED attacking Qh5: a knight on e4 attacks c3/c5/d2/d6/f2/f6/g3/g5. Do not carry an attack forward after relocating its attacker.
- Rxe4+ expelled the king to f6; Rf4+ drove it back to e6. Qf5+ forced Kd6, then Rd4# used the clear f4-e4-d4 path.
- At mate: Rd4 covers d5; Bb5 covers c6; Qf5 covers c5/e5/e6. Black's c7/d7 pawns and Be7 occupy the remaining exits. An extra piece cannot compensate for a forced king chase.
- No invalid attempts; finished with 14:04. Ke6/Nf6 took 43/41 seconds. This was a checking-defense failure with ample time, not a flag or a proven opening refutation.

## T16 final Armageddon: ...e4 branch, time loss
5.Nd5 Nxd5 6.exd5 e4 7.Qe2 Qe7 8.dxc6 exf3 9.cxd7+ Bxd7! 10.Bxd7+ Kxd7! 11.Qxe7+ Bxe7 12.gxf3 Rae8 13.d4, then flagged.
- Qe2 pins e4 to Ke8; Qe7 interposes and releases it. Exf3 captures Nf3 and attacks Qe2, but White can first answer with cxd7+.
- Bc8xd7 removes the checking pawn; Bb5xd7+ Kxd7 is forced. Bb4xe7 recaptures the queen through clear c5/d6.
- After d4: White Ke1/Ra1/Rh1/Bc1, pawns a2 b2 c2 d4 f2 f3 h2; Black Kd7/Re8/Rh8/Be7, pawns a7 b7 c7 f7 g7 h7. Black is a pawn down, not proven lost. Be7 screens Re8 from Ke1.
- Actual Black start was 450 seconds +10, despite the nominal 900+10 header. E5/Nc6 consumed 198 seconds; Bxd7/Kxd7 took 47/57. Last clock 3:24 after Rae8, then an unbounded turn responding to d4 caused the flag.
- Book/forced moves 1-5 seconds. Below five minutes use 10-15, cap 20 INCLUDING output; below 90 seconds use 1-3. Black draw odds favor sound simplification and timely resistance.

## Castled branch and T15 liquidation
5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 Be6?! 11.Bxe6 fxe6! 12.Qb3 Qe7.
- Qe7 guards Bb4 through d6/c5 and e6 vertically; Qd5 loses Bb4. No verified replacement for Be6 supplied.
- D4 Rad8 c3 Bd6! Qxb7 Rb8?! Qxc6! conceded two pawns. Queen chasing did not restore equality; Qc4 pinned e6 until Kh8.
- Later Qxd5 Qxe4 Qxe4 Rxe4! Rxb2 left Black two pawns down with equal pieces.
- R1e7? Rxe7! Bxe7! Kf7! Rxf8+ Kxe7!: Kf7 unpinned Bf8. Kxf8 was illegal because Be7 guarded f8, but Kxe7 escaped the checking file and captured that bishop.
- The rook ending was not a certified draw. Ke5 took 220 seconds and Black flagged.

## Other tactical geometry
- Qe4 hits a8 through d5/c6/b7: Ra8? Qxa8+ loses R.
- Qh4's mate threat loses to Qf3+ Bf6 R1b7#; own blockers deny exits.
- Qf2+ Kh2 Qf3?? gxf3 removes the queen's own pin on g2.
- Bc3 pins Rd4 to Qf6; Rd3?? cxd3 loses R.
- Rf4 screens Rf1 and guards f8; Re4 abandons both, allowing Rxf8#.
- Qxf5 exf5 clears e6 between Re2/Re8, allowing Rxe8+.
