# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0025-20261011-030533)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 21 | 149028 | 76288 | 51.2% | 50.5% |
| GPT-6.1 Sol | 19 | 319049 | 288384 | 90.4% | 91.2% |
| Sonnet 5.5 | 14 | 136164 | 119234 | 87.6% | 91.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6484 | 72045627 | 36157440 | 50.2% | 50.1% |
| GPT-6.1 Sol | 5215 | 150592473 | 140131072 | 93.1% | 93.5% |
| Sonnet 5.5 | 5458 | 120409593 | 114975263 | 95.5% | 96.1% |
