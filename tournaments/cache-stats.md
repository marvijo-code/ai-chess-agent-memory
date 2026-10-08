# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0005-20261008-214616)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 76 | 747312 | 335232 | 44.9% | 44.8% |
| GPT-6.1 Sol | 99 | 3237183 | 3045760 | 94.1% | 94.9% |
| Sonnet 5.5 | 118 | 3224490 | 3108984 | 96.4% | 96.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1255 | 14007206 | 6510720 | 46.5% | 46.4% |
| GPT-6.1 Sol | 1029 | 30459869 | 28460800 | 93.4% | 93.8% |
| Sonnet 5.5 | 1121 | 25857036 | 24772008 | 95.8% | 96.3% |
