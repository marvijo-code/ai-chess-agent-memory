# Open Sicilian / Taimanov as Black

## T74 SF1G1 v SF19: Old Sicilian 6.Bb5 - DRAW from -7 at m9
- 6.Bb5 pins my c6-knight TO Qd8; 6...a6? only wastes a tempo while pinned. His 7.Nxc6! made 7...bxc6?? the kill: the b-pawn LOADED the c6 square for 8.Bxc6+! Qd7 (forced) 9.Bxd7+ Kxd7 = queen-for-bishop, +7 by move 9 with nothing left to try.
- FIX: with Nc6 pinned to my queen, answer Nxc6 with the QUEEN recapture 7...Qd7! hitting the c6-knight - 8.Bxc6 then meets Qxc6 for even material. Pawn recaptures around a pinned knight are what convert a +2.5 pawn into Q-for-B. General rule: UNPIN FIRST (...Nf6/...Qc7) before any ...a6/...b5 probe; never leave the queen behind a pinned knight.
- SHELL THAT DREW: down a queen from m9, the fortress built by m15 held +8..+11 for 100+ plies while SF shuffled: king d7/d8/c7/e8 inside the Bc8+Rd8 cover; Be7 the SOLE guard of f6, never leaving e7/d8; d6 always double-covered (K+B); knight rotating c6/b8 covered a5/b8/d8/e7; Ra8+Nb8 mutual cover; ALL 1-pawn drips (g3/h5/a5/f7) ACCEPTED - drips never unlock a shell. Model: every unit double-guarded or unreachable (Ra8 sat safe behind his own a4-pawn forever). THREEFOLD IS A WIN; sell nothing for "compensation".

## Invalid-reply discipline (19 tries this game, still survived)
- A rejection whose text cites a move I did NOT play is STALE: hand-verify the intended move from the FEN piece list, then resend the SAME UCI ONCE - accepted 6x this game (Bd8/Be7/Kd7/Kd8/Ke8/Nc6). Never a 3rd try of one move. If the text cites MY move, or the same UCI is refused a 2nd time: different square AND different plan.
- In check with exactly ONE legal reply: run the pawn-path/check-replies check, resend that move once - this has been the save 10x.

## v DeepSeek V4.1 Flash - the repeated kill set
- T74R4 L forfeit (down R+2P from m25): 25...Qa5?? instead of Qd8, which kept b8 guarded. NEVER push BOTH sides of a b6/a6 clamp; push the b5 side only, when the a6 trade recapturer is not needed that turn (29...b5?? was one pawn-fork too late). His 19.Bd3! - when HIS bishop leaves a line square while my pieces are parked behind the same blocker, they are targets on MY next move: the vacation sweep counts HIS vacates too. 24...Nd6?? let his Ne2 fork b7 hitting Qb6+Rb8 with one jump - queen flight Qd8 re-guards. His zero illegal replies: take NOTHING without a full chain census to the LAST capture on the CURRENT board.
- T66R3 L m30: 19...Bxf6?? abandoned d5, guarded only through MY d7-PAWN: 20.Qxd5+ at once. A piece parked behind an attacked pawn defends through it only while the pawn survives - retreat ...Be6-class which also covers, or ...Qd7 before the break.
- T66R2 v Muse L m17 (g4-h4-g5 storm): 12...h6? GIVES him the g5 target and opens my own h-file; 13...Kh8? parks ON the built file; 14...hxg5? re-opens it MYSELF; 16...Bxg5?? blocker with NO named guard = 17.Qxh7#. Counter candidate still untested: 12...Nxd4 13.Bxd4 e5. Every kingside push against an incoming storm: pre-classify as 'covers g5/the files' or BANNED.
- T62R2/T51R1: his e5-class push bans d6/f6 for EVERY of my units, queen FIRST; 13...Qxc3?? met Qxd4 (his b2-PAWN was d4's second guard); a 7th-rank passer is contested from BEHIND only, never 17...Rfd8? into it.

## 3.e5-...Nd5 hybrid v SF (T71R2 L m21, T73R5 L m47) - PLAY AGAIN with the m11 fix
- Line: 1.e4 c5 2.Nf3 Nf6 3.e5 Nd5 4.d4 cxd4 5.Nxd4 Nc6 6.Nf3 e6 7.a3 d6 8.c4 Nb6 (16 plies), then ...Be7 10.Bxe7 Qxe7 11.exd6.
- THE KILL: his d6-PAWN attacks my e7-queen - 11...Qxd6! CAPTURES THE UNDEFENDED ATTACKER = level (nothing guards d6); my 11...Qd7?! was +2.6 and that pawn's cover ended in the Kf8/Qh8# net by m47. 10...Nxd4 in-between candidate unverified.
- Standing bans: the ...h6+...g5 pair (empties king cover; Qh8#); knight parks on the d4-h8 diagonal (20...Nc5?? Qh8#); any kingside push while a vacator sits behind his queen (list his vacators first). A hero blocker (the c5-knight) died to the FIRST pawn hit - have its relief ready before, not after.
