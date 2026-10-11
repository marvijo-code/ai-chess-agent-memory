# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0031-20261011-172532)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 50 | 558547 | 278016 | 49.8% | 49.6% |
| GPT-6.1 Sol | 42 | 1193841 | 1078912 | 90.4% | 91.6% |
| Sonnet 5.5 | 25 | 427698 | 396731 | 92.8% | 94.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8120 | 90493328 | 46435328 | 51.3% | 51.3% |
| GPT-6.1 Sol | 6513 | 189710501 | 176635264 | 93.1% | 93.6% |
| Sonnet 5.5 | 6559 | 143031511 | 136461871 | 95.4% | 96.1% |
