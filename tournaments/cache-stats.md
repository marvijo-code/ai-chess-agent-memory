# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0001-20261008-104409)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 156 | 1229175 | 657536 | 53.5% | 53.8% |
| GPT-6.1 Sol | 181 | 5254900 | 4873984 | 92.8% | 93.1% |
| Sonnet 5.5 | 173 | 3388267 | 3228771 | 95.3% | 95.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 156 | 1229175 | 657536 | 53.5% | 53.8% |
| GPT-6.1 Sol | 181 | 5254900 | 4873984 | 92.8% | 93.1% |
| Sonnet 5.5 | 173 | 3388267 | 3228771 | 95.3% | 95.7% |
