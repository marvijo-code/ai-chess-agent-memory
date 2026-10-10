# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0022-20261010-192853)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 154 | 1545266 | 837120 | 54.2% | 54.0% |
| GPT-6.1 Sol | 79 | 1525825 | 1409408 | 92.4% | 93.0% |
| Sonnet 5.5 | 111 | 2364261 | 2248867 | 95.1% | 95.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5813 | 64609357 | 31748096 | 49.1% | 49.1% |
| GPT-6.1 Sol | 4705 | 136020210 | 126542720 | 93.0% | 93.5% |
| Sonnet 5.5 | 4961 | 110084086 | 105168144 | 95.5% | 96.1% |
