# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0005-20261008-214616)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 137 | 1425311 | 598912 | 42.0% | 41.9% |
| GPT-6.1 Sol | 156 | 5307735 | 5008000 | 94.4% | 95.1% |
| Sonnet 5.5 | 152 | 3797844 | 3644966 | 96.0% | 96.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1316 | 14685205 | 6774400 | 46.1% | 46.1% |
| GPT-6.1 Sol | 1086 | 32530421 | 30423040 | 93.5% | 93.9% |
| Sonnet 5.5 | 1155 | 26430390 | 25307990 | 95.8% | 96.2% |
