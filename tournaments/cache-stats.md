# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0026-20261011-055315)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 61 | 722266 | 404480 | 56.0% | 56.0% |
| GPT-6.1 Sol | 36 | 837372 | 787968 | 94.1% | 95.1% |
| Sonnet 5.5 | 68 | 2048483 | 1983270 | 96.8% | 97.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6833 | 76555845 | 38568448 | 50.4% | 50.3% |
| GPT-6.1 Sol | 5388 | 154670485 | 143960704 | 93.1% | 93.5% |
| Sonnet 5.5 | 5719 | 126656664 | 120969079 | 95.5% | 96.1% |
