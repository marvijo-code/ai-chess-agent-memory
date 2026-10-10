# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0023-20261010-213538)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 180 | 2035004 | 1242624 | 61.1% | 61.3% |
| GPT-6.1 Sol | 101 | 2514004 | 2322944 | 92.4% | 92.9% |
| Sonnet 5.5 | 106 | 2017642 | 1902946 | 94.3% | 95.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6075 | 67538475 | 33492992 | 49.6% | 49.5% |
| GPT-6.1 Sol | 4875 | 140180475 | 130385152 | 93.0% | 93.5% |
| Sonnet 5.5 | 5138 | 113446945 | 108338649 | 95.5% | 96.1% |
