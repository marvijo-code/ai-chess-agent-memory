# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0003-20261008-163034)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 47 | 513735 | 236928 | 46.1% | 46.0% |
| GPT-6.1 Sol | 28 | 521409 | 494592 | 94.9% | 95.6% |
| Sonnet 5.5 | 68 | 1912988 | 1851824 | 96.8% | 97.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 610 | 6815397 | 3418240 | 50.2% | 50.2% |
| GPT-6.1 Sol | 490 | 13684753 | 12697344 | 92.8% | 93.1% |
| Sonnet 5.5 | 631 | 14693248 | 14109787 | 96.0% | 96.5% |
