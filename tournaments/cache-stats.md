# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0021-20261010-172846)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 240 | 2990969 | 1928704 | 64.5% | 64.5% |
| GPT-6.1 Sol | 171 | 4643310 | 4412928 | 95.0% | 95.4% |
| Sonnet 5.5 | 141 | 2719209 | 2565957 | 94.4% | 95.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5614 | 62648281 | 30716416 | 49.0% | 49.0% |
| GPT-6.1 Sol | 4602 | 134061904 | 124742400 | 93.0% | 93.5% |
| Sonnet 5.5 | 4822 | 107259455 | 102489470 | 95.6% | 96.1% |
