# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0034-20261012-050243)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 35 | 517349 | 480384 | 92.9% | 93.7% |
| GLM 5.3 Flash | 23 | 168542 | 120320 | 71.4% | 73.3% |
| GPT-6.1 Sol | 24 | 517084 | 464128 | 89.8% | 92.1% |
| Sonnet 5.5 | 35 | 813714 | 772242 | 94.9% | 96.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8577 | 96507150 | 49899648 | 51.7% | 51.6% |
| GLM 5.3 Flash | 23 | 168542 | 120320 | 71.4% | 73.3% |
| GPT-6.1 Sol | 6999 | 204705437 | 190530304 | 93.1% | 93.6% |
| Sonnet 5.5 | 7040 | 155783471 | 148683279 | 95.4% | 96.1% |
