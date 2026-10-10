# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0021-20261010-172846)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 162 | 1769237 | 1026048 | 58.0% | 57.9% |
| GPT-6.1 Sol | 100 | 2320328 | 2153216 | 92.8% | 93.2% |
| Sonnet 5.5 | 98 | 1773432 | 1667137 | 94.0% | 95.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5536 | 61426549 | 29813760 | 48.5% | 48.5% |
| GPT-6.1 Sol | 4531 | 131738922 | 122482688 | 93.0% | 93.4% |
| Sonnet 5.5 | 4779 | 106313678 | 101590650 | 95.6% | 96.1% |
