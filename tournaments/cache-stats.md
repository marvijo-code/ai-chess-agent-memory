# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0005-20261008-214616)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 22 | 137941 | 48128 | 34.9% | 33.8% |
| GPT-6.1 Sol | 67 | 2569059 | 2432768 | 94.7% | 94.8% |
| Sonnet 5.5 | 67 | 2017824 | 1951431 | 96.7% | 97.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1201 | 13397835 | 6223616 | 46.5% | 46.4% |
| GPT-6.1 Sol | 997 | 29791745 | 27847808 | 93.5% | 93.8% |
| Sonnet 5.5 | 1070 | 24650370 | 23614455 | 95.8% | 96.3% |
