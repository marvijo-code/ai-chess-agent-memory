# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0010-20261009-112258)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 219 | 2113442 | 821120 | 38.9% | 38.5% |
| GPT-6.1 Sol | 261 | 7699285 | 7147648 | 92.8% | 93.2% |
| Sonnet 5.5 | 213 | 4147165 | 3929727 | 94.8% | 95.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2666 | 29018644 | 13005568 | 44.8% | 44.7% |
| GPT-6.1 Sol | 2337 | 69770905 | 64968192 | 93.1% | 93.5% |
| Sonnet 5.5 | 2404 | 53531154 | 51157857 | 95.6% | 96.1% |
