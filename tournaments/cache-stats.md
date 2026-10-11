# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0031-20261011-172532)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 311 | 4126022 | 2391552 | 58.0% | 57.8% |
| GPT-6.1 Sol | 235 | 7915263 | 7363456 | 93.0% | 93.6% |
| Sonnet 5.5 | 244 | 6794371 | 6528657 | 96.1% | 96.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8381 | 94060803 | 48548864 | 51.6% | 51.6% |
| GPT-6.1 Sol | 6706 | 196431923 | 182919808 | 93.1% | 93.6% |
| Sonnet 5.5 | 6778 | 149398184 | 142593797 | 95.4% | 96.1% |
