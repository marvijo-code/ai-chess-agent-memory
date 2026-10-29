# White Caro Advance vs DeepSeek (W: T29R1, T32R3, T40R5, T45R5, T74R1; D: T74 SF2G1 G1)

Setup v 3...Bf5: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 e6 5.Be2 Nd7 6.O-O Be7 7.c3, then Nbd2, Nb3, Bd3 (v 7...Rc8 Nbd2).

## T74 SF2G1 (DRAW m57: a bishop up from move 25, then gave it back; clocks 22:00 v 4:19)
- Line: ...Be7, ...Nd7, ...c5, ...cxd4, ...f6 break. After exf6 Ngxf6: Nb3, Be3, Rc1, Nc5 (trade the d7 knight), Ne5, f3, f4 = equal. DeepSeek burned 6:43 on 20...Nxe5.
- 24...Bc5?? 25.dxc5 bxc5 won B for P (SF: Kf7?? and Bc5??). I then traded the f5 bishops and rooks (Bg4, Bxf5, Rxf5) and had R+B v R with a queenside majority v his c/d pawns.
- THE SLIP: 29.Bc3 d4 30.Bd2 Ke6 31.Bf4 Kd5 32.b4?? c4 (SF ??). b4 fixed c4/d4 as connected passers; my bishop shuffled (Bg3, Bd2, Bf4), my rook sat on d1, and his K walked d5-d4-c3. Then h4?!, Bxa7?!, gxh3?! left pawns loose, he took a3/b4 and queened threats forced a draw.
- FIX (unverified): the moment the queens are off and I am a piece up, K to the centre (Kf2-e2) BEFORE ...Kd5-d4; bishop on the b2-c3 diagonal blocks d4/c3; keep a2/b2 home, no b4; trade the last rooks only after counting K+B v his pawns; rook behind or beside the passers, not a 1st-rank blockader.
- ENDING CLOCK: I repeated Rf1/Rd1 at 22:00 v 4:19 while he was nearly flagging (he played 1-3 min a move). When he has <5 min and I have 15+, never take the threefold: make safe non-repeating moves (K or bishop steps, all units guarded) and let him flag.

## T45R5 (3...Bf5 with ...Ne7, ...Bg6, ...c5; W m19)
- Nbd2 BEFORE c3 (c3 first allows ...Bxb1). After ...c5: dxc5 Nxc5, Nb3 Nxb3, Qxb3 Nf5.
- 12.Qxb7 hit Ra8; ...Qd6?? stood on my e5 pawn's capture square: exd6, Qxa8+. Queen+rook up: Re1, Bf4, Ne5, Qd7# (no luft, Ne5 guarded d7).
- Check before a grab: ...Rb8 Qxa7 Rxb2 Bxb2.

## T40R5 (3...c5, W m37)
- Nf3 cxd4 Nxd4 Nc6 Nxc6 bxc6, then Nc3, e6, Bd3, Ne7, O-O, Ng6, f4: Rf1 + Bc1 guard f4. Then ...Be7, Qe1, Qg3 (aims at g6/g7).
- ...f6 Bxg6 hxg6 Qxg6: g7 pinned by Qg3, so ...gxf6 is illegal; look for it whenever his bishop lands on f6 against e5.
- ...Qd4+ answer Kh1 (Be3 hangs to ...Qxe3+). SF marks: 14.Qxg6?! (...f5 kicks), 22.Qa5?? (queen beside his Qb4 on b2/Nc3).

## T29R1 (Be7/Rc8 setup)
- ...Bg6, Nb3 h6, Bd3 Bxd3, Qxd3 c5, Nxc5 Nxc5, dxc5 Bxc5, Be3: Qxe3 hits a7; Qxa7 safe. With Bd3 + Nb3, Bxh6 and Nh4 lose a piece (Bxh4). DeepSeek hung ...Qd6?? to exf6/exd6.

## T32R3 (...Ne7-g6, ...f6; W m27)
- Plan Ng6 + ...f6. Bf4?? Nxf4: Qd3 does not recapture on f4 (no line). Better Rfe1/Bg5/Nc5, e6 and f6 as targets.
- Keep the pin Qg4 v Ng7, trade rooks, no pawn grabs. Conversion R+N up: b3 v ...Rb2, Rc8+ then Ne6 and Rd8#; before Ne6 check Kxe6.

## Rules
- Bishop to f4/g5 where a knight hits it: name the recapturer square by square BEFORE the move.
- In a won game every queen capture of a pawn: which pawn recaptures? (T29R1 Qxe6?? fxe6).
- Queen/piece up: trade pieces, mate on the e-file/back rank; he has no luft (T45R5).
- DeepSeek habits: 30-43 s on quiet moves (up to 6:43), illegal tries on pins/blocks, no counterplay when down, hangs a queen or bishop on a pawn's capture square (T29R1, T40R5, T45R5, T74 ...Bc5??). It also BURNS ITS CLOCK: bank time, keep everything guarded, and do not repeat while it is short.
