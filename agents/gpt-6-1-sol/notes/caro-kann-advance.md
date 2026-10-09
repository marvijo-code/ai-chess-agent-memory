# Caro-Kann Advance: destination safety and defenders

## T9 round 2: Black vs Stockfish 19, checkmate loss
1.e4 c6 2.d4 d5 3.e5 Bf5 4.Be2 e6 5.Nc3 Nd7 6.Nf3 Ne7 7.Nh4 Bg6 8.O-O c5 9.Nxg6 Nxg6 10.f4 cxd4 11.Nb5! Bc5 12.Nxd4 O-O 13.c3 f6 14.Kh1 Qe7 15.f5 exf5 16.Nxf5 Qxe5! 17.Bd3 Rae8 18.Qg4 Qe7?? 19.Nxe7+ Rxe7.

- This ...Nd7/...Ne7 development differed from the earlier ...Nc6/...Ng6 line. No earlier move received an adverse mark, but that does not establish a best opening repertoire.
- Bc5 pinned Nd4 to Kg1 through empty e3/f2. Kh1 released the pin. Refresh king-dependent constraints immediately.
- Nxf5 attacked Qe7; Qxe5 was marked only good and captured the central pawn. After Qg4, returning to e7 put the queen directly on Nf5's capture square.
- Qe7 defended g7, and Re8 could recapture on e7, but Nxe7+ won queen for knight. The checking capture prevented useful counterplay. A defended destination still loses material when the capturing piece is cheaper.
- Qe7 took 69 seconds with 11:38 remaining. The decisive failure was omission of a direct knight capture, not insufficient thinking time. Before submitting a queen move, enumerate enemy knight attacks on its destination.

### Counterplay and material
27.Rfd1 Ng4 28.Be3 Rxd1+ 29.Qxd1 Nxe3 recovered a bishop and attacked the queen, but required exchanging a rook. Later 33...Re5 34.Qd4 Rxb5 35.Qxg4 Rg5 36.Qc8+ Kh7 37.Qxc7 removed my remaining bishop and one knight. White retained Q+R against R+N; queen chasing had not repaired the deficit.

### Checking pawn abandons knight
After 66.a8=Q Ne4+ 67.Ke3, Black had Kg7/Ne4 and pawns b6/f6/f5. Ne4 was supported by f5. 67...f4+ vacated f5, allowing 68.Kxe4: the king escaped the pawn check and captured the newly undefended knight. The f6 pawn did not defend e4. A checking pawn push must preserve any piece that the enemy king can capture while escaping check.

### Clock
11:38 at move 18, 6:57 at move 32, 1:07 at move 59, 0:41 at move 64. Many defensive moves consumed 25-55 seconds; even below 90 seconds, ...Ne5, ...Nd3+ and ...f4+ took 24-28 seconds. Use the increment for routine defense and reserve longer searches for concrete tactics. Finished with 0:40 and no illegal attempts; clock pressure was secondary to the early queen loss.

## Earlier shared ...Nc6/...Ng6 line
1.e4 c6 2.d4 d5 3.e5 Bf5 4.Be2 e6 5.Nc3 c5 6.Bb5+ Nc6 7.Bxc6+ bxc6! 8.Nge2 Ne7 9.Na4 Ng6?! 10.Nxc5 Bxc5 11.dxc5 Nxe5 12.Nd4.
...Ng6 was inaccurate in both games; no best replacement was supplied. White's c5 pawn attacks b6/d6.

## T7 final: castling did not prevent queen giveaway
12...O-O 13.O-O Qc7?! 14.Bf4 Rac8 15.b4 f6 16.Re1 Qd6?? 17.cxd6 Ng6 18.Bd2 Rfd8 19.Re3 Rxd6.
- Qd6 defended e5/c6 but landed on c5's capture square. Bishop or rook recapture could recover only the pawn, not the queen. Qc7 had blocked Rc8's file.
- 26.Ra2 Rc1 27.Bxc1 bxc1=Q 28.Qxc1 Rxb1 29.Qxb1 Bxb1 left White 2R against B+N, with Black two extra pawns. Count the entire promotion liquidation before claiming recovery.
- 44...Bxg2 45.Kxg2 lost the bishop: neither Kf4 nor Nf5 protected g2. Later ...Kb4 abandoned the protected d2 passer to Kxd2. Lost with 5:20 remaining.

## T4 semifinal: unresolved king pin
12...Qa5+ 13.Bd2 Qxc5 14.Nxf5 exf5 15.Bc3 Qd6? 16.Qe2 f6? 17.f4 d4 18.O-O-O Qc5?! 19.Rxd4 Qe7 20.fxe5 fxe5.
- Qe2 absolutely pinned Ne5 to Ke8. ...f6 supplied support without freeing the knight; ...d4 attacked Bc3 without resolving the pin. White could castle instead of retreating and later won the knight for a pawn.
- Finish: Qe6+ Kf8 Qxf5+ Kg8 Rhf1 Rf8 Qxf8#. Rf1 protected the mating queen; Kg8 blocked Rh8. Attacking the queen permitted its protected capture with mate. Lost with 10:10 remaining.
