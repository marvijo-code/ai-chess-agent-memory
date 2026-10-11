# Ruy Lopez: forcing replies, screens and king safety

## T27 final Armageddon: White vs Stockfish 19, mate loss
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O b5 6.Bb3! Bc5 7.Re1 O-O 8.c3 d5 9.exd5 Nxd5 10.Nxe5 Bxf2+? 11.Kxf2! Nxe5 12.Bxd5?? Nd3+! 13.Kg1 Qxd5 14.Rf1 Qc5+ 15.Kh1 Nf2+ 16.Rxf2 Qxf2.
- Kxf2 was the only good move; neither knight attacked f2. This confirmed the existing capture-the-checker lesson.
- Bxd5 removed Nd5 but left Ne5's CHECKING jump to d3, attacking Kf2/Re1. Black inserted this before recapturing Bd5 with Qd8. Do not assume an exchange's next move is the obvious recapture.
- After Qxd5, material was equal: both had Q+2R+B+N and six pawns. The exposed king and Nd3 supplied further forcing play. Qc5+ drove Kh1; Nf2+ forked Kh1/Qd1, forcing Rxf2 Qxf2 and losing the exchange.
- Existing notes warned that Rxe5 needs ...Qf6+ calculation. Avoiding that candidate did not establish Bxd5's safety. No verified best move at move 12 supplied; calculate all checks for each alternative.
17.h3 Re8 18.Qg1 Re1! 19.Qxe1 Qxe1+ 20.Kh2 Qxc1.
- Qg1 invited a queen exchange but Black could insert Re1, pinning Qg1 to Kh1 along rank one. Qxe1 Qxe1+ gave Q for R; Qxc1 then took the bishop. Nb1 blocked Ra1's recapture on c1.
- h3 provided h2 against a first-rank check, but did not protect the queen or bishop. A flight square solves only the specific mate it actually prevents.
- After Qxc1: White R+N versus Black Q+R+B, six pawns each. Later pawn recovery did not repair this deficit.
39.Nd6 Qb8 40.Rh6 Re7 41.Kg1 Qb1+ 42.Kf2 Qe1+ 43.Kf3 Qe3#.
- Qb8 pinned Nd6 to Kh2 through c7/d6/e5/f4/g3. Rh6 defended Nd6 but did not release it; Kg1 did, yet Black's checks denied time to exploit the fork.
- Kf2 entered a mating net. After Qe1+, Kf3 was forced; Qe3# was protected by Re7. Queen covered f2/f4/g3, Bc8 covered g4, and White's own g2 pawn occupied g2.
- Earlier h3-h4 emptied h3 but Bc8 controlled h3 through d7/e6/f5/g4. Empty does not mean safe: audit proposed flights against every enemy ray.
- No invalid attempts; finished 7:18. Bxd5 took 35 seconds with over ten minutes left. This was a forcing-reply failure, not clock shortage. Use 3-10 seconds for verified defense when already lost.

## T27 final: Black vs Stockfish, repetition escape
6.d4 exd4 7.Re1 O-O 8.e5 Nd5 9.Nxd4 Nxd4 10.Qxd4 Nb6 11.Nc3 Nxa4 12.Qxa4 d6 13.exd6 Bxd6 14.Bf4 Be6: near equal, not proven equalization.
15.Rad1 Qf6 16.Bxd6 cxd6! 17.Qb4 Qe7 18.Qxd6 Qxd6 19.Rxd6.
- Qf6 abandoned Qd8's recapture on d6; ...Qxd6 would lose Q to Rxd6. cxd6 was forced. Queen-only defense then lost d6 to Qxd6 Qxd6 Rxd6. Black R+B versus R+N, five pawns against six.
- ...Rc7/...Kf4/Kf2 Bf5 allowed Nd5+ against Kf4/Rc7, losing a FULL rook. Scan knight checks before king invasions. ...Bf5 took 63 seconds without finding this.
- ...Kxa3 allowed Nxb5+ to take B. The a-pawn reached a2 and tied Na1 to a1, but ...Kb4 abandoned a2 to Re2xa2. White instead shuffled and repeated around +8; practical escape, not fortress evidence.

## Other retained patterns
- T27 Black Sonnet: ...Qb6?? dxe5! Nxe5 Bxb6; d4's departure uncovered Be3-b6 with tempo. ...Rxc1/...Nxd3 did not repair queen loss. Later c2/Qd1?? cxd1=Q+ was an opponent gift.
- T27 White Sonnet: Qf3 abandoned Qd1's b3 guard, allowing ...Nb3 against Ra1/Bd2. Qg6/Nf5 vs Kg8/Qf7/g7/Nh7/Bf8: Nh6+! Kh8 Nxf7+ wins Q; Qxf7+ merely traded. Nd4-f3+ forked Kg1/Re1; b4 allowed axb3 e.p. against Ra2/Bc3; Ra2?? bxa2.
- Open Ruy: Nxd4! Bxb7! Rb8 Bxa6 dxe5 c3 Ne6?! Qxd8 Rxd8 Bxb5! left pawn deficit. b7/Rb8/Ra8 pins blockader to Kg8; ...Rf8 Rxf8+ Nxf8 b8=Q removes it. ...Nf2 abandoned Kd4's guard and fell to Qxf2.
- Bh6/Qxh6/Ng5/Nh5: ...Nxh5 abandons h7; Qxh7+ Kf8 Qh8#, own Re8 blocks Ke8. Ne5 attacking Qc6 can clear ...Qxg2#.
- Nbd2 blocks Qd1-d4: ...exd4 cxd4 Nxd4 Nxd4 Bxd4 wins P. Before g3/h4 calculate ...f5/...fxe4/...Nxd5 and Qe7-f6-g5-h4+. Qb7 can abandon Nc4; h7 can allow ...Rg1+/...Rh2#.
