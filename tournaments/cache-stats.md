# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0008-20261009-055507)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 102 | 890349 | 402432 | 45.2% | 44.9% |
| GPT-6.1 Sol | 100 | 2876285 | 2654464 | 92.3% | 92.6% |
| Sonnet 5.5 | 73 | 1499843 | 1424055 | 94.9% | 95.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2099 | 23382642 | 10703360 | 45.8% | 45.7% |
| GPT-6.1 Sol | 1720 | 50895664 | 47494016 | 93.3% | 93.7% |
| Sonnet 5.5 | 1818 | 41308257 | 39517544 | 95.7% | 96.2% |
