# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0017-20261010-051708)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 355 | 4368113 | 2503808 | 57.3% | 57.4% |
| GPT-6.1 Sol | 160 | 3828449 | 3463296 | 90.5% | 90.9% |
| Sonnet 5.5 | 222 | 4702252 | 4484385 | 95.4% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4502 | 49527436 | 23682176 | 47.8% | 47.8% |
| GPT-6.1 Sol | 3669 | 105365217 | 97774336 | 92.8% | 93.3% |
| Sonnet 5.5 | 3897 | 85770358 | 81900748 | 95.5% | 96.1% |
