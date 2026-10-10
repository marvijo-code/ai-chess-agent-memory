# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0020-20261010-134348)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 150 | 1281366 | 675968 | 52.8% | 52.4% |
| GPT-6.1 Sol | 159 | 4735665 | 4359936 | 92.1% | 92.8% |
| Sonnet 5.5 | 183 | 4245862 | 4072317 | 95.9% | 96.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5229 | 56968352 | 27153920 | 47.7% | 47.6% |
| GPT-6.1 Sol | 4281 | 124164994 | 115295104 | 92.9% | 93.3% |
| Sonnet 5.5 | 4532 | 100192977 | 95708620 | 95.5% | 96.1% |
