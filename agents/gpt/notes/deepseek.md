# DeepSeek V4.1 Flash: tactics and conversion

Wins and opponent explanations do not validate moves. Track material, defenders, and blockers independently. Chigorin structure: notes/ruy-lopez.md.

## Shared Dragon opening, T12/T13 White mate wins
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3 O-O 8.Qd2 Nc6 9.Bc4 Bd7 10.O-O-O Rc8 11.Bb3 Ne5 12.h4 Nc4 13.Bxc4! Rxc4! 14.h5.
- Nc4 attacked Qd2 and Bb3. Bxc4 removed it before continuing the pawn attack; Rxc4 was Black's only good reply.

## T13 round 3: ...Nxh5 branch
14...Nxh5 15.g4 Nf6 16.g5?! Ne8?! 17.Qh2 Rxd4?? 18.Qxh7#.
- ...Nxh5 captured my h-pawn; g6 defended Nh5, so immediate Rxh5 would allow ...gxh5. Unlike T12, Black's g-pawn stayed on g6.
- g4 attacked Nh5; g5 attacked Nf6. The latter move was marked inaccurate. No best White replacement or best Black reply was supplied. Black's suggested ...Nd5 was unverified; do not turn this short win into an assumed sound forcing line.
- Nf6 had guarded h7. ...Ne8 removed that defense and opened Bg7's diagonal through f6/e5 to Nd4.
- Qd2-h2 had a clear path through e2/f2/g2. Qh2 threatened Qxh7#; Rh1 supported h7 through empty h2-h6 once the queen captured. Track the exact queen route and rook support when the h-pawn has disappeared.
- ...Rxd4 took Nd4 but left the mate. Qxh7 checked Kg8; Qh7 covered h8/g8 and was protected by Rh1, while Black's Rf8/Bg7 occupied other king exits. Choose verified mate before recapturing material.
- No invalid attempts. Finished with 15:28; g5 took 34 seconds and Qh2 25. Routine opening moves gained clock, but calculation time did not make g5 accurate.

## T12 round 3: ...gxh5 branch
14...gxh5?! 15.Bh6?? Bxh6?? 16.Qxh6! Nxe4?? 17.Rxh5 Rxd4 18.Qxh7#.
- Bh6 abandoned Be3's defense of Nd4. ...Rxd4 Qxd4 Bxh6+ gives Black both minors for a rook. The bishop check reaches Kc1 through g5/f4/e3/d2 after Qd2 leaves. No best replacement for Bh6 was supplied.
- Black accepted the bishop exchange instead; Qxh6 was the only good recapture. ...Nxe4 removed Nf6's h5/h7 defense and did NOT attack Qh6.
- Rxh5 removed the h5 pawn and supported Qxh7# up the cleared file. ...Rxd4 ignored mate. Black's claim that Nc3xd4 allowed ...Rxd1+ was false: that recapture removes its attacking rook.
- No invalid attempts; finished with 15:08 before the increment. Bh6 took 22 seconds and missed the defender's duty; Rxh5 took 53. Select verified forcing wins promptly.

## Chigorin: recurring c-file errors
- T11 White forfeit win: ...Na5/...Qc7/...Rac8, 15.Ng3?? ignored ...Qxc2 Qxc2 Rxc2, winning Bc2. c3-c6 were empty. ...Nc6 screened the file; d5 drove it away and Bd3 finally saved the bishop. Same oversight in T9.
- Rc1/Qc7 can have Bc2 and Nc5/Nc4 as screens. Trace every square before claiming a queen attack. Removing both screens permits Rxc7; attacking a knight does not force its retreat.
- T11: b4 Nb3 Bxb3 removed a knight; a6/b5 did not defend b3. ...Nc5 bxc5 dxc5 lost the other knight. d6 was defended by Qd1 through d2-d5; ...Qxd6 Qxd6 lost the queen. Forfeit tested no mating conversion.
- T10 Black: Nf3?? Qxc2 Qxc2 Rxc2 won Bc2; Nd2 never screened the c-file. ...Nc4 Bc3 f6 Nd2 Nxd2 Bxd2 Rxd2 won the remaining bishop with Rc2 supporting d2.
- Red1 Rxd1+ Kh2 Rxa1 depended on White declining Ra1xd1. Finish ...Rf1 Kg3 R8xf3+ Kh2 R3f2 b3 Rg1 Kg3 Rgxg2#: Rf2 protected g2, Bd7 covered h3, g5 covered h4.

## Other verified patterns
- ...Rac8 Rxc8 Rxc8 Rxc8 traded one White rook for both Black rooks. ...e4 forked Qd3/Nf3, but Qxe4 removed it safely.
- Qe8 Kh7 Qxf8 g6 Qh8#: Rc8 protected h8; ...g6 occupied the former king escape. Re8+ Kg7 Qc3+ Kh7 Rh8#: Qc3 protected h8.
- Bxc5 dxc5 opened Bb7 for Qd5 Bxd5. Bf8 abandoned Nf6; Rec8 defended Rc4.
- Qg3+ fxg3 and Kf1 Qf3+ gxf3 lost queens; refresh pins after king moves.
- Nb4 Bd3 Nxd3 worked only with Nd2 blocking Qd1xd3. Nc4 allowed bxc4; Qb3 allowed cxb3.
- Bd4+ allowed Kxd4; Qe3+ allowed fxe3; Bd6+ abandoned Nh4 to Kxh4. Checks require capture verification.
