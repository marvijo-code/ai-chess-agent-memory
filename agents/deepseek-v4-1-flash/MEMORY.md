# Chess memory
Note files (read when the opening appears), one line each:
- notes/capture-safety.md - 5 s scan + blunder catalogue g1-g43
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Chigorin as White
- notes/sicilian-black.md - Dragon/Rauzer as Black
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/four-knights-black.md - 4.Bb5 Bb4 as Black

## Rule 1 - pre-move scan (5 s on the FINAL position, EVERY move)
1. Destination: list ALL enemy attackers (pawn, knight, bishop, rook on rank/file, queen, king) and my defenders. Attacked+undefended -> reject. Vacated squares lose their guard; a pawn push stops guarding its old squares.
2. Open lines: my pawn capture can open a file for his rook onto mine. g43: 18.axb4 opened the a-file; Ra1 was UNDEFENDED (Bb1 blocked Qd1/Re1); 19...Nxb4 vacated a6; 20...Rxa1!. When a file opens at my rook, trade it (20.Rxa8!, which also wins the loose knight next move) or move/defend it THAT move - never a side move (19.Ba3?!) or grab (20.Bxb4??) first.
3. His rook/pawn to an open file at my loose unit = emergency (g42,g43). Scan ALL loose units vs ALL his lines every move.
4. Queen: never on a square his pawn/slider/rook attacks (g37 Qxc3?? bxc3; g43 22.Qa4?? Rxa4 - a-file rook and b5-pawn both cover a4). Every queen capture/trade: count recapturers incl. rooks on the destination rank/file and PAWNS (g42 17.Qxd5?? Rxd5; g36 14...Qxa4??). No Q for R/B/N/P (g18,g35-g43).
5. Knight: never onto an undefended square or one a pawn takes, esp. down material (g24,g40); count recapturers even on checks (g6,g22); pinned Nd7 stays (g15).
6. Forks: cover both targets or vacate one; never step onto a forker's square; 2v2 = last recapturer (g23,g27).
7. Mate nets: Qa1# (Kc1); Qd4# (open d-file, Kf2); Qxh7# with Ng5/Nf5+Qh5 -> ...g6 before her Qh5; back rank: his Q/R on the 8th, no luft; Qe1+/Qxd1# vs loose Rd1.
8. Pawn pushes: never onto a defended piece, a knight/bishop/pawn-attacked square, where his queen gains tempo, while it guards my piece (g12-g30,g40).
9. Never grab a pawn a recapturer defends; B for P loses (g6,g34,g39,g42; g43 21.Bxd6? Bxd6, 28.Bxb5 Bxb5).
10. Legality before sending (3 illegal = forfeit): trace the path square by square; geometry (g43 Qg4 illegal - Nf3 blocked d1-g4, cost a try).
11. Lost position: no 'active' piece to an undefended square; defend/trade; 5-15 s.

## Rule 2 - time
Routine <=15 s; from m10 NO move >25 s. g43: 47-82 s on m14-22 produced the whole collapse; long thinks never fixed anything, the 5-s destination scan does. g43 used 19:00 vs his 5:00 (ended 1:26); g36/g42 flagged/burned clock. Opponents bank time; spend mine only on the scan.

## Openings
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, ...Na5 ...c5 ...Qc7 ...Bb7 ...Rac8; equal through 15...Qxa5, then 16.Bd2 hits Qa5 -> retreat ...Qd8/...Qb6 (never ...Rfd8?? g41). Resolve the centre or reroute knights BEFORE his 15.d5; ...g6 vs Nf5/Ng5+Qh5 (g40). Keep f7 covered; never ...Nc4 with his b3 pawn.
- RL as White (Chigorin): 14...Nb4 -> 15.Bb1!; 14...Nb8: 15.Nf1 Nbd7 16.Be3; 14...Rac8 15.Ne3 Nc4: keep e3 EMPTY (g33). 17.b4 axb4 18.axb4 OPENS a-FILE: fix Ra1 (trade Rxa8) before anything; after 19...Nxb4 20.Rxa8! NOT 20.Bxb4?? Rxa1 (g43). No Q on pawn/rook-attacked squares; never Bx a defended pawn down material.
- Sicilian as Black: Dragon ...d6 ...cxd4 ...Nf6 ...Nc6 ...g6 ...Bg7 ...O-O ...a6 ...Bd7 ...Rc8 ...Qa5 (g28,g36). Rauzer: 11...gxf6! not Bxf6; never leave Bd7 as d6's only shield; no ...Qxa4/...Qxc4 vs rook files; no ...f5/...f4 pushes that guard a knight (g30).
- 4N as Black (4.Bb5 Bb4): 6.Nd5 Nxd5! 7.exd5 Nd4!; nothing on f5 while his Qf3 (g26); no ...Bg4 after h3; play ...Qe7/...Qc8/...Bb5.
- Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O; all four losses were trades/grabs: no B-for-P (12.Bxf6?!, 12.Bxe5??, 10.Bxd4??); keep Bc5 defended while Rfc8/Ra8 can come (g42); after ...d5 count pawn/rook recapturers on d5 (g39,g42); after O-O-O no queen on a1-net squares (g6).

## Opponents
- Stockfish 19 (g6..g43): ~0 s/move; punishes loose units, queens on attacked squares/lines, loose bishops on open files (g42), back-rank.
- Sonnet 5.5 (g7..g43): banks clock; takes EVERY free/attacked unit instantly (Nxa1, Rxb2, Rxd6, Bxe4, Bxa5; g43 Nxb4, Rxa1, Rxa4, Rxc4, Qxc1, Qxe1+, Qxe4, Qxd5). Keep every piece and pawn defended; move an attacked queen at once; a loose rook facing his rook on an open file is lost.
- GPT-6.1 Sol (g9..g38): closed RL, fast; punishes queens on his lines/files; captures must survive recapture (Qxc1??, Nb6?? g35,g38).
