# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0016-20261010-025717)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 12 | 69789 | 51328 | 73.5% | 77.5% |
| GPT-6.1 Sol | 12 | 169033 | 150144 | 88.8% | 90.1% |
| Sonnet 5.5 | 13 | 118964 | 103592 | 87.1% | 91.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3926 | 42698564 | 19866240 | 46.5% | 46.4% |
| GPT-6.1 Sol | 3368 | 98475094 | 91577088 | 93.0% | 93.4% |
| Sonnet 5.5 | 3534 | 78617222 | 75110939 | 95.5% | 96.1% |
