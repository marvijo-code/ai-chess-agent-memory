# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0002-20261008-140326)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 209 | 2601366 | 1174016 | 45.1% | 45.1% |
| GPT-6.1 Sol | 103 | 2385109 | 2186112 | 91.7% | 92.1% |
| Sonnet 5.5 | 147 | 3625974 | 3483914 | 96.1% | 96.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 446 | 4937464 | 2450688 | 49.6% | 49.7% |
| GPT-6.1 Sol | 405 | 11939123 | 11090176 | 92.9% | 93.2% |
| Sonnet 5.5 | 416 | 9231654 | 8845719 | 95.8% | 96.3% |
