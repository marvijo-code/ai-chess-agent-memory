# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0031-20261011-172532)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 80 | 1231782 | 843264 | 68.5% | 68.6% |
| GPT-6.1 Sol | 42 | 1193841 | 1078912 | 90.4% | 91.6% |
| Sonnet 5.5 | 50 | 1301633 | 1248700 | 95.9% | 96.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8150 | 91166563 | 47000576 | 51.6% | 51.5% |
| GPT-6.1 Sol | 6513 | 189710501 | 176635264 | 93.1% | 93.6% |
| Sonnet 5.5 | 6584 | 143905446 | 137313840 | 95.4% | 96.1% |
