# Four Knights: branches, defense and deadlines

## T16 final Armageddon: Black vs Stockfish 19, time loss
1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.Nd5 Nxd5 6.exd5 e4 7.Qe2?! Qe7 8.dxc6 exf3 9.cxd7+ Bxd7! 10.Bxd7+ Kxd7! 11.Qxe7+ Bxe7 12.gxf3 Rae8 13.d4, then flagged.
- This is the UNCASTLED 5.Nd5 branch, not 5.O-O O-O 6.Nd5. Recalculate checks and king geometry rather than importing the castled line.
- Qe2 initially pins e4 to Ke8. Qe7 interposes on that file, allowing ...exf3, which captures Nf3 and attacks Qe2. White can answer with cxd7+ before recovering f3.
- Bc8xd7 removes the checking pawn. Bb5xd7+ removes that bishop; Ke8xd7 is the only good recapture. After Qxe7+, Bb4xe7 completes the queen exchange through clear c5/d6. Losing castling rights here did not establish a tactical loss.
- After 13.d4: White Ke1, Ra1/Rh1, Bc1, pawns a2 b2 c2 d4 f2 f3 h2; Black Kd7, Re8/Rh8, Be7, pawns a7 b7 c7 f7 g7 h7. White has an extra doubled pawn, not equal material. Depth-5 evaluation was about +0.10; this suggests practical resistance, not a certified draw or a verified best reply to d4.
- With Black draw odds, prioritize sound activity, king safety and timely moves. Evaluate rook lines when Be7 moves; it currently screens Re8 from Ke1.

### Clock failure
- Actual Black start was 450 seconds with 10-second increments, despite the nominal 900+10 header. White started with 600 seconds.
- ...e5 took 121 seconds and ...Nc6 77: 198 seconds, 44% of the initial budget, on routine opening moves. ...Bxd7 and ...Kxd7 took 47 and 57 despite both being marked only good moves.
- Last submitted clock was 3:24 after ...Rae8. Black then exhausted it responding to d4. No invalid attempts; no marked Black tactical error. The decisive failure was an unbounded turn.
- Set a deadline before thinking and include serialization/output. Book/forced moves 1-5 seconds; below five minutes tactics 10-15, hard cap 20; below 90 seconds 1-3. Never infer usable time from a stale PGN clock.

## Castled branch: opening weaknesses
1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 Be6 11.Bxe6 fxe6 12.Qb3 Qe7.
- Both pairs of knights disappear. Qe7 guards Bb4 through d6/c5 and e6 vertically; Qd5 permits Qxb4.
- T15 ...Be6 was inaccurate; ...fxe6 was the only good recapture. An open f-file did not prove compensation for weakened pawns. No verified replacement for Be6 supplied.

## T15 final: active liquidation, then time loss
13.d4 Rad8 14.c3 Bd6! 15.Qxb7 Rb8?! 16.Qxc6! Rb6 17.Qc4 Kh8 18.Qe2 e5 19.d5 e4 20.g3 Rf3 21.Be3 Rb8 22.Rae1 Qe5 23.Bxa7 Rb7 24.Bd4 Qxd5 25.Qxe4 Qxe4 26.Rxe4! Rxb2.
- Queen chasing conceded b7/c6. Bd6 saved the attacked bishop but did not defend e6. Qc4 pinned e6 to Kg8; Kh8 released it. Be3 attacked Rb6 through d4/c5.
- After the queen exchange/Rxb2, Black remained two pawns down with equal pieces; activity was resistance, not equality.
27.Kg2 Rf7 28.Re8+ Bf8 29.a4 Ra2 30.Bc5 Kg8 31.Rfe1 Rxa4 32.R1e7? Rxe7! 33.Bxe7! Kf7! 34.Rxf8+ Kxe7!.
- Kf7 unpinned Bf8 and attacked Be7. Kxf8 was illegal because Be7 guarded f8; Kxe7 captured that bishop while escaping the checking file. Result R+3 vs R+4, not a certified draw.
- ...Ke5 later took 220 seconds; flagged after h4. Earlier ...Rf3/...Rb7/...Rxe7 took 64/80/67. Accurate liquidation did not excuse clock waste.

## Other tactical failures
- T14 Qe4 attacked a8 through d5/c6/b7. ...Ra8? Qxa8+ lost a rook: Rf6 supplied no recapturer.
- ...Qh4 threatened mate but Qf3+ Bf6 R1b7# won first. Rb8 protected Rb7; own e6/Bf6/Rg6 blocked exits.
- ...Bxf4? Bxf4 Rxf4 lost the bishop while White collected pawns. ...Rd6 Qa8+ Rd8 Qxa7: queen attack answered by check.
- Qf2+ Kh2 Qf3?? gxf3 removed the queen's own horizontal pin on g2. Rook support did not justify queen for pawn.
- ...a8=Q ignored Qxg6+ Kh8 Qxh6# with Rg1 support.
- Bc3 pinned Rd4 to Qf6; Rd3?? cxd3 lost it. Rf4 screened Rf1 and guarded f8; ...Re4 abandoned both, allowing Rxf8#.
- Qxf5 exf5 cleared e6 between Re2/Re8, allowing Rxe8+. Repetition escapes did not establish compensation.
