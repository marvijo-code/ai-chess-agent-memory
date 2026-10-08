# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0003-20261008-163034)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 246 | 2582621 | 1023104 | 39.6% | 39.4% |
| GPT-6.1 Sol | 204 | 6499253 | 6282624 | 96.7% | 96.9% |
| Sonnet 5.5 | 189 | 4607682 | 4419091 | 95.9% | 96.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 809 | 8884283 | 4204416 | 47.3% | 47.3% |
| GPT-6.1 Sol | 666 | 19662597 | 18485376 | 94.0% | 94.3% |
| Sonnet 5.5 | 752 | 17387942 | 16677054 | 95.9% | 96.4% |
