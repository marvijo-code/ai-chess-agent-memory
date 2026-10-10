# Four Knights: defense, liquidation and time

## Shared opening
1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 Be6 11.Bxe6 fxe6 12.Qb3 Qe7.
- Both pairs of knights disappear. Qe7 defends Bb4 via d6/c5 and e6 vertically. Qd5 attacks Qb3 but permits Qxb4.
- T15 marked ...Be6 inaccurate and ...fxe6 the only good recapture. Opening the f-file did not establish compensation for weakened pawns; no best replacement for Be6 supplied.

## T15 final: Black vs Stockfish 19, time loss
13.d4 Rad8 14.c3 Bd6! 15.Qxb7 Rb8?! 16.Qxc6! Rb6 17.Qc4 Kh8 18.Qe2 e5 19.d5 e4 20.g3 Rf3 21.Be3 Rb8 22.Rae1 Qe5 23.Bxa7 Rb7 24.Bd4 Qxd5 25.Qxe4 Qxe4 26.Rxe4! Rxb2.
- ...Rb8 attacked the queen but conceded c6 as well as b7. Repeated queen attacks did not recover the opening loss. ...Bd6 was required after c3 attacked Bb4; it did NOT defend e6 (same file).
- Qc4 pinned e6 to Kg8 through d5/e6/f7; Kh8 released the pawn. e4 then supported Rf3. Be3 attacked Rb6 through d4/c5, requiring a rook response.
- Qxd5 left e4 available to Qxe4. After the queen exchange and Rxb2, White had R+R+B and five pawns against R+R+B and three; activity was resistance, not equality.

### Calculated escape to a rook ending
27.Kg2 Rf7 28.Re8+ Bf8 29.a4 Ra2 30.Bc5 Kg8 31.Rfe1 Rxa4 32.R1e7? Rxe7! 33.Bxe7! Kf7! 34.Rxf8+ Kxe7!.
- Rxe7 exchanged one rook pair. Kf7 moved the king off the eighth rank, unpinning Bf8 and attacking Be7.
- Rxf8+ checked along the f-file. Kxf8 was illegal because Be7 defended f8; Kxe7 captured that bishop while leaving the checking file. Enumerate king captures away from the checker.
- Result: White Kg2/Rf8, c3 f2 g3 h2; Black Ke7/Ra4, c7 g7 h7. One pawn down with active rook, not a certified theoretical draw. Depth-4 evaluation fell from roughly +5 to +1.3 after White's marked mistake.
35.Rf4 Ra3 36.Rg4 Kf7 37.Rc4 Ra7 38.Rh4 Kg6 39.Rc4 Kf5 40.Kf3 Ke5 41.h4, then flagged.
- Ra3 pressured c3; Rc4 guarded it. Keep reassessing king activity, checks and pawn targets rather than replaying a stale threat.

### Time failure despite a recoverable position
- Opening moves mostly took 3-7 seconds, banking 16 minutes. Later Rf3 took 64 seconds, Rb7 80, Rxe7 67, and Ke5 220.
- Ke5 reduced the submitted clock from 8:39 to 5:09. The game ended on time during the response to h4; the final PGN clock was the last submitted value, not time safely available indefinitely.
- Set a turn deadline before calculation. Routine moves 3-10 seconds, tactical turns usually 20-40; below ten minutes generally cap tactical turns at 30. Include output time. A routine king move must never consume several minutes.
- No invalid attempts. Accurate liquidation did not excuse the clock failure.

## T14 final: rook loss and forcing mate
...Qh4/g3/Qxd4 recovered d4 without exchanging Bd6, but later:
21.Qe4 R5f6?! 22.Bxa7 Ra8? 23.Qxa8+ Bf8 24.Qc6.
- Qe4 attacked a8 through empty d5/c6/b7. Rf8-a8 attacked Ba7 but had no recapturer; Rf6 did not protect a8. A protected blocking bishop after the capture recovered no rook.
- Trace queen lines before choosing a useful rook destination; viewer marks understated the direct loss.
...Rg6/Qh4 threatened Qxh3#, but Qf3+ Bf6 R1b7# won first.
- Rb8 controlled e8/f8/g8 and protected Rb7. Black's e6/Bf6/Rg6 occupied other exits; Bf6 was pinned by Qf3. Test all enemy checks before a mate threat.

## Earlier failures
- T13: ...Qh4 f4 Bxf4? Bxf4 Rxf4 removed my bishop while White collected b7/c6. ...Rd6 Qa8+ Rd8 Qxa7: queen attack answered by check and capture.
- Qf2+ Kh2 Qf3?? gxf3: moving the queen removed its own horizontal pin on g2. Rf6 support did not justify queen for pawn.
- ...a8=Q Rxa8 ignored Qxg6+ Kh8 Qxh6# with Rg1 support.
- Bc3 pinned Rd4 to Qf6; Rd3?? cxd3 lost it. Rf4 screened Rf1 and could recapture f8; ...Re4 abandoned both, allowing Rxf8#.
- Qxf5 exf5 cleared e6 between Re2/Re8, allowing Rxe8+. Repetition escapes did not establish compensation.
