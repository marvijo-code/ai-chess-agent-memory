# Ruy Lopez: clearance, king forks and passers

## T27 final: Black vs Stockfish 19, repetition escape
6.d4 exd4 7.Re1 O-O 8.e5 Nd5 9.Nxd4 Nxd4 10.Qxd4 Nb6 11.Nc3 Nxa4 12.Qxa4 d6 13.exd6 Bxd6 14.Bf4 Be6.
- Evaluations stayed near equal through development. This is a usable reference against 6.d4, not a proven equalizing line.
15.Rad1 Qf6 16.Bxd6 cxd6! 17.Qb4 Qe7 18.Qxd6 Qxd6 19.Rxd6 Rfd8 20.Red1 Rxd6 21.Rxd6 Rc8.
- Moving Q off d8 removed Bd6's relative pin but abandoned the queen recapture on d6: ...Qxd6 would lose Q to Rxd6. cxd6 was the only good move.
- Qe7 nominally guarded b7/d6, but d6 had only queen defense against Qb4 and Rd1. Qxd6 Qxd6 Rxd6 traded queens and won a pawn. Count the complete exchange; no verified improvement supplied.
- Result: R+B versus R+N, Black five pawns against six. Rook activity and king centralization did not recover the pawn.
22.f3 Kf8 23.Rd2 Ke7 24.a3 Rc4 25.Nd1 Kf6 26.Nc3 a5 27.Rd6 Ke5 28.Rb6! Rc7 29.Rb5+! Kf4?! 30.Kf2 Bf5 31.Nd5+ Kg5 32.Nxc7.
- Before entering f4, examine Nc3-d5+: d5 attacks BOTH f4 and c7. Kf2 restricted the king further; Bf5 interrupted the rook's fifth-rank control but did not solve the fork. Nd5+ won a FULL rook, not an exchange. No verified best replacement supplied for ...Kf4.
- After ...Kg5, Bf5 was pinned by Rb5 to Kg5; ...Kg6 released it. Refresh pins when king endpoints move.
- ...Bf5 took 63 seconds; routine endgame moves often took 20-35. Finished 7:12 with no invalid attempts. Slow thinking did not supply the missing fork scan.
- Counterplay: ...Kxc5 removed White's c-passer; ...Bxb5 removed its b-passer. ...Kxa3 allowed Nxb5+ to win the bishop, leaving White R+N against pawns. The a-pawn reached a2 and tied Na1 to a1.
- With White Re2, ...Ka3-b4 abandoned a2's king guard and allowed Rxa2. A blockading knight does not prevent a rook from capturing the passer across rank two.
- White instead shuffled rooks; ...Ka3/...Kb4 play ended in a repetition award despite evaluations around +8. Seek practical repetition when lost, but do not infer a fortress or sound compensation.

## T27 semifinal: Black vs Sonnet, mate after queen loss
...cxd4 cxd4/Nc6, Nb3 a5/Be3 a4/Nbd2 Bb7/Rc1 Rac8/Bd3 Qb6?? dxe5! Nxe5 Bxb6.
- d4 screened Be3-b6; dxe5 cleared it while attacking Nc6. Defending b5 did not make Qb6 safe. No verified replacement.
- Rxc1 Qxc1 Nxd3 Qc7 Rc8 Qxb7 Re8 Re3: the fork recovered Bd3, but Qc7/Re3 saved White's major pieces and Qxb7 took Bb7. No sound compensation.
- ...c3 Nd4 Bxd4 Qxd4 c2 31.Qd1?? cxd1=Q+ captured Q and promoted. c2 attacks b1/d1; Re3 could not recapture d1. This gift enabled the win.

## T27 White vs Sonnet: missed win, then mate loss
- Qd1 guarded d4 and b3 through c2; Qf3 abandoned ...Nb3 against Ra1/Bd2. Solve this before g4/h4/g5.
- Qg6/Nf5 vs Kg8/Qf7/g7/Nh7/Bf8: 33.Nh6+! pins g7; only ...Kh8, then Nxf7+ wins Q. Played Qxf7+ Kxf7: legal equal queen trade, missed winning fork.
- Nd4-f3+ forked Kg1/Re1 and won the exchange. b4 allowed axb3 e.p., attacking Ra2 and abandoning Bc3. Later Ra2?? bxa2; Nc2 Rxc2 cleared a1 for promotion.

## Other retained patterns
- T27 White SF: before g3/h4 calculate ...f5/...fxe4/...Nxd5 and Qe7-f6-g5-h4+. Qb7 abandoned Nc4; h7 allowed ...Rg1+/...Rh2#.
- T26 Open Ruy: Nxd4! Bxb7! Rb8 Bxa6 dxe5 c3 Ne6?! Qxd8 Rxd8 Bxb5! left a pawn deficit. b7/Rb8/Ra8 pinned Rb8 to Kg8; ...Rf8 Rxf8+ Nxf8 b8=Q removed the blockader. ...Nf2 abandoned Kd4's guard and later fell to Qxf2.
- Bh6/Qxh6/Ng5/Nh5: ...Nxh5 abandons h7; Qxh7+ Kf8 Qh8#, own Re8 blocks Ke8. Ne5 attacking Qc6 can clear ...Qxg2#.
- Nbd2 blocks Qd1-d4: ...exd4 cxd4 Nxd4 Nxd4 Bxd4 wins P. ...Bc5/O-O/d5: exd5 Nxd5 Nxe5 Bxf2+ Kxf2! Nxe5; d4?? Qh4+ Kg1 Ng4. Rxe5 needs ...Qf6+ calculation.
