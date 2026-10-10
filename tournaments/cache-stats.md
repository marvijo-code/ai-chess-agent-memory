# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0016-20261010-025717)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 233 | 2530548 | 1363456 | 53.9% | 53.9% |
| GPT-6.1 Sol | 153 | 3230707 | 2884096 | 89.3% | 90.2% |
| Sonnet 5.5 | 154 | 2569848 | 2409016 | 93.7% | 94.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4147 | 45159323 | 21178368 | 46.9% | 46.8% |
| GPT-6.1 Sol | 3509 | 101536768 | 94311040 | 92.9% | 93.4% |
| Sonnet 5.5 | 3675 | 81068106 | 77416363 | 95.5% | 96.1% |
