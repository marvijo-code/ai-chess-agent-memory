# Chess memory - Muse Spark 1.3 Contributor (3600+10)

## Record
- T66R1 W v DeepSeek V4.1 Flash: D 1/2-1/2 m67 insufficient-material flag draw. Caro Classical. 24.Re4?? Qxc4 dropped Q through own Bd4 screen. Held down Q 40+ moves to bare K vs RR flag.
- T64R1 W v Stockfish 19: D 1/2-1/2 m37 threefold. Yugoslav. 11.Bd4 over Bc4?, 12.Bc5! vs e5, 13.Ba3? Qb6, 14.Rb1?? Nxc3 e4! Bxf8 Bxc3+ bxc3 Qxb1+. Drew by Bc2 + Kg3/Kf2 repeat.
- T63R1 B v DeepSeek V4.1 Flash 1017: W 0-1 m54 Rh4#. English 1.c4 e5. Exchange up after Nxa8/Qxa8, won via Re6??/Bxb7??, Be8 blockade, a2-a1=Q, Q+R mate.
- T63R3 W v Stockfish 19: D 1/2-1/2 m20 threefold. Yugoslav 11.Bc4? Nxe3 left Bc4 loose, 12.Bc5! vs e5, 13.b3? Qxc3. Held by Rf2/Rf1 repetition.
- T63F W v Stockfish 19: L 0-1 m18 Bxc3#. Yugoslav bxc6! line. O-O-O? into Bf5/Qc7/Rfb8, Qc1? met Rxb2+ Ka1 Rb7+ c3 Qxc3 Bxc3#. 0 illegal.

## Key lessons (read before EVERY move)
- LEGALITY FIRST: walk piece, actual square, occupant, destination, path. After 1 rejection pick a different piece/idea; 3 rejects one move = forfeit. Zero illegal; keep it.
- DESTINATION SWEEP EVERY move, quiet included: enemy pawn captures (both forward diagonals) first, then knights, bishop/rook/queen rays, king captures. 14...c5?, 17...Bf5??, 19...Nce7?? were engine-flagged; development or defense does not make a square safe.
- MOVER ABANDONS A GUARD: name what left and who hits it now. e4 was hit 3x so 16...exd3 was forced; do not hold a triple-attacked pawn with loose pieces.
- OWN SCREEN KILLS BATTERIES: 24.Re4?? Qxc4 dropped Q because own Bd4 on d4 blocked Re4-c4. Rxc4 was illegal through own bishop. Before any Q+R alignment walk path square by square and name OWN blockers first. Same as Nd2 blocks Qd1-d3, Be3 blocks Re1-e4.
- CARO Qc4 DANCE IS LOOSE: 16.Qxd4 Qb6 hit d4, 17.Qc4 met 17...Qb4 tempo, 18.b3 Qb6 hits b3/f2, 23.Bd4 Qc7 24.Re4 Qxc4. Keep Q off c4 while Qb6/Qb4 + Be7 live. Meet ...c5 with guards on d4, no Rab1/Qe3 drift.
- YUGOSLAV d5 BREAK + B-FILE RULE: after exd5 Nxd5 Nxc6 Black plays bxc6! (only good, keeps d5, OPENS b-file). Bd4 guards c3 and is the fix over Bc4?; after e5 Bc5! escapes with tempo on f8 (engine !). BANS after bxc6!: Bc4?, b3?, O-O-O, Ba3?, Rb1?. Before any Ba3/Rb1 list Nxc3 + e4! opening Bg7 to c3, Qb6/Rb8 hits on b2, and Bxc3+ bxc3 Qxb1+ idea. Rb1 on the b-file invites Qxb1+.
- Nxc3 + e4! PATTERN: Qxc3! is the right recapture but e4! opens g7-c3 and hits f3/d3. Do not assume Qxc3 consolidates; after e4! keep f3 covered, expect Bxc3+ sac, keep rook OFF b1 where Qxb1+ wins with check.
- NEVER CASTLE LONG INTO OPEN B-FILE: bxc6 removed b7 so Rb8/Qc7/Qb6/Bg7 all see b2. O-O-O went +1.92 after Bf5, +4.30 after Qc7. With b-file open keep K central/short, play Bd4/Be2, block c2, contest b-file first. O-O-O needs b2 x2 guarded and c2 covered.
- Qc1 DOES NOT HOLD b2 vs SAC: 15.Qc1? (K-only guard) met Rxb2+ Ka1 Rb7+ c3 Qxc3+ Qxc3 Bxc3#. Before Qc1 count Rxb2+ Kxb2 Qb6+/Qc7+, Rxa2+ ideas, Bg7 x-ray on b2, a2 loose. Answer is no Qc1 while a2/b2/c2 all loose.
- TRAPPED CORNER KNIGHT: after Nbc7/Nxa8, Ne7 held f5/d5 and Q+d5 held escapes. Qxa8 recovered it. When he grabs a8 with N, centralize, cover escapes, take it; do not chase before guarding.
- FREE UNIT FIRST, THEN CONSOLIDATE: h5 was loose Bxh5, b7 fell after Rxd3, Rxg3+ won tempo. Take only after sweep, recount material, rescan loose units.
- UP MATERIAL = BLOCKADE + PASSER: Be8 stopped e6/e7, Rd7/Rxe7 removed last pawn, a2-a1=Q decided. Keep blockader on, 5-15 s moves.
- DOWN HUGE CAN DRAW VS FLAGGABLE OPP: T66 down Q at m24 held 40+ moves to RR vs bare K flag draw. Shell: Kf1/Kg1/Kf2 holds f2/g2, Rf2/Rd2/Re2 2nd rank, Be5/Bd4 central, Ng3 blocks Qh2+, NO pawn pushes. Seek Rxe5 Bxe5 Q-for-R cuts, BxN/KxB freebies. Never resign; up clock = force checks, keep 10-30 s moves, let him flag.
- DOWN HUGE v SF CAN DRAW: K behind f2/f3/g2, rooks covering, no pawn pushes, no opening files, repeat same shell. T64 model down Q vs R+B at +11: Bc2 blockades c-passer, Kg3 holds f3/g2/h2, Kf2 behind f3, invite Qc5+/Qg5+/Qd2+ for Kg3/Kf2 threefold.
- Q+R v bare K finisher: Qe1+ Re4+ Qe3+ Rg4+ Qg3+ Rh4#. Drive to edge with defended checks, rook check seals.
- MATERIAL FROM BOARD EVERY move; after every trade recount guards. Equal trades preserve a deficit.
- CLOCK: routine 10-20 s, capture/check 30-40 s, hard cap 60 s; up material 5-15 s; under 5 min 3-5 s. 2:47 Bc5!, 1:44 Rb1??, 2:42 Ke2, 2:59 Ke1 found nothing. Time goes on destination list, never narrative.

## Openings
- B vs English 1.c4 e5 line that won (14 plies): 1.c4 e5 2.Nc3 Nc6 3.g3 Nf6 4.Bg2 Bc5 5.Nc3 d6 6.d3 O-O 7.O-O h6
- Ideas: Bb6 keeps diagonal after Be3, Be6 hits c4, Re8 contests file, Na5 hits c4, e4 hits Nf3/d3, c5 hits Nd4, Bd7/Qb8/Qc7 hold d6/c5, Ng6/Ne6/Ne5 eyes d3/f4. BANS pending verification: c5?, Bf5??, Nce7?? do not auto-repeat.
- W Caro Classical 3.Nc3 dxe4 line level to m13 (16 plies): 1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.h5 Bh7 8.Nf3 Nd7
- Ideas: Bd3 BxB QxB, Bf4, O-O, Rfe1 vs Be7/O-O, hold d4 vs ...c5, no Rab1/Qc4 drift. BAN: 24.Re4?? through Bd4 screen into Qxc4.
- W vs Dragon Yugoslav level to d5 (16 plies): 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.f3 O-O 8.Qd2 d5
- Ideas: exd5 Nxd5 Nxc6 bxc6! was played 3x; expect bxc6! not recapture to d-file. Fix is Bd4 (guards c3, Q holds b2) then Bc5! vs e5 with tempo on f8. BANS: Bc4?, b3?, O-O-O, Ba3?, Rb1? after bxc6?. Guard e3/b2/c2, meet Bf5-c2/Qc7-c2/Rb8-b2 before castling long. Keep rook off b1 into Qxb1+.

## Opponents
- DeepSeek V4.1 Flash 1017: English g3/Bg2/Nf3/d3/Be3/Qd2/Rfe1, queenside N play, e4/e5 breaks, f4/h4/h5 pushes, Qe5. Leaves N trapped on a8, rooks/pawns loose (Re6??, Bxb7??). 0 illegal, banks clock. Keep every unit guarded, take loose units after sweep, blockade passers. Caro Classical Bf5/Bg6/Bh7/Nd7/e6/Ngf6/Be7/O-O + ...c5, Qb6/Qb4/Qc7/Qc5 dance; converts Q-up but flags low (T66 0:38 + 1 illegal). Fight on down material, keep shell, force moves.
- Stockfish 19: drew Yugoslav m20 and m37, mated Final m18. Punished 11.Bc4? with Nxe3/Rb8/Qa5/Qxc3, 12.O-O-O? with Bf5/Qc7/Rfb8/Rxb2+, 13.Ba3?/14.Rb1?? with Nxc3/e4!/Bxc3+/Qxb1+. Plays bxc6! to keep d5 and open b-file, e5+e4 to open Bg7. No gifts, castle early but never long into open b-file, guard e3/b2/c2, no Bc4/Ba3/Rb1 while Qb6/Rb8 live. Down huge keep Bc2 + Kf2/Kg3 shell for repeat.

## Notes
- notes/english-e5-black.md - T63R1 English e5 win: setup, flagged moves, conversion.
- notes/dragon-yugoslav-white.md - T63R3 draw + T63F loss + T64R1 draw vs SF: bxc6!/b-file, Bd4/Bc5! fix, Bc4?/b3?/O-O-O/Ba3?/Rb1? bans, Nxc3/e4! and Rxb2+ tactics, Bc2 + Kg3/Kf2 repetition.
- notes/caro-white.md - T66R1 Caro Classical draw: h4-h5 squeeze, Qc4/Re4 screen blunder, down-Q shell to flag draw.
