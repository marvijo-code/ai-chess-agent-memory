# DeepSeek V4.1 Flash: tactics and conversion

Wins, forfeits, and opponent explanations do not validate moves. Track material, defenders, and blockers independently. Chigorin structure: notes/ruy-lopez.md.

## T12 round 3: White, Dragon checkmate win
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3 O-O 8.Qd2 Nc6 9.Bc4 Bd7 10.O-O-O Rc8 11.Bb3 Ne5 12.h4 Nc4 13.Bxc4! Rxc4! 14.h5 gxh5?! 15.Bh6?? Bxh6?? 16.Qxh6! Nxe4?? 17.Rxh5 Rxd4 18.Qxh7#.
- Nc4 attacked Qd2 and Bb3, not b2. Bxc4 removed the knight with tempo before continuing the pawn attack. The rook recapture was Black's only good reply.
- Bh6 abandoned Be3's diagonal defense of Nd4. Rc4 could capture it: ...Rxd4, and Qxd4 Bxh6+ gives Black both minors for a rook. The bishop check reaches Kc1 through g5/f4/e3/d2 after the queen leaves d2. Calculate this before relying on a routine Dragon bishop exchange; no engine-best replacement for Bh6 was supplied.
- Black accepted the bishop exchange instead. Qxh6 was the only good recapture. Nf6 had guarded h5 and h7; ...Nxe4 removed those functions. It did NOT attack Qh6: Ne4 attacks c3/c5/d2/d6/f2/f6/g3/g5.
- Rxh5 removed the h5 pawn and supported Qxh7# up the h-file once Qh6 moved. With Bg7 gone, g7 was empty and covered by Qh7; f8 was occupied by Black's rook. The protected queen covered the remaining king destinations.
- ...Rxd4 captured Nd4 but ignored mate. Do not automatically recapture when a verified mating move is available. Black's claim that Nc3xd4 allowed ...Rxd1+ was false: that recapture would remove its attacking rook.
- No invalid attempts. Finished with 15:08 before the final increment. Book moves were quick; Bh6 took 22 seconds and still missed the defender's duty. Rxh5 took 53 seconds; select the verified mate promptly.

## T11 round 3: White, technical forfeit
After ...Na5/...Qc7/...Rac8, 15.Ng3?? ignored ...Qxc2 Qxc2 Rxc2, winning Bc2 while exchanging queens. c3-c6 were empty. ...Nc6 screened the file; d5 drove it away and Bd3 finally saved the bishop. This repeated T9's oversight.
- Later Rc1/Qc7 had Bc2 and Nc5 as screens. Rc1 was inaccurate; no best replacement supplied.
- b4 Nb3 Bxb3 removed an undefended knight and cleared the bishop screen. Black's a6/b5 pawns did not defend b3. ...Nc5 bxc5 dxc5 lost its other knight.
- d6 attacked Qc7 and was defended by Qd1 through d2-d5. ...Qxd6 Qxd6 lost the queen outright. The forfeit tested no mating conversion; finished with 13:38.

## T10 third place: Black, mate win
...Na5/...Rac8 followed by Nf3?? Qxc2 Qxc2 Rxc2 won Bc2. Nd2 never screened the c-file.
- Bd2 attacked Na5 via c3/b4. ...Nc4 Bc3 f6 Nd2 Nxd2 Bxd2 Rxd2 exchanged knights and won the remaining bishop; Rc2 supported d2 horizontally.
- Red1 Rxd1+ Kh2 Rxa1: declining Ra1xd1 lost White's other rook; this was not forced.
- ...Rf1 Kg3 R8xf3+ Kh2 R3f2 b3 Rg1 Kg3 Rgxg2#. Rf2 protected g2; Bd7 covered h3 and g5 covered h4. Finished with 11:49; lengthy rook maneuvers were unnecessary.

## Earlier White wins
- T10: Rc1/Qc7 had Bc2 and Nc4 as screens. Bb3 removed one; ...Nb6 removed the other, allowing Rxc7. The bishop attack did not force that retreat; Nc4's queen pin was not absolute.
- ...Rac8 Rxc8 Rxc8 Rxc8 exchanged one White rook for both Black rooks. ...e4 forked Qd3/Nf3, but Qxe4 removed it safely.
- Qe8 Kh7 Qxf8 g6 Qh8#: Rc8 protected h8; ...g6 occupied Kg6's former escape.
- T9: Ng3 again ignored ...Qxc2; Bd3 saved the bishop after Black missed it. With the file clear, Rc1 Qxc1 Bxc1 Rxc1 Qxc1 gave Black Q+R for R+B. Finish: Re8+ Kg7 Qc3+ Kh7 Rh8#, with Qc3 protecting h8.

## Recurring patterns
- Bxc5 dxc5 opened Bb7 for Qd5 Bxd5. Bf8 abandoned Nf6; Rec8 defended Rc4.
- Qg3+ fxg3 and Kf1 Qf3+ gxf3 lost queens; refresh pins after king moves.
- Nb4 Bd3 Nxd3 worked only because Nd2 blocked Qd1xd3. Nc4 allowed bxc4; Qb3 allowed cxb3.
- Bd4+ allowed Kxd4; Qe3+ allowed fxe3; Bd6+ abandoned Nh4 to Kxh4. Checks require capture verification.
