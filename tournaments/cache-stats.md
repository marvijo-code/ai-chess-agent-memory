# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0032-20261011-203427)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 161 | 1928998 | 870400 | 45.1% | 44.7% |
| GPT-6.1 Sol | 102 | 2866572 | 2660224 | 92.8% | 93.4% |
| Sonnet 5.5 | 91 | 1998493 | 1887683 | 94.5% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8542 | 95989801 | 49419264 | 51.5% | 51.4% |
| GPT-6.1 Sol | 6846 | 200382549 | 186578688 | 93.1% | 93.6% |
| Sonnet 5.5 | 6869 | 151396677 | 144481480 | 95.4% | 96.1% |
