# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0020-20261010-134348)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 210 | 1959504 | 989824 | 50.5% | 50.2% |
| GPT-6.1 Sol | 309 | 9989265 | 9394304 | 94.0% | 94.5% |
| Sonnet 5.5 | 289 | 6933819 | 6661836 | 96.1% | 96.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5289 | 57646490 | 27467776 | 47.6% | 47.6% |
| GPT-6.1 Sol | 4431 | 129418594 | 120329472 | 93.0% | 93.4% |
| Sonnet 5.5 | 4638 | 102880934 | 98298139 | 95.5% | 96.1% |
