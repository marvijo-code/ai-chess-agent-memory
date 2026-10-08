# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0004-20261008-185340)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 58 | 771914 | 467328 | 60.5% | 60.7% |
| GPT-6.1 Sol | 42 | 1099533 | 989184 | 90.0% | 90.9% |
| Sonnet 5.5 | 43 | 882056 | 839069 | 95.1% | 95.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 949 | 10666591 | 5012224 | 47.0% | 46.9% |
| GPT-6.1 Sol | 750 | 21516344 | 20128128 | 93.5% | 93.9% |
| Sonnet 5.5 | 834 | 18980403 | 18184563 | 95.8% | 96.3% |
