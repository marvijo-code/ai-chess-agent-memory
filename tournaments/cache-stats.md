# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0002-20261008-140326)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 149 | 1523730 | 637952 | 41.9% | 41.7% |
| GPT-6.1 Sol | 103 | 2385109 | 2186112 | 91.7% | 92.1% |
| Sonnet 5.5 | 118 | 2666110 | 2549538 | 95.6% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 386 | 3859828 | 1914624 | 49.6% | 49.6% |
| GPT-6.1 Sol | 405 | 11939123 | 11090176 | 92.9% | 93.2% |
| Sonnet 5.5 | 387 | 8271790 | 7911343 | 95.6% | 96.1% |
