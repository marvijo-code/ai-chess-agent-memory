# DeepSeek V4.1 Flash: concrete tactics

Wins, sparse marks and explanations do not validate moves. Track material, pawn squares, defenders and blockers independently.

## T22 round 3: White Classical Caro, mate win
Classical: e4 c6 d4 d5 Nc3 dxe4 Nxe4 Bf5 Ng3 Bg6 h4 h6 h5 Bh7! Bd3 Bxd3 Qxd3! e6 Nf3 Nd7 Bf4 Ngf6 O-O-O Be7 Kb1 O-O Ne5 Nxe5 dxe5 Qxd3 Rxd3 Nd5 Bd2 Nb4?! Rd7?! Nd5?? Rxb7?! Rfb8 Rxb8+ Rxb8 b3 Bf6?! exf6 gxf6.
- dxe5 attacked Nf6 AND cleared the d-file between the queens. Black could exchange queens before saving Nf6. After Rxd3, ...Nd5 attacked Bf4: Bd2 answered the actual threat.
- Rd7 and Rxb7 were marked inaccuracies despite the win. After ...Nd5, the knight defended Be7. Examine c4 attacking this defender before taking b7; no engine-best replacement was supplied. Rxe7 alone permits Nxe7: a rook invasion does not make the bishop free.
- ...Bf6 landed on e5's capture square. exf6 gxf6 exchanged my pawn for a bishop; pawn protection did not make the cheaper capture harmless.
- c4 Nc7 Bxh6 Rxb3+ axb3 won a rook outright: a2's pawn could capture the checking rook. Then ...Nd5 cxd5 exd5 gave Black's knight for a pawn, despite e6's support. A check or defended destination does not establish a sound sacrifice.
- Rd1 c5 Rxd5: c6 had defended d5, but c5 attacked b4/d4 instead. Refresh pawn guards after advances; adjacent pawns are not automatically a supported chain.
- ...f5 Nxf5 Kh7 Rd8 f6 Bg7 a6 Rh8#. Rd8 alone did not establish Rh8 mate: without Bg7, Kh7 could capture Rh8. Bg7 protected h8 and h6; Nf5 protected Bg7, h5 barred g6, and Rh8 covered g8. Name the essential guard before claiming a mating threat.
- No invalid White attempts; Black had one. Finished 15:39. Book 3-6 seconds; Rd7 took 29, c4 23, Rd1 22. Ample clock did not prevent the missed opportunity on move 19.

## T21 round 3: White Dragon, mate win
...Ne5 h4 h5 Bg5 Nc4 Bxc4 Rxc4! Kb1? Qa5?? Nb3! Rfc8?? Nxa5.
- Kb1 was marked a mistake; no verified replacement supplied. Nb3 saved Nd4 from Rc4 and attacked Qa5. Doubling rooks ignored the queen attack; no forced queen win before that error established.
- ...Rxc3 Qxc3 Rxc3 bxc3 left White 2R+N+B against 2B+N: White lost Q+Nc3, Black Q+2R. Count the whole liquidation.
- Rxd6/Bxf6/Rxd7 removed Nf6 before taking Bd7. After ...Bxc3, Nc6 saved Na5 from the bishop's new attack.
- Rbg7+ Bxg7 Rxg7+ Kxg7 gave BOTH rooks for B, leaving N+5P vs 4P. Include the final king recapture; preserve a rook unless a concrete finish justifies liquidation.
- The a-passer won the race while Black chased f3/e4. Protected queen checks separated king and e-passer before Qxe2.
- Qa7/Nd6 immobilized Kd8. Preserve Black's pawn tempi rather than stalemating: ...gxh3 Ke5 h2 Ke6 h1=Q Qd7#. Finished 12:00; shorten routine conversion moves.

## Earlier Chigorin games as Black
- Qb6 behind Be3/d4 allowed dxe5 to uncover a queen attack AND hit Nf6. Qxc8 Rxc8 Rxc8+ Bxc8 left Black Q against R.
- ...Nf4 attacked Re2 AND cleared Qc4-d3-e2. Bxf4 Qxe2 took R before recovering B; Ng3 Qe1+ Nf1 exf4 used check first.
- ...e2 bxa4 e1=Q# used Qe5's guard of e1/h2. Test promotions before remote grabs.
- ...Nxe3 forked Qd1/Bc2 and cleared Qc7/Rc8. Re1+ Kh2 Be5# exploited Rc2's absolute pin of g2.

## Dragon pawn order and h-file
- ...Ne5 h4 Nc4 Bxc4 Rxc4: answer the fork on Qd2/Bb3 before attacking.
- g4 BEFORE h5 permits gxh5 after ...Nxh5. h5 FIRST Nxh5 g4 Nf6 Bh6 Bxh6 Qxh6 Qe8 g5 Nh5 leaves g6 guarding Nh5; Rxh5 gxh5 gives R for N without proven compensation.
- hxg6 hxg6 clears Rh1's file. Bxg7 Kxg7 Qh6+ Kg8 Qh7# worked after errors; Kg8 was not forced. Rh1 supplies Qxh7's support; Rxh4 clears its blocker.
- Rh1 abandons Rd1's guard of Nd4. Bh6 can also abandon Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for R. DeepSeek missed this; do not reuse it as sound.
- Nf6 guards h7. ...Nxe4 can abandon mate defense; test the finish immediately without expecting repeated errors.
