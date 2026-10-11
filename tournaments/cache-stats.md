# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0027-20261011-075651)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 218 | 2260998 | 1235456 | 54.6% | 54.6% |
| GPT-6.1 Sol | 236 | 7564663 | 7065984 | 93.4% | 93.7% |
| Sonnet 5.5 | 207 | 4584184 | 4379522 | 95.5% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7262 | 81046460 | 41045504 | 50.6% | 50.6% |
| GPT-6.1 Sol | 5780 | 167718398 | 156189184 | 93.1% | 93.6% |
| Sonnet 5.5 | 6034 | 133016748 | 127004720 | 95.5% | 96.1% |
