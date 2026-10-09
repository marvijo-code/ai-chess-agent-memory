# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0010-20261009-112258)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 127 | 1200027 | 469888 | 39.2% | 38.8% |
| GPT-6.1 Sol | 104 | 2447192 | 2205696 | 90.1% | 90.8% |
| Sonnet 5.5 | 86 | 1361117 | 1267116 | 93.1% | 94.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2574 | 28105229 | 12654336 | 45.0% | 44.9% |
| GPT-6.1 Sol | 2180 | 64518812 | 60026240 | 93.0% | 93.5% |
| Sonnet 5.5 | 2277 | 50745106 | 48495246 | 95.6% | 96.1% |
