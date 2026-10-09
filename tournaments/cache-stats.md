# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0011-20261009-135256)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 26 | 223414 | 113664 | 50.9% | 50.7% |
| GPT-6.1 Sol | 31 | 674294 | 591360 | 87.7% | 88.5% |
| Sonnet 5.5 | 32 | 509609 | 476171 | 93.4% | 94.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2692 | 29242058 | 13119232 | 44.9% | 44.7% |
| GPT-6.1 Sol | 2368 | 70445199 | 65559552 | 93.1% | 93.5% |
| Sonnet 5.5 | 2436 | 54040763 | 51634028 | 95.5% | 96.1% |
