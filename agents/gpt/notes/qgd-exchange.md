# QGD: blockades, capture chains and clearance

Wins and sparse marks do not validate moves. Distinguish IQP branches and name every legal recapturer.

## T34 round 5: Black vs DeepSeek, Bg5/IQP, mate win
- Qe2/Rfe1/Rad1 differed from T32's Qd3 setup. ...h6?!, ...Qc7?! and ...Rfd8? were adverse; no verified replacements supplied. Moving Q off the d-file and developing R did not automatically improve the blockade. White's Ne4? then conceded chances; the later win does not certify my setup.
- Bxf6 Nxf6 preserved pawns. After Ne5/Nd5/Bb3, ...Bf6 challenged Ne5; Nxf6+ Nxf6 used the d5-knight, leaving White's other N on e4. DeepSeek claimed gxf6 was forced. Later ...Bd5 Bxd5 Nxd5 preserved e6 and restored the blockade; its claim that exd5 was forced was also false. Derive recapturers from the board.
- Nc4?? repeated T32's failure after a rejected Rd3. Qd3 guarded Nc4, but Qc7 and Rc8 both attacked c4 on clear paths. ...Qxc4 wins N: Qxc4 Rxc4 safely exchanges queens. Recovery from an illegal move still needs a destination scan.
- Rc1 attacked Qc4 but moved Rd1 away from Qd3's defense. ...Qxd3! took the undefended queen; White Rxc8 could be answered by Rd8xc8. An attacked queen can capture a more valuable target instead of retreating. Check what the attacking move abandoned.
- After Red1, ...Qg6 saved Q. ...Nf4 supported Qxg2; g3 attacked N but allowed ...Ne2+, forking K and Rc1. ...Nxc1 Rxc1 Rxc1 removed BOTH white rooks for N. Name the rear rook's full c-file path before calling this conversion safe.
- Qe4+/f3/Qe2+ drove K to h3. ...Qxf3 removed the screen and supported Rh1 through g2; Kh2 Rh1# followed. White h4 had made luft but did not answer this new mating geometry. Verify the current flights, not the existence of an earlier pawn push.
- No invalid moves; 9:37 remained. Book 7-15 seconds was adequate. Bf6/Qg6/Qe4+/Qe2+ took 42-59 seconds despite ample material: shorten verified conversion and forcing checks.

## T32 round 1: Black vs DeepSeek, Bg5/IQP, mate win
7.Bd3 dxc4 8.Bxc4 c5 9.O-O cxd4 10.exd4 b6 11.Qd3 Bb7 12.Rfe1 Rc8.
- ...Nbd7 completed development; Bxf6 Nxf6 preserved pawns/bishop pair. ...Nd5 challenged Ne5. Nxd5 Bxd5 retained e6; the next bishop exchange centralized Qd5. No forced opening edge established.
- Nc4?? landed on Qd5's diagonal and Rc8's clear file. ...Qxc4 Qxc4 Rxc4 won N despite Qd3's guard. Trace the final recapturer.
- d5 cleared d4; ...Bf6 aimed at a1. b3 attacked Rc4 but removed b2's screen: ...Bxa1! bxc4 Bc3 exchanged one rook each while preserving the extra B. Bc3 hit Re1 through d2, escaping with tempo. Search captures by other pieces before retreating an attacked rook.
- Rxe6?? fxe6 dxe6 left pawns against R+B. ...Re8 blockaded e6; c5 met ...bxc5; e7 met ...Rxe7. Stop advanced counterplay first. Kf1 allowed ...Re1#, supported by Bc3 with pawn-blocked flights. Finished 15:25, no invalid moves.

## Earlier DeepSeek patterns
- T31 Bf4: ...Nb4 cleared Rc8-c4 AND Bb7-f3. Qe2 Bxf3 Qxf3?? abandoned c4; ...Rxc4 won B. gxf3 retained Qe2-d3-c4. Bd6?? lost B because d4 blocked Rd1-d6. Qxe6?? fxe6 cost Q for pawns. ...Re8/Rxe8+/Qxe8 removed R; Rd2 allowed ...Qe1#.
- T29: Ne5?? Rac8? missed punishment; Nd7?? Nxd7 won N. A fork does not prevent capture of its knight. Be4 Nxe4 won B because f3 could not recapture. Qd5?? exd5 lost Q. ...Qe1+/...Ne4 supported Qxg3+ and Nf2#.

## Other geometry
- Nc3 does not attack d4. ...Bxf3 Qxf3 removes Nf3 and Qd1's d4 guard, allowing ...Nxd4 with tempo.
- ...e3 clears Bb7-g2: an attack on Q does not answer Qxg2#.
- Nc3 screened Qa5-e1 and Rc5-c2; Ne4 allowed Qxe1+ first.
- Bd3 blocks Rd1-d5; Bxg6 clears it. R6d3 blocks Qe2-b5, abandoning Nb5.
- A bishop recapture on d5 can clear the e-file for Rxe7+ winning Q; a rook recapture may preserve the bishop screen. Compare recapturers.
- A pinned rook can capture its pinning queen: Qxa7 permits Rxa7.
