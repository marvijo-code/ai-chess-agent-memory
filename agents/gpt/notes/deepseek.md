# DeepSeek V4.1 Flash: concrete tactics

Wins, sparse marks and opponent explanations do not validate moves. Track material, defenders, pawn squares and blockers independently. More Chigorin history: notes/ruy-lopez.md.

## T19 round 2: Black, Chigorin mate win
Opening through 12...cxd4 13.cxd4 Nc6 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bb7 17.Rc1 Rac8 18.Bd3 Qb6?? 19.Qc2?? Nb4?! 20.Qxc8?? Rxc8 21.Rxc8+ Bxc8.
- Qb6 defended b5 but stood on Be3-d4-c5-b6 behind White's movable d4 pawn. Test 19.dxe5: it opens the bishop's attack on Qb6 AND attacks Nf6. Merely moving Nc6 off the c-file was not sufficient justification. This is a concrete candidate/refutation mechanism, not a supplied engine best line. ...Nb4 was also marked inaccurate; no verified best replacements supplied.
- Nb4 attacked Qc2/Bd3. Qxc8 was not an exchange win: White surrendered Q+Rc1 for both Black rooks. Bc8 recaptured along b7-c8, leaving Black Q against White's remaining R with minors otherwise intact.
- 22.Bc4 bxc4 23.Nxc4 Qc7: b5's pawn captured the bishop; Nc4 then attacked Qb6. Refresh attacks immediately after each capture; do not let a safe capture become a queen loss.
- ...Nd3 attacked Re1. Re2 Qc1+ Nf1 Qc4 supported Nd3. ...Qxa2 Nc4 Qxc4 took a knight that landed on the queen's diagonal a2-b3-c4.
- ...Nf4 attacked Re2 and cleared Qc4-d3-e2. After Bxf4, Qxe2 took the rook before recapturing the bishop: N for R. Ng3 attacked Qe2, but Qe1+ Nf1 exf4 gained time to recover Bf4. Calculate checking replies before assuming a queen must retreat passively.
- e5 dxe5 dxe5 Qxe5 removed the pawn attacking Nf6. Ne3 fxe3 captured White's final knight with the pawn now on f4. Never reuse the pawn's earlier square.
- ...e2 bxa4 e1=Q#: Qe5 guarded e1 and h2; the promoted queen covered f1/f2/h1, while g2 was occupied by White's pawn. Check promotion mates before pursuing remote pawns.
- No invalid Black attempts; finished with 10:31. Some winning moves took 38-53 seconds unnecessarily. DeepSeek spent 36-71 seconds on routine moves and miscounted exchanges; these observed errors are opportunities, not guarantees.

## T18 round 1: Black, Chigorin mate win
After ...cxd4 cxd4, ...Bb7/...Rfe8/...Rac8: Bg5?? h6?? Be3?? Nc4?? Nh5?? Nxe3 fxe3 Qxc2 Qxc2 Rxc2 Nxf6+ Bxf6.
- ...h6/...Nc4 were marked blunders; the win does not validate them. Nxe3 forked Qd1/Bc2 and cleared c4 for Qc7/Rc8. Queen exchanges left Black an extra bishop.
- Re2 was undefended: Rxe2 won R, then Rxe1+ won the other. Kf2 attacked the rook but did not recapture it; Rc1 saved it. Track actual moves over explanations.
- ...Rec8/...R8c3+/...R1c2+ coordinated rooks. Nd4 exd4 captured White's last piece. Re1+ Kh2 Be5# used Rc2's absolute pin of g2: g3 was an illegal interposition. Finished with 13:09.

## Dragon as White: pawn order and h-file
Shared opening: e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 g6 Be3 Bg7 f3 O-O Qd2 Nc6 Bc4 Bd7 O-O-O Rc8 Bb3 Ne5 h4 Nc4 Bxc4! Rxc4!.
- Nc4 attacks Qd2/Bb3; remove it before continuing the attack.
- T17: g4 Rc8?! h5 Nxh5?! gxh5 Qa5 Kb1 Qb4 Bh6 Qb6 hxg6 hxg6 Bxg7 Kxg7 Qh6+ Kg8 Qh7#. With g4 present, Nxh5 loses N for pawn. h7xg6 clears Rh1's file. Kg8 was not forced; no forced win before Black's errors established.
- h5 FIRST: Nxh5 g4 Nf6 Bh6 Bxh6? Qxh6 Qe8 g5? Nh5! Rxh5 gxh5 trades R for N without proven compensation. g5 cannot capture Nh5; g6 protects it.
- Qh6 alone does not protect Qxh7. Rh1 supplies support; Rxh4 clears the blocker. Rh1 abandons Rd1's guard of Nd4, but ...Rxd4 can ignore mate.
- T16 ...Nxe4 abandoned h7; T13 ...Nh5 with g4 still present allowed gxh5. Test ...Nh5 before claiming g5 forces Nf6 away.
- ...gxh5 Bh6?? abandons Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for R. DeepSeek missed it. ...Nxe4 then abandoned h5/h7; Rxh5 cleared the file and supplied mate support.
