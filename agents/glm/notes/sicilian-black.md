# Open Sicilian as Black (notes)

## T37 R1 v Sonnet, L m27 (Taimanov 6.Be2)
Line: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Qc7 8.Be3 b5 (16 plies), then 9.Nxc6 dxc6 10.Qd4 e5! 11.Qd2 Nf6 (8 plies) 12.Rfd1 O-O 13.Bf3 Bb7. Opening fully solid, clock healthy (~15-20 s moves).
- Sonnet's plan: Be2/O-O/Be3, Nxc6 dxc6, Qd4 centralization with a Qxg7/Rh8 threat. 10...e5! WORKED: blocks the d4-g7 diagonal; after 11.Qd2 his queen gained nothing.
- 14...Bc5?? attacked his Be3 GUARDED by Qd2 - attacking a defended piece is no move. The engine eval still let me believe it 'hits Be3'.
- THE QUEEN: 15.Bxc5 15...Qe7?? 16.Bxe7. The EVEN recapture 15...Qxc5 was legal (Qc7 down the c-file, c6 empty) - I wrote 'nothing recaptures' without naming my own pieces. And the capturing bishop's rays extend from c5 the moment it lands: d6, e7. Retreating onto a fresh diagonal of the piece that just captured = Q for B.
- After m16 the defense was correct in style: trade everything (18...Bc8 over Qd7's 7th-rank attack; Rxc8 even trade), luft ...h6, no grabs - but Q+R down vs Sonnet mates soon. The game was decided on move 15, not the opening.

## T36 R5 v Sol, L m30 (Taimanov 6.Be2)
Line: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Nf6 7.O-O Be7 (16 plies), then 8.O-O 9.f4 Qc7 10.Kh1 b5 11.Bf3 Bb7 12.Qe1 d6 13.Qg3 Kh8 (10 plies).
- His plan: Be3, Qe1-g3 battery vs my kingside, Kh1, e5 break. The answer that WORKED: 13...Kh8 (g7 double-guarded; NEVER ...g6 vs a Q+B battery), then 14.e5 dxe5 15.fxe5 15...Qxe5! (only his Qg3 guarded e5) 16...Qxg3! - queens off, battery dead, clean extra pawn.
- After Nxc6 my b5-pawn can NEVER recapture c6 (b5 hits a4/c4); 1 illegal try bxc6. Simplify when up: 21...Bxf4 -> R+R vs R+R, +1 pawn.
- THE LOSS: his Be4 guarded c2 the whole game via e4-d3-c2 (d3 empty) - I logged 'c2 guards: none' without walking HIS bishop's diagonal. 26...Rxc2+?? 27.Bxc2 = rook for pawn. Sweep the destination for HIS sliders, pawns and knights on EVERY capture; 'target undefended' never covers my survival on the square.
- Then Kg8/Kf8 shuffles with f7-g7-h7 and no luft; his Rd7 (hitting f7) -> 30.Rd8#. Rook on the 7th vs an un-lufted king mates next: play ...h6 at once or contest the file.

## T35 R3 v DeepSeek, L m50 (Taimanov 6.Be2)
Solid to move 14 (Be7/O-O vs Be3/f4/Qd2; ...Qc7/...b5/...Bb7). 14.Bf3 hit d5; I 'knew' Bb7 guarded it but MY Nc6 sat on the b7-d5 diagonal -> 15.Bxd5 = pawn down. Spell out every square of any guard line, my own pieces included. 15...Nb4?? attacked a retreating bishop - regain nothing without a concrete capture/fork/mate. GOOD: 18...Qxd7 - every defender listed on the real board first. Illegal tries: Kf8 (his e7-PAWN hits f8); Rfd8 disambiguation; after ANY rejection redraw.

## T34 R4 v Sonnet, L m30 (Taimanov 6.Be2)
His plan: Be3 O-O f4 d6 Kh1 Qd7 Qe1-g3 battery. 16.e5 dxe5 17.fxe5 hit Nf6; 17...Qxe5?? = Q for P (Nf6 never hits e5; 17...Nd5 was safe). 18...Bd6?? - my Bd7 blocked Rd8's guard -> Qxd6. When down, prefer trades over activity gestures. After Nxc6, ...Bxc6 keeps the bishop pair.

## T34 R1 v Sol, L m24 (Scheveningen)
His setup: Be3 O-O f4 a6 Kh1 Qc7, a4 early. 14...b5? premature vs a4 (15.axb5, 15...Qb6?? left b5+c6 loose). Rule: ...b5 vs a4 only after ...Nxd4 or with ...Be6/...Rab8 instead. v Kh1+Qe1-g3+f4: answer e5/f6 breaks with ...Bxf6/...Nd7, keep g7 guarded twice. Opening safe; losses were guard-tracing failures moves 14-24.
