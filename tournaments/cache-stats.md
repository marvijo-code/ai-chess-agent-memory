# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0031-20261011-172532)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 176 | 2402997 | 1516032 | 63.1% | 63.2% |
| GPT-6.1 Sol | 94 | 2292977 | 2050176 | 89.4% | 90.5% |
| Sonnet 5.5 | 141 | 3925622 | 3772449 | 96.1% | 96.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8246 | 92337778 | 47673344 | 51.6% | 51.6% |
| GPT-6.1 Sol | 6565 | 190809637 | 177606528 | 93.1% | 93.5% |
| Sonnet 5.5 | 6675 | 146529435 | 139837589 | 95.4% | 96.1% |
