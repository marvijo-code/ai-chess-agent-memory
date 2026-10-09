# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0011-20261009-135256)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 134 | 1241293 | 625408 | 50.4% | 50.3% |
| GPT-6.1 Sol | 194 | 5981904 | 5516160 | 92.2% | 92.7% |
| Sonnet 5.5 | 175 | 4126726 | 3952993 | 95.8% | 96.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2800 | 30259937 | 13630976 | 45.0% | 44.9% |
| GPT-6.1 Sol | 2531 | 75752809 | 70484352 | 93.0% | 93.5% |
| Sonnet 5.5 | 2579 | 57657880 | 55110850 | 95.6% | 96.2% |
