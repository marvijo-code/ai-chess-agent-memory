# Four Knights: defense before activity

## Shared opening
1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 Be6 11.Bxe6 fxe6 12.Qb3.
- Both pairs of knights disappear. Qe7 defends Bb4 via d6/c5 and e6 vertically. Qd5 attacks Qb3 but permits Qxb4.

## T14 final: Black vs Stockfish 19, mate loss
13.d4 Bd6 14.Qxb7 Rab8?! 15.Qa6?! Qh4 16.g3 Qxd4 17.Qxc6 Rb6 18.Qg2 Rb5 19.a4 Rbf5 20.Be3 Qxb2 21.Qe4.
- Unlike T13, g3 allowed Qxd4 to recover a pawn without exchanging the attacking bishop. After Qxb2, pawn counts were equal. This does not certify the opening: ...Rab8 was inaccurate and Qa6 was also inaccurate; no best replacements supplied.

### Rook destination on a queen diagonal
21...R5f6?! 22.Bxa7 Ra8? 23.Qxa8+ Bf8 24.Qc6.
- R5f6 defended e6 but was marked inaccurate; White then took a7. No best replacement supplied.
- Before ...Ra8: White Kg1/Qe4/Ra1/Rf1/Ba7; Black Kg8/Qb2/Rf8/Rf6/Bd6. Qe4 attacked a8 through EMPTY d5/c6/b7.
- Rf8-a8 attacked Ba7 but put a whole rook on that diagonal without a recapturer. The other rook on f6 did not protect a8. White captured with check instead of retreating the bishop.
- ...Bf8 blocked the check and was protected by Rf6, but recovered none of the lost rook. A protected blocker after a loss is not compensation.
- Trace enemy queen ranks, files and diagonals to the proposed rook square BEFORE evaluating its useful purpose. Viewer marked ...Ra8 only a mistake despite the direct rook loss; marks do not replace calculation.

### My mate threat loses to forcing checks
25.Rab1 Qe5 26.Rb5 Qd6 27.Rb8+ Bf8 28.Qb7 Kf7 29.c4 Be7 30.Rb1 c5 31.Rf1 Qd4 32.a5 Qxc4 33.h3 Rg6 34.Rb1 Qh4 35.Qf3+ Bf6 36.R1b7#.
- ...Rg6 pinned g3 to Kg1; ...Qh4 threatened Qxh3#. White's check took priority over this threat.
- Qf3 checked Kf7 along the f-file. ...Bf6 blocked it, but Rb1-b7 then checked along the seventh rank.
- Rb8 controlled e8/f8/g8 and protected Rb7; Rb7 controlled e7/g7. Black's e6 pawn, Bf6 and Rg6 occupied the other neighboring squares. Bf6 was pinned to the king by Qf3. The apparent attacking pieces helped enclose my king.
- Before a mating threat, calculate all enemy checks through their next forcing move. With one enemy rook on the eighth rank, explicitly test the other rook arriving on the seventh.
- No invalid attempts. ...R5f6 took 46 seconds, ...Ra8 52; finished with 8:54. This was capture and mate verification failure, not clock shortage.

## T13 final: failed attack and self-released pin
13.d4 Rad8 14.c3 Bd6 15.Qxb7 Qh4 16.f4 Bxf4? 17.Bxf4 Rxf4 18.Qxc6 Rxf1+ 19.Rxf1 Qe7.
- f4 interrupted Bd6's diagonal. The bishop exchange removed my attack while White collected b7/c6. Repeating this earlier failed plan did not repair it.
- ...Rd6 Qa8+ Rd8 Qxa7: a queen attack was answered by check and another capture.
- Qf2+ Kh2 Qf3?? gxf3: Qf2 pinned g2 horizontally; moving that queen removed its OWN pin. Rf6's support did not justify queen for pawn.
- Later a8=Q Rxa8 ignored Qxg6+ Kh8 Qxh6#. The opened g-file let Rg1 protect the queen attack. Scan checks before promotion recaptures.

## Earlier crossed attacks and lost screens
- T13 round 1: Bc3 pinned Rd4 to Qf6. Bxe3 fxe3 attacked the rook; Rd3?? cxd3 lost it and exposed Qf6. Rooks cannot capture diagonally.
- Qxd3 behind Bc3 allowed Bxg7+ Kg8 Qxd3: the bishop cleared Qb3's line with check, supported by Rf7. Kxf7 recovered only a rook.
- Rf4 screened Rf1 and could recapture f8; ...Re4 abandoned both, allowing Rxf8#. ...Qe3+ Kh1 Qxc3 also ignored that mate.
- Kf6/Re7 allowed protected Bg5+ and Bxe7. A defended rook can lose to a checking skewer.
- Qxf5 exf5 cleared e6 between Re2/Re8, allowing Rxe8+. Repetition escapes did not establish compensation.
