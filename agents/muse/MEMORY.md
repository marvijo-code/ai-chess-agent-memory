# Chess memory - Muse Spark 1.3 Contributor (3600+10)

## Record
- T63R1 B v DeepSeek V4.1 Flash 1017: W 0-1 m54 Rh4#. English 1.c4 e5. Exchange up after Nxa8/Qxa8, won via Re6??/Bxb7??, Be8 blockade, a2-a1=Q, Q+R mate.

## Key lessons (read before EVERY move)
- LEGALITY FIRST: walk piece, actual square, occupant, destination, path. After 1 rejection pick a different piece/idea; 3 rejects on one move = forfeit. Zero illegal this game; keep it.
- DESTINATION SWEEP EVERY MOVE, quiet included: enemy pawn captures (both forward diagonals) first, then knights, bishop/rook/queen rays, king captures. My 14...c5?, 17...Bf5??, 19...Nce7?? were engine-flagged; development or defense does not make a square safe.
- MOVER ABANDONS A GUARD: name what left and who hits it now. e4 was hit 3x so 16...exd3 was forced; do not hold a triple-attacked pawn with loose pieces.
- TRAPPED CORNER KNIGHT: after Nbc7/Nxa8, Ne7 held f5/d5 and Q+d5 held escapes. Qxa8 recovered it. When he grabs a8 with N, centralize, cover escapes, take it; do not chase before guarding.
- FREE UNIT FIRST, THEN CONSOLIDATE: h5 was loose Bxh5, b7 fell after Rxd3, Rxg3+ won tempo. Take only after sweep, recount W/B material, rescan my loose units.
- UP MATERIAL = NO GRABS, BLOCKADE + PASSER: Be8 stopped e6/e7, Rd7/Rxe7 removed last pawn, a2-a1=Q decided. Keep blockader on, 5-15 s moves.
- Q+R v bare K finisher: Qe1+ Re4+ Qe3+ Rg4+ Qg3+ Rh4#. Drive to edge with defended checks, rook check seals.
- MATERIAL FROM BOARD EVERY MOVE; after every trade recount guards. Equal trades preserve a deficit.
- CLOCK: routine 10-20 s, capture/check 30-40 s, hard cap 60 s; up material 5-15 s; under 5 min 3-5 s. Finished 4:37 left vs 30:15; 5:11 on Qb8 and 2:51 on Bg4 found nothing. Time goes on destination list, never narrative.

## Openings
- B vs English 1.c4 e5 line that won (14 plies): 1.c4 e5 2.Nc3 Nc6 3.g3 Nf6 4.Bg2 Bc5 5.Nf3 d6 6.d3 O-O 7.O-O h6
- Ideas: Bb6 keeps diagonal after Be3, Be6 hits c4, Re8 contests file, Na5 hits c4, e4 hits Nf3/d3, c5 hits Nd4, Bd7/Qb8/Qc7 hold d6/c5, Ng6/Ne7/Ne5 eyes d3/f4. BANS pending verification: c5?, Bf5??, Nce7?? do not auto-repeat.

## Opponents
- DeepSeek V4.1 Flash 1017: English g3/Bg2/Nf3/d3/Be3/Qd2/Rfe1, queenside N play Na4/Nd4/Nb5/Nd5/Nc7/Nxa8, e4/e5 breaks, f4/h4/h5 pushes, Qe5 centralization. Leaves N trapped on a8, rooks/pawns loose (Re6??, Bxb7??). 0 illegal, banks time. Keep every unit guarded, take loose units after sweep, blockade passers.
- Stockfish 19: not faced yet; take no loose-unit lesson as forced vs it. No gifts, castle early, luft early, no pawn-square landings.

## Notes
- notes/english-e5-black.md - T63R1 English e5 win: setup, flagged moves, conversion.
