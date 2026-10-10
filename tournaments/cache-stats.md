# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0015-20261010-001334)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 119 | 1331630 | 639744 | 48.0% | 47.9% |
| GPT-6.1 Sol | 72 | 1772491 | 1611520 | 90.9% | 91.2% |
| Sonnet 5.5 | 81 | 1631841 | 1547888 | 94.9% | 95.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3726 | 40467469 | 18759168 | 46.4% | 46.3% |
| GPT-6.1 Sol | 3202 | 93390282 | 86738688 | 92.9% | 93.3% |
| Sonnet 5.5 | 3375 | 75254799 | 71901670 | 95.5% | 96.1% |
