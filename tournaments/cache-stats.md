# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0016-20261010-025717)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 47 | 352415 | 190080 | 53.9% | 53.9% |
| GPT-6.1 Sol | 45 | 816617 | 736640 | 90.2% | 90.8% |
| Sonnet 5.5 | 30 | 293442 | 258751 | 88.2% | 91.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3961 | 42981190 | 20004992 | 46.5% | 46.5% |
| GPT-6.1 Sol | 3401 | 99122678 | 92163584 | 93.0% | 93.4% |
| Sonnet 5.5 | 3551 | 78791700 | 75266098 | 95.5% | 96.1% |
