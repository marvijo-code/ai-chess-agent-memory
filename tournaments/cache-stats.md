# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0005-20261008-214616)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 53 | 404499 | 183168 | 45.3% | 45.1% |
| GPT-6.1 Sol | 88 | 2914611 | 2736000 | 93.9% | 94.7% |
| Sonnet 5.5 | 118 | 3224490 | 3108984 | 96.4% | 96.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1232 | 13664393 | 6358656 | 46.5% | 46.5% |
| GPT-6.1 Sol | 1018 | 30137297 | 28151040 | 93.4% | 93.8% |
| Sonnet 5.5 | 1121 | 25857036 | 24772008 | 95.8% | 96.3% |
