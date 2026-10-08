# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0001-20261008-104409)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 134 | 1119597 | 615168 | 54.9% | 55.2% |
| GPT-6.1 Sol | 154 | 4775710 | 4460800 | 93.4% | 93.7% |
| Sonnet 5.5 | 145 | 3017430 | 2887092 | 95.7% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 134 | 1119597 | 615168 | 54.9% | 55.2% |
| GPT-6.1 Sol | 154 | 4775710 | 4460800 | 93.4% | 93.7% |
| Sonnet 5.5 | 145 | 3017430 | 2887092 | 95.7% | 96.0% |
