# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0001-20261008-104409)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 237 | 2336098 | 1276672 | 54.6% | 54.8% |
| GPT-6.1 Sol | 302 | 9554014 | 8904064 | 93.2% | 93.4% |
| Sonnet 5.5 | 269 | 5605680 | 5361805 | 95.6% | 96.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 237 | 2336098 | 1276672 | 54.6% | 54.8% |
| GPT-6.1 Sol | 302 | 9554014 | 8904064 | 93.2% | 93.4% |
| Sonnet 5.5 | 269 | 5605680 | 5361805 | 95.6% | 96.1% |
