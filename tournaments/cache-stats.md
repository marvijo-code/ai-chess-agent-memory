# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0016-20261010-025717)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 23 | 178379 | 100992 | 56.6% | 57.0% |
| GPT-6.1 Sol | 18 | 285782 | 261760 | 91.6% | 92.7% |
| Sonnet 5.5 | 13 | 118964 | 103592 | 87.1% | 91.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3937 | 42807154 | 19915904 | 46.5% | 46.4% |
| GPT-6.1 Sol | 3374 | 98591843 | 91688704 | 93.0% | 93.4% |
| Sonnet 5.5 | 3534 | 78617222 | 75110939 | 95.5% | 96.1% |
