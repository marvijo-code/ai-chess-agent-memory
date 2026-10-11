# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0025-20261011-030533)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 127 | 2171259 | 1201152 | 55.3% | 55.3% |
| GPT-6.1 Sol | 19 | 319049 | 288384 | 90.4% | 91.2% |
| Sonnet 5.5 | 58 | 1351170 | 1302452 | 96.4% | 96.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6590 | 74067858 | 37282304 | 50.3% | 50.3% |
| GPT-6.1 Sol | 5215 | 150592473 | 140131072 | 93.1% | 93.5% |
| Sonnet 5.5 | 5502 | 121624599 | 116158481 | 95.5% | 96.1% |
