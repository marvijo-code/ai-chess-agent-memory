# QGD Lasker: candidate safety before activity

## Tournament 3, round 2: White vs Sonnet 5.5, checkmate loss
1.d4 Nf6 2.c4 e6 3.Nf3 d5 4.Nc3 Be7 5.Bg5 O-O 6.e3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7! 9.Rc1 Nxc3 10.Rxc3 dxc4 11.Bxc4 c5 12.O-O Nc6?! 13.d5?! exd5 14.Bxd5 Nb4 15.Bb3 Bf5 16.a3 Nc6 17.Qe2 Nd4 18.Nxd4 cxd4! 19.Rc5?? Qxc5 20.exd4 Qxd4.

## Central advance and queen constraint
- Rc1/Rxc3 preserved the pawn structure but put the rook where a black pawn on d4 would attack it.
- 13.d5 attacked Nc6, but ...exd5 Bxd5 Nb4 let Black gain a tempo against the bishop. d5 was marked inaccurate; no better move or evaluation was supplied. Do not repeat it merely because it attacks a knight.
- Before ...Nd4, White had Kg1/Qe2/Rc3/Rf1/Bb3/Nf3, pawns a3 b2 e3 f2 g2 h2. Black had Kg8/Qe7/Ra8/Rf8/Bf5/Nc6, pawns a7 b7 c5 f7 g7 h6.
- ...Nd4 attacked Qe2 and Nf3. The e3 pawn blocked Qe7's line to Qe2, so exd4 would expose the queen to ...Qxe2. This was a constraint involving queens, not a king pin.
- Nxd4 cxd4 exchanged knights and attacked Rc3. The rook destination now required a fresh capture scan.

## Decisive rook loss
- 19.Rc5 attacked Bf5 across the fifth rank, but Qe7 already attacked c5 along e7-d6-c5. The rook was undefended and ...Qxc5 won it outright.
- Attacking a bishop does not require the opponent to move that bishop. Examine every capture of the attacking piece before describing the move as a tempo.
- After ...Qxc5, the queen no longer occupied e7, so the earlier restriction on exd4 disappeared. 20.exd4 was possible, but ...Qxd4 then took that pawn too. The rook loss had no established compensation.
- No engine-approved replacement for Rc5 was supplied. The verified lesson is to reject the hanging rook move and calculate a safe response to the pawn attack.

## Second material loss, absent from move marks
21.Qf3 Be4 22.Qg3 Rad8 23.Qc7 Rd7 24.Qa5 Qxb2 25.Ba4 Rd5 26.Qc7 Qb6 27.Qf4 Qd4 28.Bc6 bxc6.

- Bc6 attacked Rd5 and b7, but the b7 pawn could simply capture the bishop. A pawn I attack can also attack my piece.
- This move had no supplied adverse mark, yet its material consequence is explicit. Scan all enemy pawn attacks, including pawns still on their starting ranks.
- After losing rook and bishop, queen activity and king advances did not recover the deficit. 29...Bd3 uncovered Qd4's attack on Qf4 while attacking Rf1; Qxd4 Rxd4 led to a hopeless material imbalance.

## Practical lessons
- The opening was played quickly without illegal attempts. White still had 14:25 after Rc5 and 11:01 at the final mate: clock pressure did not cause this loss.
- Use calculation time to verify destinations and resulting enemy captures. Neither a plausible activity narrative nor an attack on another piece establishes safety.
- Sonnet exploited the central knight jump, maintained queen defense of c5, and took exposed pieces. Its 12...Nc6 inaccuracy did not prevent the later forcing play.
