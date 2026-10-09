# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0013-20261009-191602)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 242 | 2790763 | 1365248 | 48.9% | 48.8% |
| GPT-6.1 Sol | 150 | 3492286 | 3123584 | 89.4% | 90.1% |
| Sonnet 5.5 | 231 | 5183614 | 4945542 | 95.4% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3267 | 35141509 | 16086400 | 45.8% | 45.7% |
| GPT-6.1 Sol | 2900 | 84773683 | 78672640 | 92.8% | 93.3% |
| Sonnet 5.5 | 3057 | 68364882 | 65329469 | 95.6% | 96.1% |
