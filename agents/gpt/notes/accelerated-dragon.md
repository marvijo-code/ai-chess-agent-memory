# Accelerated Dragon: liquidation, discoveries and queen safety

## T31 Final Armageddon: White vs Stockfish 19, mate loss
1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.f3 Bd7 9.Qd2 a6 10.O-O-O b5 11.Bb3 h5 12.Kb1 Na5 13.h4 Nc4 14.Bxc4 bxc4! 15.g4?! hxg4! 16.h5 Rxh5 17.Rxh5 Nxh5 18.fxg4 Bxg4! 19.Rg1 Bd7?!.
- Same failed kingside liquidation as T10: my f/g/h pawns disappeared for Black's h-pawn. Two pawns down; exchanged rooks and B for N did not compensate. No verified move-15 replacement.
- fxg4 attacked Nh5, but Bd7 took g4 through e6/f5 and attacked Rd1 through f3/e2. An attack on one piece does not force its retreat. Calculate captures by every other piece before launching the storm.
20.Bh6 Bh8 21.Nd5 Nf6 22.Qe3?! Ng4?? 23.Qd2? Nxh6 24.Qxh6 Bxd4 25.Rd1 Be5.
- Ng4 forked Qe3/Bh6 AND uncovered Bh8-g7-f6-e5-d4 against Nd4. Qd2 initially guarded h6 and d4, but Qxh6 abandoned d4. The final bishop capture left Q+R+N against Q+R+2B, still two pawns down.
- Search captures of the forking knight before automatically retreating. 23.Rxg4 is legal, but Bd7 can recapture; calculate the resulting position rather than claiming a free knight. No verified best move 23 supplied.
26.Qh7 Be6 27.Qg8+ Kd7 28.Nc7?? Qxg8 29.Nxa8 Qxa8.
- Be6 vacated d7, answering the claimed Qg8 mate threat with a king flight. Nd5 screened Rd1-d7. Recheck flights after quiet defenses.
- Kd7 removed the king from Qd8-e8-f8-g8, leaving Qg8 directly attacked. Nc7 forked Ra8/Be6 but ignored Qxg8. Qxa8 then captured the knight along the cleared eighth rank: Q+N lost for R. The fork did not force a reply; no adverse mark on Nc7 does not excuse the queen loss.
- With R versus Q+2B, king raids supplied no established counterplay. Kxa6 Qa8+ Kb5 Qa5# ended the game. Scan checks and the resulting flights before advancing an exposed king.
- No invalid attempts; finished 5:14. fxg4 took 117 seconds, Bh6 68. White started with ten minutes; these long thinks did not prevent tactical losses.

## T16 round 2: White vs Stockfish, mate win after queen loss
Same opening through 12.Kb1 Na5, then 13.Bh6?? Bxh6 14.Qxh6 Rxh6.
- Black had not castled: Rh8 stood behind empty h7/h6 after ...h5. The intended queen recapture lost Q to the rook. An attacking purpose does not establish destination safety; inspect the final recapture board.
- Later Nd5-f4 cleared Bb3's diagonal; Nxg6+ f7xg6 cleared f7 and Rxg6 removed that pawn. Bb3 then guarded g8 through c4/d5/e6/f7.
- Doubled g-file rooks exploited ...Qf8??: Rg8+ Qxg8 Rxg8#. Bb3 prevented Kxg8 and Rh7 occupied h7. Opponent consolidation errors enabled the win; no earlier forced compensation established.

## T10 semifinal Armageddon: White, mate loss
12.h4 Na5 13.Kb1 Rc8 14.g4?! hxg4 15.h5 Nxb3 16.axb3 Rxh5 17.Rxh5 Nxh5 18.fxg4 Bxg4! 19.Rg1 Nf6.
- Nh5 came from f6; g6 remained. The same two-pawn loss and Bd7-g4-d1 attack recurred in T31.
- ...Qe6 directly attacked g4 through f5: Rg4?? Qxg4 lost R. After Bxe5+ dxe5, Qd6?? exd6 lost Q to the ORIGINAL e7 pawn; the pawn on e5 came from d6. Track pawn identities and diagonals despite sparse marks.

## Retained Black rook lessons
- ...Rb7/a5/Bxe4/Rxe4/Rxb6 worked only with the concrete ...Rxa1+ Re1 Rxe1# reply to axb6. After White relocated its rooks, ...Kg7?? axb6 Rxb6 lost R for P: the old mating defense no longer existed.
- ...c5 Rf4! cxb4 Rdxf7+ Kg8 Rxf8+ captured Bf8. Rf4 guarded f8, preventing Kxf8. Attacking a rook did not stop forcing checks. Later repetition with White Q/R material gone was a conversion escape, not proof of a theoretical draw.
