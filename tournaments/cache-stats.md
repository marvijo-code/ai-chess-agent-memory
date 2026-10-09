# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0013-20261009-191602)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 289 | 3689189 | 1842560 | 49.9% | 49.9% |
| GPT-6.1 Sol | 150 | 3492286 | 3123584 | 89.4% | 90.1% |
| Sonnet 5.5 | 261 | 6208860 | 5944217 | 95.7% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3314 | 36039935 | 16563712 | 46.0% | 45.9% |
| GPT-6.1 Sol | 2900 | 84773683 | 78672640 | 92.8% | 93.3% |
| Sonnet 5.5 | 3087 | 69390128 | 66328144 | 95.6% | 96.2% |
