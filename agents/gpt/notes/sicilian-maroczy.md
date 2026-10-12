# Open Sicilian: pinned guards, clearance and king files

## T34 Final: White vs Stockfish 19, mate loss
- Maroczy c4/Nc3 met ...Qa5 before f3. Be3? reinforced d4 but left e4 defended only by Nc3, absolutely pinned to Ke1 along a5-b4-c3-d2-e1. ...Nxe4! won the pawn. Count legal defenders BEFORE routine development. No engine-verified move-7 replacement supplied; distinguish the earlier f3/Qxd4 branch.
- Nxc6 attacked Qa5, but ...dxc6 removed the knight and ...Nf6 escaped Qd4. I never recovered e4. A tempo against the queen did not establish compensation. Qh4?! met ...h5; no verified better queen destination supplied.
- O-O-O/Rhe1 changed the diagonal's endpoint from Ke1 to Re1. Nc3 was now its screen, and Rd1 guarded Re1 through d1-e1. Nxd5 removed Nc3; ...cxd5/cxd5 also emptied Black's c6 and my c4. Trace a previously pinned piece's rear line even after castling releases the king pin.
- Bd3 invited ...Bxd3. Rxd3 moved Rd1, Re1's LAST defender, allowing ...Qxe1+ along e1-d1-c1. Before proposing a trade, place the eventual recapture and list what its departure exposes. Neither the rook's activity nor its support of d5 answered the queen's capture. No verified best replacement supplied.
- Rd1 blocked the queen check but tied the rook to shielding Kc1. ...Rfc8+ then used the empty c-file: c7/c6/c5/c4/c3/c2 were clear. Bc5 fell to ...Rxc5+; Qc4 fell to ...Rxc4+; Kb1 allowed ...Qxd1#. Calculate the next capture of a checking block, plus the other attacker's lines. Seek king flights before giving successive blockers.
- No invalid attempts; 12:02 remained. Nxd5/Bd3 took 47/48 seconds, routine Rxd3 six. A familiar recapture deserves critical time when it moves the last guard. Clock shortage did not cause this loss.

## T34 semifinal 1: White vs DeepSeek, mate win
- Be2/O-O/Be3/f4/Kh1, a4/Bf3/Qe1-g3 coordinated against ...d6/...Nc6/...e6. Distinguish Scheveningen/Classical from Dragon/Maroczy; no forced opening edge established.
- ...Nxd4 Bxd4 created Bd4-e5-f6-g7 support for Qg3. ...Bc6/...Nd7 left f6 clear. ...e5 attacked B and screened the diagonal; fxe5 Nxe5 replaced that pawn with a d6-guarded knight.
- Nd5 hit Qc7/Bc6/Be7. Ne5 could not capture d5 without uncovering Qxg7#. ...Qd7? allowed Bxe5, removing the screen while retaining bishop support of g7. ...Bxd5? ignored Qxg7#. Guarding the screen materially did not solve its mating duty; no verified best Black defenses supplied.
- Finished 13:22; Nd5/Bxe5 took 54 seconds each. Shorten follow-ups once the battery and recapturers are verified.

## T34 round 1: White vs GLM, mate win
- ...Rfc8-b8/...b5? against a4 allowed axb5, hitting Nc6. ...Qb6? ignored bxc6; later exchanges retained my extra minor.
- Ra1/Rf1 guarded each other through empty b1-e1; Ruy bishops had blocked the same recapture. Rfb1 defended b2.
- ...b5 cleared b7, exchanges cleared c6, and e5 cleared e4, uncovering Bf3-a8. ...dxe5 ignored Bxa8; Rxa8 converted my extra minor into an extra rook.
- ...Qd3 allowed c2xd3. exf6 captured N and supported g7; ...Rxd3 ignored Qxg7#. Finished 13:51, no invalid moves.

## T31: White Maroczy vs Stockfish, mate loss
- With f3/Qxd4/Be3/Be2, O-O?! allowed ...Ng4 hitting Be3 AND uncovering Bg7 against Qd4. Qd2/Qxe3 preserved pawns but conceded bishop pair; no verified castling replacement.
- Rfd1?! allowed Bxc4 Bxc4 Rxc4, losing P. A bishop guard enabled an exchange, not a free recapture. Nd5 cleared Rc8-c1 against Rc1.
- Rxd6 won one pawn while ...Qxa2/...Qxb2 won two. Queen trade left R+N versus R+B, four pawns versus six.
- ...Rb1+ forced king defense of loose Rb7: Kb3 screened the rook ray; Ka4?? exposed ...Rxb7. Examine legal blocks and rays beyond K. ...a2! later outran Kxa3 despite Nxd6 removing Ba3. Finished 9:11.

## Retained warnings
- Refresh support after cxb5 or queen relocation. ...Qa5 pins Nc3; Bd2 blocks Qd1-d4.
- Scan capture-promotions: guarding d1 does not stop ...dxc1=Q.
- A bishop can escape a knight fork with check; a king can screen its rook's support of a promoted queen.
