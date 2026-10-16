# Open Sicilian: queen checks, screens and actual structure

## T42 round 2: White Maroczy vs SF19, mate loss
- c4/Nc3 met Qa5. f3 reinforced e4 because Nc3 was pinned to Ke1; after Nxd4, Qxd4! was the only good move. Qd2?! was inaccurate despite leaving Bg7's diagonal and preparing development. No verified replacement supplied.
- Be2/O-O met Be6/Bxc4. Bxc4 Qc5+ combined a check on Kg1 through d4/e3/f2 with an attack on Bc4. The f-pawn was on f3, so f2 no longer screened that diagonal. I anticipated the check but treated it as a future queen-chasing opportunity instead of calculating its consequences.
- Kh1 Qxc4 left Q on c4 with d3/e2 empty: it attacked Rf1. Be2 had vacated e2 to capture on c4; Kh1 had removed Rf1's king guard. Qd2 did not guard f1. The bishop exchange removed one bishop each; Black retained an extra pawn, not an extra bishop.
- b3 attacked Qc4 but Qxf1# captured the rook along c4-d3-e2-f1. Qf1 checked Kh1 through g1 and controlled g1/g2; h2 was occupied by my pawn. There was no capture or interposition. A queen attack does not force retreat when she can mate.
- Pattern: after a checking queen pickup, reconstruct her NEW rays before planning counterplay. On Kh1, explicitly inspect f1 and c4-f1 when e2 is empty. Resolve the mating threat before b3 or development. No engine-verified defensive replacement supplied.
- Zero invalid; finished 15:25. Bxc4 took 32 seconds, Kh1/b3 twelve each. Clock shortage was irrelevant; the missing work was the capture and mate scan. Sparse marks did not flag the final blunder.

## T41 GLM: distinguish the actual center
- Black omitted cxd4: my d-pawn remained d4 and N remained f3. Automatic Nc3/Be2/O-O/Be3 was adverse; no verified replacements. This was not the usual Nxd4 board.
- d5/exd5/exd5 renewed the pawn attack on Nc6; O-O ignored it and dxc6 won N for P after Qxc6. Refresh pawn diagonals after recaptures.
- Qd2 was inaccurate. Nd5 hit Qb6/Be7; Nxd5/Qxd5 preserved the extra N. After Qxb2 I had N for two pawns. Rab1 chased Q; Bd3/Qe4 threatened Qxh7# AND Be7. Qc7 answered only the bishop threat. Verify Bd3-h7's clear path and king flights.

## T40 GLM: Ndb5 and conversion
- d6/Be2/O-O/Be3/a6 met Nd4! Nxd4 Bxd4 and Be3! after e5. Qb6+ required Kh1; Qxb2 attacked Nc3. Qd3 was inaccurate; no verified replacement.
- Nd5/Nxd5/exd5 attacked Be6. Rfd8 ignored dxe6 while d6 screened Rd8-Qd3. Rab1 escaped Bf6-a1 with tempo; Rf1 still guarded Bf4 through f2/f3.
- Safe queen exchanges reduced counterplay while B ahead. Rxd7 took an unguarded rook. Bxe5/dxe5 cleared Rf1-f5. Re8/Raxe8/fxe8=Q+ removed Black's last rook and promoted, also uncovering Rd7's check. Include capture-promotions and vacated rays.

## T40 DeepSeek: pawn as queen screen
- Be2/O-O/Be3/f4 met Nxd4; Bxd4 kept B active. With Qf3 opposite Rf8 and Black's f-pawn gone, my f4/f5 pawn screened MY QUEEN. fxe6 cleared the file and allowed Rxf3. Later gifts did not validate it.

## Retained warnings
- Qa5 pins Nc3; f3 guards e4. Ng4 hits Be3 AND uncovers Bg7 against Qd4. b3/Bf2 can uncover Qa5-c3; Qd1 does not guard c3.
- Bh6 reaches Rc1 through g5/f4/e3/d2. Qh3 loses Q to Be6 through f5/g4; f4 does not block f5.
- Long castling: Nc3 screens Qa5-e1; Rd1 guards Re1. Nxd5 or Bd3/Bxd3/Rxd3 can abandon those duties. Short castling: exchanges can enable Bd4+ against Kg1/Ra1 with b2 empty.
- e5 hits Nf6 and clears Bf3's diagonal. Qg3/Bxe5 opens mate only with f6 clear; Nf6 blocks it. Kf8 releases g7's pin.
- Qd5's double attack/support does not prevent Rxd5: Black may stop exchanging. Re7 lands on Nd5's capture square. Bc4 loses to b5xc4; guarding d1 does not stop capture-promotion there.
