# Ruy Lopez: central breaks, guards and passers

## T27 round 1: White vs Stockfish 19, mate loss
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O b5 6.Bb3! Bc5 7.c3 d6 8.d4 Bb6 9.Re1 O-O 10.h3 Bb7 11.a4 h6 12.Be3 Na5 13.Bc2 Nc4 14.Nbd2 Nxb2 15.Qb1 Nxa4 16.Bxa4 bxa4 17.Rxa4.
- Nc4 attacked Be3 and threatened Nxb2 with a fork of Qd1/Ra4. Nxb2 instead forked Qd1/Ra1 on the actual board; Qb1 saved Q but allowed Nxa4. Bxa4 captured N, not a pawn. Bxa4 bxa4 Rxa4 traded B for N and lost White's a/b pawns for Black's b-pawn: one pawn down; Black's original a6 pawn remained. No verified opening improvement supplied.
17...Bc6 18.Ra3 Qe7 19.d5 Bxe3 20.Rxe3 Bd7 21.Qa1 Bc8 22.Nc4 Nh5 23.Kh2 Nf4 24.h4? f5 25.Qb1 Qf7 26.g3 fxe4 27.Rxe4 Nxd5 28.Qd3 Nf6 29.Re1 e4 30.Rxe4 Nxe4 31.Qxe4 Bf5 32.Qb7 Qxc4.
- h4 was the only marked White mistake; the reported Black advantage jumped from about 1.28 to 5.64 after ...f5. Moving an attacked pawn before a planned knight kick cost a tempo and weakened shelter. With Qe7, trace e7-f6-g5-h4: ...Qxh4+ is a forcing resource to examine before g3. Calculate the central break immediately, not after completing the pawn plan. No verified best replacement supplied.
- ...fxe4 attacked Nf3; Rxe4 then allowed ...Nxd5. ...Nf6 attacked the rook, and after Re1, ...e4 forked Qd3/Nf3. Rxe4 Nxe4 Qxe4 gave R for N and a pawn; it did not restore material equality.
- Bf5 attacked Qe4. Qb7 threatened Ra8 but abandoned Nc4's queen guard. Qf7-e6-d5-c4 was clear: ...Qxc4 took N before answering the rook threat. A forcing-looking queen retreat still needs a guard audit.
- h4/Qb1/g3 took 46/43/52 seconds; Qb7 took 54. These were calculation failures with ample clock. Use shorter verified replies when worse.
- Later c4 Bxc4 Rxc4 recovered B, but Black retained two rooks against R+N. The a-passer forced Nxa2 Raxa2, leaving one rook against two. Stopping promotion was a material sacrifice, not a recovery.
- Final: White Kg5/Rg7/h6; Black Kd5/Ra1/Rf2. 61.h7 Rg1+ 62.Kh6 Rh2#. Rh2 checked along h2-h6; Rg1 covered g5/g6, own Rg7 occupied g7, and own h7 blocked h7. h6-h7 also removed the pawn's guard of Rg7. Scan enemy rook checks and the resulting king box before pushing a seventh-rank passer. No invalid attempts; 2:20 remained.

## T26 final: Black vs Stockfish, mate loss
Open Ruy 6.d4 exd4 7.Re1 b5 8.Bb3 O-O 9.a4 Bb7 10.e5 Ne8 11.Bd5 d6 12.Nxd4 Nxd4! 13.Bxb7! Rb8 14.Bxa6 dxe5 15.c3 Ne6?! 16.Qxd8 Rxd8 17.Bxb5!.
- Bxb7 captured Bb7 instead of recapturing Nd4. Rb8 saved Ra8 with tempo. Ne6 saved the knight but allowed queen exchange/Bxb5, leaving an outside a-passer and pawn deficit. No verified replacement.
- ...Nd6/Bf6/Nc5/Nce4/Ng5 spent tempi while a5 advanced. Be3/f3 could kick the outposts; central activity gave no established compensation.
- Rxb7 axb7 Rb8 Ra8 absolutely pinned Rb8 to Kg8. ...Rxb7 was illegal; ...Rf8 Rxf8+ Nxf8 b8=Q removed the blockader. Check pins and full liquidation before calling a blockade secure.
- ...Nf2 left Kd4's guard; ...Ke4/...Kd3 did not restore it and Qxf2 won N. Many 25-60-second losing maneuvers wasted time.

## Earlier White lessons
- Breyer: Nf1 restores Qd1-d4. Bh6/Qxh6 is safe with Black castled, unlike the uncastled Dragon Rh8 trap. Ng5/Nh5 threatens Qg7#; ...Nxh5 abandons h7, allowing Qxh7+ Kf8 Qh8#. Own Re8 denied Ke8.
- Nbd2 blocks Qd1-d4: ...exd4 cxd4 Nxd4 Nxd4 Bxd4 wins P. Ne5 attacking Qc6 can clear ...Qxg2# with Bb7 support.
- ...Bc5/O-O/d5: exd5 Nxd5 Nxe5 Bxf2+ Kxf2! Nxe5; d4?? Qh4+ Kg1 Ng4. Rxe5 needs ...Qf6+ fork calculation.
- e5 clears Bc2-h7. ...f5 exf6 e.p. Nxf6 Rxe7 won Q for R. d5 Bxd5 lost P because Nf6 blocked Qxd5.
- Bh5/Qe2 share Nf3: Ne5 Bxe2. Ne5 screens Re6-e1: Nxf7 Re1#. Own d4 blocks Qd1-d5: Rxd5 Qxd5.
