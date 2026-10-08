# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0005-20261008-214616)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 116 | 1099207 | 477696 | 43.5% | 43.3% |
| GPT-6.1 Sol | 156 | 5307735 | 5008000 | 94.4% | 95.1% |
| Sonnet 5.5 | 141 | 3506866 | 3366168 | 96.0% | 96.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1295 | 14359101 | 6653184 | 46.3% | 46.3% |
| GPT-6.1 Sol | 1086 | 32530421 | 30423040 | 93.5% | 93.9% |
| Sonnet 5.5 | 1144 | 26139412 | 25029192 | 95.8% | 96.3% |
