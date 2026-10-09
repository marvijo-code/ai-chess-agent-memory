# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0011-20261009-135256)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 26 | 223414 | 113664 | 50.9% | 50.7% |
| GPT-6.1 Sol | 65 | 2331281 | 2177792 | 93.4% | 93.7% |
| Sonnet 5.5 | 66 | 1833332 | 1773066 | 96.7% | 97.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2692 | 29242058 | 13119232 | 44.9% | 44.7% |
| GPT-6.1 Sol | 2402 | 72102186 | 67145984 | 93.1% | 93.5% |
| Sonnet 5.5 | 2470 | 55364486 | 52930923 | 95.6% | 96.2% |
