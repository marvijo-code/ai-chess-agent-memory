# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0003-20261008-163034)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 275 | 3029576 | 1196928 | 39.5% | 39.3% |
| GPT-6.1 Sol | 217 | 6697784 | 6448000 | 96.3% | 96.6% |
| Sonnet 5.5 | 201 | 4921042 | 4719932 | 95.9% | 96.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 838 | 9331238 | 4378240 | 46.9% | 46.9% |
| GPT-6.1 Sol | 679 | 19861128 | 18650752 | 93.9% | 94.2% |
| Sonnet 5.5 | 764 | 17701302 | 16977895 | 95.9% | 96.4% |
