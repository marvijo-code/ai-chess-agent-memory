# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0020-20261010-134348)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 150 | 1281366 | 675968 | 52.8% | 52.4% |
| GPT-6.1 Sol | 235 | 7290609 | 6792064 | 93.2% | 93.7% |
| Sonnet 5.5 | 259 | 6475620 | 6234885 | 96.3% | 96.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5229 | 56968352 | 27153920 | 47.7% | 47.6% |
| GPT-6.1 Sol | 4357 | 126719938 | 117727232 | 92.9% | 93.4% |
| Sonnet 5.5 | 4608 | 102422735 | 97871188 | 95.6% | 96.1% |
